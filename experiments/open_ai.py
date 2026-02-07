# openai

import openai
from opennn import openai_key
openai.api_key = openai_key
def motivational_lines():
    prompt="tell few  motivational lines"
    response= openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "tell few motivational lines"}
        ]
    )
    print(response.choice[0]["message"]["content"])

if __name__ =="__main__":
    motivational_lines()



# gemini
import google.generativeai as genai
from gemini_key import api_key  # assuming you have your API key in this file

# Configure API key
genai.configure(api_key=api_key)

# Use Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")  

response = model.generate_content("What is linkedin about? Why do we use it?")

print(response.text)