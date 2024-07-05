from apify_client import ApifyClient
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import sys
import requests
import vertexai
from vertexai.generative_models import GenerativeModel
import webbrowser
from openURLs import getURLsFromQuery, extract_text_from_url, getDescsFromQuery

results_per_page = 1
# open companyNames.txt and read content per line
with open('companyNames.txt', 'r') as f:
    company_names = f.readlines()

# for each line, search the company name on Google and get the description of the company
company_descriptions = []
for company_name in company_names:
    print (company_name)
    # perform Google search and extract description
    description = getDescsFromQuery(company_name)
    print (description)
    company_descriptions.append((company_name.strip(), description))

# write the company name and description to a new file, companyDescriptions.txt
with open('companyDescriptions.txt', 'w') as f:
    for company_name, description in company_descriptions:
        f.write(f'{company_name}: {description}\n')

# close both files
f.close()
