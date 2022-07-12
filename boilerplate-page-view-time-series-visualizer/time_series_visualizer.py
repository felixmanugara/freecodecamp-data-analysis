import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 0, parse_dates = True)

# Clean data
df = df.drop(df[(df['value'] <= df['value'].quantile(0.025)) | (df['value'] >= df['value'].quantile(0.975))].index)


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize =(32,9))

    ax.plot(df['value'], color ='red')
    ax.set(title ='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
           xlabel ='Date',
           ylabel ='Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['Month'] = pd.DatetimeIndex(df_bar.index).month

    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    df_bar = df_bar.unstack()
    month_names= list(calendar.month_name)[1:]
    
    # Draw bar plot
    fig = df_bar.plot(kind= 'bar', figsize = (10,8)).figure

    plt.title('')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    l = plt.legend(title= 'Months', fontsize = 15, labels = month_names)
    l_title = l.get_title()
    l_title.set_fontsize(15)


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig 

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # sort value according to month order
    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1,2, figsize =(28,10))
    sns.boxplot(x = "year", y = "value", data = df_box, ax= axs[0])
    axs[0].set_title("Year-wise Box Plot (Trend)")
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')

    sns.boxplot(x='month',y='value',data=df_box, ax= axs[1])
    axs[1].set_title("Month-wise Box Plot (Seasonality)")
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
