"""
Group name: DANALA 04
Syed Haroon Ahmad = s393516
Md Adnan Abir = s382198
Simbarashe Mutyambizi = s385833
Najmus Sakeeb= s393942
"""


#%%
import pandas as pd 
import numpy as np
import glob
import os


#Question 2 Seasonal Average
#%%
file_name = "average_temp.txt"
content = ""
with open(file_name, "w") as file:
    file.write(content)
#%%
df = pd.read_csv('temperatures\stations_group_1986.csv')


#%%

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

# Create new DataFrame
df_season_avg = pd.DataFrame([
    [summer_avg, autumn_avg, winter_avg, spring_avg]  # second row values
], columns=['Summer', 'Autumn', 'Winter', 'Spring'])

output_text = f"""
Summer: {summer_avg}°C
Winter: {winter_avg}°C
Autumn: {autumn_avg}°C
Spring: {spring_avg}°C
"""

with open(file_name, "w") as f:
    f.write(output_text)

