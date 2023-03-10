from elasticsearch import Elasticsearch

from app.settings import ELASTICSEARCH_PASSWORD, ELASTICSEARCH_CLOUD_ID

"""
Connect to elasticsearch cloud
"""

es_client = Elasticsearch(
    cloud_id=ELASTICSEARCH_CLOUD_ID,
    basic_auth=("elastic", ELASTICSEARCH_PASSWORD)
)
