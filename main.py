import openai
from flask import *

openai.api_type = "azure"
openai.api_base = "https://hackmee1-fc.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "a2f35be0feb04e2187945ef2e7c03b0b"

app = Flask(__name__)


@app.route("/", methods=['POST'])
def f1():
    json = request.get_json()
    inputString = json["input_string"]
    message = "Answer in single word Categorise the statement " + inputString + " into the following search / buy / scroll down / scroll up  / exit"
    print(message)
    response = openai.ChatCompletion.create(
        engine="TheGeneratorsGPT35",
        messages=[
            {"role": "user", "content": message}
        ]
        ,
        temperature=0.3,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    userIntent = response.choices[0].message.content
    print("Intent : " + userIntent)
    return userIntent


if __name__ == '__main__':
    app.run(port=7777)
