from playwright.sync_api import sync_playwright
import os


class PyGPT:
    def __init__(self, fjs_base, js_base_holder, finitprompt, profilepath, gptchaturl=None, debug=False):
        self._base = (fjs_base.read(), js_base_holder)
        fjs_base.close()
        
        os.system('start chrome.exe --remote-debugging-port=9222 --user-data-dir="{profile}"'.format(profile=profilepath))
        
        if debug: print("Launched chrome debugger.")
            
        self._p = sync_playwright().start()
        self._b = self._p.chromium.connect_over_cdp("http://localhost:9222")
        self._ctx = self._b.contexts[0]
        self._page = self._ctx.pages[0]
        self._page.goto("https://chatgpt.com")
        if gptchaturl:
            self._page.goto(gptchaturl)
        input("Logged-in to ChatGPT account and on a chat page? (Enter)")
        if finitprompt:
            self.ask(finitprompt.read())
            finitprompt.close()

        
    def _basetocode(self, code: str) -> str:
        return self._base[0].replace(self._base[1], code)

    def send(self, prompt: str) -> None:
        self._page.evaluate_handle(self._basetocode("sendPrompt(`{prompt}`)"))

    def ask(self, prompt: str) -> str:
        return str(self._page.evaluate_handle(self._basetocode(f"return askPrompt(`{prompt}`)")))
    
    @property
    def lastMessage(self) -> str:
        return str(self._page.evaluate_handle(self._basetocode(f"return getLastMessage()")))