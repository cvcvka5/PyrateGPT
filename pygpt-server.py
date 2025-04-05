from gevent import monkey
monkey.patch_all()

from flask import Flask, request, jsonify
from pygpt import PyGPT
from flask_limiter import Limiter
import time
import json
import os.path


# Default Config
# {
#     "initPrompt": "util/initprompt.txt",
#     "scriptJS": "util/inject.js",
#     "scriptJSPlaceholder": "//##PYGPT##",
#     "profilePath": "C:/selenium/ChromeProfile",
#     "limiter": "1 per 5 seconds",
#     "port": 1821,
#     "GPTChatURL": null
# }
#
config = None
if os.path.exists("config.json"):
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

customGPThat = config["GPTChatURL"]

gpt = PyGPT(fjs_base=open(config["scriptJS"], "r"), js_base_holder=config["scriptJSPlaceholder"], 
            finitprompt=open(config["initPrompt"]), profilepath=config["profilePath"], gptchaturl=config["GPTChatURL"],
            debug=True)

app = Flask(__name__)
limiter = Limiter(
    key_func = lambda: True,
    app=app
)

@app.route('/ask', methods=['GET'])
@limiter.limit(config["limiter"], error_message=config["limiter"])
def ask_prompt():
    last_response = gpt.lastMessage
    
    prompt = request.args["prompt"]
    raw = "raw" in request.args.keys()
    pretty = "pretty" in request.args.keys()
    
    
    response = gpt.ask(prompt=prompt)
        
    if response == last_response:
        time.sleep(2)
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
    app.run(port=config["port"])