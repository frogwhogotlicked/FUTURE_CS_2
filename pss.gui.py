import re
import tkinter as tk
from tkinter import messagebox

def password_strength(password):
    criteria = {
        'Length (8+ characters)': len(password) >= 8,
        'Lowercase Letter': bool(re.search(r'[a-z]', password)),
        'Uppercase Letter': bool(re.search(r'[A-Z]', password)),
        'Digit': bool(re.search(r'\d', password)),
        'Special Character (!@#$%^&*()-_+=)': bool(re.search(r'[!@#$%^&*()\-_=+]', password))
    }
    
    score = sum(criteria.values())
    
    if score == 5:
        strength = 'Strong'
    elif 3 <= score < 5:
        strength = 'Moderate'
    else:
        strength = 'Weak'
    
    result = f"Password Strength: {strength}\n\n"
    for key, passed in criteria.items():
        status = '✔' if passed else '✖'
        result += f"{status} {key}\n"
    return result

def analyze_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return
    result = password_strength(password)
    messagebox.showinfo("Password Analysis", result)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x200")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

analyze_button = tk.Button(root, text="Analyze", command=analyze_password, font=("Arial", 12))
analyze_button.pack(pady=10)

root.mainloop()
