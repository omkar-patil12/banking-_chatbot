function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    let chatlog = document.getElementById("chatlog");

    chatlog.innerHTML += `<p><b>You:</b> ${userInput}</p>`;
    document.getElementById("userInput").value = "";

    fetch('/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'message': userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatlog.innerHTML += `<p><b>Bot:</b> ${data.response}</p>`;
        chatlog.scrollTop = chatlog.scrollHeight;
    });
}
