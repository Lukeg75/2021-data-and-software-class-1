#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data(filename,delimiter=',',starting_row=0):
    """This function reads data from a specified filename. 
    The specified filename should point to a .csv file."""
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt(filename, delimiter=delimiter,skip_header=5)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    temperature_data = np.array(all_data[starting_row:,:], dtype=float)
    return temperature_data

temperature_data = read_data("data/110-tavg-12-12-1950-2020.csv", starting_row=5)

# Compute a new column by multiplying column number 1 to Kelvin
temperature_kelvin = (temperature_data[:,1,None] - 32) * 5/9 + 273

# Append this new column to the existing temperature_data array
processed_temperature_data = np.append(temperature_data, temperature_kelvin,1)
print (processed_temperature_data)

# Create a figure of the processed data
temperature_figure = plt.figure()
temperature_plot = plt.bar (processed_temperature_data[:,0],processed_temperature_data[:,2], width=30, color='green')
plt.show(block=True)
temperature_figure.savefig('results/temperature-over-time.pdf')

all_data = pd.read_csv("data/110-tavg-12-12-1950-2020.csv", index_col='Date', header=4)
all_data.info()
all_data.to_json("results/data_output.json")

print("hello world", all_data.loc['195012':'197512','Value'])

json_data = pd.read_json("results/data_output.json")
json_data.info()

temperature_plot = plt.bar (all_data.loc[:,"Value"], height=all_data.loc[:,"Value"], width=30)
plt.show(block=True)

