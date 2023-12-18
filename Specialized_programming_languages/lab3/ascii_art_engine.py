import pyfiglet
from termcolor import colored
from colorama import Fore, Style
from termcolor import COLORS

class Ascii_art_generator:
    def __init__(self):
        self.available_fonts = ['standard', 'slant', 'alphabet', 'banner3-D', 'doh', 'bulbhead', 'letters', '6x10']
        self.available_colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
        
    def user_input(self):
        user_text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")
        
        self.show_colors()
        user_color = self.get_color("Виберіть номер доступного кольору: ")
        
        self.show_fonts()
        user_font = self.get_font("Виберіть номер доступного шрифту: ")
        
        width = self.get_param("Введіть ширину ASCII-art-ту (кількість символів у ширину): ")
        height = self.get_param("Введіть висоту ASCII-art-ту (кількість символів у вистоу): ")

        use_custom_chars = input("Ви хочете обрати спец-символ? (y/n): ").lower()
        user_char = self.get_custom_char() if use_custom_chars == 'y' else None
        
        user_preview_chosse = input("Хочете попередньо переглянути арт перед тим як зберегти його?(y/n): ").lower()
        
        user_save_chossoe = input("Хочете зберегти створений ASCII-art у текстовий файл?(y/n): ").lower()
        
        return user_text, user_font, user_color, user_preview_chosse, user_save_chossoe, user_char, height, width
        
    # Функція для вибору кольору користувачем
    def show_colors(self):
        print("Доступні кольори:")
        for index, color in enumerate(self.available_colors, start=1):
            print(f"{index}. {color}")
            
    def get_color(self,message):        
        while True:
            try:
                choice = int(input(message))
                if 1 <= choice <= len(self.available_colors):
                    return self.available_colors[choice - 1]
                else:
                    print("Виберіть правильний номер кольору.")
            except ValueError:
                print("Виберіть правильний номер кольору.")
                
    # def set_color(self):
        

    def show_fonts(self):
        
        print("Доступні шрифти:")
        for index, font in enumerate(self.available_fonts, start=1):
            print(f"{index}. {font}")
            
    def get_font(self, message):
        while True:
            try:
                choice = int(input(message))
                if 1 <= choice <= len(self.available_fonts):
                    return self.available_fonts[choice - 1]
                else:
                    print("Виберіть правильний номер шрифту.")
            except ValueError:
                print("Виберіть правильний номер шрифту.")
                
    def get_param(self, message):
        while True:
            try:
                number = int(input(message))
                if number > 0:
                    return number
                else:
                    print("Введіть число ібльше за 0.")
            except ValueError:
                print("Будь ласка введіть правильне число.")
                
    def get_custom_char(self):
        return input("Введіть символ яікий хочите використовувати ('@', '#', '*', ...): ")
        
    def creating_ascii_art(self, user_text, user_font, user_color, user_char, width, height ):
        
        ascii_art = pyfiglet.figlet_format(user_text, font=user_font)
        ascii_lines = ascii_art.split('\n')
        
        scaled_ascii_lines = []
        char_set_length = len(user_char) if user_char else 0
        for line in ascii_lines:
            scaled_line = ""
            for char in line:
                if char == ' ':
                    scaled_line += ' '
                else:
                    if user_char:
                        scaled_line += user_char[hash(char) % char_set_length]
                    else:
                        scaled_line += char
            scaled_ascii_lines.append(scaled_line.center(width)[:width])

        scaled_ascii_text = '\n'.join(scaled_ascii_lines[:height])
               
        colored_ascii_art = colored(scaled_ascii_text, user_color)
        
        final_ascii_art = colored_ascii_art
        
        return final_ascii_art
    
    def show_ascii_art(self, ascii_art):
        print(ascii_art)
    
    def save_ascii_art_to_txt(self, final_ascii_art, file_name):
        with open(f"{file_name}.txt", "w") as file:
            file.write(final_ascii_art)
        print(f"Ваш ASCII-art успішно збережений у файл з ім'ям {file_name}.txt! :D")
        
    def ascii_art_preview(self, ascii_art, preview_chosse):
        if preview_chosse == 'y':
            self.show_ascii_art(ascii_art)
            