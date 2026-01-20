import tkinter as tk
import random
from tkinter import messagebox

# Game settings
ROWS = 4
COLS = 4
TIME_LIMIT = 60  # seconds

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game")

        self.cards = list("AABBCCDDEEFFGGHH")
        random.shuffle(self.cards)

        self.buttons = []
        self.first_card = None
        self.second_card = None
        self.matched = 0
        self.time_left = TIME_LIMIT

        self.timer_label = tk.Label(root, text=f"Time Left: {self.time_left}s", font=("Arial", 14))
        self.timer_label.grid(row=0, column=0, columnspan=COLS)

        self.create_board()
        self.update_timer()

    def create_board(self):
        index = 0
        for r in range(ROWS):
            for c in range(COLS):
                btn = tk.Button(
                    self.root,
                    text="?",
                    width=6,
                    height=3,
                    font=("Arial", 14),
                    command=lambda i=index: self.flip_card(i)
                )
                btn.grid(row=r + 1, column=c)
                self.buttons.append(btn)
                index += 1

    def flip_card(self, index):
        if self.buttons[index]["text"] != "?" or self.second_card:
            return

        self.buttons[index]["text"] = self.cards[index]

        if self.first_card is None:
            self.first_card = index
        else:
            self.second_card = index
            self.root.after(800, self.check_match)

    def check_match(self):
        i, j = self.first_card, self.second_card

        if self.cards[i] == self.cards[j]:
            self.matched += 2
            if self.matched == len(self.cards):
                messagebox.showinfo("Congratulations!", "You won the game 🎉")
                self.root.destroy()
        else:
            self.buttons[i]["text"] = "?"
            self.buttons[j]["text"] = "?"

        self.first_card = None
        self.second_card = None

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showerror("Game Over", "Time's up ⏰")
            self.root.destroy()

# Run game
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
