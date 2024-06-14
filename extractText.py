import requests
from bs4 import BeautifulSoup
import vertexai
from vertexai.generative_models import GenerativeModel
import time
from apify import getURLsFromQuery

# Initialize Vertex AI
project_id = "radiant-snow-426403-b4"  # Your project ID here
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel(model_name="gemini-1.5-flash-001")
chat = model.start_chat()

initialPrompt = """You are my personal summarizer. I work in IMDA, and I'm looking to conduct research on the capabilities of certain technologies, including their use cases and 
applicability to Singapore. Summarize the following texts while keeping in mind the key points and the context of the text. Don't add asterisks to the texts, 
as I plan to copy the content to a Google 
Document."""

query = 'applications vertex ai gemini nano singapore use cases case study'

chat.send_message(initialPrompt, stream=True)

def get_response_from_prompt(prompt):
    response = chat.send_message(prompt)
    return response.text

# Function to extract text from a URL
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    except Exception as e:
        return f"Error extracting text from {url}: {e}"

def invoke(text):
    completed = False
    sleep_time = 2
    attempts = 0
    while not completed:
        try:
            response = get_response_from_prompt(text)
            completed = True
        except Exception as e:
            print(f"Exception occurred: {e}")
            attempts += 1
            if attempts > 5:
                print("Too many exceptions, exiting.")
                break
            time.sleep(sleep_time)
            sleep_time *= 2
    return response

def write_text_to_file(text):
    with open('text.txt', 'a') as file:
        file.write(text + "\n")


text = ''

# Assume you have a function to get URLs from a query
# For demonstration, this will be a placeholder list of URLs
urls = getURLsFromQuery(query)

# Extract and summarize text from each URL
for url in urls:
    extracted_text = extract_text_from_url(url)
    summarized_text = invoke(extracted_text)
    write_text_to_file(summarized_text)

print("Text extraction and summarization completed.")
