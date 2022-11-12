# Data preparation and understanding

Use this file to provide evidence for data preparation and understanding.

### Import necessary libraries
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
```
## Data Preparation
In the `main` function, the path to the excel file is defined, then the excel file is loaded into a pandas dataframe.

```
if __name__ == "__main__":
    # Define the path to the excel datafile in a way that works on both Mac and Windows
    trfc_raw_xlsx = Path(__file__).parent.joinpath('data', 'data_set_initial.xlsx')
    # Load the xlsx file into a pandas DataFrame 
    df_trfc_raw_xlsx = pd.read_excel(trfc_raw_xlsx, sheet_name ='interstate-traffic')
```
All the required code for data preparation is gathered in a function called `process_data()`, its argument is `data` which is the pandas Dataframe of the interstate traffic data set.

```
def process_data(data):
    """
    Main function to introduce pandas functions for data preparation and understanding.

    Uses the interstate traffic data set for tracking hourly Interstate 94 Westbound traffic volume.

    Args:
        data: Pandas dataframe of the traffic data

    Returns:
        DataFrame: Prepared pandas dataframe 
    """
```
Dataframe with the data:
```
    df = data
```
Total number of rows and columns in the DataFrame
```
    print("\nShape\n", df.shape)
```
The dataframe has *48204* rows and *9* columns

Print the column headings only
```
    print("\nColumns\n",df.columns)
```
Rename columns; "rain_1h", "snow_1h", "clouds_all" and "weather_main" for simplicity
```
    df.rename(columns = {"rain_1h": "rain","snow_1h": "snow","clouds_all": "cloud","weather_main": "weather"},inplace = True)
```
Print details of the dataframe 
```
    print("\nInfo\n", df.info(verbose=True))
```
**Observation:** We find that there are no missing values in the data. The datatypes of 'holiday','weather' and 'weather_description' are `object`, dataypes of 'temp', 'rain' and 'snow' are `float64`, datatypes of 'cloud' and 'traffic_volume' are `int64` and finally, the dataype of 'date_time' column is  `datetime64[ns]`

Print the first 5 rows
```
    print("\nHead - first 5 rows\n", df.head(5))
```
Set pandas display options to the number of columns and rows in the dataframe
```
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
```
Drop the column weather_description as it causes too much redundancy with weather column
```
    df = df.drop(['weather_description'], axis=1)
```
Convert temperature in Kelvin to Celcius for simplicity
```
    df["temp"] = (df["temp"]-273.15)
```

Print statistical descriptions of the data
```
    print("\Statistical descriptions of data\n", df.describe())
```
**Observation:** There may be inconsistent data entries as temperature records at absolute zero is observed. The distributions of 'snow' and 'rain' are not well defined as there are outliers with extreme high or low records, we may later decide to remove these weather attributes as the attribute 'weather' identifies whether its raining or snowing or not.

**Note:** This command would only include the description of numerical dataype columns, below we include the object type

INCLUDE INFO ABOUT DISTRIBUTION TENDENCIES

Print statistical descriptions of the 'object' type columns
```
    print("\Statistical descriptions of categorical data\n", df.describe(include='object'))
```
Print the number of ocurrences of values in the holiday column
```
    print("\Ocurrences/distribution of values in holiday\n", df['holiday'].value_counts()) 
```
**Observation:** We find that 'None' (working day) with 48143 occurences in the dataset compiles a vast majority of the 'holiday' column

Print the number of duplicates in date column
```
    print("\Duplicates in date\n", df['date_time'].duplicated().sum())
```
**Observation:** There are 7629 duplicate entries in 'date_time' column.

Investigate which observations are duplicates and print them
```
    duplicates = df[df.duplicated(keep=False)]
    print("\Visualize duplicates in date\n", duplicates['date_time'])
