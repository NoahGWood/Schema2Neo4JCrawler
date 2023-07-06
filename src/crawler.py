import requests
import requests_cache
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from gzip import decompress
import re
import json

from full_map import MAP, load_class

# Function to check if the URL is allowed by robots.txt
def is_url_allowed(url, user_agent="*"):
    robots_url = urljoin(url, "/robots.txt")
    response = requests.get(robots_url)
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
    session = requests_cache.CachedSession("crawl_cache")
    response = session.get(url)
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

def extract_class(jdict):
    classes = []
    if type(jdict) == type([]):
        for each in jdict:
            classes.extend(extract_class(each))
    elif type(jdict) == type({}):
        if "@type" in jdict.keys():
            if jdict["@type"] in MAP.keys():
                x = load_class(MAP[jdict["@type"]])
                print(x)
                classes.append(x(**jdict))
        for each in jdict.keys():
            if type(each) == type([]):
                classes.extend(extract_class(each))
    return classes

# Function to crawl the sitemap and extract LD+JSON data
def crawl_sitemap(url):
    #response = decompress(requests.get(url).content)
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
#                for each in data:
#                    if '@type' in each:
#                        if each["@type"] in MAP.keys():
#                            x = load_class(MAP[each["@type"]])
#                            print(x)
#                            classes.append(x(**each))
        print(classes)

# Example usage
base_url = "https://wellsr.com"
sitemap_url = urljoin(base_url, "/sitemap.xml")
sitemap_url = "https://www.foodnetwork.com/sitemaps/sitemap_food_1.xml.gz"
crawl_sitemap(sitemap_url)
