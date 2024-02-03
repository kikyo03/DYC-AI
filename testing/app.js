function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatMessages = document.getElementById('chatMessages');

    if (userInput.value.trim() !== '') {
        const userMessage = document.createElement('div');
        userMessage.className = 'message user';
        userMessage.textContent = userInput.value;
        chatMessages.appendChild(userMessage);

        // Simulate a response from the chatbot (you can replace this with actual ChatGPT logic)
        const chatbotMessage = document.createElement('div');
        chatbotMessage.className = 'message chatbot';
        chatbotMessage.textContent = 'This is a ChatGPT response.';
        chatMessages.appendChild(chatbotMessage);

        // Clear the input field after sending the message
        userInput.value = '';

        // Scroll to the bottom of the chat messages
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const chatContainer = document.querySelector('.chat-container');
    const arrowButton = document.querySelector('.toggle-sidebar');

    sidebar.classList.toggle('minimized');
    chatContainer.classList.toggle('expanded');

    // Toggle the arrow direction
    arrowButton.textContent = sidebar.classList.contains('minimized') ? '→' : '←';
}

let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
  arrow[i].addEventListener("click", (e)=>{
 let arrowParent = e.target.parentElement.parentElement;//selecting main parent of arrow
 arrowParent.classList.toggle("showMenu");
  });
}

let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", ()=>{
  sidebar.classList.toggle("close");
});


