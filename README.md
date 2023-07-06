# Schema2Neo4JCrawler
A web-crawler that extracts &amp; converts schemas into Neo4J databases.

## Requirements

* requests_cache
* bs4
* neo4j

## Usage

```bash
git clone https://github.com/NoahGWood/Schema2Neo4JCrawler.git
cd Schema2Neo4JCrawler/src
python3 crawler.py
```

## Rebuilding Models

It may be necessary to rebuild models from time to time. Models are created by scraping the Schema.org website and generating python class definitions.

```
python3 schema2class.py
```

