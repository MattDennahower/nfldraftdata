import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the NFL Combine data
data_path = r'\PATH'  # Update with the actual path
combine_data = pd.read_excel(data_path)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Average 40-yard dash times by position with enhanced visuals
avg_40yd_by_pos = combine_data.groupby('Pos')['40yd'].mean().sort_values()
filtered_combine_data = combine_data[~combine_data['Pos'].isin(['K', 'P'])]

# Create a box plot for 40-yard dash times, excluding K and P positions
plt.figure(figsize=(16, 12))
sns.boxplot(x='40yd', y='Pos', data=filtered_combine_data, palette="coolwarm",
            order=filtered_combine_data.groupby('Pos')['40yd'].median().sort_values().index)

# Adjusting the x-axis to show increments of 0.25 seconds
max_time = filtered_combine_data['40yd'].max()
min_time = filtered_combine_data['40yd'].min()
plt.xticks(np.arange(np.floor(min_time * 4) / 4, np.ceil(max_time * 4) / 4, 0.25))

plt.title('2024 NFL Draft Combine 40-yard Dash Times by Position', fontsize=16)
plt.xlabel('Time (seconds)', fontsize=14)
plt.ylabel('Position', fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