```
*Observation:* We see that the duplicates on the variable 'date_time' indicates that for the same day and same time, the record exists in several copies. We must remove the duplicates to clean the data.

Drop the duplicate date entries, keeping only the last duplicated item, print the duplicated sum of 'date_time" column again
```
    df.drop_duplicates(subset=['date_time'],keep='last', inplace=True)
    print("\Duplicates in date\n", df['date_time'].duplicated().sum())
```
*Note:* We have dropped all duplicates in date column

Find the range of the data entries
```
    print("\Min & Max values of data\n", df['date_time'].min(),df['date_time'].max()) 
```
**Observation:** The data entries span a 6 year date range between *2012-10-02 09:00:00* and *2018-09-30 23:00:00*

## Data Exploration

In order to understand how traffic volume changes with respect to date and time, date time column must be parsed to reveal seasonal, annual or daily patterns. 

There are 3 customized functions created to parse 'date_time' column and add additional categorized hour and weekday columns, these are `parse_datetime()`, `categorize_hour()` and `categorize_day()`

### Define a function called `parse_datetime()` to parse the timestamp column and reveal new characteristics such as 'year', 'month', 'hour' ...

```
def parse_datetime(df):
    """
    This function creates new attributes such as Year, Month, Day, etc. by parsing timestamp object and 
    creates additional colums 'categorized_hour' and 'categorized_weekday'

    Args:
        dataframe: pandas dataframe with timestamp 

    Returns:
        dataframe: copy of pandas dataframe with parsed datetime columns and textual descriptions of based from 'Hour' and 'Weekday'
        
    """
    df_copy = df.copy()
    df_copy['Year'] = df_copy['date_time'].dt.year
    df_copy['Month'] = df_copy['date_time'].dt.month
    df_copy['Day'] = df_copy['date_time'].dt.day
    df_copy['Weekday'] = df_copy['date_time'].dt.weekday
    df_copy['Hour'] = df_copy['date_time'].dt.hour
```
Using `categorize_hour()`, add a column to the dataframe giving textual decription of time periods based on hours
```
    df_copy['categorized_hour'] = df_copy['Hour'].apply(categorize_hour)
```
Using `categorize_day()`, add a column to the dataframe giving textual decription of weekdays 
```
   df_copy['categorized_weekday'] = df_copy['Weekday'].apply(categorize_day)
    return df_copy
```

### Define a function called `categorize_hour()` to categorize hours into differet time periods such as; 'Late Night', 'Early Morning'..

Categorizing a day based on its hours can reveal cruical daily patterns such as rush hours where the traffic volumes are exceptionally high

```
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
        return "Evening"
    elif Hour in [21,22,23,0]:
        return "Night"
```


### Define a function called `categorize_day()` to categorize days into days of the week such as; 'Monday','Tuesday'... 

Categorizing a week based on its days can reveal weekly driving patterns of people. Acknowledging which days of the week yield the highest/lowest traffic volumes are important for planning
```
#define a function to categorize days into days of the week 
def categorize_day(Day):
    """
    This function categorizes days of the week into textual variables

    Args:
        Day : Numerical data to be categorized 

    Returns:
        str: Textual description of the asssociated Day
    """
    if Day == 0:
        return "Monday"
    elif Day == 1:
        return "Tuesday"
    elif Day == 2:
        return "Wednesday"
    elif Day == 3:
        return "Thursday"
    elif Day == 4:
        return "Friday"
    elif Day == 5:
        return "Saturday"
    else:
        return "Sunday"
```




## PLOTS
In order to answer the data science questions for the target audience we will implement visualosation tecniques. Through visually observing how certain variables change wih respect to the predictor and outcome variables insightful patterns can be revealed.

### Plot 1 : Aggregate traffic volume with respect to special holiday days (exluding 'None' holiday)
```
def plot_hldy(df_hldy):
    """
    This function creates a new dataframe replacing holiday column with holiday column without None entries
    this function plots the new dataframe's modified column with respect to aggreagate traffic volume

    Args:
        df: dataframe to be plotted

    Returns:
        None
        
    """
