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


def calculate_category(wind_speed_mph: int) -> int:
    """
    Returns which category a hurricane falls into based on its wind speed.

    Parameters:
        wind_speed_mph (int): The maximum wind speed in miles per hour

    Returns:
        int: The category of the hurricane from 0 (not hurricane strength) to 5.
    """
    if wind_speed_mph > 156:
        return 5
    elif wind_speed_mph >= 130:
        return 4
    elif wind_speed_mph >= 111:
        return 3
    elif wind_speed_mph >= 96:
        return 2
    elif wind_speed_mph >= 74:
        return 1
    else:
        return 0


def get_point_color(category: int) -> str:
    """
    Specifies the color that a data point should be drawn in based on the hurricane's category.

    Parameters:
        category (int): The category level of the hurricane from 0 (not hurricane strength) to 5.

    Returns:
        str: The turtle color name to be used for that category.
    """
    if category == 0:
        return "white"
    elif category == 1:
        return "blue"
    elif category == 2:
        return "green"
    elif category == 3:
        return "yellow"
    elif category == 4:
        return "orange"
    elif category == 5:
        return "red"


def get_line_size(category: int) -> int:
    """
    Specifies the pen thickness to draw with based on the hurricane's category.

    Parameters:
        category (int): The category level of the hurricane from 0 (not hurricane strength) to 5.

    Returns:
        int: The turtle pen thickness to be used for that category.
    """
    return category + 1


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

    # Prepare the turtle and the file
    noah.penup()
    noah.hideturtle()
    f = open(data_filename, "r")
    all_hurricane_data = f.readlines()

    for line in all_hurricane_data:
        # skip empty lines
        if line.strip() == "":
            continue

        data_points = line.split(",")

        # Expected CSV columns: date, time, latitude, longitude, wind_speed, pressure
        lat_str = data_points[2]
        lon_str = data_points[3]
        wind_str = data_points[4]

        # convert to numeric types
        latitude = float(lat_str)
        longitude = float(lon_str)
        wind_speed = int(float(wind_str))

        # set drawing properties
        category = calculate_category(wind_speed)
        color = get_point_color(category)
        pen_size = get_line_size(category)

        # draw and label the point
        noah.pensize(pen_size)
        noah.pencolor(color)
        noah.goto(longitude, latitude)
        if category != 0:
            noah.write(str(category))

        # prepare the turtle for moving to the next location
        noah.pendown()
        noah.showturtle()

    f.close()
    # DO NOT MODIFY THE FOLLOWING LINE! (It make sure the turtle window stays
    # open).
    turtle.done()


# Do not modify anything after this point.
if __name__ == "__main__":
    filename = input("Enter the name of the hurricane data file: ")
    animate_hurricane(filename)
