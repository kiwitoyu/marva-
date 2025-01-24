import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class BiologyQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BioBot - Advanced Biology Quiz")
        self.root.geometry("600x700")
        self.root.resizable(False, False)

        # Background Image
        bg_image = Image.open("C:/Users/Tanaya/Desktop/ty internship/bluebackground.jpeg")
        bg_image = bg_image.resize((600, 700))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Bot and User Avatars
        bot_img = Image.open("C:/Users/Tanaya/Desktop/ty internship/bot.png").resize((50, 50))
        self.bot_avatar = ImageTk.PhotoImage(bot_img)

        user_img = Image.open("C:/Users/Tanaya/Desktop/ty internship/user.png").resize((50, 50))
        self.user_avatar = ImageTk.PhotoImage(user_img)

        # Chat Window
        self.chat_window = tk.Text(self.root, wrap=tk.WORD, bg="white", fg="black", font=("Arial", 12))
        self.chat_window.place(x=10, y=10, width=580, height=600)
        self.chat_window.config(state=tk.DISABLED)

        # Entry Box
        self.entry_box = tk.Entry(self.root, font=("Arial", 12))
        self.entry_box.place(x=10, y=620, width=500, height=40)

        # Send Button
        self.send_button = tk.Button(self.root, text="Send", font=("Arial", 12, "bold"), bg="#008CBA", fg="white", command=self.handle_user_input)
        self.send_button.place(x=520, y=620, width=70, height=40)

        # Questions and Answers
        self.questions = [
            {"question": "What is the powerhouse of the cell?", "answer": "mitochondria", "explanation": "Mitochondria generate energy for the cell."},
            {"question": "What is the liquid portion of blood called?", "answer": "plasma", "explanation": "Plasma carries nutrients, hormones, and waste products."},
            {"question": "Which part of the plant conducts photosynthesis?", "answer": "leaf", "explanation": "Leaves contain chloroplasts, where photosynthesis occurs."},
            {"question": "What is the basic unit of life?", "answer": "cell", "explanation": "The cell is the fundamental structural and functional unit of all living organisms."},
            {"question": "What is the largest organ in the human body?", "answer": "skin", "explanation": "Skin acts as a barrier and protects internal organs."},
        ]
        self.current_question_index = 0

        # Greet the user
        self.ask_question()

    def display_message(self, message, is_bot=True):
        
        self.chat_window.config(state=tk.NORMAL)

        if is_bot:
            self.chat_window.insert(tk.END, "\n\n")
            if self.bot_avatar:
                self.chat_window.image_create(tk.END, image=self.bot_avatar)
            self.chat_window.insert(tk.END, f" BioBot: {message}\n", ("bot",))
            self.chat_window.tag_config("bot", background="#cce7ff", foreground="#000000", font=("Arial", 12), borderwidth=5, wrap=tk.WORD)
        else:
            self.chat_window.insert(tk.END, "\n\n")
            self.chat_window.insert(tk.END, " " * 40)  # Indent to the right
            if self.user_avatar:
                self.chat_window.image_create(tk.END, image=self.user_avatar)
            self.chat_window.insert(tk.END, f" You: {message}\n", ("user",))
            self.chat_window.tag_config("user", background="#f0f0f0", foreground="#000000", font=("Arial", 12), borderwidth=5, wrap=tk.WORD)

        self.chat_window.config(state=tk.DISABLED)
        self.chat_window.yview(tk.END)

    def ask_question(self):
        
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]["question"]
            self.display_message(f"Question: {question}", is_bot=True)
        else:
            self.display_message("Quiz complete! Great job!", is_bot=True)

    def handle_user_input(self):
        
        user_input = self.entry_box.get().strip().lower()
        if not user_input:
            return

        self.display_message(user_input, is_bot=False)
        self.entry_box.delete(0, tk.END)

        # Check the answer
        correct_answer = self.questions[self.current_question_index]["answer"].lower()
        explanation = self.questions[self.current_question_index]["explanation"]

        if user_input == correct_answer:
            self.display_message("Correct! Nice job.", is_bot=True)
        else:
            self.display_message(f"Oops! The correct answer is: {correct_answer}", is_bot=True)
            self.display_message(f"Explanation: {explanation}", is_bot=True)

        # Move to the next question
        self.current_question_index += 1
        self.ask_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = BiologyQuizApp(root)
    root.mainloop()
