// ── Memory object (mirrors your memory.json) ──
const memory = { name: null, location: null, interests: [], mood: null };

// ── Sentiment keywords ──
const positiveWords = ["happy","great","awesome","love","amazing","good","excited","fantastic","wonderful","glad","joy","done","finished","proud"];
const negativeWords = ["sad","upset","angry","hate","bad","terrible","awful","frustrated","depressed","stressed","worried","worst"];

// ── Get sentiment from text ──
function getSentiment(text) {
  const t = text.toLowerCase();
  if (positiveWords.some(w => t.includes(w))) return "positive";
  if (negativeWords.some(w => t.includes(w))) return "negative";
  return "neutral";
}

// ── Update sidebar memory panel ──
function updateMemoryPanel() {
  document.getElementById("mem-name").textContent      = memory.name      || "—";
  document.getElementById("mem-location").textContent  = memory.location  || "—";
  document.getElementById("mem-interests").textContent = memory.interests.length ? memory.interests.join(", ") : "—";
  document.getElementById("mem-mood").textContent      = memory.mood      || "—";
}

// ── Extract memory from user message ──
function extractMemory(text) {
  const t = text.toLowerCase();

  if (t.includes("my name is")) {
    memory.name = text.split(/my name is/i)[1].trim().split(" ")[0];
  }
  if (t.includes("i live in") || t.includes("i am from")) {
    memory.location = text.split(/i live in|i am from/i)[1].trim().split(" ")[0];
  }
  if (t.includes("i like") || t.includes("i love")) {
    const thing = text.split(/i like|i love/i)[1].trim().split(/[.,!?]/)[0];
    if (thing && !memory.interests.includes(thing)) memory.interests.push(thing);
  }

  const sentiment = getSentiment(text);
  if (sentiment !== "neutral") memory.mood = sentiment;

  updateMemoryPanel();
}

// ── Add a message bubble to the chat ──
function addMessage(text, role) {
  const messages  = document.getElementById("messages");
  const sentiment = getSentiment(text);
  const sentClass = sentiment === "positive" ? "sent-positive"
                  : sentiment === "negative" ? "sent-negative"
                  : "sent-neutral";
  const initial = role === "user" ? "Y" : "C";

  const div = document.createElement("div");
  div.className = `msg ${role}`;
  div.innerHTML = `
    <div class="msg-avatar">${initial}</div>
    <div>
      <div class="bubble">${text}</div>
      <div class="sentiment-tag ${sentClass}">${sentiment}</div>
    </div>`;

  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

// ── Show / hide typing indicator ──
function showTyping(show) {
  const existing = document.getElementById("typing-row");
  if (existing) existing.remove();

  if (show) {
    const messages = document.getElementById("messages");
    const div = document.createElement("div");
    div.className = "msg bot";
    div.id = "typing-row";
    div.innerHTML = `
      <div class="msg-avatar">C</div>
      <div class="typing-indicator">
        <span></span><span></span><span></span>
      </div>`;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }
}

// ── Send message ──
async function sendMessage() {
  const input = document.getElementById("chatInput");
  const text  = input.value.trim();
  if (!text) return;

  input.value = "";
  input.style.height = "auto";

  addMessage(text, "user");
  extractMemory(text);
  showTyping(true);

  try {
    // calls your Flask backend
    const res  = await fetch("/chat", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ message: text, memory })
    });
    const data = await res.json();
    showTyping(false);
    addMessage(data.reply, "bot");

  } catch (err) {
    showTyping(false);
    addMessage("Sorry, I couldn't reach the server. Is app.py running?", "bot");
  }
}

// ── Enter to send, Shift+Enter for new line ──
function handleKey(e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
}

// ── Auto-grow textarea ──
function autoResize(el) {
  el.style.height = "auto";
  el.style.height = Math.min(el.scrollHeight, 100) + "px";
}

// ── Clear chat ──
function clearChat() {
  document.getElementById("messages").innerHTML = "";
  addMessage("Chat cleared! How can I help you?", "bot");
}

// ── Init ──
updateMemoryPanel();