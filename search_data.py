import requests
from elasticsearch import Elasticsearch

# declaring constants
API_URL = "https://rickandmortyapi.com/api/character"
HOST = "localhost"
PORT = 9200
INDEX_NAME = "rickandmorty"

# Create an Elasticsearch client connected
# to localhost:9200
es = Elasticsearch([{'host': HOST, 'port': PORT}])

query_1 = es.search(index=INDEX_NAME, body={"query": {"match" : { "species" : "human"}}}) 

print("Number of Humans:", query_1['hits']['total']['value'])