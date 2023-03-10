# E-commerce Scraper API
This application was built for educational purposes and is not intended 
for production use.

## Overview
This is a web scraper API that provides product information from supported 
e-commerce websites. Web crawlers run as `celery` tasks, parsed data is stored 
in `elasticsearch`. Results are sent to a callback url.

### Motives
The main reason for creating this application was to practice web scraping, 
explore `celery` and `elasticsearch`

Main features:
- FastAPI framework
- HTTP requests using `requests` library
- Data extraction with `beautifulsoup`
- Distributed task queuing with `celery`
- `redis` as a message broker for `celery` app
- data storage in `elasticsearch`
- scraping results sent to callback url, used `pipedream.com` for testing
- OOP where applicable
- testing with `pytest`

TODO:
- support more e-commerce websites

### Supported e-commerce websites:
`www.x-kom.pl`

## Get started
To run the API you will need connect to `elasticsearch`, we use `Elastic Cloud`.
Get your `Elastic Cloud` credentials, create the `.env` file 
(use the `.env.dist` for reference) and add the `ELASTICSEARCH_CLOUD_ID` and 
`ELASTICSEARCH_PASSWORD` variables.

### Authentication
To authenticate incoming requests, we check the `api_key` header.
Create the `.env` file (use the `.env.dist` for reference) 
and add `API_KEY` to environment variables.

### Dependencies
Dependency management is handled using `requirements.txt` file.

### Local setup
1. Install dependencies from `requirements.txt` file
2. Run redis server with `redis-cli`
3. Run celery worker with `celery -A app.celery_app worker -Q crawling --pool=solo --loglevel=INFO`
4. Run the app: `uvicorn app.main:app --reload`

## Documentation
Once the application is up and running, you can access FastAPI automatic docs 
at index page `/`

## Endpoints
| Method | Endpoint | Description                     |
|--------|----------|---------------------------------|
| GET    | /crawl   | Create a data scraping task     |


## Examples
### Hit API endpoint
```shell
curl -X 'GET' 'http://127.0.0.1:8080/crawl?url={XKOM_URL}&callback_url={CALLBACK_URL}' -H 'accept: application/json'
  ```

