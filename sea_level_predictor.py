import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.figure(figsize=(14, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    recent_slope, recent_intercept, recent_r_value, recent_p_value, recent_std_err = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    sec_x_pred = pd.Series([i for i in range(2000, 2051)])
    sec_y_pred = recent_intercept + recent_slope * sec_x_pred
    plt.plot(sec_x_pred, sec_y_pred, 'b')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()