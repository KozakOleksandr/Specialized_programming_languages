# Import the Ascii_art_generator class from the ascii_art_engine module
from ascii_art_engine import Ascii_art_generator

# Class for running the ASCII art generator
class Ascii_art_runner:
    def run_ascii_art_gen(self):
        # Create an instance of the Ascii_art_generator class
        ascii_art_gen = Ascii_art_generator()

        # Get user input for text, color, preview choice, and save choice
        user_text, color, preview_choose, save_choose = ascii_art_gen.user_input()

        # Generate ASCII art based on user input
        ascii_art = ascii_art_gen.creating_ascii_art(user_text, color)

        # Display the ASCII art preview based on user's preview choice
        ascii_art_gen.ascii_art_preview(ascii_art, preview_choose)

        # If user chose to save the ASCII art, save it to a text file
        if save_choose == "y":
            ascii_art_gen.save_ascii_art_to_txt(ascii_art, "ascii_art")
