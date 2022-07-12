import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # Create scatter plot
    scatter = plt.scatter(x, y)
    # Create first line of best fit
    linreg = linregress(x, y)
    line1 =plt.plot(x, linreg.slope * x + linreg.intercept)
    # Create second line of best fit
    line2 =plt.plot(np.arange(2000,2050), linreg.slope*np.arange(2000,2050) + linreg.intercept)
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
    
