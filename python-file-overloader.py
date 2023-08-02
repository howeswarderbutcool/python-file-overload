import tkinter as tk
from tkinter import messagebox
import hashlib
from functools import partial
import time

hashIng = True
filePath = "hash_codes.txt"


def calculate_hash(text, algorithm="sha256"):
    global hashIng
    # Create a new hash object based on the selected algorithm
    if algorithm == "sha256":
        hash_obj = hashlib.sha256()
        hashIng = True
    elif algorithm == "sha512":
        hash_obj = hashlib.sha512()
        hashIng = True
    elif algorithm == "none":
        hashIng = False
        return None  
    else:
        raise ValueError("Invalid algorithm. Supported options are 'sha256' and 'sha512'.")

    # Update the hash object with the input text (encoded as bytes)
    hash_obj.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash code
    hash_code = hash_obj.hexdigest()

    return hash_code

def hash_button_clicked():
    global hashIng
    text = text_entry.get()
    algorithm = algorithm_var.get()

    if hashIng is True:
        hash_code = calculate_hash(text, algorithm)
        if hash_code is not None:
            frequency = int(frequency_entry.get())
            # Save the hash code to a file with the specified frequency
            with open(filePath, "a") as file:
                for _ in range(frequency):
                    file.write(hash_code + "\n")

    else:
        # Hashing is disabled, save the original text to the file
        frequency = int(frequency_entry.get())
        with open("hash_codes.txt", "a") as file:
            for _ in range(frequency):
                file.write(text + "\n")



def delete_file_contents(filePath):
    try: 
        with open(filePath, "w") as file:
            file.truncate(0)
        messagebox.showinfo("File Cleared", "All contents have been deleted from the file.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete file contents: {str(e)}")


app = tk.Tk()
app.title("file-overloader")
app.geometry("500x150")

# Create widgets
text_label = tk.Label(app, text="Enter the text:")
text_entry = tk.Entry(app, width=30)
algorithm_var = tk.StringVar(value="sha256")
algorithm_label = tk.Label(app, text="Select hashing algorithm:")
algorithm_menu = tk.OptionMenu(app, algorithm_var, "sha256", "sha512","none")
frequency_label = tk.Label(app, text="Enter frequency:")
frequency_entry = tk.Entry(app, width=5)
hash_button = tk.Button(app, text="Start", command=hash_button_clicked)
delete_button = tk.Button(app, text="Delete File", command=partial(delete_file_contents, filePath))


# Grid the widgets to place them in the window
text_label.grid(row=0, column=0, pady=5)
text_entry.grid(row=0, column=1, pady=5)
algorithm_label.grid(row=1, column=0, pady=5)
algorithm_menu.grid(row=1, column=1, pady=5)
frequency_label.grid(row=2, column=0, pady=5, sticky="w")
frequency_entry.grid(row=2, column=1, pady=5, sticky="w")
hash_button.grid(row=4, column=0, columnspan=2, pady=10)
delete_button.grid(row=4, column=3, columnspan=2, pady=10)


# Start the main event loop
app.mainloop()



