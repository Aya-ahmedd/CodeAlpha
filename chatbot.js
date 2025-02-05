document.getElementById('send-btn').addEventListener('click', function() {
  const userInput = document.getElementById('user-input').value;
  if (userInput.trim() === "") return;
  addMessage(userInput, 'user');
  getChatbotResponse(userInput);
  document.getElementById('user-input').value = "";
});

function addMessage(message, sender) {
  const chatArea = document.getElementById('chat-area');
  const messageDiv = document.createElement('div');
  messageDiv.classList.add(sender);
  messageDiv.textContent = message;
  chatArea.appendChild(messageDiv);
  chatArea.scrollTop = chatArea.scrollHeight;
}

function getChatbotResponse(userQuery) {
  fetch('http://127.0.0.1:5000/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "user_input": userQuery })
  })
  .then(response => response.json())
  .then(data => addMessage(data.response, 'bot'))
  .catch(error => {
    console.error('Error:', error);
    addMessage("There was an error with the chatbot.", 'bot');
  });
}
