# Data preparation and understanding

Use this file to provide evidence for data preparation and understanding.

### Import necessary libraries
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
```
## Data preparation
In the `main` function, the path to the excel file is defined, then the excel file is loaded into a pandas dataframe.

```
if __name__ == "__main__":
    # Define the path to the excel datafile in a way that works on both Mac and Windows
    trfc_raw_xlsx = Path(__file__).parent.joinpath('data', 'interstate-traffic.xlsx')
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
**Observation:** There may be inconsistent data entries as temperature records at absolute zero is observed. The distributions of 'snow' and 'rain' are not well defined as there are outliers with extreme high or low records.

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
*Note:* We're only interested in duplicates in date column as duplicates are already expected in all other columns
```
    print("\Duplicates in date\n", df['date_time'].duplicated().sum())
```
**Observation:** There are 7629 duplicate entries in 'date_time' column.

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