
class Coloration():
    COLORS = {
        "black": 30,
        "grey": 30,  # Actually black but kept for backwards compatibility
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "light_grey": 37,
        "dark_grey": 90,
        "light_red": 91,
        "light_green": 92,
        "light_yellow": 93,
        "light_blue": 94,
        "light_magenta": 95,
        "light_cyan": 96,
        "white": 97,
    }

    RESET = "\033[0m"

    def colored(
        text: str,
        color: str | None = None,
    ) -> str:
        """Colorize text.

        Available text colors:
            black, red, green, yellow, blue, magenta, cyan, white,
            light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
            light_magenta, light_cyan.

        Example:
            colored('Hello, World!', 'red')
        """

        fmt_str = "\033[%dm%s"
        if color is not None:
            text = fmt_str % (Coloration.COLORS[color], text)

        return text + Coloration.RESET
