from apify_client import ApifyClient
from bs4 import BeautifulSoup
import requests
import vertexai
from vertexai.generative_models import GenerativeModel
import webbrowser

# TODO(developer): Update and un-comment below line
project_id = "radiant-snow-426403-b4"

vertexai.init(project=project_id, location="us-central1")

model = GenerativeModel(model_name="gemini-1.0-pro")


# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_mng3qXg5oUW4rbFeuh0oJi9KBTfRGn0bNYda")

def getURLsFromQuery(query):
    # Prepare the Actor input
    run_input = {
        "queries": query,
        "resultsPerPage": 10,
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

queries = """gemini vertex ai use cases case study singapore"""

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

