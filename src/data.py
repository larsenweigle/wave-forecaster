import pandas as pd
import numpy as np


def text_to_dataframe(data_path):
    historical_data = pd.read_csv(data_path, delim_whitespace=True, header=0)

    # drop the units row
    units = historical_data.iloc[0]
    historical_data.drop(0, inplace=True)

    # reset the index since we are now missing a row
    historical_data = historical_data.reset_index(drop=True)

    return units, historical_data


def convert_to_numerical_data(dataframe):
    # Convert all columns to numerical values
    dataframe.apply(pd.to_numeric)

    # Convert specific columns to integers
    columns_to_convert_to_int = ['#YY', 'MM', 'DD', 'hh', 'mm']
    for col in columns_to_convert_to_int:
        dataframe[col] = dataframe[col].astype(int)


def convert_to_hourly(dataframe, minute=0):
    # Drop rows where 'mm' column is not 0
    drop_indices = dataframe[dataframe['mm'] != minute].index
    dataframe.drop(drop_indices, inplace=True)


def check_for_missing_rows(dataframe):
    # NOTE: This function assumes that the dataframe is sorted by datetime
    missing_indices = []

    # Iterate over rows and check for a time difference of more than 60 minutes
    for i in range(1, dataframe.shape[0]):
        time_diff = dataframe.index[i] - dataframe.index[i-1]
        if time_diff > pd.Timedelta(minutes=60):
            missing_indices.append(i)

    return missing_indices


def build_supervised_learning_dataset(dataframe, missing_indices, feature_set=['WVHT', 'DPD', 'APD', 'MWD'], window=24, lead=24, step=1):
    # Convert missing_indices to a set for faster lookup
    missing_set = set(missing_indices)

    X, y = [], []

    for i in range(dataframe.shape[0] - window * step - lead + 1):
        if any([(i + j * step) in missing_set for j in range(window)]):
            continue
        
        indices = [i + j * step for j in range(window)]
        x_i = dataframe.iloc[indices][feature_set].to_numpy()

        x_i = x_i.flatten()

        y_i = dataframe.iloc[indices[-1] + lead]['WVHT']

        X.append(x_i)
        y.append(y_i)

    return np.array(X), np.array(y)


def process_file_to_hourly_last(file_path):
    data = pd.read_csv(file_path, delim_whitespace=True, skiprows=1)
    data.columns = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'WDIR', 'WSPD', 'GST', 'WVHT', 'DPD', 'APD', 'MWD', 'PRES', 'ATMP', 'WTMP', 'DEWP', 'VIS', 'TIDE']
    data['datetime'] = pd.to_datetime(data[['Year', 'Month', 'Day', 'Hour', 'Minute']])
    
    # Removing the minute component from the datetime
    data['datetime'] = data['datetime'].apply(lambda dt: dt.replace(minute=0))
    # Dropping the 'Minute' column
    data.drop(columns=['Minute'], inplace=True)
    
    # Setting the datetime as the index
    data.set_index('datetime', inplace=True)
    
    # Replace outlier values
    outlier_values = [99, 999, 9999]
    for column in data.columns:
        if data[column].dtype in [float, int]:
            data[column] = data[column].replace(outlier_values, np.nan)

    # Keeping only the last entry for each hour
    data_hourly_last = data.groupby(data.index).last()

    return data_hourly_last