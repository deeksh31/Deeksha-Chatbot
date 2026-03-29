import tkinter as tk
import random
import datetime

# ---------------- MAIN CHATBOT WINDOW ---------------- #
def open_chatbot():
    welcome_screen.destroy()

    global root, chat_window, entry, send_btn

    root = tk.Tk()
    root.title("Deeksha's Chatbot 🤖")
    root.geometry("420x550")
    root.configure(bg="#0f172a")

    def show_welcome():
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "🤖 Bot: Hello Deeksha! 💙\n", "bot")
        chat_window.insert(tk.END, "🤖 Bot: How can I help you today? 😊\n\n", "bot")
        chat_window.config(state=tk.DISABLED)

    def clear_placeholder(event):
        if entry.get() == "Type your message...":
            entry.delete(0, tk.END)

    def show_bot_message(response):
        chat_window.config(state=tk.NORMAL)
        chat_window.delete("end-2l", "end-1l")
        chat_window.insert(tk.END, "🤖 Bot: " + response + "\n\n", "bot")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)

    def bot_reply(response):
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "🤖 Bot is typing...\n", "bot")
        chat_window.config(state=tk.DISABLED)
        root.after(1000, lambda: show_bot_message(response))

    def send_message(event=None):
        user_input = entry.get().strip()
        if user_input == "" or user_input == "Type your message...":
            return

        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "👩 You: " + user_input + "\n", "user")
        entry.delete(0, tk.END)

        msg = user_input.lower()

        if msg == "hello":
            response = "Hi there! 😊"
        elif "time" in msg:
            response = "Current time is " + datetime.datetime.now().strftime("%H:%M ⏰")
        elif "date" in msg:
            response = "Today's date is " + datetime.datetime.now().strftime("%d %B %Y 📅")
        elif "joke" in msg:
            response = random.choice([
                "Why do programmers hate bugs? Because they bug them 🐛😂",
                "I told my computer I needed a break... it froze 😅"
            ])
        elif msg == "bye":
            response = "Goodbye! 👋"
        else:
            response = random.choice([
                "Hmm 🤔 I didn't understand that.",
                "Try asking something else 😊"
            ])

        chat_window.config(state=tk.DISABLED)
        bot_reply(response)

    # UI
    title = tk.Label(root, text="💬 Chatbot",
                     font=("Segoe UI", 16, "bold"),
                     bg="#0f172a", fg="white")
    title.pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    chat_window = tk.Text(frame,
                          wrap=tk.WORD,
                          yscrollcommand=scrollbar.set,
                          bg="#f8fafc",
                          fg="#0f172a",
                          font=("Segoe UI", 12),
                          bd=0)
    chat_window.pack(fill=tk.BOTH, expand=True)

    scrollbar.config(command=chat_window.yview)
    chat_window.config(state=tk.DISABLED)

    chat_window.tag_config("user",
                           foreground="white",
                           background="#22c55e",
                           lmargin1=50, lmargin2=10, rmargin=10)

    chat_window.tag_config("bot",
                           foreground="black",
                           background="#e2e8f0",
                           lmargin1=10, lmargin2=10, rmargin=50)

    entry_frame = tk.Frame(root, bg="#0f172a")
    entry_frame.pack(padx=10, pady=10, fill=tk.X)

    entry = tk.Entry(entry_frame, font=("Segoe UI", 14))
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

    entry.insert(0, "Type your message...")
    entry.bind("<FocusIn>", clear_placeholder)
    entry.bind("<Return>", send_message)

    send_btn = tk.Button(entry_frame, text="Send", command=send_message)
    send_btn.pack(side=tk.RIGHT)

    root.after(500, show_welcome)
    root.mainloop()


# ---------------- OPENING SCREEN ---------------- #
welcome_screen = tk.Tk()
welcome_screen.title("Welcome 🤖")
welcome_screen.geometry("420x550")
welcome_screen.configure(bg="#0f172a")

# Animated text
text_label = tk.Label(welcome_screen,
                      text="",
                      font=("Segoe UI", 18, "bold"),
                      bg="#0f172a",
                      fg="white")
text_label.pack(pady=100)

full_text = "Welcome to Deeksha's Chatbot 🤖✨"

def animate_text(index=0):
    if index <= len(full_text):
        text_label.config(text=full_text[:index])
        welcome_screen.after(50, animate_text, index + 1)

animate_text()

# Subtitle
sub_text = tk.Label(welcome_screen,
                    text="Your smart assistant 💙",
                    font=("Segoe UI", 12),
                    bg="#0f172a",
                    fg="#94a3b8")
sub_text.pack(pady=10)

# Start Button
start_btn = tk.Button(welcome_screen,
                      text="Start Chat 🚀",
                      font=("Segoe UI", 12, "bold"),
                      bg="#2563eb",
                      fg="white",
                      padx=20, pady=10,
                      command=open_chatbot)
start_btn.pack(pady=40)

welcome_screen.mainloop()