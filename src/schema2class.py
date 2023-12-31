import requests
import keyword
from requests_cache import CachedSession
from bs4 import BeautifulSoup
from pydantic import BaseModel
from typing import Optional
from urllib.parse import urlparse

DONT_CRAWL = [
"DataType",
"Time",
"Number",
"Text",
"CssSelectorType",
"PronounceableText",
"URL",
"XPathType",
"Boolean",
"False",
"True",
"DateTime",
]


# Create a cached session for requests
session = CachedSession('schemaorg_cache', backend='sqlite', expire_after=36000)

# Define the sitemap URL
sitemap_url = "https://schema.org/docs/sitemap.xml"

# Send a GET request to the sitemap URL
response = session.get(sitemap_url)

# Parse the sitemap XML
sitemap_xml = response.text
soup = BeautifulSoup(sitemap_xml, "xml")

# Find all URL elements in the sitemap
url_elements = soup.find_all("url")

# Function to determine the depth of a URL
def get_url_depth(url):
    parsed_url = urlparse(url)
    return parsed_url.path.count('/')

MODELS = []

# Iterate over the URL elements
for url_element in url_elements:
    # Extract the URL
    page_url = url_element.find("loc").text

    # Check if the URL has a depth of 1
    nam = page_url.split("/")[-1]
    if get_url_depth(page_url) == 1 and len(nam) > 1 and nam not in DONT_CRAWL and nam[0].isupper():
        # Send a GET request to the page URL
        page_response = session.get(page_url)

        # Parse the page HTML
        page_html = page_response.text
        page_soup = BeautifulSoup(page_html, "html.parser")

        # Find the definition table
        definition_table = page_soup.find("table", class_="definition-table")

        if definition_table:
            # Extract class name from the page URL
            class_name = page_url.split("/")[-1]
            MODELS.append(class_name)
            # Start building the class string
            class_string = f"""from typing import Optional, Any\n\nclass {class_name}(BaseModel):\n"""

            # Find property names in the definition table
            property_elements = definition_table.find_all("th")
            i=0
            num_props = 0
            for property_element in property_elements:
                try:
                    if "supertype-name" in property_element['class']:
                        if i==1:
                            sup = property_element.find("a").text.strip()
                            x = f"from models.{sup} import {sup}\n\n"
                            class_string = x + class_string.replace("BaseModel", sup)
                            break
                        i+=1
                    elif "prop-nam" in property_element['class']:
                        num_props+=1
                        property_name = property_element.text.strip()
                        if keyword.iskeyword(property_name):
                            property_name = '_' + property_name
                        class_string += f"    {property_name}: Optional[Any] = None\n"
                except:
                    pass
            if i <= 1:
                # Not a subclass
                class_string = "from pydantic import BaseModel\n" + class_string
            if num_props == 0:
                # Empty class
                class_string += "    pass\n"
            # Print the generated class
#            print(class_string)
#            print()

            # Save the generated class in a separate Python file
            with open(f"models/{class_name}.py", "w") as f:
                f.write(class_string)
                f.write("\n")

map = ""
for each in MODELS:
    map += f"    '{each}': 'models.{each}',\n"

mapString = """# WARNING: This file is auto-generated by schema2class.py
# Changes will be overwritten
import importlib

# Custom import function to dynamically load classes
def load_class(class_name):
    m = globals().get(class_name.split(".")[-1])
    if m is None:
        module = importlib.import_module(class_name)
        m = getattr(module, class_name.split(".")[-1])
    return m
""" + "\n\nMAP = {" + map + "}\n"

with open(f"full_map.py", "w") as f:
    f.write(mapString)
    f.write("\n")