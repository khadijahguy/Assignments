# Creator : Khady Gueye

import pandas as pd
import matplotlib.pyplot as plt

# Task 1:
df = pd.read_csv('car_info.csv')

# Print the shape of the DataFrame
print(f"Shape of the dataframe: {df.shape}")

# Task 2:
japanese_v6_cars = df[(df['origin'] == 'japan') & (df['cylinders'] == 6)]['name'].tolist()
print(f"Japanese v6 cars: {japanese_v6_cars}")

# Task 3:
cars_missing_horsepower = df[df['horsepower'].isnull()]['name'].tolist()
print(f"Cars with missing horsepower data: {cars_missing_horsepower}")

# Task 4: 
cars_with_mpg_20_or_more = df[df['mpg'] >= 20].shape[0]
print(f"Number of cars having mpg >= 20: {cars_with_mpg_20_or_more}")

# Task 5:
car_with_highest_mpg = df.loc[df['mpg'].idxmax()]['name']
print(f"Car with the highest mpg: {car_with_highest_mpg}")

# Task 6: 
max_weight = df['weight'].max()
min_weight = df['weight'].min()
avg_weight = df['weight'].mean()
print(f"Maximum weight: {max_weight}, Minimum weight: {min_weight}, Average weight: {avg_weight:.2f}")

# Task 7: 
df_cleaned = df.dropna()
print(f"Shape after removing the missing values: {df_cleaned.shape}")

# Task 8: 
country_counts = df['origin'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Proportion of Cars Manufactured in Different Countries')
plt.show()

# Task 9: 
fig, axes = plt.subplots(2, 1, figsize=(8, 12))

# Subplot i: Scatter plot showing mpg vs. weight
axes[0].scatter(df['mpg'], df['weight'], color='b', label='MPG vs Weight')
axes[0].set_xlabel('MPG')
axes[0].set_ylabel('Weight')
axes[0].legend()
axes[0].set_title('MPG vs Weight')

# Subplot ii: Line plot showing mpg vs displacement
axes[1].plot(df['displacement'], df['mpg'], color='g', label='MPG vs Displacement')
axes[1].set_xlabel('Displacement')
axes[1].set_ylabel('MPG')
axes[1].legend()
axes[1].set_title('MPG vs Displacement')

plt.tight_layout()
plt.show()
