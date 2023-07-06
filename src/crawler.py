import re
import json
import requests_cache
from gzip import decompress
from bs4 import BeautifulSoup
from neo4j import GraphDatabase
from urllib.parse import urljoin

from full_map import MAP, load_class

SESSION = requests_cache.CachedSession("crawl_cache")

# Neo4j Connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

DRIVER = GraphDatabase.driver(uri, auth=(username, password))

# Function to check if the URL is allowed by robots.txt
def is_url_allowed(url, user_agent="*"):
    robots_url = urljoin(url, "/robots.txt")
    response = SESSION.get(robots_url)
    robots_txt = response.text

    user_agent_pattern = f"User-agent: {re.escape(user_agent)}"
    rules = re.findall(r"(?s)" + user_agent_pattern + r".*?(?:User-agent:|\Z)", robots_txt)

    for rule in rules:
        if "Disallow:" in rule:
            disallowed_path = re.search(r"Disallow:\s*(.*)", rule).group(1).strip()
            if disallowed_path == "/":
                return False
            elif url.startswith(urljoin(robots_url, disallowed_path)):
                return False

    return True

# Function to extract LD+JSON data from a webpage
def extract_ldjson(url):
    response = SESSION.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    ldjson_data = soup.find_all("script", {"type": "application/ld+json"})

    extracted_data = []
    for script in ldjson_data:
        try:
            data = json.loads(script.string)
            extracted_data.append(data)
        except json.JSONDecodeError:
            pass

    return extracted_data

# Function to extract classes & nested classes from LD+JSON data
def extract_class(jdict):
    classes = []
    if type(jdict) == type([]):
        for each in jdict:
            classes.extend(extract_class(each))
    elif type(jdict) == type({}):
        if "@type" in jdict.keys():
            if jdict["@type"] in MAP.keys():
                x = load_class(MAP[jdict["@type"]])
                print(jdict)
                classes.append(x(**jdict))
        for each in jdict.keys():
            if type(each) == type([]):
                classes.extend(extract_class(each))
    return classes

# Function to crawl the sitemap and extract LD+JSON data
def crawl_sitemap(url):
    #response = decompress(SESSION.get(url).content)
    #soup = BeautifulSoup(response, "xml")
    #urls = soup.find_all("loc")
    urls = ["https://www.foodnetwork.com/recipes/tomato-gorgonzola-soup-recipe-2103464",
            "https://en.wikipedia.org/wiki/Lockstep_(computing)"]
    classes = []
    for url in urls:
        url = url
        if is_url_allowed(url):
            ldjson_data = extract_ldjson(url)
            # Do something with the extracted LD+JSON data
            for data in ldjson_data:
                classes.extend(extract_class(data))
        yield classes

# Squash the class and return primitive types
def squash_class(clss):
    out = {}
    for each in clss.__dict__.keys():
        out[each] = repr(clss.__dict__[each])
    return out

# Function to insert nodes into the database
def insert_node(tx, node, label):
    tx.run(
        f"MERGE (n:{label}) "
        f"SET n += $props",
        props = squash_class(node)
    )

# Function to insert relationships into the database
def insert_relationship(tx, source_id, target_id, relationship_type):
    tx.run(
        "MATCH (source), (target) "
        "WHERE source.id = $source_id AND target.id = $target_id "
        "MERGE (source)-[r:" + relationship_type + "]->(target)",
        source_id=source_id,
        target_id=target_id
    )



# Example usage
base_url = "https://wellsr.com"
sitemap_url = urljoin(base_url, "/sitemap.xml")
sitemap_url = "https://www.foodnetwork.com/sitemaps/sitemap_food_1.xml.gz"

with DRIVER.session() as session:
    for class_list in crawl_sitemap(sitemap_url):
        for each in class_list:
            session.write_transaction(insert_node, each, each.__class__.__name__)
