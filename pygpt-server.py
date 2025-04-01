from gevent import monkey
monkey.patch_all()

from flask import Flask, request, jsonify
from pygpt import PyGPT
from sys import argv
from flask_limiter import Limiter

gpt = PyGPT(fjs_base=open("./util/frame.txt", "r"), js_base_holder="//##PYGPT##", debug=True,
            finitprompt=open("./util/initprompt.txt"))

app = Flask(__name__)
limiter = Limiter(
    key_func = lambda: True,
    app=app
)


@app.route('/send', methods=['GET'])
@limiter.limit("1 per 5 seconds", error_message='1 per 5 seconds')
def send_prompt():
    prompt = request.args["prompt"]
    gpt.ask(prompt=prompt)
    
    return jsonify({"status": "okay"})

@app.route('/ask', methods=['GET'])
@limiter.limit("1 per 5 seconds", error_message='1 per 5 seconds')
def ask_prompt():
    prompt = request.args["prompt"]
    raw = "raw" in request.args.keys()
    pretty = "pretty" in request.args.keys()
    
    response = gpt.ask(prompt=prompt)
    
    if pretty: return response.replace("\n", "<br>")
    if raw: return response
    return jsonify({"response": response, "status": "okay"})

@app.route('/last', methods=['GET'])
def last_message():
    raw = "raw" in request.args.keys()
    pretty = "pretty" in request.args.keys()

    if pretty: return gpt.lastMessage.replace("\n", "<br>") 
    if raw: return gpt.lastMessage
    return jsonify({"response": gpt.lastMessage})

if __name__ == "__main__":
    try:
        port = int(argv[1])
    except IndexError:
        port = 1821

    app.run(port=port)