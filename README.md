<!-- ABOUT THE PROJECT -->
## About The Project

This is an [Elasticsearch](https://www.elastic.co/products/elasticsearch) project, where we bring a cluster up, and do some basic operations in it.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop)

If not included with your Docker Desktop Installation, make sure that you have [Docker Compose](https://docs.docker.com/compose/install/)

### Getting our cluster up and running

1. Clone the repo
   ```
   git clone https://github.com/luccabb/elasticsearch.git
   ```
2. If you're running from an Ubuntu machine you may need the following line (to increase virtual memory)
   ```
   sudo sysctl -w vm.max_map_count=262144
   ```
3. Build our image
   ``` 
   docker-compose build
   ```
4. Run containers
   ```
   sudo docker-compose up -d
   ```

If those steps have worked properly, you should be able to navigate to the [Elasticsearch UI](http://localhost:9200) on your localhost.
## Doing some basic operations

### Prerequisites

* [python](https://www.python.org/downloads/)

* Python Elasticsearch Client
  ```
  pip install elasticsearch
  ```

### Creating a new index

```
python create_index.py
```

### Indexing some data

```
python index_data.py
```

### Searching for data

```
python search_data.py
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
