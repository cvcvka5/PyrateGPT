() => {
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    function _setPrompt(txt) {
        const p = document.createElement("p")
        p.textContent = txt
        const inputArea = document.querySelector("#prompt-textarea")
        inputArea.querySelector("p").remove()
        inputArea.appendChild(p)
    }

    function _flushPrompt() {
        document.querySelector("button#composer-submit-button").click()
    }

    // Errors mostly stem from here
    function isReadyToRead() {
        msg = getLastMessage()
        const writingOrDone = !(msg.charCodeAt(0) == 8203 || msg == "\n")
        const notWriting = !(document.querySelector(".streaming-animation") != null || document.querySelector("*[class*=fadeIn]") != null)
        return writingOrDone && notWriting
    }

    // Errors mostly stem from here
    function getLastMessage() {
        const msgs = document.querySelectorAll("article")
        const ps = msgs[msgs.length-1].querySelectorAll("p")
        let out = ""
        for (let i = 0; i < ps.length; i++) {
            out += ps[i].innerText+"\n"
        }
        return out
        
    }

    function sendPrompt(prompt) {
        _setPrompt(prompt)
        setTimeout(_flushPrompt, 50)
    }

    async function askPrompt(prompt) {
        sendPrompt(prompt)
        await sleep(2000)
        return new Promise(async resolve => {
            while (!isReadyToRead()) { 
                await sleep(100)
            }
            await sleep(500)
            resolve(getLastMessage())   
        })
    }
    
    //##PYGPT##
}