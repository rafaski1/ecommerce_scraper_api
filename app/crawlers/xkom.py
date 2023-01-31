from bs4 import BeautifulSoup
from collections import OrderedDict
from elasticsearch import NotFoundError

from app.enums import Indexes
from app.schemas import Product
from app.crawlers.base_crawler import Base
from app.clients.es import es_client


class Xkom(Base):
    """
    A crawler class that supports product data scraping from x-kom.pl domain
    """

    headers = OrderedDict({
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Encoding": "gzip, deflate, utf-8",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "www.x-kom.pl",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) "
            "Gecko/20100101 Firefox/110.0"
        )
    })
    # TODO rotate user-agent
    # TODO https://medium.com/geekculture/rotate-ip-address-and-user-agent-to-scrape-data-a010216c8d0c

    def parse(self, url: str) -> dict:
        """
        Scrape product data from website and save results to elasticsearch
        """
        # check elasticsearch before scraping http request
        try:
            doc = es_client.get(index=Indexes.PROFILES_V2, id=url)
            return doc.get("_source")
        except NotFoundError:
            pass

        # get a html text file
        response = self.request(url=url, headers=self.headers)
        
        # TODO error handling for bs
        doc = BeautifulSoup(response, "html.parser")

        # extract data from response
        name = doc.find(class_="sc-1bker4h-4 hMQkuz").text
        price_currency_str = doc.find(class_="sc-n4n86h-4 jwVRpW").text
        price = int(price_currency_str.split(",")[0].replace(" ", ""))
        currency = price_currency_str.split(" ")[-1][-2:]
        average_rating = doc.find(
            class_="sc-1h16fat-0 sc-1ngc1lj-1 eKEFnB sc-1bker4h-6 gDIfGT"
        )
        average_rating = float(average_rating["title"][-4:])
        review_count = doc.find(class_="sc-1ngc1lj-2 eJPDue").text
        review_count = int(review_count.split(" ")[0][1:])
        all_reviews = doc.find_all(
            class_="sc-u1peis-1 etZjkD sc-s2qgtg-21 gIUavP"
        )
        reviews = []
        for review in all_reviews:
            reviews.append(review.text)

        product = Product(
            name=name,
            price=price,
            currency=currency,
            review_count=review_count,
            average_rating=average_rating,
            reviews=reviews,
            url=url
        )
        self.save(product=product)

        return product.dict()
