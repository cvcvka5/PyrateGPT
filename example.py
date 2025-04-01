from requests import get
import time

# time limit -> 5 seconds

# webhook link
# webhook.site
WEBHOOK = "https://webhook.site/dceb2fc7-309d-4bab-8d10-096edda3342b?interesting={fact}"

while True:
    resp = get("http://localhost:1821/ask?prompt=tell me something i dont know make it interesting")
    data = resp.json()
    info = data["response"]
    get(WEBHOOK.format(fact=info))
    print(info, "\n")
    
    time.sleep(5)