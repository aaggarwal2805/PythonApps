import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

TYPE_PLOT_FILENAME = "Type.png"
DAYS_PLOT_FILENAME = "Days.png"

def parse(raw_file):
    """
    Parses CSV file to create dictionary entries
    """
    parsed_data = []
    with open(raw_file, 'r') as r:
        rows = csv.reader(r)
        fields = rows.next()
        counter = 0
        for r in rows:
            parsed_data.append(dict(zip(fields, r)))

    return parsed_data

def fetch_incident_by_days(parsed_data):
    """
    Parse and return number of incidents by day of the week
    """
    incident_counter = dict()

    for incident in parsed_data:
        day_of_week = incident['DayOfWeek']
        if day_of_week in incident_counter:
            incident_counter[day_of_week] += 1
        else:
            incident_counter[day_of_week] = 1

    return incident_counter


def visualize_days(parsed_data, output_dir):
    """Visualize data by day of week"""

    # Returning no. of incidents by each day of the week
    counter = fetch_incident_by_days(parsed_data)

    # data_list = fetch_incident_by_days.keys()

    # Separating the counter to have an ordered list
    y_values = [
                  counter["Monday"],
                  counter["Tuesday"],
                  counter["Wednesday"],
                  counter["Thursday"],
                  counter["Friday"],
                  counter["Saturday"],
                  counter["Sunday"]
                ]

    # Creating labels for x-axis
    x_labels = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assigning the data to plot
    plt.plot(y_values)

    # Assigning xticks on x-axis
    plt.xticks(range(len(x_labels)), x_labels)

    # Save the graph and show the figure
    file_name = os.path.join(output_dir, DAYS_PLOT_FILENAME)
    plt.savefig(file_name)
    plt.show()


def fetch_incident_by_category_and_resolution(parsed_data):
    """
    Parse and return count of total incidents and unresolved incidents by category
    """
    incident_counter = dict()

    for incident in parsed_data:
        category = incident['Category']
        resolution = incident['Resolution']
        if category in incident_counter:
            incident_counter[category][0] += 1
            if resolution == "NONE":
                incident_counter[category][1] += 1
        else:
            if resolution == "NONE":
                incident_counter[category] = [1, 1]
            else:
                incident_counter[category] = [1, 0]

    return incident_counter


def visualize_type(parsed_data, output_dir):
    """Data visualization of total incidents and fraction
    of unresolved incidents per category via bar graph"""

    # Fetching incident data by category
    counter = fetch_incident_by_category_and_resolution(parsed_data)

    # List of total incidents by Category
    # list of unsolved incidents by Category
    y1_values = [item[0] for item in counter.values()]
    y2_values = [item[1] for item in counter.values()]

    # Category labels
    x_labels = tuple(counter.keys())

    # Width of each bar
    bar_width = 0.4

    # bar locations on x-axis
    x1_locations = np.arange(len(x_labels))
    x2_locations = x1_locations + bar_width

    # assigning data to a bar plot
    plt.bar(x1_locations, y1_values, width=bar_width, label = "Total")
    plt.bar(x2_locations, y2_values, width=bar_width, label = "Unresolved")

    # Assigning labels and tick location to x-axis
    plt.xlabel('Incident Category', fontweight='bold')
    plt.ylabel('Incident Count', fontweight='bold')
    plt.xticks(x1_locations + bar_width/2, x_labels, rotation=90)

    # Giving some more room below x-axis
    plt.subplots_adjust(bottom=0.4)

    # Making the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    plt.legend()
    file_name = os.path.join(output_dir, TYPE_PLOT_FILENAME)
    plt.savefig(file_name)
    plt.show()

def main(input_file, output_dir):
    parsed_data = parse(input_file)
    visualize_days(parsed_data, output_dir)
    visualize_type(parsed_data, output_dir)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    main(input_file, output_dir)
