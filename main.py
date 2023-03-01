from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("Dark")

#window
window = customtkinter.CTk()
window.title("Tasks List")
window.geometry("620x430")
window.iconbitmap("icon.ico")
window.resizable(False, False)

#Definujeme fonty a barvy
main_font = ("Times New Roman", 12)
main_color = "#dd7f00"
button_color = "#ffa033"


# Funkce
def add_text():
    list_box.insert(END, user_input.get())
    user_input.delete(0, END)

def remove_text_item():
    # odstrani jednu polozku seznamu
    list_box.delete(ANCHOR)

def remove_all_items():
    # odstrani vsechny polozky seznamu
    list_box.delete(0, END)

def save_tasks():
    # ulozi ukoly do textoveho souboru
    with open("tasks.txt", "w") as my_file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                my_file.write(f"{one_task}")
            else:
                my_file.write(f"{one_task}\n")

def open_tasks():
    try:
        with open("tasks.txt", "r") as my_file:
            for one_line in my_file:
                list_box.insert(END, one_line)
    except:
        print("Chyba ve funkci na otevirani souboru tasks.txt")


# Framy
input_frame = customtkinter.CTkFrame(window)
text_frame = customtkinter.CTkFrame(window)
button_frame = customtkinter.CTkFrame(window)
input_frame.pack(pady=5)
text_frame.pack(pady=5)
button_frame.pack(pady=5)

# Input_frame - obsah
user_input = Entry(input_frame, width=70, borderwidth=3, font=main_font)
user_input.grid(row=0,column=0, padx=5, pady=5)
add_button = customtkinter.CTkButton(input_frame, text="Add", command=add_text)
add_button.grid(row=0,column=1,padx=5, pady=5,ipadx=20 )



# Text_frame-obsah
list_box = Listbox(text_frame, height=22, width=100, borderwidth=3, font=main_font,highlightthickness=0)
list_box.grid(row=0, column=0, sticky="nsew")

# Scroll Bar
text_scrollbar = customtkinter.CTkScrollbar(text_frame, command=list_box.yview)
text_scrollbar.grid(row=0, column=1,sticky=N+S)  #scrollbar po cele delce list_boxu

list_box.configure(yscrollcommand=text_scrollbar.set)

# Propojeni Srollbaru a Listboxu
#text_scrollbar.config(command=list_box.yview)

#text_scrollbar.config(command=list_box.yview)

# Button frame-obsah
remove_button = customtkinter.CTkButton(button_frame, text="Remove",command=remove_text_item)
clear_button = customtkinter.CTkButton(button_frame, text="Clear",command=remove_all_items)
save_button = customtkinter.CTkButton(button_frame, text="Save",command=save_tasks)
quit_button = customtkinter.CTkButton(button_frame, text="Quit",command=window.destroy)

remove_button.grid(row=0, column=0, padx=2, pady=10)
clear_button.grid(row=0, column=1, padx=2, pady=10)
save_button.grid(row=0, column=2, padx=2, pady=10)
quit_button.grid(row=0, column=3, padx=2, pady=10)

#Nacteme seznam ukolu do List_boxu
open_tasks()


# Hlavni cyklus
window.mainloop()


