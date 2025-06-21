import tkinter as tk
import random

# ---- WORD SETUP ----
word_list = ['python', 'banana', 'laptop', 'hangman', 'rocket']
secret_word = random.choice(word_list)
print("🔍 Secret word is:", secret_word)
display_word = ['_' for _ in secret_word]
guessed_letters = []
tries_left = 6

# ---- FUNCTIONS ----
def guess_letter():
    global tries_left
    letter = entry.get().strip().lower()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        result_label.config(text="❗ Enter a single letter.", fg="darkred")
        return

    if letter in guessed_letters:
        result_label.config(text="🔁 Already guessed that.", fg="darkorange")
        return

    guessed_letters.append(letter)

    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                display_word[i] = letter
        result_label.config(text=f"✅ '{letter}' is correct!", fg="green")
    else:
        tries_left -= 1
        result_label.config(text=f"❌ '{letter}' is not in the word.", fg="red")

    word_label.config(text=' '.join(display_word))
    tries_label.config(text=f"Tries left: {tries_left}")

    if '_' not in display_word:
        result_label.config(text="🎉 You guessed the word!", fg="green")
        entry.config(state=tk.DISABLED)
        submit_button.config(state=tk.DISABLED)
    elif tries_left == 0:
        word_label.config(text=secret_word)
        result_label.config(text=f"💀 Game Over! Word was: {secret_word}", fg="red")
        entry.config(state=tk.DISABLED)
        submit_button.config(state=tk.DISABLED)

# ---- GUI SETUP ----
root = tk.Tk()
root.title("Hangman Game")
root.geometry("500x400")
root.configure(bg="#f5deb3")  # Light brown background

# Fonts
font_main = ("Courier", 24, "bold")
font_small = ("Arial", 14)

# Word display
word_label = tk.Label(root, text=' '.join(display_word), font=font_main,
                      bg="#f5deb3", fg="#000000")
word_label.pack(pady=30)

# Tries left
tries_label = tk.Label(root, text=f"Tries left: {tries_left}", font=font_small,
                       bg="#f5deb3", fg="#000000")
tries_label.pack()

# Entry field
entry = tk.Entry(root, font=font_small, width=5, justify='center',
                 bg="white", fg="black")
entry.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="Guess", font=font_small, command=guess_letter,
                          bg="#deb887", fg="black", width=10)
submit_button.pack(pady=5)

# Result message
result_label = tk.Label(root, text="", font=font_small,
                        bg="#f5deb3", fg="black")
result_label.pack(pady=20)

# Start GUI
root.mainloop()
