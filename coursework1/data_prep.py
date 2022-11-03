import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#define a function to parse timestamp column date_time
def parse_datetime(df, date_time):
    """
    This function creates new attributes such as Year, Month, Day, etc. by parsing timestamp object

    Args:
        df: dataframe with timestamp 
        date_time: datetime object

    Returns:
        
    """
    # Converting date_time feature to 'Date-time format'
    #df[date_time] = pd.to_datetime(df[date_time])
    df['Year'] = df[date_time].dt.year
    df['Month'] = df[date_time].dt.month
    df['Day'] = df[date_time].dt.day
    df['Weekday'] = df[date_time].dt.weekday
    df['Hour'] = df[date_time].dt.hour


#define a function to categorize hours into different time periods
def categorize_hour(Hour):
    """
    This function categorizes hours of the day into textual variables describing time periods

    Args:
        Hour : Numerical data to be categorized 

    Returns:
        str: Textual description of the asssociated hours
    """
    if Hour in [1,2,3,4]:
        return "Late Night"
    elif Hour in [5,6,7,8]:
        return "Early Morning"
    elif Hour in [9,10,11,12]:
        return "Morning"
    elif Hour in [13,14,15,16]:
        return "Afternoon"
    elif Hour in [17,18,19,20]:
        return "Evening/Rush Hour"
    elif Hour in [21,22,23,0]:
        return "Night"







def process_data(data):
    """
    Main function to introduce pandas functions for data preparation and understanding.

    Uses the interstate traffic data set for tracking hourly Interstate 94 Westbound traffic volume.

    Args:
        data: Pandas dataframe of the traffic data

    Returns:
        None
    """
    # Dataframe with the data
    df = data
    # Print the total number of rows and columns in the DataFrame
    print("\nShape\n", df.shape)
    # Print the column headings only
    print("\nColumns\n",df.columns)
    # Rename columns for simplicity
    df.rename(columns = {"rain_1h": "rain","snow_1h": "snow","clouds_all": "cloud","weather_main": "weather"},inplace = True)
    # Print details about the rows and columns, including data types
    print("\nInfo\n", df.info(verbose=True))  #there are no missing values, 
    # Print the first 5 rows
    print("\nHead - first 5 rows\n", df.head(5))
    # Print descriptions of the data 
    print("\Statistical descriptions of data\n", df.describe())
    #convert temperature in Kelvin to Celcius for simplicity
    df["temp"] = (df["temp"]-273.15)
    print(df.head(5))
    #what is the number of ocurrences of values in the holiday column
    print("\Ocurrences/distribution of values in holiday\n", df['holiday'].value_counts())
    #print to see if there are any missing values
    print("\Missing Values\n", df.isnull().sum())  
    # Print the number of duplicates in date column
    print("\Duplicates in date\n", df['date_time'].duplicated().sum())
    # Drop the duplicate date entries 
    df.drop_duplicates(subset=['date_time'],keep='last', inplace=True)
    print("\Duplicates in date\n", df['date_time'].duplicated().sum())
    # Find the range of the data entries
    print("\Min & Max values of data\n", df['date_time'].min(),df['date_time'].max()) 
    # use customized function parse_datetime to parse datetime object
    parse_datetime(df, 'date_time')
    print("\dataframe with parsed dates\n", df.head(5))
    #
    print("\Ocurrences/distribution of values in hour\n", df['Hour'].value_counts().sum())
    # Add a column to the dataframe giving textual decription of time periods 
    df['Hour_desc'] = df['Hour'].apply(categorize_hour)
    print(df['Hour_desc'].value_counts())
    print(df.head(5))

    # Set pandas display options to the number of columns and rows in the dataframe
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)

    # plot 2 subplots of traffic volume over date time, 1st plot is a line plot, 2nd is a bar plot
    #fig, axs = plt.subplots(2, 1, figsize=(9, 3))
    #fig.suptitle('Categorical Plotting')
    #axs[0].plot(df['date_time'], df['traffic_volume'])
    #axs[1].bar(df['date_time'], df['traffic_volume'])
    #plt.show()
    df.corr().abs()[["traffic_volume"]]
 
    # plot Traffic volume per years
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(df['date_time'], df['traffic_volume'])
    ax.set_title('Traffic volume per year')
    plt.show()  #notice there is large gap for year 2015 -SHOULD WE DROP ROWS CORRESPONDING TO THE GAP

    #aggregate traffic volume hour description 
    df_hour_traffic = df.groupby('Hour_desc').aggregate({'traffic_volume':'mean'})
    print(df_hour_traffic)

    #plot the mean of traffic volume for each group of hour desciption 
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(df_hour_traffic.index, df_hour_traffic['traffic_volume'])
    ax.set_title('Average traffic volume per hour descriptions')
    plt.show() 




 
    ##Drop weather_description as it causes too much redundancy with weather_main
    ##df = df.drop(['weather_description'], axis=1)
    ## are there inconsistent values?
    ## Print the unique values in the `Date` column
    ## print("\nUnique values in the date column\n", df['date_time'].unique())



     
    


    


if __name__ == "__main__":
    # Define the path to the excel datafile in a way that works on both Mac and Windows
    trfc_raw_xlsx = Path(__file__).parent.joinpath('data', 'interstate-traffic.xlsx')
    # Load the xlsx file into a pandas DataFrame 
    df_trfc_raw_xlsx = pd.read_excel(trfc_raw_xlsx, sheet_name ='interstate-traffic')
    # Call the data_prep function and pass the data
    process_data(df_trfc_raw_xlsx)