import vertexai
from vertexai.generative_models import GenerativeModel
import os

# TODO(developer): Update and un-comment below line
project_id = os.getenv("PROJECT_ID") 

vertexai.init(project=project_id, location="us-central1")

model = GenerativeModel(model_name="gemini-1.5-flash-001")
prompt = "What is the meaning of life?"

response = model.generate_content(prompt)

print(response.text)