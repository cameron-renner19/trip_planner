"""
Basic Tkinter setup as an example
"""
import tkinter as tk


class Ui:
    window = tk.Tk()
    window.title("Trip Planner")
    window.resizable(True, True)
    max_width = window.winfo_screenwidth()
    max_height = window.winfo_screenheight()
    window.geometry(f"{max_width}x{max_height}")
    greeting = tk.Label(window, text="Hello World")
    greeting.grid(padx=10, pady=10)
    button = tk.Button(window, text="Click Me")
    button.grid(padx=10, pady=10)
    window.mainloop()

if __name__ == '__main__':
    Ui()

