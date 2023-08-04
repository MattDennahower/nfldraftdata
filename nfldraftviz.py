import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn's style
sns.set(style="whitegrid")

# Load all sheets in the excel file
all_sheets = pd.read_excel('/path_to_your_file/2023 Draft.xlsx', sheet_name=None)

# Rename columns, remove first row, add year column
for sheet, data in all_sheets.items():
    data.columns = data.iloc[0]
    data.drop(index=0, inplace=True)
    data['Year'] = int(sheet)

# Merge data from all sheets
merged_data = pd.concat(all_sheets.values(), ignore_index=True)

# Convert 'No data' to NaN and these columns to float type
numeric_cols = ['Rnd', 'Pick', 'Age']
merged_data[numeric_cols] = merged_data[numeric_cols].replace('No data', np.nan).astype(float)

# Group 'T', 'G', and 'C' positions as 'OL' for the years 2019 and 2020
merged_data.loc[(merged_data['Year'].isin([2019, 2020])) & (merged_data['Pos'].isin(['T', 'G', 'C'])), 'Pos'] = 'OL'

# Create a grouped DataFrame: count of positions for each year
grouped_data_year = merged_data.groupby(['Year', 'Pos']).size().unstack().fillna(0)

# Get top 5 positions
top_positions = merged_data['Pos'].value_counts().head(5).index.tolist()

# Filter the grouped data to include only top 5 positions
grouped_data_year_top5 = grouped_data_year[top_positions]

# Set x-axis values in increments of 1 starting at 2019 and ending at 2023
grouped_data_year_top5 = grouped_data_year_top5.reindex(range(2019, 2024), fill_value=0)

# Set distinct colors for the top 5 positions
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Plot with distinct colors
plt.figure(figsize=(14, 8))
for position, color in zip(grouped_data_year_top5.columns, colors):
    plt.plot(grouped_data_year_top5.index, grouped_data_year_top5[position], marker='o', linewidth=2.5, color=color, label=position)

plt.title('Number of Players Drafted for Top 5 Positions by Year (with OL grouped)', fontsize=20)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Number of Players Drafted', fontsize=15)
plt.grid(True)
plt.xticks(range(2019, 2024), fontsize=12)  # Ensure x-axis only shows integer years
plt.yticks(fontsize=12)
plt.legend(title='Position', title_fontsize='13', fontsize='12')
plt.show()