```
We have previusly found that 'None' composes of the vast majority of 'holiday' column, In a new dataframe we replace holiday column with holiday column without None entries to visualize the distribution of special days with respect to traffic volumes
```
    spcl_df = df_hldy[df_hldy['holiday'] != 'None']
```
aggregate traffic volume per holiday features in a new dataframe 
```
    df_trfc_spcl = df_hldy.groupby(spcl_df['holiday']).aggregate({'traffic_volume':'mean'})
    print(df_trfc_spcl)
```
plot aggregate traffic volume with respect to holiday days
```
    fig, ax = plt.subplots(figsize=(15,8))
    ax.bar(df_trfc_spcl.index, df_trfc_spcl['traffic_volume'])
    ax.set_title('Average traffic volume per Holiday days')
    plt.show()  
```
**Observation:** From the plot, we observe that the most intense traffic jams happen during New Years Day, than respectively Memorial and Independence Day. Least traffic congestion happens on Colombus Day.



## Plot 2 : Aggregate traffic volume in 2 subplots, first with respect to categorized hour than to categorized weekday
```
def sbplt_categorize_dates(df_ctgrz):
    """
    this function creates 2 subplots aggregate traffic volume per categorized hour and weekday

    Args:
        df_ctgrz: dataframe to be plotted indexing categorized datetime characteristics

    Returns:
        None
        
    """
```
In order to understand how traffic volume changes within a day, plotting aggegate traffic volume over hour descriptions such as 'Afternoon', 'Morning' would be insightfull in understanding daily patterns

aggregate traffic volume per hour description in a new dataframe 
```
    df_hour_traffic = df_ctgrz.groupby('categorized_hour').aggregate({'traffic_volume':'mean'})
    print(df_hour_traffic)
```
Understanding how traffic volume changes within a week is also really important in distinguishing which days of the week yield the most traffic jams 

aggregate traffic volume per categorized weekday in a new dataframe 
```
    df_day_traffic = df_ctgrz.groupby('categorized_weekday').aggregate({'traffic_volume':'mean'})
    print(df_day_traffic)
```
create 2 subplots plotting the mean of traffic volume for each category of hour and weekday 
```
    fig, axs = plt.subplots(2)
    fig.suptitle('Average traffic volume per categorized hour and weekday')
    axs[0].bar(df_hour_traffic.index, df_hour_traffic['traffic_volume'])
    axs[1].bar(df_day_traffic.index, df_day_traffic['traffic_volume'])
    plt.show() 
```
**Observation from categorized hour plot:** We observe that majoirty of the poeple go put in traffic mostly in the Afternoon hours (13,14,15,16) than in the morning. Than, almost at equal traffic volumes comes Early Morning and Afternoon, which is intuitave given these are the times when most people leave for and come back from work. Least traffic congestion by far is observed at Late Nights.

**Observation from categorized weekday plot:** we observe that weekdays or working days usually indicate higher traffic volumes whereas in weekends there is relatively less traffic.

*Remark:* Plotting mean traffic volume over categorized hours imply that early morning and afternoon yield relatively high traffic volumes, which are usually times when people leave and come back from work or school. Plotting mean traffic volume over categorized days imply that weekdays (Monday to Friday) yield relatively higher traffic volumes than weekends (Saturday and Sunday). Hence, we can presume that  for the given road withing the specified timeframe people usually tend to drive on weekdays mostly between early morning to afternoon to get to their work/school. 

## Plot 3: Traffic volume per weather feature
```
def plot_wthr(df_wthr_trfc):
    """
    this function plots traffic volumes per weather features

    Args:
        df_wthr_trfc: dataframe to be plotted

    Returns:
        None
        
    """
```
Understanding the impact of each weather feature on traffic volume is crucial to understand usually under which weather conditions do people tend to go out in traffic

Plot weather over traffic volume
```
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(df_wthr_trfc['weather'], df_wthr_trfc['traffic_volume'])
    ax.set_title('traffic volume per weather features')
    plt.show()
