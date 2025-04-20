import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Statistical info
df=pd.read_csv("C:/Users/Dell/OneDrive/Documents/Public_Libraries (1).csv")
print(df.info())


#Cleaning the dataset
missing = df.isnull().sum()
print("Missing values:\n", missing[missing > 0])


#dropping column with 100% missing values
df.drop(columns=['Registrations Per Capita Served', 'Use of Public Internet Computers'], inplace=True, errors='ignore')

# Filling missing values with median
columns_to_fill = [
    'Population of Service Area',
    'Reference Questions',
    'Library Visits Per Capita Served',
    'Total Library Visits',
    'Total Program Attendance & Views Per Capita Served',
    'Total Program Attendance & Views',
    'Total Programs (Synchronous + Prerecorded)',
    'Wages & Salaries Expenditures',
    'Collection Per Capita Served',
    'Percent of Residents with Library Cards',
    'Tax Appropriation Per Capita Served',
    'AENGLC Rank',
    'Operating Income Per Capita',
    'Total Registered Borrowers',
    'Operating Expenditures Per Capita',
    'Library Materials Expenditures',
    'Total Collection',
    'Town Tax Appropriation for Library',
    'Circulation Per Capita Served',
    'Operating Expenditures',
    'Total Operating Income',
    'Total Circulation'
]

for col in columns_to_fill:
    df[col] = df[col].fillna(df[col].median())

print("Remaining missing values:\n", df.isnull().sum()[df.isnull().sum() > 0])

# Save cleaned data to a new CSV file
df.to_csv("C:/Users/Dell/OneDrive/Documents/Public_Libraries (1)_Cleaned.csv", index=False)


df['Reference Questions Per Capita Served'] = df['Reference Questions Per Capita Served'].fillna(df['Reference Questions Per Capita Served'].median())


#Loading the cleaned dataset
df = pd.read_csv("C:/Users/Dell/OneDrive/Documents/Public_Libraries (1)_Cleaned.csv")

# OBJECTIVE1: Scatter plot to visualize the relationship between Population and Total Library Visits.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Population of Service Area', y='Total Library Visits', data=df, color='blue')
plt.title('Population vs Total Library Visits')
plt.xlabel('Population of Service Area')
plt.ylabel('Total Library Visits')
plt.grid(True)
plt.show()

correlation = df['Population of Service Area'].corr(df['Total Library Visits'])
print(f"Correlation between Population and Total Library Visits: {correlation:.2f}")
#Interpretation of Scatter Plot:There seems to be a positive trend, especially for smaller populations (under 60,000), where an increase in population generally increases visits.





#OBJECTIVE-2: Relationship between Population and Total Registered Borrowers

plt.figure(figsize=(10, 6))
sns.regplot(x='Population of Service Area', y='Total Registered Borrowers', data=df, scatter_kws={"color": "green"}, line_kws={"color": "black"})
plt.title('Regression Plot: Population vs Total Registered Borrowers')
plt.xlabel('Population of Service Area')
plt.ylabel('Total Registered Borrowers')
plt.grid(True)
plt.tight_layout()
plt.show()

correlation2 = df['Population of Service Area'].corr(df['Total Registered Borrowers'])
print(f"Correlation between Population and Total Registered Borrowers: {correlation2:.2f}")






#Objective 3: Average Operating Expenditure by County
# Step 1: Group and calculate mean
avg_expenditure = df.groupby('County')['Operating Expenditures'].mean().reset_index()

# Step 2: Sort values for clearer visualization
avg_expenditure_sorted = avg_expenditure.sort_values(by='Operating Expenditures', ascending=False)

# Step 3: Bar chart
plt.figure(figsize=(14, 6))
sns.barplot(x='Operating Expenditures', y='County', data=avg_expenditure_sorted, palette='viridis')

# Step 4: Labels and titles
plt.title('Average Operating Expenditure by County', fontsize=16)
plt.xlabel('Average Operating Expenditure')
plt.ylabel('County')
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()





#OBjective-4: Top Counties by Library Visits

# Grouping and aggregating
county_visits = df.groupby('County')['Total Library Visits'].sum()

# Selecting top 5 counties
top_counties = county_visits.nlargest(5)

# Plotting pie chart
plt.figure(figsize=(8, 8))
top_counties.plot.pie(autopct='%1.1f%%', startangle=140, cmap='Set3', ylabel="")
plt.title('Top 5 Counties by Total Library Visits')
plt.tight_layout()
plt.show()

colors = sns.color_palette("husl", len(top_counties))  # 'husl' is a vibrant color set
top_counties.plot.pie(
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    ylabel=""
)


#Objective-5 Distribution of Collection Per Capita by County

plt.figure(figsize=(12, 6))
sns.boxplot(x='County', y='Collection Per Capita Served', data=df, palette='Set2')
plt.title('Distribution of Collection Per Capita by County', fontsize=16)
plt.xlabel('County')
plt.ylabel('Collection Per Capita Served')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

