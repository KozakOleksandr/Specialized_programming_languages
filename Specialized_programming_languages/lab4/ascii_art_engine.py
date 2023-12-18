# Import necessary modules
import fonts
from coloration import Coloration


# Class for generating ASCII art
class Ascii_art_generator:

    def __init__(self):
        # Define available colors
        self.available_colors = ['black', 'grey', 'red', 'green', 'blue', 'magenta', 'cyan', 'yellow']

    # Get user input for ASCII art generation
    def user_input(self):
        user_text = input("Enter a word or phrase to convert to ASCII-art: ")

        # Display available colors and get user's color choice
        self.show_colors()
        user_color = self.get_color("Select an available color number: ")

        # Get user choices for preview and saving
        user_preview_choose = self.get_user_choose("Want to preview ASCII-art before saving it?(y/n): ").lower()
        user_save_chose = self.get_user_choose(
            "Do you want to save the created ASCII-art to a text file?(y/n): ").lower()

        return user_text, user_color, user_preview_choose, user_save_chose

    # Generate ASCII art based on the selected font
    def generate_ascii_art(self, text):
        selected_font = fonts.banner
        ascii_art = ""
        for line in range(len(selected_font['a'].split('\n'))):
            for char in text:
                if char.isalpha():
                    if char in selected_font:
                        ascii_art += selected_font[char].split('\n')[line]
                    else:
                        ascii_art += " " * 5  # Default space if character is not available
                else:
                    ascii_art += "\n"  # Move to the next line for non-letter characters
            ascii_art += "\n"  # Move to the next line after completing a line of characters
        return ascii_art

    # Create colored ASCII art
    def creating_ascii_art(self, user_text, user_color):
        ascii_art = self.generate_ascii_art(user_text)
        colored_ascii_art = Coloration.colored(ascii_art, user_color)
        return colored_ascii_art

    # Display available colors
    def show_colors(self):
        print("Available colors:")
        for index, color in enumerate(self.available_colors, start=1):
            print(f"{index}. {color}")

    # Get user choice (yes or no) with input validation
    def get_user_choose(self, message):
        while True:
            try:
                choice = input(message)
                if choice.lower() in ['y', 'n']:
                    return choice
                else:
                    print("Select the right option!")
            except ValueError:
                print("Input must be a string data type!")

    # Get user's color choice with input validation
    def get_color(self, message):
        while True:
            try:
                choice = int(input(message))
                if 1 <= choice <= len(self.available_colors):
                    return self.available_colors[choice - 1]
                else:
                    print("Select the correct color number!")
            except ValueError:
                print("Input must be a numeric data type!")

    # Display ASCII art
    def show_ascii_art(self, ascii_art):
        print(ascii_art)

    # Save ASCII art to a text file
    def save_ascii_art_to_txt(self, final_ascii_art, file_name):
        with open(f"{file_name}.txt", "w") as file:
            file.write(final_ascii_art)
        print(f"Your ASCII-art successfully saved to a file named {file_name}.txt! :D")

    # Display ASCII art preview based on user's choice
    def ascii_art_preview(self, ascii_art, preview_chose):
        if preview_chose == 'y':
            self.show_ascii_art(ascii_art)
