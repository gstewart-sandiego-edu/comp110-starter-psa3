"""
Module: hurricane_tracker

Program to visualize the path of a Hurricane in the North Atlantic Basin.

Authors:
1) Gabriel Stewart - gstewart@sandiego.edu
2) Parker Brown - parkerbrown@sandiego.edu
"""
import turtle


def initialize_screen():
    """
    Creates the Turtle and the Screen with the map background
    and coordinate system set to match latitude and longitude.

    Returns:
    A list containing the turtle, the screen, and the background image.

    DO NOT MODIFY THIS FUNCTION IN ANY WAY!!!
    """

    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.tracer(0, 0)
    wn.title("Hurricane Tracker")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()

    # set the coordinate system to match lat/long
    turtle.setworldcoordinates(-90, 0, -17.66, 45)

    map_bg_img = tkinter.PhotoImage(file="atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("hurricane.gif")
    t.shape("hurricane.gif")

    return [t, wn, map_bg_img]


# Define the get_category function here

def animate_hurricane(data_filename):
    """
    Animates the path of a hurricane.

    Parameters:
    data_filename (string): Name of file containing hurricane data (CSV format).
    """

    # initialize_screen returns a list of three items: the turtle to draw with, the
    # screen object for the window, and the background image of the window.
    # We only care about the turtle though.
    setup_data = initialize_screen()

    # Give a name to the turtle that we were given back. We'll call it Noah,
    # in honor of the NOAA (National Oceanic and Atmospheric Administration).
    noah = setup_data[0]


    # Your code to perform the animation will go after this line.


    # DO NOT MODIFY THE FOLLOWING LINE! (It make sure the turtle window stays
    # open).
    turtle.done()


# Do not modify anything after this point.
if __name__ == "__main__":
    filename = input("Enter the name of the hurricane data file: ")
    animate_hurricane(filename)
