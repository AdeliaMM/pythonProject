from tkinter import *
from tkinter import ttk
import file_processing
from Variables import *


main_window = Tk()

main_window.title('Шифрование')

main_window.geometry(
    f'{WINDOW_LENGTH}x{WINDOW_HEIGHT}+{WINDOW_X_SHIFT}+{WINDOW_Y_SHIFT}'
)

main_window.resizable(True, True)

main_window.minsize(WINDOW_X_MIN_SIZE, WINDOW_Y_MIN_SIZE)

main_window.maxsize(WINDOW_X_MAX_SIZE, WINDOW_Y_MAX_SIZE)

main_window.config(background=bg_color)

for c in range(5):
    main_window.columnconfigure(index=c, weight=1)

for r in range(15):
    main_window.rowconfigure(index=r, weight=1)

label_style = ttk.Style()
label_style.configure('My.TLabel',
                      font='Times 15',
                      foreground='white',
                      background=bg_color,
                      anchor='center')

label_widget_cipher = ttk.Label(
    master=main_window,
    text=phrase_cipher[english],
    style='My.TLabel'
)

label_widget_todo = ttk.Label(
    master=main_window,
    text=phrase_todo[english],
    style='My.TLabel'
)


def change_lang_2():
    global english
    english = not english
    path.set(entry_path_text[english])
    if cipher == 0:
        key.set(entry_caesar_text[english])
    else:
        key.set(entry_key_text[english])
    entry_path.icursor(END)
    entry_key.icursor(END)
    label_widget_language['text'] = phrase_language[english]


def fix_entry_set(entry):
    if entry.get() == entry_path_text[english] or entry.get() == entry_key_text[english] or entry.get() == \
            entry_caesar_text[english]:
        entry.set('')
    main_window.unbind_all('<Alt-Shift_L>')
    main_window.bind_all('<Alt-Shift_L>', lambda event: change_lang_3())


def change_lang_3():
    global english
    english = not english
    label_widget_language['text'] = phrase_language[english]


def delete_start():
    combo_cipher.destroy()
    label_widget_cipher.destroy()
    combo_todo.destroy()
    label_widget_todo.destroy()
    btn.unbind('<Return>')
    btn.unbind('<Button-1>')
    btn.forget()
    main_window.unbind_all('<Alt-Shift_L>')


def set_cipher():
    global cipher, todo
    cipher = combo_cipher.current()
    todo = combo_todo.current()
    delete_start()
    start()


btn = ttk.Button(text=btn_text[english],
                 style='My.TButton')
btn_style = ttk.Style()
btn_style.configure("My.TButton",
                    relief='flat'
                    )
btn_style.map('My.TButton', foreground=[('!disabled', bg_color), ('active', 'white')],
              background=[('!disabled', 'white'), ('active', bg_color)])

btn.focus_set()
btn.bind('<Return>', lambda event: set_cipher())
btn.bind('<Button-1>', lambda event: set_cipher())

combo_cipher = ttk.Combobox(main_window,
                            values=combo_cipher_lang[english],
                            state='readonly',
                            style='My.TEntry')
combo_cipher.bind('<<ComboboxSelected>>', lambda event: btn.focus_set)

combo_todo = ttk.Combobox(main_window,
                          values=combo_todo_lang[english],
                          state='readonly',
                          style='My.TEntry')
combo_todo.bind('<<ComboboxSelected>>', lambda event: btn.focus_set)

label_widget_language = ttk.Label(
    master=main_window,
    text=phrase_language[english],
    style='My.TLabel',
    foreground='#BBBBBB',
    font='Times 12'
)


def change_lang():
    global english
    english = not english
    label_widget_language['text'] = phrase_language[english]
    label_widget_cipher['text'] = phrase_cipher[english]
    label_widget_todo['text'] = phrase_todo[english]
    combo_cipher_current = combo_cipher.current()
    combo_cipher['values'] = combo_cipher_lang[english]
    combo_cipher.current(combo_cipher_current)
    combo_todo_current = combo_todo.current()
    combo_todo['values'] = combo_todo_lang[english]
    combo_todo.current(combo_todo_current)
    btn['text'] = btn_text[english]


