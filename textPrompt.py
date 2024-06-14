import vertexai
from vertexai.generative_models import GenerativeModel

# TODO(developer): Update and un-comment below line
project_id = "radiant-snow-426403-b4"

vertexai.init(project=project_id, location="us-central1")

model = GenerativeModel(model_name="gemini-1.5-flash-001")
prompt = "What is the meaning of life?"

response = model.generate_content(prompt)

print(response.text)