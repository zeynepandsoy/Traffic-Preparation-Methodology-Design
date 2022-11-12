import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path



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


#define a function to parse timestamp column date_time 
def parse_datetime(df):
    """
    This function creates new attributes such as Year, Month, Day, etc. by parsing timestamp object

    Args:
        df: pandas dataframe with timestamp 

    Returns:
        df: pandas dataframe with parsed datetime columns 'year', 'month', 'day', 'weekday', 
        'hour', and another categorical column; 'Hour_desc' created using categorize_hour(Hour)
        
    """
    df_copy = df.copy()
    df_copy['Year'] = df_copy['date_time'].dt.year
    df_copy['Month'] = df_copy['date_time'].dt.month
    df_copy['Day'] = df_copy['date_time'].dt.day
    df_copy['Weekday'] = df_copy['date_time'].dt.weekday
    df_copy['Hour'] = df_copy['date_time'].dt.hour
    # Add a column to the dataframe giving textual decription of time periods based on hours
    df_copy['Hour_desc'] = df_copy['Hour'].apply(categorize_hour)
    return df_copy


def plot_hldy(df_hldy):
    """
    This function creates a new dataframe replacing holiday column with holiday column without None entries
    this function plots the new dataframe's modified column with respect to aggreagate traffic volume

    Args:
        df: dataframe to be plotted

    Returns:
        None
        
    """
    #'None' composes of the vast majority of 'holiday' column. remove None to visualize the distribution of special days
    spcl_df = df_hldy[df_hldy['holiday'] != 'None']
    #aggregate traffic volume hour description in a new dataframe 
    df_trfc_spcl = df_hldy.groupby(spcl_df['holiday']).aggregate({'traffic_volume':'mean'})
    print(df_trfc_spcl)

    fig, ax = plt.subplots(figsize=(15,8))
    ax.bar(df_trfc_spcl.index, df_trfc_spcl['traffic_volume'])
    ax.set_title('Average traffic volume per Holiday days')
    plt.show()  

def plot_hour_desc(df_hr_dsc):
    """
    this function plots aggregate traffic volume per hour descriptions such as afternoon, late night ...

    Args:
        df_hr_dsc: dataframe to be plotted

    Returns:
        None
        
    """
    #aggregate traffic volume hour description in a new dataframe 
    df_hour_traffic = df_hr_dsc.groupby('Hour_desc').aggregate({'traffic_volume':'mean'})
    print(df_hour_traffic)

    #plot the mean of traffic volume for each group of hour desciption 
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(df_hour_traffic.index, df_hour_traffic['traffic_volume'])
    ax.set_title('Average traffic volume per hour descriptions')
    plt.show() 

def plot_wthr(df_wthr_trfc):
    """
    this function plots traffic volumes per weather features

    Args:
        df_wthr_trfc: dataframe to be plotted

    Returns:
        None
        
    """
    #Plot weather over traffic volume
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(df_wthr_trfc['weather'], df_wthr_trfc['traffic_volume'])
    ax.set_title('traffic volume per weather features')
    plt.show()

def sbplt_trfc_date(df_trfc):
    """
    This function generates 2 subplots displaying how traffic volume changes with respect to time

    Args:
        df_trfc: dataframes to be plotted

    Returns:
        None
        
    """
    #aggregate traffic volume over years
    df_agg_trfc = df_trfc.groupby('Year').aggregate({'traffic_volume':'mean'})
    # plot Traffic volume per years
    fig, axs = plt.subplots(2)
    fig.suptitle('Traffic volume over the years')
    axs[0].plot(df_trfc['date_time'], df_trfc['traffic_volume'])
    axs[1].plot(df_agg_trfc.index, df_agg_trfc['traffic_volume'])
    plt.show() 

