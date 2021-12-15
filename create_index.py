from elasticsearch import Elasticsearch

# declaring constants
API_URL = "https://rickandmortyapi.com/api/character"
HOST = "localhost"
PORT = 9200
INDEX_NAME = "rickandmorty"
PRIMARY_SHARDS = 3
REPLICA_SHARDS = 2

# Create an Elasticsearch client connected
# to localhost:9200
es = Elasticsearch([{'host': HOST, 'port': PORT}])

request_body = {
    "settings" : {
        "number_of_shards": PRIMARY_SHARDS,
        "number_of_replicas": REPLICA_SHARDS
}}

# create index
es.indices.create(index=INDEX_NAME, body=request_body)
