from apify_client import ApifyClient
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import sys
import requests
import vertexai
from vertexai.generative_models import GenerativeModel
import webbrowser

# Load environment variables from .env file
load_dotenv()

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN")
PROJECT_ID = os.getenv("PROJECT_ID")

vertexai.init(project= PROJECT_ID, location="us-central1")

model = GenerativeModel(model_name="gemini-1.0-pro")

# Initialize the ApifyClient with your API token
client = ApifyClient(APIFY_TOKEN)
results_per_page = 1
def getURLsFromQuery(query):
    # Prepare the Actor input
    run_input = {
        "queries": query,
        "resultsPerPage": results_per_page,
        "maxPagesPerQuery": 1,
        "languageCode": "",
        "mobileResults": False,
        "includeUnfilteredResults": False,
        "saveHtml": False,
        "saveHtmlToKeyValueStore": False,
        "includeIcons": False,
    }

    # Run the Actor and wait for it to finish
    run = client.actor("nFJndFXA5zjCTuudP").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    data = client.dataset(run["defaultDatasetId"]).list_items().items

    return [result["url"] for result in data[0]["organicResults"]]

def getDescsFromQuery(query):
    # Prepare the Actor input
    run_input = {
        "queries": query,
        "resultsPerPage": results_per_page,
        "maxPagesPerQuery": 1,
        "languageCode": "",
        "mobileResults": False,
        "includeUnfilteredResults": False,
        "saveHtml": False,
        "saveHtmlToKeyValueStore": False,
        "includeIcons": False,
    }

    # Run the Actor and wait for it to finish
    run = client.actor("nFJndFXA5zjCTuudP").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    data = client.dataset(run["defaultDatasetId"]).list_items().items

    return [result["description"] for result in data[0]["organicResults"]]

# Function to extract text from a URL
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    except Exception as e:
        return f"Error extracting text from {url}: {e}"

def openURLs(urls):
    for url in urls:
        print('Opening', url)
        webbrowser.open(url)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Please provide a number and query in the format 'python openURLs.py <number> <query>'.")

    results_per_page = int(sys.argv[1])
    query = ' '.join(sys.argv[2:])

    urls = getURLsFromQuery(query)
    openURLs(urls)

