import pyfiglet
while True:
    # Функція для отримання списку доступних шрифтів
    def get_available_fonts():
        return pyfiglet.FigletFont.getFonts()

    # Функція для вибору шрифту користувачем
    def choose_font():
        available_fonts = get_available_fonts()

        print("Доступні шрифти:")
        for index, font in enumerate(available_fonts, start=1):
            print(f"{index}. {font}")

        while True:
            try:
                choice = int(input("Виберіть номер шрифту: "))
                if 1 <= choice <= len(available_fonts):
                    return available_fonts[choice - 1]
                else:
                    print("Виберіть правильний номер шрифту.")
            except ValueError:
                print("Виберіть правильний номер шрифту.")

    def main():
        # Запит користувача на введення слова або фрази
        text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")

        # Вибір шрифту користувачем
        font = choose_font()

        # Створення ASCII-арт з введення користувача та вибраного шрифту
        ascii_art = pyfiglet.figlet_format(text, font=font)

        # Виведення ASCII-арт на екран
        print(ascii_art)

    if __name__ == "__main__":
        main()
    