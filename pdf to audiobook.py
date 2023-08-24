import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog

# Create a GUI window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Open a file picker dialog
pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

try:
    # Open the selected PDF file
    path = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfReader(path)

    from_page = pdfReader.pages[0]
    text = from_page.extract_text()

    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

except FileNotFoundError:
    print("File not found.")
except PyPDF2.utils.PdfReadError:
    print("Error reading the PDF.")
except Exception as e:
    print("An error occurred:", e)
