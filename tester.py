from requests import get


a = get("http://localhost:1821/ask?raw&prompt=15 minus 14=?").text
print(a)
b = get("http://localhost:1821/ask?raw&prompt=12 plus 12=?").text
print(b)