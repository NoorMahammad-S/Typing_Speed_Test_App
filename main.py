import tkinter as tk
import random
import time
import json

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        # Sample words for typing test
        self.words = ["programming", "keyboard", "challenge", "practice", "speed", "improve", "accuracy", "language", "coding", "developer", "Python", "OpenAI", "learning", "project", "creative"]

        # Initialize class variables
        self.current_word = ""
        self.start_time = None

        # GUI elements
        self.typing_entry = tk.Entry(root, font=("Arial", 20))
        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.start_button = tk.Button(root, text="Start", command=self.start_typing_test)
        self.show_score_button = tk.Button(root, text="Show High Scores", command=self.show_high_scores)
        self.difficulty_label = tk.Label(root, text="Difficulty:")
        self.difficulty_var = tk.StringVar()
        self.difficulty_menu = tk.OptionMenu(root, self.difficulty_var, "Easy", "Medium", "Hard")
        self.timer_label = tk.Label(root, text="Timer: 60s")

        # Place GUI elements on the window
        self.typing_entry.pack(pady=10)
        self.result_label.pack()
        self.start_button.pack()
        self.show_score_button.pack()
        self.difficulty_label.pack()
        self.difficulty_menu.pack()
        self.timer_label.pack()

        # Load high scores from a file
        self.high_scores = self.load_high_scores()

    def start_typing_test(self):
        # Choose a random word for the typing test
        self.current_word = random.choice(self.words)

        # Clear the entry field and enable it for typing
        self.typing_entry.delete(0, tk.END)
        self.typing_entry.config(state="normal")
        self.typing_entry.focus_set()

        # Record the start time and disable the "Start" button
        self.start_time = time.time()
        self.start_button.config(state="disabled")

        # Bind the Enter key to check typing speed
        self.root.bind("<Return>", self.check_typing_speed)

        # Start the countdown timer (60 seconds)
        self.update_timer(60)

    def check_typing_speed(self, event):
        # Calculate the user's typing speed and accuracy
        user_input = self.typing_entry.get()
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        words_per_minute = len(user_input.split()) / (elapsed_time / 60) if elapsed_time > 0 else 0
        accuracy = self.calculate_accuracy(user_input, self.current_word)

        # Display the results
        result_text = f"Speed: {words_per_minute:.2f} WPM, Accuracy: {accuracy:.2%}"
        self.result_label.config(text=result_text)

        # Disable the entry field, enable the "Start" button, and unbind the Enter key
        self.typing_entry.config(state="disabled")
        self.start_button.config(state="normal")
        self.root.unbind("<Return>")

        # Update the high scores based on the user's performance
        self.update_high_scores(words_per_minute)

    def update_timer(self, seconds):
        # Update the countdown timer on the GUI
        if seconds >= 0:
            self.timer_label.config(text=f"Timer: {seconds}s")
            self.root.after(1000, lambda: self.update_timer(seconds - 1))
        else:
            # When the timer reaches zero, disable the entry field and enable the "Start" button
            self.typing_entry.config(state="disabled")
            self.start_button.config(state="normal")

    def calculate_accuracy(self, user_input, target_word):
        correct_characters = sum(c1 == c2 for c1, c2 in zip(user_input, target_word))
        return correct_characters / max(len(target_word), len(user_input))

    def show_high_scores(self):
        high_scores_window = tk.Toplevel(self.root)
        high_scores_window.title("High Scores")
        high_scores_label = tk.Label(high_scores_window, text="High Scores", font=("Arial", 16))
        high_scores_label.pack()

        for difficulty, scores in self.high_scores.items():
            score_label = tk.Label(high_scores_window, text=f"{difficulty} Difficulty:", font=("Arial", 14))
            score_label.pack()

            if not scores:
                no_scores_label = tk.Label(high_scores_window, text="No scores yet", font=("Arial", 12))
                no_scores_label.pack()
            else:
                for i, score in enumerate(scores, start=1):
                    score_text = f"{i}. {score} WPM"
                    score_label = tk.Label(high_scores_window, text=score_text, font=("Arial", 12))
                    score_label.pack()

    def load_high_scores(self):
        try:
            with open("high_scores.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"Easy": [], "Medium": [], "Hard": []}

    def save_high_scores(self):
        with open("high_scores.json", "w") as file:
            json.dump(self.high_scores, file)

    def update_high_scores(self, score):
        # Update the high scores for the selected difficulty level
        difficulty = self.difficulty_var.get()
        if score > 0:
            self.high_scores[difficulty].append(score)
            self.high_scores[difficulty].sort(reverse=True)
            self.high_scores[difficulty] = self.high_scores[difficulty][:5]  # Keep the top 5 scores
            self.save_high_scores()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
