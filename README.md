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
   ```sh
   git clone https://github.com/luccabb/elasticsearch.git
   ```
3. Build our image
   ``` 
   docker-compose build
   ```
4. Run containers
   ```
   sudo docker-compose up -d
   ```

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

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* [Docker Desktop](https://www.docker.com/products/docker-desktop)

If not included with your Docker Desktop Installation, make sure that you have [Docker Compose](https://docs.docker.com/compose/install/)


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