label_widget_cipher.grid(row=1, column=1, columnspan=3, sticky='swne')

combo_cipher.grid(row=2, column=1, columnspan=3, sticky='sn')
combo_cipher.current(cipher)

label_widget_todo.grid(row=4, column=1, columnspan=3, sticky='swne')

combo_todo.grid(row=5, column=1, columnspan=3, sticky='sn')
combo_todo.current(todo)

label_widget_language.grid(row=10, column=1, columnspan=3, sticky='swne')

btn.grid(row=7, column=1, columnspan=3)

path = StringVar()

entry_path = ttk.Entry(main_window,
                       textvariable=path,
                       justify='left',
                       style='MyPath.TEntry',
                       )
entry_path.bind('<BackSpace>', lambda event: fix_entry_set(path))

path_style = ttk.Style()
path_style.configure('MyPath.TEntry', font='Times 17', selectbackground='grey')
path_style.map('MyPath.TEntry', foreground=[('!focus', 'grey'), ('focus', 'black')])

key = StringVar()

entry_key = ttk.Entry(main_window,
                      textvariable=key,
                      justify='left',
                      style='MyKey.TEntry',
                      )
entry_key.bind('<BackSpace>', lambda event: fix_entry_set(key))

key_style = ttk.Style()
key_style.configure('MyKey.TEntry', font='Times 17', selectbackground='grey')
key_style.map('MyKey.TEntry', foreground=[('!focus', 'grey'), ('focus', 'black')])


def set_path(entry):
    global path
    if entry.get() == '':
        path_style.map('MyPath.TEntry', foreground=[('!focus', 'red'), ('focus', 'black')])
        path.set(entry_path_text[english])
    else:
        path_style.map('MyPath.TEntry', foreground=[('!focus', 'grey'), ('focus', 'black')])
        main_window.focus_set()


def set_key(entry):
    global key
    if entry.get() == '':
        key_style.map('MyKey.TEntry', foreground=[('!focus', 'red'), ('focus', 'black')])
        if cipher == 0:
            key.set(entry_caesar_text[english])
        else:
            key.set(entry_key_text[english])
    else:
        key_style.map('MyKey.TEntry', foreground=[('!focus', 'grey'), ('focus', 'black')])
        main_window.focus_set()


def start():
    path.set(entry_path_text[english])
    entry_path.grid(row=5, column=1, columnspan=3, sticky='swne')
    entry_path.bind('<Return>', lambda event: set_path(entry_path))
    entry_path.bind('<FocusOut>', lambda event: set_path(entry_path))
    if cipher == 0:
        key.set(entry_caesar_text[english])
    else:
        key.set(entry_key_text[english])
    entry_key.grid(row=8, column=1, columnspan=3, sticky='swne')
    entry_key.bind('<Return>', lambda event: set_key(entry_key))
    entry_key.bind('<FocusOut>', lambda event: set_key(entry_key))
    btn.grid(row=9, column=2, columnspan=1)
    btn.bind('<Return>', lambda event: set_path_key())
    btn.bind('<Button-1>', lambda event: set_path_key())
    main_window.bind_all('<Alt-Shift_L>', lambda event: change_lang_2())


def set_path_key():
    if path.get() != entry_path_text[english] and key.get() not in (
    entry_key_text[english], entry_caesar_text[english]):
        btn.forget()
        file_processing.processing(path, key.get(), cipher, todo, phrase_error[english], entry_frequency_error[english], key, path_style)
    if path.get() == entry_path_text[english]:
        path_style.map('MyPath.TEntry', foreground=[('!focus', 'red'), ('focus', 'black')])
    if key.get() in (entry_key_text[english], entry_caesar_text[english]):
        key_style.map('MyKey.TEntry', foreground=[('!focus', 'red'), ('focus', 'black')])


main_window.bind_all('<Alt-Shift_L>', lambda event: change_lang())
