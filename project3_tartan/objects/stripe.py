import re
from constants import is_color_existing


class Stripe:

    def __init__(self, pattern):
        self.color = re.search("[a-zA-Z]+", pattern).group()
        self.width = re.search("\d+", pattern).group()

        if not is_color_existing(self.color):
            print(f"Invalid color sequence: {self.color}")
            self.color = None
            self.width = None

    def __str__(self):
        if not self.is_valid():
            return "N/A"
        else:
            return self.color + self.width

    def is_valid(self):
        return self.color is not None