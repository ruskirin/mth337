# by Rinat Ibragimov


import numpy as np


class MayflyModel:

    # Attributes should not be modified directly, only thru .set_params()
    def __init__(self, growth_const=None, pop_init=None):
        self._growth_const = np.random.uniform(0.0, 4.0)
        self._pop_init = np.random.uniform(0.0, 1.0)

        if growth_const is not None:
            self.set_growth_const(growth_const)
        if pop_init is not None:
            self.set_pop_init(pop_init)
        
        self._pop_history = [self._pop_init]

    def __str__(self):
        return (f"Mayfly Model: \n"
              f"\tGrowth constant: {self._growth_const}\n"
              f"\tPopulation initial: {self._pop_init}\n"
              f"\tPopulation history: {self._pop_history}")

    def set_growth_const(self, const):
        # If argument within permitted range, change model variable and
        #   reset the history
        if 0.0 <= const <= 4.0:
            self._growth_const = const
            self._pop_history = [self._pop_init]

    def set_pop_init(self, pop_init):
        # If argument within permitted range, change model variable and
        #   reset the history
        if 0.0 <= pop_init <= 1.0:
            self._pop_init = pop_init
            self._pop_history = [self._pop_init]

    # Prefixed attributes with '_', labeling them as "protected", want to avoid
    #   direct access, so using getter and setter methods
    def get_attrs(self):
        return self._growth_const, self._pop_init

    # A recursive function that fills {self.pop_history} until it contains the
    #   population for requested amount of years
    def set_pop(self, years):
        if years <= len(self._pop_history):
            return

        # Following the recursive function:
        #   pop_current = growth_const * (1 - pop_last) * pop_last
        last = self._pop_history[-1]
        current = self._growth_const * (1.0 - last) * last
        self._pop_history.append(current)

        self.get_pop(years)

    # Returns the population history up to {years} [:years]
    def get_pop(self, years):
        if years > len(self._pop_history):
            self.set_pop(years)

        return self._pop_history[:years]
