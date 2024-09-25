import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='purple', alpha=0.5)
    


    # Create first line of best fit (1880 - 2050)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    future_years = range(1880, 2051)
    line_fit = [slope * year + intercept for year in future_years]
    plt.plot(future_years, line_fit, color='red', label='Best fit line (1880-2050)')

    # Create second line of best fit (2000 - 2050)

    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    future_years_recent = range(2000, 2051)
    line_fit_recent = [slope_recent * year + intercept_recent for year in future_years_recent]
    plt.plot(future_years_recent, line_fit_recent, color='green', label='Best fit line (2000-2050)')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()