### API response
```json
{
  "success": true,
  "message": "Task accepted",
  "result": null
}
```
### Elasticsearch API console
```shell
GET /profiles-v2/_search
````
```json
{
  "hits": {
    "hits": [
      {
        "_score": 1,
        "_id": "https://www.x-kom.pl/p/1054822-notebook-laptop-133-apple-macbook-air-m2-16gb-256-mac-os-midnight.html#Specyfikacja",
        "_source": {
          "review_count": 46,
          "name": "Apple MacBook Air M2/16GB/256/Mac OS Midnight",
          "average_rating": 5.91,
          "url": "https://www.x-kom.pl/p/1054822-notebook-laptop-133-apple-macbook-air-m2-16gb-256-mac-os-midnight.html#Specyfikacja",
          "price": 6999,
          "currency": "z??",
          "reviews": [
            "Mam ten komp tylko z dyskiem 1TB, - to jest bestia. U??ywam do fullstack developmentu, masa apek, docker, jetbrains rider + webstorm, nodejs, .net core, teamsy, dsiesi??tki tab??w w chrome, parallels z win11 - ??adnego problemu. CPU temp na poziomie 35 - 50C, przewa??nie 35C, 50 osi??ga przy indeksacji projektu albo ??adowaniu win11 - wszystko jest mega szybkie. Tak powinien wygl??da?? sprz??t przysz??o??ci. Nigdy wi??cej komp??w z wiatrakami.... Rozwi?? dalej",
            "??ona zadowolona a szcz????liwa kobieta to mo??liwo???? wyj??cia z kumplami na piwo.... Rozwi?? dalej",
            "Zaczn?? od minus??w: dla kogo?? kto od 25 lat korzysta?? wy????czanie z Windows to jest to \"kulturowy szok\". ??eby nie by??o, ja uwielbiam windowsa i uwa??am ??e jest to ??wietny system. Dlatego przyzwyczajenie si?? do MacOS zajmie du??o czasu. W okres adaptacji mocno spadnie efektywno???? pracy. Nie dzia??aj?? klasyczne skr??ty klawiszowe, przyzwyczajenia z Windows b??d?? przeszkadza?? w pracy. Po pewnym czasie jednak zaczyna by?? wygodniej. Do minus??w nale??y te?? zaliczy?? ograniczenia systemu (nie jest tak otwarty jak windrws). Teraz plusy: wygl??d fenomenalny, bateria absolutnie genialna, kultura pracy dotychczas nieosi??galna nawet na naprawd?? topowych maszynach z windows.... Rozwi?? dalej",
            "Jak dla mnie to genialny sprz??t do l??ejszej pracy i domowego u??ytku. Bateria wytrzymuje ca??y dzie?? bez ??adowania. 8GB ramu te?? wystarcza do wi??kszo??ci zada?? domowych (obs??uga kilkunastu zak??adek w chromie, spotify, evernote, outlook).... Rozwi?? dalej",
            "To m??j pierwszy Mac, wcze??niej windows, w tym wydajne maszyny biznesowe do pracy biurowej. Jako???? wykonania na najwy??szym poziomie, touchpad i klawiatura nie maj?? sobie r??wnych. Klawisze maj?? przyjemny click, jest wyra??na \"podr????\" klawisza, ale te na thinkpadach chyba przyjemniejsze s??. P??ynno???? dzia??ania i performance na najwy??szym poziomie, wszystko chodzi niesamowicie p??ynnie i znosi ca??kiem mocny multitasking. Nie testowa??em jeszcze niczego bardziej wymagaj??cego (rendering fotografii, Machine learning etc). Je??li zastanawiasz si?? czy na pewno Mac to jest dobra droga, to po 2 tygodniach m??wi?? zdecydowanie ??e tak. Wygl??da niesamowicie, bateria starcza na bardzo d??ugo - kilkana??cie godzin bym powiedzia??. Jako ca??kliem power user, jeszcze jest pare rzeczy do kt??rych si?? musz?? przyzwyczai?? ale generalnie jest bajka. Super g??o??niki graj?? jak na tak ma???? obudow??, nawet nie wiedzia??em, ??e to zwr??ci moj?? uwag?? a s?? super wywa??one, ofc ma??o basu, ale czego tu wymaga?? od laptopa kt??ry jest gruby na troch ponad centymetr.Z wad mo??e si zdarzy??, ??e ten dysk b??dzie za ma??y, ale je??li ma si?? dysk zewn i lubi korzysta?? z chmury to powinno by?? bez problemu. Ludzie co m??wi??, ??e s?? smugi i si ten kolor rysuje. Smugi zupe??nie nie przeszkadzaj??, s?? ??atwo zmywalne i serio to nie przeszkadza, chyba ??e dla jakich?? pedant??w. Ten kolor wygl??da nieprawdopodobnie elegancko i nowocze??nie. Pono?? po d??u??szym czasie si rysuje i wida?? kolor aluminimum - nie wiem, po prostu kupi??em bardzo dobry pokrowiec i wk??adam go podczas przenoszenia.... Rozwi?? dalej",
            "Laptop jest super!... Rozwi?? dalej",
            "W mojej opinii to bardzo dobrze wykonany sprzet. W mojej pracy wystarcza a czesto kompiluje programy. Nie odczuwam spadku mocy procka. Dla por??wnania pracuje te?? na macbook'u pro M1 32GB i kompilacja program??w trwa w przybli??eniu tyle samo.... Rozwi?? dalej",
            "Petarda jak dla mnie w tej konfiguracji przepa???? techniczna do maca pro z 2017???.kolor palcuje si??... Rozwi?? dalej",
            "Na ten moment bez zastrze??e??, idealnie sprawdza si?? przy pracy biurowej oraz przy obr??bce zdj????/video - cho?? w przypadku tego drugiego po pod????czeniu do monitora. Jedyny minus to strasznie uci????liwe ??lady palc??w przy tym kolorze Maca.... Rozwi?? dalej",
            "Mia??em wielkie szcz????cie, ??e m??j MacBook z poszukiwan?? specyfikacj?? by?? ju?? w moim miejskim sklepie. Zam??wi??em w sobot?? rano - i w sobot?? przy obiedzie dostalem SMSa ze Mackbook gotowy do odbioru.No i jak to zawsze z Apple - bardzo dobrze i bezpiecznie zapakowane. Unboxing laptopa to tez bardzo przyjemna rzecz, nie by??o ??adnych wad.Dzi??ki X-KOM za dobr?? i szybk?? obs??ug??.... Rozwi?? dalej",
            "??wietny ultrabook, kt??ry w zasadzie zast??pi?? mi na co dzie?? mocn?? stacjonark?? we wszystkich zastosowaniach poza najnowszymi grami. Do 15 godzin pracy na baterii, jasna matryca, pi??kna metalowa obudowa, klawiatura wygodna jak ??adna inna. W zwi??zku z powy??szym opr??cz niszowych zastosowa?? typu programowanie w stacku Microsoftu przestaj?? widzie?? jakikolwiek sens istnienia dla laptop??w na Windowsie (nawet tych dro??szych).... Rozwi?? dalej",
            "To jest fajna maszyna... Rozwi?? dalej",
            "Pobiera 5W, by wykona?? t?? sam?? prac?? co PC metr obok, z Ryzenem 7 3700X.Je??eli komu?? potrzeba procesora z dobrym IPC pod software typu NodeJS, czy nawet w C#, kt??ry nie wyssie ??ycia z baterii, to Intel/AMD w tym ??wietle zaczynaj?? traci?? na warto??ci.... Rozwi?? dalej",
            "Super sprz??t , w brew temu co sugerowa?? sprzedawca nie nagrzewa si?? i nie zwr??ci??em go :)... Rozwi?? dalej",
            "FAJNY SPRZ??T... Rozwi?? dalej"
          ]
        }
      }
    ]
  }
}
```
### Pipedream callback payload
```shell
HTTP POST
```
```json
{
  "body": {
    "average_rating": 5.91,
    "currency": "z??",
    "name": "Apple MacBook Air M2/16GB/256/Mac OS Midnight",
    "price": 6999,
    "review_count": 46,
    "reviews": [
            "Mam ten komp tylko z dyskiem 1TB, - to jest bestia. U??ywam do fullstack developmentu, masa apek, docker, jetbrains rider + webstorm, nodejs, .net core, teamsy, dsiesi??tki tab??w w chrome, parallels z win11 - ??adnego problemu. CPU temp na poziomie 35 - 50C, przewa??nie 35C, 50 osi??ga przy indeksacji projektu albo ??adowaniu win11 - wszystko jest mega szybkie. Tak powinien wygl??da?? sprz??t przysz??o??ci. Nigdy wi??cej komp??w z wiatrakami.... Rozwi?? dalej",
            "??ona zadowolona a szcz????liwa kobieta to mo??liwo???? wyj??cia z kumplami na piwo.... Rozwi?? dalej",
            "Zaczn?? od minus??w: dla kogo?? kto od 25 lat korzysta?? wy????czanie z Windows to jest to \"kulturowy szok\". ??eby nie by??o, ja uwielbiam windowsa i uwa??am ??e jest to ??wietny system. Dlatego przyzwyczajenie si?? do MacOS zajmie du??o czasu. W okres adaptacji mocno spadnie efektywno???? pracy. Nie dzia??aj?? klasyczne skr??ty klawiszowe, przyzwyczajenia z Windows b??d?? przeszkadza?? w pracy. Po pewnym czasie jednak zaczyna by?? wygodniej. Do minus??w nale??y te?? zaliczy?? ograniczenia systemu (nie jest tak otwarty jak windrws). Teraz plusy: wygl??d fenomenalny, bateria absolutnie genialna, kultura pracy dotychczas nieosi??galna nawet na naprawd?? topowych maszynach z windows.... Rozwi?? dalej",
            "Jak dla mnie to genialny sprz??t do l??ejszej pracy i domowego u??ytku. Bateria wytrzymuje ca??y dzie?? bez ??adowania. 8GB ramu te?? wystarcza do wi??kszo??ci zada?? domowych (obs??uga kilkunastu zak??adek w chromie, spotify, evernote, outlook).... Rozwi?? dalej",
            "To m??j pierwszy Mac, wcze??niej windows, w tym wydajne maszyny biznesowe do pracy biurowej. Jako???? wykonania na najwy??szym poziomie, touchpad i klawiatura nie maj?? sobie r??wnych. Klawisze maj?? przyjemny click, jest wyra??na \"podr????\" klawisza, ale te na thinkpadach chyba przyjemniejsze s??. P??ynno???? dzia??ania i performance na najwy??szym poziomie, wszystko chodzi niesamowicie p??ynnie i znosi ca??kiem mocny multitasking. Nie testowa??em jeszcze niczego bardziej wymagaj??cego (rendering fotografii, Machine learning etc). Je??li zastanawiasz si?? czy na pewno Mac to jest dobra droga, to po 2 tygodniach m??wi?? zdecydowanie ??e tak. Wygl??da niesamowicie, bateria starcza na bardzo d??ugo - kilkana??cie godzin bym powiedzia??. Jako ca??kliem power user, jeszcze jest pare rzeczy do kt??rych si?? musz?? przyzwyczai?? ale generalnie jest bajka. Super g??o??niki graj?? jak na tak ma???? obudow??, nawet nie wiedzia??em, ??e to zwr??ci moj?? uwag?? a s?? super wywa??one, ofc ma??o basu, ale czego tu wymaga?? od laptopa kt??ry jest gruby na troch ponad centymetr.Z wad mo??e si zdarzy??, ??e ten dysk b??dzie za ma??y, ale je??li ma si?? dysk zewn i lubi korzysta?? z chmury to powinno by?? bez problemu. Ludzie co m??wi??, ??e s?? smugi i si ten kolor rysuje. Smugi zupe??nie nie przeszkadzaj??, s?? ??atwo zmywalne i serio to nie przeszkadza, chyba ??e dla jakich?? pedant??w. Ten kolor wygl??da nieprawdopodobnie elegancko i nowocze??nie. Pono?? po d??u??szym czasie si rysuje i wida?? kolor aluminimum - nie wiem, po prostu kupi??em bardzo dobry pokrowiec i wk??adam go podczas przenoszenia.... Rozwi?? dalej",
            "Laptop jest super!... Rozwi?? dalej",
            "W mojej opinii to bardzo dobrze wykonany sprzet. W mojej pracy wystarcza a czesto kompiluje programy. Nie odczuwam spadku mocy procka. Dla por??wnania pracuje te?? na macbook'u pro M1 32GB i kompilacja program??w trwa w przybli??eniu tyle samo.... Rozwi?? dalej",
            "Petarda jak dla mnie w tej konfiguracji przepa???? techniczna do maca pro z 2017???.kolor palcuje si??... Rozwi?? dalej",
            "Na ten moment bez zastrze??e??, idealnie sprawdza si?? przy pracy biurowej oraz przy obr??bce zdj????/video - cho?? w przypadku tego drugiego po pod????czeniu do monitora. Jedyny minus to strasznie uci????liwe ??lady palc??w przy tym kolorze Maca.... Rozwi?? dalej",
            "Mia??em wielkie szcz????cie, ??e m??j MacBook z poszukiwan?? specyfikacj?? by?? ju?? w moim miejskim sklepie. Zam??wi??em w sobot?? rano - i w sobot?? przy obiedzie dostalem SMSa ze Mackbook gotowy do odbioru.No i jak to zawsze z Apple - bardzo dobrze i bezpiecznie zapakowane. Unboxing laptopa to tez bardzo przyjemna rzecz, nie by??o ??adnych wad.Dzi??ki X-KOM za dobr?? i szybk?? obs??ug??.... Rozwi?? dalej",
            "??wietny ultrabook, kt??ry w zasadzie zast??pi?? mi na co dzie?? mocn?? stacjonark?? we wszystkich zastosowaniach poza najnowszymi grami. Do 15 godzin pracy na baterii, jasna matryca, pi??kna metalowa obudowa, klawiatura wygodna jak ??adna inna. W zwi??zku z powy??szym opr??cz niszowych zastosowa?? typu programowanie w stacku Microsoftu przestaj?? widzie?? jakikolwiek sens istnienia dla laptop??w na Windowsie (nawet tych dro??szych).... Rozwi?? dalej",
            "To jest fajna maszyna... Rozwi?? dalej",
            "Pobiera 5W, by wykona?? t?? sam?? prac?? co PC metr obok, z Ryzenem 7 3700X.Je??eli komu?? potrzeba procesora z dobrym IPC pod software typu NodeJS, czy nawet w C#, kt??ry nie wyssie ??ycia z baterii, to Intel/AMD w tym ??wietle zaczynaj?? traci?? na warto??ci.... Rozwi?? dalej",
            "Super sprz??t , w brew temu co sugerowa?? sprzedawca nie nagrzewa si?? i nie zwr??ci??em go :)... Rozwi?? dalej",
            "FAJNY SPRZ??T... Rozwi?? dalej"
    ],
    "url": "https://www.x-kom.pl/p/1054822-notebook-laptop-133-apple-macbook-air-m2-16gb-256-mac-os-midnight.html#Specyfikacja"
  }
}
```