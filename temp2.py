import openai
from flask import *
from flask_cors import CORS

openai.api_type = "azure"
openai.api_base = "https://hackmee1-fc.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "a2f35be0feb04e2187945ef2e7c03b0b"

app = Flask(__name__)
CORS(app)

input_string = "show some red dress"
message ="Answer in single word. Categorise the statement  for shopping app user input " + input_string + " into the following search / buy / pick  / scroll down / scroll up  / exit "
response = openai.ChatCompletion.create(
    engine="TheGeneratorsGPT35-16k",
    messages=[
        {"role": "user", "content": message},
        {"role": "system", "content": "A shopping app where user is searching by voice. Search means user is trying to query for a product "},
        {"role": "system", "content":" Exit means he wants to end the conversation. Pick means he wants to select a particular one based on the index of the item or the description of the product . Buy means user likes it and  ready to take the product"}
    ]
    ,
    temperature=0.3,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)
x = response.choices[0].message.content
print(x)
