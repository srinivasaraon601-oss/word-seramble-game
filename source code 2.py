import tkinter as tk
import random

words = ["python", "computer", "keyboard", "student", "program"]

word = random.choice(words)
scrambled = "".join(random.sample(word, len(word)))

def check():
    if entry.get().lower() == word:
        result.config(text="Correct!", fg="green")
    else:
        result.config(text="Wrong! Try Again.", fg="red")

root = tk.Tk()
root.title("Word Scramble Game")

tk.Label(root, text="Unscramble the word").pack(pady=5)
tk.Label(root, text=scrambled, font=("Arial", 18, "bold")).pack(pady=10)

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check", command=check).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()