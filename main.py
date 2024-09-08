import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
import argparse


def search_gsmarena(phone_model):
    base_url = "https://www.gsmarena.com/res.php3?sSearch="
    
    search_url = base_url + urllib.parse.quote(phone_model)
    response = requests.get(search_url)
    
    # If the search itself was successful
    if response.status_code != 200:
        print("Failed to retrieve the search results")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', class_='makers')
    
    if not search_results:
        print(f"No phone model: {phone_model} found")
        return None

    first_result = search_results[0].find('a')
    
    if first_result:
        phone_link = first_result['href']
        full_phone_url = "https://www.gsmarena.com/" + phone_link
        return full_phone_url
    else:
        print(f"No phone model: {phone_model} found")
        return None

def extract_models_from_page(url):
    response = requests.get(url)
    
    # check sucess
    if response.status_code != 200:
        print("Cannot access the page!")
        return None
    
    print("Parsing GSMArena page ...")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find model aliases
#    specs_table = soup.find('table', {'class': 'specs-table'})
    models_td = soup.find('td', {'data-spec': 'models'})
    
    if models_td:
#        models_row = specs_table.find('td', string='Models')
#        if models_row:
#        models_text = models_row.find_next_sibling('td').text.strip()
#        model_number = models_row.find_next_sibling('td').text.strip()
#        return model_number
        models_text = models_td.text.strip()
        models = models_text.split(', ')
        return models
            
#        else:
#            print(f"Models not found in page {url}")
#            return None
            
    else:
        print(f"Cannot extract specs table for {url}")
        return None
        
        
def build_regex_from_models(specific_models):
    # Only specific regex patterns supported for now
    regex_pattern = '|'.join(re.escape(model) for model in specific_models)
    return regex_pattern
    
    
#def search_and_extract_models(phone_model):
#    phone_page_url = search_gsmarena(phone_model)
#    
#    if phone_page_url:
#        print(f"Phone page found: {phone_page_url}")
#        models = extract_models_from_page(phone_page_url)
#        
#        if models:
#            print(f"Models found: {models}")
#            regex_pattern = build_regex_from_models(models)
#            print(f"Regex pattern for specific models: {regex_pattern}")
#        else:
#            print("No models found on the page")
#    else:
#        print("No phone page found")


def main(args):
    if args.url:
        print(f"Extracting models from URL: {args.url}")
        models = extract_models_from_page(args.url)
        if models:
            print(f"Models found: {models}")
            regex_pattern = build_regex_from_models(models)
            print(f"Regex pattern: {regex_pattern}")
        else:
            print("No models found on the page.")
    
    elif args.model:
        print(f"Searching for phone model: {args.model}")
        phone_page_url = search_gsmarena(args.model)
        
        if phone_page_url:
            print(f"Phone page found: {phone_page_url}")
            models = extract_models_from_page(phone_page_url)
            
            if models:
                print(f"Models found: {models}")
                regex_pattern = build_regex_from_models(models)
                print(f"Regex pattern: {regex_pattern}")
            else:
                print("No models found on the page.")
        else:
            print("No phone page found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract phone models and generate regex from GSMArena.")
    
    parser.add_argument('--url', type=str, help="GSMArena phone model URL to extract models from")
    parser.add_argument('--model', type=str, help="Phone model name to search on GSMArena and extract models from")

    args = parser.parse_args()
    
    main(args)
