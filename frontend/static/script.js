document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chat-form");
    const chatHistory = document.getElementById("chat-history");
    const userInput = document.getElementById("user-input");

    chatForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        // Get user input
        const message = userInput.value.trim();
        if (!message) return;

        // Add user message to chat history
        addMessageToChat("user-message", message);

        // Send message to backend
        try {
            const response = await fetch("/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message }),
            });

            const data = await response.json();
            if (data.reply) {
                addMessageToChat("bot-response", data.reply);
            } else {
                addMessageToChat("bot-response", "I'm sorry, I couldn't understand your query.");
            }
        } catch (error) {
            addMessageToChat("bot-response", "There was an error connecting to the server. Please try again.");
        }

        // Clear user input
        userInput.value = "";
    });

    function addMessageToChat(className, text) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add(className);
        messageDiv.textContent = text;
        chatHistory.appendChild(messageDiv);
        chatHistory.scrollTop = chatHistory.scrollHeight; // Scroll to the latest message
    }
});
