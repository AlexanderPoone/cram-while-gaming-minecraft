import tkinter as tk
from tkinter import ttk
import subprocess
import os
from tkinter import font as tkFont  # Import the font module

def create_window():
    window = tk.Tk()
    window.title("Cram while Playing - Minecraft")
    
    window.configure(bg='#1a1a1a')

    # Load the custom font
    try:
        custom_font = tkFont.Font(family="Minecraft Seven", size=16)
    except Exception as e:
        print(f"Error loading font: {e}")
        custom_font = ("Arial", 16, "bold")  # Fallback font

    # Header with some padding
    header = tk.Label(window, text="Cram while Playing - Minecraft", font=custom_font, bg='#1a1a1a', fg='white')
    header.pack(pady=10, padx=20)

    # Frame for horizontal layout
    control_frame = tk.Frame(window, bg='#1a1a1a')
    control_frame.pack(pady=10, padx=20, fill=tk.X)  # Fill horizontally

    # Version dropdown
    version_label = tk.Label(control_frame, text="Version:", bg='#1a1a1a', fg='white', font=custom_font)
    version_label.pack(side=tk.LEFT, padx=(0, 5))
    versions = ["1.0", "1.1", "1.2"]
    version_combo = ttk.Combobox(control_frame, values=versions, style='TCombobox')
    version_combo.pack(side=tk.LEFT, padx=(0, 10))

    # Styling for Combobox
    style = ttk.Style()
    style.theme_use('default')
    style.configure("TCombobox", selectbackground='#1a1a1a', fieldbackground='#333333', background='#1a1a1a', foreground='white')

    # Button for Quizlet import
    quizlet_button = tk.Button(control_frame, text="From Quizlet", command=show_quizlet_entry, bg='#333333', fg='white', activebackground='#4d4d4d', font=custom_font)
    quizlet_button.pack(side=tk.LEFT, padx=(0, 5))

    # Button for Minecraft grammar cram
    mc_grammar_button = tk.Button(control_frame, text="(From MC) Cram Grammatical Gender", command=execute_script, bg='#333333', fg='white', activebackground='#4d4d4d', font=custom_font)
    mc_grammar_button.pack(side=tk.LEFT)

    # Adjust window to fit contents with a slight adjustment for width
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    window.geometry(f"{width}x{height}")

    return window

def show_quizlet_entry():
    quizlet_window = tk.Toplevel()
    quizlet_window.title("Enter Quizlet ID")
    quizlet_window.configure(bg='#1a1a1a')

    # Load the custom font again for this window
    try:
        custom_font = tkFont.Font(family="Minecraft Seven", size=12)
    except Exception as e:
        print(f"Error loading font: {e}")
        custom_font = ("Arial", 12)  # Fallback font

    # ID Entry
    id_label = tk.Label(quizlet_window, text="Enter Quizlet ID:", bg='#1a1a1a', fg='white', font=custom_font)
    id_label.pack(pady=5, padx=20)
    id_entry = tk.Entry(quizlet_window, bg='#333333', fg='white', font=custom_font)
    id_entry.pack(pady=5, padx=20)

    # Buttons
    button_frame = tk.Frame(quizlet_window, bg='#1a1a1a')
    button_frame.pack(pady=5, padx=20)
    enter_button = tk.Button(button_frame, text="Enter", command=lambda: print("Enter clicked with ID:", id_entry.get()), bg='#333333', fg='white', activebackground='#4d4d4d', font=custom_font)
    enter_button.pack(side=tk.LEFT, padx=5)
    cancel_button = tk.Button(button_frame, text="Cancel", command=quizlet_window.destroy, bg='#333333', fg='white', activebackground='#4d4d4d', font=custom_font)
    cancel_button.pack(side=tk.LEFT, padx=5)

def execute_script():
    script_output_window = tk.Toplevel()
    script_output_window.title("Script Output")
    script_output_window.configure(bg='#1a1a1a')

    # Execute the script with UTF-8 encoding
    try:
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True, encoding='utf-8', errors='replace')
        output = result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        output = f"Error executing script: {str(e)}"

    # Display the output in a read-only text area
    output_text = tk.Text(script_output_window, wrap=tk.WORD, bg='#333333', fg='white', state='disabled', height=20, width=100)
    output_text.pack(pady=10, padx=20)
    output_text.configure(state='normal')
    output_text.insert('1.0', output)
    output_text.configure(state='disabled')

    # OK button to exit
    ok_button = tk.Button(script_output_window, text="OK", command=script_output_window.destroy, bg='#333333', fg='white', activebackground='#4d4d4d')
    ok_button.pack(pady=10)

    # Fit the window to its content
    script_output_window.update_idletasks()
    width = script_output_window.winfo_width()
    height = script_output_window.winfo_height()
    script_output_window.geometry(f"{width}x{height}")

if __name__ == "__main__":
    main_window = create_window()
    main_window.mainloop()