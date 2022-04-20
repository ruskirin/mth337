# by Rinat Ibragimov


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.widgets import Slider
from math import ceil


# TODO: ONLY GOES UP TO 6!
# Create graphs for each (const, pop_init) pair passed
def snapshot(model, years, model_attrs):
    rows = ceil(len(model_attrs) / 2)
    graph_size = (3, 2) # (width, height)

    fig = plt.figure(
        figsize=(6, rows*(graph_size[1])), # width=6, height=depends on rows
        tight_layout=True) # Adds padding between axes

    # iterate through passed {model_attrs} and make a graph for each tuple
    for i, attr in enumerate(model_attrs):
        place = (i//2, i%2) # (row, column) placement

        plt.subplot2grid(
            graph_size,
            place,
            title=f"$const: {attr[0]}$, $pop_i: {attr[1]}$",
            ylim=(0, 1.0))

        model.set_growth_const(attr[0])
        model.set_pop_init(attr[1])

        pop = model.get_pop(years)
        plt.plot(pop)


# Used the following resource to aid in building an interactive plot:
#   https://matplotlib.org/3.3.1/gallery/widgets/slider_demo.html
class InteractiveGraph:

    def __init__(self, model):
        # model to graph
        self.model = model

        fig, ax_interact = plt.subplots(
            num="Interactive Mayfly Population")

        # Toggle on interactive mode
        plt.ion()
        # New normalized left and bottom position of graph
        plt.subplots_adjust(0.1, 0.25)

        ax_interact.grid()
        ax_interact.set_ylim(0.0, 1.0)
        ax_interact.set_ylabel("Population")
        ax_interact.set_xlabel("Years")
        # Sets the interval of the ticks, found here:
        #   https://stackoverflow.com/a/19972993/13557629
        ax_interact.xaxis.set_major_locator(ticker.MultipleLocator(5))
        ax_interact.yaxis.set_major_locator(ticker.MultipleLocator(0.1))

        self.years = 40
        pop = self.model.get_pop(self.years)

        self.line, = ax_interact.plot(pop)

        color_slider = "mistyrose"

        # Create new axes for Sliders with the specified shape/positioning.
        # Rectangle dimensions: [left, bottom, width, height]
        ax_const = plt.axes([0.2, 0.1, 0.65, 0.03],
                            facecolor=color_slider)
        ax_pop_init = plt.axes([0.2, 0.05, 0.65, 0.03],
                               facecolor=color_slider)

        # retrieve the model's parameters
        growth_const, pop_init = model.get_attrs()

        self.slider_growth_const = Slider(
            ax=ax_const,
            label="Growth Constant",
            valmin=0.0,
            valmax=4.0,
            valinit=growth_const,
            dragging=True,
            valstep=0.1)

        self.slider_pop_init = Slider(
            ax=ax_pop_init,
            label="Initial Population",
            valmin=0.0,
            valmax=1.0,
            valinit=pop_init,
            dragging=True,
            valstep=0.05)

        # call function update() whenever sliders' values changed
        self.slider_growth_const.on_changed(self.update)
        self.slider_pop_init.on_changed(self.update)

    # Function to update model with newly set values.
    # This function is automatically called by Slider().on_changed()
    #   and must accept 1 float parameter to be callable
    def update(self, val):

        self.model.set_growth_const( # update growth constant
            self.slider_growth_const.val)

        self.model.set_pop_init( # update initial population
            self.slider_pop_init.val)

        pop = self.model.get_pop(self.years) # calculate new population history
        self.line.set_ydata(pop)

        # Redraw the graph (if interactive mode is off: plt.ioff())
        # fig.canvas.draw_idle()