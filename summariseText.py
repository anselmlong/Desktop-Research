import requests
import sys
from bs4 import BeautifulSoup
import vertexai
from vertexai.generative_models import GenerativeModel
import time
from openURLsFromQuery import getURLsFromQuery
import os

# Initialize Vertex AI
project_id = os.getenv("PROJECT_ID")  # Your project ID here
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel(model_name="gemini-1.5-flash-001")
chat = model.start_chat()

initialPrompt = """You are a chatbot that summarises content. 
I'm looking to conduct research on the capabilities of certain technologies, including their use cases.
Summarize the following texts while keeping in mind the key points and the context of the text. 
Summarise the text in this form:
Title: [Title of the text]
Date of publication: [Date of publication]
Summary: [Summary of the text]
URL: [URL of the text]
Please summarize the following texts:
"""
# restructure this to take in a query from the command line, but throw error if no argument is passed
query = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else sys.exit("No query provided.")

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

urls = getURLsFromQuery(query)

# Extract and summarize text from each URL
for url in urls:
    print("Extracting text from", url)
    extracted_text = extract_text_from_url(url)
    summarized_text = invoke(extracted_text)
    write_text_to_file(summarized_text)

print("Text extraction and summarization completed.")
