from ascii_art_engine import *

class Ascii_art_runner:
    def run_ascii_art_gen(self):
        ascii_art_gen = Ascii_art_generator()
        
        user_text, font, color, preview_chosse, save_chosse, user_cahr, height, width   = ascii_art_gen.user_input()
        
        ascii_art = ascii_art_gen.creating_ascii_art(user_text, font, color, user_cahr, height, width)

        ascii_art_gen.ascii_art_preview(ascii_art, preview_chosse)
        
        if save_chosse == "y":
            ascii_art_gen.save_ascii_art_to_txt(ascii_art, "ascci_art")