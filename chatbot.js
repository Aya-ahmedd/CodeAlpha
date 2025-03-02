function sendMessage() {
  let userInput = document.getElementById("user-input").value;
  if (userInput.trim() === "") return;

  let chatBox = document.getElementById("chat-box");

  // Display user message
  let userMessage = document.createElement("div");
  userMessage.className = "user-message";
  userMessage.innerText = userInput;
  chatBox.appendChild(userMessage);

  // Clear input field
  document.getElementById("user-input").value = "";

  // Auto-scroll to bottom
  chatBox.scrollTop = chatBox.scrollHeight;

  // Simulated bot response
  setTimeout(() => {
      let botMessage = document.createElement("div");
      botMessage.className = "bot-message";
      botMessage.innerText = getBotResponse(userInput);
      chatBox.appendChild(botMessage);
      chatBox.scrollTop = chatBox.scrollHeight;
  }, 1000);
}

// Simple bot responses (you can replace this with an AI API)
function getBotResponse(input) {
  input = input.toLowerCase();
  if (input.includes("hello")) {
      return "Hi there! How can I help?";
  } else if (input.includes("how are you")) {
      return "I'm just a bot, but I'm doing great! What about you?";
  } else if (input.includes("bye")) {
      return "Goodbye! Have a nice day.";
  } else {
      return "I'm not sure how to respond to that. Can you ask something else?";
  }
}