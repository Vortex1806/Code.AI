import openai
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
key = "sk-xxxxxxxxxx"

def codecraftonepy(prompt):
    openai.api_key = key
    print(prompt)
    hey = openai.Completion.create(
        model="davinci-002",
        prompt=f"\"\"\"\nCreate a code for {prompt} \n\"\"\"\n\nPython:\n",
        temperature=0,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop = ["\"\"\""]
    )
    print(hey["choices"][0]["text"])
    return hey["choices"][0]["text"]

def codecraftonejs(prompt):
    openai.api_key = key
    print(prompt)
    hey = openai.Completion.create(
        model="davinci-002",
        prompt=f"/* create a javascript code for {prompt} */\n\n javascipt:\n",
        temperature=0,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop = ["\"\"\"", "/*", "/"]
    )
    print(hey["choices"][0]["text"])
    return hey["choices"][0]["text"]

def codecraftonec(prompt):
    openai.api_key = key
    print(prompt)
    hey = openai.Completion.create(
        model="davinci-002",
        prompt=f"/* create a C code for {prompt} */\n\n C:\n",
        temperature=0,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["/*", "/",]
    )
    print(hey["choices"][0]["text"])
    return hey["choices"][0]["text"]

def codecraftonecpp(prompt):
    openai.api_key = key
    print(prompt)
    hey = openai.Completion.create(
        model="davinci-002",
        prompt=f"/* create a cpp code for {prompt} */\n\n C++:\n",
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["/*", "/"]
    )
    print(hey["choices"][0]["text"])
    return hey["choices"][0]["text"]

def codecraftonejava(prompt):
    openai.api_key = key
    print(prompt)
    hey = openai.Completion.create(
        model="davinci-002",
        prompt=f"/*Write a java code for {prompt} */\n\n Java:\n",
        temperature=0,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["/*", "/"]
    )
    print(hey["choices"][0]["text"])
    return hey["choices"][0]["text"]



def commentaione(prompt):
    openai.api_key = key
    print(prompt)
    response = openai.Completion.create(
        model="davinci-002",
        prompt=f"\"\"\"\nAdd comments wherever necessary and rewrite the whole code\n {prompt} \"\"\"\n\n With Comments:\n",
        temperature=0,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    print(response["choices"][0]["text"])
    return response["choices"][0]["text"]

def summarizecodeone(prompt):
    openai.api_key = key
    print(prompt)
    response = openai.Completion.create(
        model="davinci-002",
        prompt=f"{prompt}\n\"\"\"\nHere's what the given function is doing:\n1.",
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\"\"\""]
    )
    print(response["choices"][0]["text"])
    return response["choices"][0]["text"]

def transcodeone(prompt,language):
    openai.api_key = key
    print(prompt)
    response = openai.Completion.create(
        model="davinci-002",
        prompt=f"#Convert To {language}: \ncode: {prompt}\n\n{language}:",
        temperature=0,
        max_tokens=250,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\"", "#"]
    )
    print(response["choices"][0]["text"])
    return response["choices"][0]["text"]


app = Flask(__name__)
CORS(app)

@app.route('/codecraftjs', methods=['PUT'])
@cross_origin()
def codecraftjs():
    input_text = request.json['prompt']
    response_text = codecraftonejs(input_text)
    print(response_text)
    return jsonify(response=response_text)

@app.route('/codecraftpy', methods=['PUT'])
@cross_origin()
def codecraftpy():
    input_text = request.json['prompt']
    response_text = codecraftonepy(input_text)
    print(response_text)
    return jsonify(response=response_text)

@app.route('/codecraftc', methods=['PUT'])
@cross_origin()
def codecraftc():
    input_text = request.json['prompt']
    response_text = codecraftonec(input_text)
    print(response_text)
    return jsonify(response=response_text)

@app.route('/codecraftcpp', methods=['PUT'])
@cross_origin()
def codecraftcpp():
    input_text = request.json['prompt']
    response_text = codecraftonecpp(input_text)
    print(response_text)
    return jsonify(response=response_text)

@app.route('/codecraftjava', methods=['PUT'])
@cross_origin()
def codecraftjava():
    input_text = request.json['prompt']
    response_text = codecraftonejava(input_text)
    print(response_text)
    return jsonify(response=response_text)

@app.route('/commentai', methods=['PUT'])
@cross_origin()
def commentai():
    input_text = request.json['prompt']
    response_text = commentaione(input_text)
    print(response_text)
    return jsonify(response= response_text )

@app.route('/summarizecode', methods=['PUT'])
@cross_origin()
def summarizecode():
    input_text = request.json['prompt']
    response_text = summarizecodeone(input_text)
    print(response_text)
    return jsonify(response="Here's what the given function is doing:\n1." + response_text)

@app.route('/transcode', methods=['PUT'])
@cross_origin()
def transcode():
    input_text = request.json['prompt']
    language_selected = request.json['language']
    print(input_text)
    response_text = transcodeone(prompt=input_text,language=language_selected)
    return jsonify(response=f"{language_selected}:\n" + response_text)

if __name__ == '__main__':
    app.run(port=4000)
