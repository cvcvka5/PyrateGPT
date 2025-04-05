from pygpt import PyGPT


gpt = PyGPT(fjs_base=open("./util/frame.txt", "r"), js_base_holder="//##PYGPT##", debug=True, finitprompt=None)

while True:
    print("out:", gpt.ask(input("sor")))
    print()