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

json_data = requests.get(API_URL).json()

# insert data into es
for document in json_data['results']:
    es.index(index=INDEX_NAME, body=document)
