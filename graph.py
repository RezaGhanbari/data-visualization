from collections import Counter
import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = "sample_sfpd_incident_all.csv"


def pars(raw_file, delimiter):
    """Parses a raw csv file to a JSON-like object"""

    # Open csv file, and safely close it when you're done
    open_file = open(raw_file)

    # Read the csv data
    csv_data = csv.reader(open_file, delimiter=delimiter)

    # Setup an empty list
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()

    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close the csv file
    open_file.close()

    return parsed_data


def visualize_days():
    """Visualize data by day of week"""

    # grab our parsed data that we parsed earlier
    data_file = pars(MY_FILE, ",")

    # make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)
    # separate the x-axis data (the days of the week) from the
    # 'counter' variable from the y-axis data (the number of
    # incidents for each day)
    data_list = [
        counter["Monday"],
        counter["Tuesday"],
        counter["Wednesday"],
        counter["Thursday"],
        counter["Friday"],
        counter["Saturday"],
        counter["Sunday"],
    ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assign the data to a plot
    plt.plot(data_list)

    # Assign labels to the plot from day_list
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the graph
    plt.savefig("Days.png")

    # Close figure
    plt.clf()


def visualize_type():
    """Visualize data by category in a bar graph"""

    # Grab our parsed data
    data_file = pars(MY_FILE, ",")

    # Same as before, this returns a dict where it sums the total
    # incidents per Category
    counter = Counter(item["Category"] for item in data_file)

    # Set the labels which are based on the keys of our counter.
    # Since order doesn't matter, we can just used counter.keys()
    labels = tuple(counter.keys())

    # Set where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5

    # Width of each bar
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width+0.01)

    # Assign labels and ticks location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.5)

    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save the plot!
    plt.savefig("Type.png")

    # Close figure
    plt.clf()


def main():
    visualize_days()
    visualize_type()


if __name__ == '__main__':
    main()
