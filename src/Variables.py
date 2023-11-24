cipher = 0
todo = 0
english = True
file = ''
key = ''

phrase_cipher = ('Выберите ваш шифр', 'Choose your cipher')
phrase_todo = ('Вы хотите зашифровать или расшифровать ваш файл?', 'Do you want to encrypt or to decrypt your file?')
phrase_language = ('Use Alt+Shift to change the language', 'Для смены языка используйте Alt+Shift')
btn_text = ('Ввести', 'Enter')
combo_cipher_lang = (['Шифр Цезаря', 'Шифр Виженера', 'Шифр Вернама'],
                     ['Caesar cipher', 'Vigenère cipher', 'Vernam cipher'])
combo_todo_lang = (['Зашифровать', 'Расшифровать'], ['Encrypt', 'Decrypt'])
entry_path_text = ('Введите путь к вашему файлу', 'Enter path to your file')
entry_key_text = ('Введите ключ', 'Enter key')
entry_caesar_text = ('Введите ключ или \"-\" если хотите использовать частотный анализ',
                     'Enter key or \"-\" if you want to use frequency analysis')
phrase_error = ('Адрес не существует', 'Address do not exists')
entry_frequency_error = ('Невозможно подобрать ключ', 'Can not find the key')

WINDOW_LENGTH = 900
WINDOW_HEIGHT = 300
WINDOW_X_SHIFT = 100
WINDOW_Y_SHIFT = 200
WINDOW_X_MIN_SIZE = 600
WINDOW_Y_MIN_SIZE = 250
WINDOW_X_MAX_SIZE = 900
WINDOW_Y_MAX_SIZE = 300

bg_color = '#656560'
