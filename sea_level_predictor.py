import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df_sea_level = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    df_sea_level.plot(x='Year', y='CSIRO Adjusted Sea Level', kind='scatter', ax=ax);
    ax.set_title('Rise in Sea Level')
    ax.set_ylabel('Sea Level (inches)')

    # Create first line of best fit
    lr = linregress(x=df_sea_level.Year, y=df_sea_level['CSIRO Adjusted Sea Level'])
    _2014_to_2050 = pd.Series(range(2014,2051))
    x = pd.concat([df_sea_level.Year, _2014_to_2050], axis=0)
    ax.plot(x, lr.intercept + lr.slope*x, 'r');

    # Create second line of best fit
    df_sea_level_after_2000 = df_sea_level[df_sea_level.Year >= 2000]
    lr2 = linregress(x=df_sea_level_after_2000.Year, y=df_sea_level_after_2000['CSIRO Adjusted Sea Level'])
    x2 = pd.concat([df_sea_level_after_2000.Year, _2014_to_2050], axis=0)
    ax.plot(x2, lr2.intercept + lr2.slope*x2);

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()