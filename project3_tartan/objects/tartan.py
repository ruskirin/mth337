import constants
from objects import stripe


class Tartan:

    def __init__(self, name: str):
        self.name = name
        self.pattern = []

        if constants.is_tartan_existing(name):
            print(f"Tartan {name} exists. "
                  f"Pattern: {constants.TARTANS[name]}")

            self.pattern = constants.TARTANS[name]

        else:
            while True:
                pattern = input("Great, new Tartan! "
                                     "Please enter its stripe pattern:\n"
                                     "(Example format: \'RB8 K4 RB6 K24 ...\')")

                for c in pattern.split(" "):
                    s = stripe.Stripe(c)

                    if s.is_valid(): # Check that color exists
                        self.pattern.append(s)

                if len(self.pattern) >= 4: # Check that enough colors were provided
                    print(f"Created Tartan \'{self.name}\'")
                    break

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Pattern: {[str(a) for a in self.pattern]}\n"