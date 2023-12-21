#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from googletrans import Translator
import wikipedia

translator = Translator()

# Set up the GUI
root = tk.Tk()
root.title("Multilingual Chatbot")

# Create widgets
input_label = tk.Label(root, text="Enter your question:")
input_box = tk.Entry(root, width=50)
language_label = tk.Label(root, text="Select language to translate to:")
language_var = tk.StringVar()
language_var.set("en")  # default language is English
language_menu = tk.OptionMenu(root, language_var, "en", "fr", "es", "de", "ja", "ko", "zh-cn","te","hi")
output_label = tk.Label(root, text="Answer:")
output_box = tk.Text(root, height=10, width=50)

def get_input_and_translate():
    input_text = input_box.get()
    dest_language = language_var.get()
    
    # Use Wikipedia to get the answer to the question
    
    try:
        if input_text in ['hi', 'hello']:
            answer = "Hi there! How can I assist you today?"
        elif input_text in ['how are you', 'how are you doing']: 
            answer = "I'm doing well, thank you. How about you?"
        elif input_text in ['what is your name', 'who are you']:
            answer = "My name is ChatBot. How can I help you today?"
        elif input_text in ['thank you', 'thanks']:
            answer = "You're welcome. Is there anything else I can help you with?"
        else :
            answer = wikipedia.summary(input_text)
    except:
            answer = "Sorry, I couldn't find an answer to that question."
    
    # Translate the answer to the desired language
    if dest_language != "en":
        answer = translator.translate(answer, dest=dest_language).text
    
    # Display the answer in the output box
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, answer)

# Add widgets to the GUI
input_label.pack()
input_box.pack()
language_label.pack()
language_menu.pack()
output_label.pack()
output_box.pack()

# Add a button to get the input and translate
translate_button = tk.Button(root, text="Send", command=get_input_and_translate)
translate_button.pack()

# Run the GUI
root.mainloop()


# In[ ]:


pip install wikipedia


# In[ ]:




