# [DEPRECATED]
# PyrateGPT

A pirated-ish version of the ChatGPT API for test uses and small personal use projects.



## Important

This isn't meant for commercial use and probably isn't optimized/fit enough for it, only use for personal projects for when you aren't sure if you're gonna commit to the project or not.

## API Reference
####
```
host = localhost
port = config.json->port 
```
#### Get all items
```http
  GET /ask
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `prompt` | `string` | **Required**. Your prompt. |
| `pretty` | `bool` | Shows the formatted response. |
| `raw` | `bool` | Shows the raw response. |

#### Get the last response

```http
  GET /last
```

## Run Locally

1. Create a fresh Chrome profile.

```bash
start chrome.exe --user-data-dir="x/x/PyrateGPTProfile"
```

2. Clone the project

```bash
  git clone https://github.com/cvcvka5/PyGPT
```

3. Go to the project directory

```bash
  cd PyGPT
```

4. Install the dependencies

```bash
  pip install -r requirements.txt
```

5. Check *config.json* for some tweaks.

6. Start the server

```bash
  python pygpt-server.py
```

7. Log-in to (or create) your ChatGPT account (don't worry its persistent).

8. Manually switch to (or create a new) chat with ChatGPT. (for captcha prevention)

## Customization (config.json)

To run this project, you will need to add the following environment variables to your .env file

```json
{
    "initPrompt (REQUIRED)": "The prompt that is sent on initialization you can make this null if you don't want to send an initialization prompt.",
    "scriptJS (REQUIRED)": "The script that initializes the javascript end for this project, you can add some additional js code if needed or the project is outdated.",
    "scriptJSPlaceholder (REQUIRED)": "The placeholder in inject.js that gets replaced on function calls for the bot to function.",
    "profilePath (REQUIRED)": "Chrome profile path",
    "limiter (REQUIRED)": "The server request limiter 'flask_limiter' that returns an error message if the user makes to many GET calls to the endpoint.",
    "port (REQUIRED)": "The port for the Flask endpoint to be hosted.",
    "GPTChatURL": "A ChatGPT chat URL for the browser to redirect to. (if you're lazy or want to keep a persistent chat that you don't want to miss)"
}
```


## Known Issues
The server returns an empty string if the bot's response is in a pop-up bubble (this happens on really long text and the given init prompt mostly fixes this).


---
### Authors
- [@cvcvka5](https://www.github.com/cvcvka5)


[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