def sbplts_wthr(df_wthr):
    """
    this function generates 3 subplots of weather features

    Args:
        df_wthr: dataframes to be plotted

    Returns:
        None
        
    """

    df_rain_trfc = df_wthr.groupby('rain').aggregate({'traffic_volume':'mean'})
    #rain has an outlier that is its max value which distorts the distribution 
    df_rain_trfc = df_wthr[df_wthr['rain'] != df_wthr['rain'].max()]
    df_snow_trfc = df_wthr.groupby('snow').aggregate({'traffic_volume':'mean'})
    df_cloud_trfc = df_wthr.groupby('cloud').aggregate({'traffic_volume':'mean'})
    

    #Plot weather features over traffic volume
    fig, axs = plt.subplots(3)
    fig.suptitle('Traffic volume per numeric weather features')
    axs[0].bar(df_rain_trfc.index, df_rain_trfc['traffic_volume'])
    axs[1].bar(df_snow_trfc.index, df_snow_trfc['traffic_volume'])
    axs[2].bar(df_cloud_trfc.index, df_cloud_trfc['traffic_volume'])
    plt.show()


def process_data(data):
    """
    Main function to introduce pandas functions for data preparation and understanding.

    Uses the interstate traffic data set for tracking hourly Interstate 94 Westbound traffic volume.

    Args:
        data: Pandas dataframe of the traffic data

    Returns:
        DataFrame: Prepared pandas dataframe 
    """
    # Dataframe with the data
    df = data

    # Print the total number of rows and columns in the DataFrame
    print("\nShape\n", df.shape)

    # Print the column headings only
    print("\nColumns\n",df.columns)

    # Rename columns for simplicity
    df.rename(columns = {"rain_1h": "rain","snow_1h": "snow","clouds_all": "cloud","weather_main": "weather"},inplace = True)

    # Print details - including data types about the rows and columns
    print("\nInfo\n", df.info(verbose=True))  # there are no missing values

    # Print the first 5 rows
    print("\nHead - first 5 rows\n", df.head(5))

    # Set pandas display options to the number of columns and rows in the dataframe
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)

    # Drop weather_description as it causes too much redundancy with weather_main
    df = df.drop(['weather_description'], axis=1)
    print(df.head(5))

    #convert temperature in Kelvin to Celcius for simplicity
    df["temp"] = (df["temp"]-273.15)

    # Print descriptions of the data 
    print("\Statistical descriptions of data\n", df.describe()) 

    # Print descriptions of the categorical data 
    print("\Statistical descriptions of categorical data\n", df.describe(include='object'))

    # Print the number of ocurrences of values in the holiday column
    print("\Ocurrences/distribution of values in holiday\n", df['holiday'].value_counts()) 

    # Print the number of duplicates in date column
    print("\Duplicates in date\n", df['date_time'].duplicated().sum())

    # Drop the duplicate date entries 
    df.drop_duplicates(subset=['date_time'],keep='last', inplace=True)
    print("\Duplicates in date\n", df['date_time'].duplicated().sum())

    # Find the range of the data entries
    print("\Min & Max values of data\n", df['date_time'].min(),df['date_time'].max()) 

    return df
    

    


if __name__ == "__main__":
    # Define the path to the excel datafile in a way that works on both Mac and Windows
    trfc_raw_xlsx = Path(__file__).parent.joinpath('data', 'interstate-traffic.xlsx')
    # Load the xlsx file into a pandas DataFrame 
    df_trfc_raw_xlsx = pd.read_excel(trfc_raw_xlsx, sheet_name ='interstate-traffic')
    # Call the data_prep function and pass the data, return the processed data
    df_processed = process_data(df_trfc_raw_xlsx) 
    #parse_datetime  
    df_new = parse_datetime(df_processed)
    # Save the prepared dataframe
    prepared_data_xlsx_name = Path(__file__).parent.joinpath('data', 'prepared_data.xlsx')
    df_processed.to_excel(prepared_data_xlsx_name, index = False) ##WRONG
      
    #plot_hour_desc(df_new)
    #plot_hldy(df_processed)
    #plot_wthr(df_processed)
    #sbplt_trfc_date(df_processed)
    sbplts_wthr(df_processed)