```
**Observation:** We find that almost all weather conditions yield similar traffic volumes expect for 'squal' in wich case we see a sudden drop in traffic intensity.

## Plot 4: (Aggregate) traffic volume over the years
```
def sbplt_trfc_date(df_trfc):
    """
    This function generates 2 subplots displaying how traffic volume changes with respect to time

    Args:
        df_trfc: dataframes to be plotted

    Returns:
        None
        
    """
```
Undertanding how traffic volume changes over time can reveal useful insights about seasanol and annual patterns of traffic volumes.

Aggregate traffic volume over years
```
    df_agg_trfc = df_trfc.groupby('Year').aggregate({'traffic_volume':'mean'})
````
plot 2 subplots; 1st is Traffic volume per years, 2nd is aggregate traffic volume over the years
```
    fig, axs = plt.subplots(2)
    fig.suptitle('Traffic volume over the years')
    axs[0].plot(df_trfc['date_time'], df_trfc['traffic_volume'])
    axs[1].plot(df_agg_trfc.index, df_agg_trfc['traffic_volume'])
    plt.show() 
```
**Observation:** When we look at the annual recorded traffic volume plot, we see a gap within the data between 2014 and 2015 meaning we dont have any records of traffic volume data for year 2015. Hence, in future modeling and prediction stages, the focus will be on the period between 2016 and 2018 which appear to include complete information. From 2nd plot we can also see this decrease.
buna bidaha bak


## Plot 5: Aggregate traffic volume per weather features
```
def sbplts_wthr(df_wthr):
    """
    this function generates 3 subplots of weather features

    Args:
        df_wthr: dataframes to be plotted

    Returns:
        None
        
    """
```
'rain' has an outlier that is its max value which distorts the distribution, we replace the 'rain' column in a new dataframe removing its max value to visualise a cleaner distribution
```
    df_rain_trfc = df_wthr[df_wthr['rain'] != df_wthr['rain'].max()]
```
Aggregate traffic volume per weather feature
```
    df_rain_trfc = df_wthr.groupby('rain').aggregate({'traffic_volume':'mean'})
    df_snow_trfc = df_wthr.groupby('snow').aggregate({'traffic_volume':'mean'})
    df_cloud_trfc = df_wthr.groupby('cloud').aggregate({'traffic_volume':'mean'})
```
Plot weather features over traffic volume
```
    fig, axs = plt.subplots(3)
    fig.suptitle('Traffic volume per numeric weather features')
    axs[0].bar(df_rain_trfc.index, df_rain_trfc['traffic_volume'])
    axs[1].bar(df_snow_trfc.index, df_snow_trfc['traffic_volume'])
    axs[2].bar(df_cloud_trfc.index, df_cloud_trfc['traffic_volume'])
    plt.show()
```
**Observation:**

## Saving the preparared dataframe and calling the functions within the `main` function.

First, call the data preparation function`process_data()` and pass the data, return the processed data
```
if __name__ == "__main__":
    ...
    # Call the data_prep function and pass the data, return the processed data
    df_processed = process_data(df_trfc_raw_xlsx) 
```
Now, parse datetime object in a new dataframe `df_new` to visualize the impact of each date and time characteristics on traffic volume
```
    df_new = parse_datetime(df_processed)
```
 Save the prepared dataframe (`df_processed`) in excel format
```
    prepared_data_xlsx_name = Path(__file__).parent.joinpath('data', 'data_set_prepared.xlsx')
    df_processed.to_excel(prepared_data_xlsx_name, index = False) 
 ```
**Call the plot functions to explore the data visaluations**
Categorized hours and days are plotted using the the parsed dataframe which has the 'Hour' and 'Weekday' information
```     
    sbplt_categorize_dates(df_new)
```
For other plots, the processed data used for simplicity
```
    plot_hldy(df_processed)
    plot_wthr(df_processed)
    sbplt_trfc_date(df_processed)
    sbplts_wthr(df_processed)
```