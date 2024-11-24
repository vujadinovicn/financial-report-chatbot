import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import html
from parse_sections import get_items_to_extract


def get_edgar_10k(company_metadata):
    soup = parse_html_document(company_metadata['FORM10KLINKS'])

    json_data = {
        "cik": company_metadata["CIK"],
        "cusip6": company_metadata["CUSIP"][:6],
        "cusip": [company_metadata["CUSIP"]],
        "names": [company_metadata["NAME"]],
        "source": company_metadata['FORM10KLINKS']
    }

    for key, (start, end) in get_items_to_extract(company_metadata['NAME']).items():
        json_data[key] = extract_item(soup, start, end)
        if not json_data[key]:
            return None

    return json_data

def parse_html_document(url):
    headers = {
        "User-Agent": "Your Name <your.email@example.com>",
        "Accept-Encoding": "gzip, deflate",
        "Host": "www.sec.gov"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch filing HTML from {url}")
    
    html_content = html.unescape(response.text).replace('\u00A0', ' ').replace('&nbsp;', ' ').replace('\u2019', "'").replace("\u201c", "\"").replace("\u201d", "\"").replace("\u2014", " ").replace("\u2022", "\"")

    soup = BeautifulSoup(html_content, "html.parser")
    return soup

def extract_item(soup, start, end):
    item_tag = soup.find(lambda tag: tag.name == "span" and start in tag.get_text(strip=True) and not tag.find_parent("div").find_parent("td"))
    if not item_tag:
        return 0

    item_content = []
    current_element = item_tag.find_parent("div")
    if not current_element:
        return 0

    while current_element:
        if current_element.find(string=lambda text: text and end in text):
            break
        text_content = current_element.get_text(strip=True)
        if text_content not in (entry.strip() for entry in item_content):
            item_content.append(text_content + '\n') 
        current_element = current_element.find_next()

    item_content = " ".join(item_content)
    return item_content[:8000]


if __name__ == "__main__":
    companies_metadata = pd.read_csv("data/company_metadata.tsv", sep='\t')
    for index, (_, company_metadata) in enumerate(companies_metadata.iterrows()):
        file_path = f"data/form10ks/{company_metadata['NAME'].split(' ')[0].lower()}-{company_metadata['CIK']}.json"
        if os.path.exists(file_path):
            continue

        print(company_metadata['NAME'])
        form = get_edgar_10k(company_metadata)
        if form:
            with open(file_path, "w") as f:
                json.dump(form, f, indent=4)