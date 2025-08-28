"""
Group name: DANALA 04
Syed Haroon Ahmad = s393516
Md Adnan Abir = s382198
Simbarashe Mutyambizi = s385833
Najmus Sakeeb= s393942
"""
#%% 
# Declaration of libraries

import pandas as pd 
import glob
import os
#Question 2: Seasonal Average
# Create empty files for outputs of all 3 parts of Question 2
# If the files already exist, they will be overwritten with empty content
file_name = "average_temp.txt"
content = ""
with open(file_name, "w") as file:
    file.write(content)  
file_name_2 = "largest_temp_range_station.txt"
with open(file_name_2, "w") as file:
    file.write(content)
file_name_3 = "temperature_stability_stations.txt"
with open(file_name_3, "w") as file:
    file.write(content)
# this function will read and concat all of them into one big dataframe
def read_and_concat_csv(folder_path):
    # Get all CSV files in the folder
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    
    # Read and store each CSV into a list
    dfs = []
    for file in csv_files:
        df = pd.read_csv(file)
        dfs.append(df)
    
    # Concatenate all dataframes vertically
    big_df = pd.concat(dfs, ignore_index=True)
    
    return big_df
# Here I utilize the function and we can get a concatenated dataframe of all the csv files in the temperatures folder
folder_path = r"D:\Masters\Masters_work\Study\Y1_S1\HIT137\Assignment_2\HIT_137_Assignment_2\temperatures"
df = read_and_concat_csv(folder_path)
df_months = df.iloc[:,4:16]
df_month_avg = pd.DataFrame([df_months.columns, df_months.mean(axis=0).values])
# Define month groups for each season
summer_cols = ['December', 'January', 'February']
autumn_cols = ['March', 'April', 'May']
winter_cols = ['June', 'July', 'August']
spring_cols = ['September', 'October', 'November']
# Calculate seasonal averages
summer_avg = df_months[summer_cols].mean(axis=1).mean().round(1)
autumn_avg = df_months[autumn_cols].mean(axis=1).mean().round(1)
winter_avg = df_months[winter_cols].mean(axis=1).mean().round(1)
spring_avg = df_months[spring_cols].mean(axis=1).mean().round(1)
# Create new DataFrame to contain the seasonal averages
df_season_avg = pd.DataFrame([
    [summer_avg, autumn_avg, winter_avg, spring_avg]  # second row values
], columns=['Summer', 'Autumn', 'Winter', 'Spring'])
# generate the output text that is going to be written to the average_temp.txt file
output_text = f"""
Summer: {summer_avg}°C
Winter: {winter_avg}°C
Autumn: {autumn_avg}°C
Spring: {spring_avg}°C
"""
#write file into the average_temp.txt file
with open(file_name, "w") as f:
    f.write(output_text)
# Question 2: Temparature Range 
# group by the first column so all of the stations are grouped together
df_sorted = df.sort_values(by=df.columns[0], key=lambda col: col.astype(str))
df_sorted = df_sorted.reset_index(drop=True)
# this function calculates the range of the temperatures for each station
def calculate_range(df_sorted):
    # Define the number of columns to consider for max, min, and range calculations
    cols_to_consider = df_sorted.columns[4:]

    # Initialize lists to store results
    first_values = []
    max_values = []
    min_values = []
    ranges = []

    # Iterate over groups of 20 rows
    for i in range(0, len(df_sorted), 20):
        group = df_sorted.iloc[i:i+20]

        # Get the first value from the first column
        first_value = group.iloc[0, 0]
        first_values.append(first_value)

        # Calculate max, min, and range for the group
        group_max = group[cols_to_consider].max().values
        group_min = group[cols_to_consider].min().values

        # Append max, min, and range values to lists
        max_values.append(group_max)
        min_values.append(group_min)

    # Create a new dataframe with the results
    df_new = pd.DataFrame({
        'Station_Name': first_values,
        'Max Values': max_values,
        'Min Values': min_values,
    })
    max_col = 'Max Values'
    min_col = 'Min Values'
    # Calculate max and min values for each list
    df_new['Max'] = df_new[max_col].apply(lambda x: max(x))
    df_new['Min'] = df_new[min_col].apply(lambda x: min(x))

    # Calculate range for each list
    df_new['Highest_Range'] = df_new.apply(lambda row: row['Max'] - row['Min'], axis=1)
    df_new = df_new.drop(columns=[max_col, min_col])
    return df_new

# calcualte the range of the temperatures for each station and store it in the df_new dataframe    
df_new = calculate_range(df_sorted)
results = df_new.loc[[df_new['Highest_Range'].idxmax()]].reset_index(drop=True, inplace=False)
# finding the row with the higheest range its corresponding max and min values
Max_range = results["Highest_Range"].values[0]
Max_station = results['Station_Name'].values[0]      
Max_value = results["Max"].values[0]
Min_value = results["Min"].values[0]
# generate the output text that is going to be written to the largest_temp_range_station.txt file
output_text_2 = f"""
Station {Max_station}: Range {Max_range:.1f}°C(Max: {Max_value:.1f}°C, Min: {Min_value:.1f}°C)"""
with open(file_name_2, "w") as f:
    f.write(output_text_2)
# Question 2: Temperature Stability

# generate the funciton that calculates the standard deviation of the temperatures for each station
def calculate_SD(df_sorted):
    # Define the number of columns to consider for max, min, and range calculations
    cols_to_consider = df_sorted.columns[4:]

    # Initialize lists to store results
    first_values = []
    SD_values = []


    # Iterate over groups of 20 rows
    for i in range(0, len(df_sorted), 20):
        group = df_sorted.iloc[i:i+20]

        # Get the first value from the first column
        first_value = group.iloc[0, 0]
        first_values.append(first_value)

        # Calculate max, min, and range for the group
        group_SD = group[cols_to_consider].stack().std()
            
        SD_values.append(group_SD)

    # Create a new dataframe with the results
    df_new = pd.DataFrame({
        'Station_Name': first_values,
        'SD Values': SD_values,
    }) 
    return df_new
df_new = calculate_SD(df_sorted)
# This will find he lasrgest and smallest standard deviation values and their corresponding station names
SD_max_results = df_new.loc[[df_new['SD Values'].idxmax()]].reset_index(drop=True, inplace=False)
SD_min_results = df_new.loc[[df_new['SD Values'].idxmin()]].reset_index(drop=True, inplace=False)
# finding the row with the higheest range its corresponding max and min values
MostStable_SD_Station = SD_min_results["Station_Name"].values[0]
MostVariable_SD_Station = SD_max_results["Station_Name"].values[0]
MostStable_SD_Value = SD_min_results["SD Values"].values[0]
MostVariable_SD_Value = SD_max_results["SD Values"].values[0]
# the output text that is going to be written to the temperature_stability_stations.txt file
output_text_3 = f"""
Most Stable: Station {MostStable_SD_Station}: StdDev {MostStable_SD_Value:.1f}°C
Most Variable: Station {MostVariable_SD_Station}: StdDev {MostVariable_SD_Value:.1f}°C"""
# writing the final output text to the temperature_stability_stations.txt file
with open(file_name_3, "w") as f:
    f.write(output_text_3)