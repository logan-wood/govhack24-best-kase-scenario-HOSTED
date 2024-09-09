function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

async function askGemini() {
    const SERVER_DOMAIN = 'http://127.0.0.1:8000'

    const crashData = localStorage.getItem("crashData")

    console.log(crashData)
    
    if (!crashData) {
        console.log("data does not exist")
        return
    }

    document.getElementById('loading').style.display = "inline"


    const response = await fetch(`${SERVER_DOMAIN}/askGemini`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: crashData
    })

    console.log(response)
    const ai_response = await response.text();
    document.getElementById('ai-response').innerText = ai_response

    document.getElementById('loading').style.display = "none"

    document.getElementById('pdf').style.display = "inline"
}