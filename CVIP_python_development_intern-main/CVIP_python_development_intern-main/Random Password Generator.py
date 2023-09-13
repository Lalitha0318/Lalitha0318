import tkinter as tk
import random
import string

def generate_password(length=12, strength="medium"):
    characters = ""
    if strength == "weak":
        characters = string.ascii_letters
    elif strength == "medium":
        characters = string.ascii_letters + string.digits
    elif strength == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_show_password():
    password_strength = strength_var.get()
    password_length = int(length_entry.get())
    password = generate_password(password_length, password_strength)
    password_label.config(text="Generated Password: " + password)

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")
root.configure(bg="skyblue")

strength_label = tk.Label(root, text="Select Password Strength:")
strength_label.pack(pady=10)

strength_var = tk.StringVar()
strength_var.set("medium")

strength_radio_frame = tk.Frame(root)
strength_radio_frame.pack()

weak_radio = tk.Radiobutton(strength_radio_frame, text="Weak", variable=strength_var, value="weak")
weak_radio.pack(side="left", padx=10)

medium_radio = tk.Radiobutton(strength_radio_frame, text="Medium", variable=strength_var, value="medium")
medium_radio.pack(side="left", padx=10)

strong_radio = tk.Radiobutton(strength_radio_frame, text="Strong", variable=strength_var, value="strong")
strong_radio.pack(side="left", padx=10)

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_show_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="", font=("Arial", 12),bg="lightblue")
password_label.pack(pady=10)

root.mainloop()
