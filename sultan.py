import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv('C:\\Users\\MAZ YAFAI\\OneDrive\\Desktop\\10-1310-data-interim-equality-impact-he-funding-figure-4.csv', skiprows=2)

# Extract the data for plotting
deciles = data['Decile']
men_income = data['Men']
women_income = data['Women']

# Create a figure and plot a line chart for income by decile
plt.figure(figsize=(10, 6))

# Plot lines for men and women
plt.plot(deciles, men_income, label='Men', marker='o', color='blue')
plt.plot(deciles, women_income, label='Women', marker='x', color='red')

# Set plot labels and title for the line chart
plt.xlabel('Decile')
plt.ylabel('Income')
plt.title('Income by Decile for Men and Women (Line Plot)')

# Add a legend
plt.legend()

# Show the line chart
plt.tight_layout()
plt.show()



# Extract the data for plotting
men_income = data['Men']

# Create a figure and plot a bar chart of men's income
plt.figure(figsize=(10, 6))

# Create blue bars for men's income
plt.bar(range(len(men_income)), men_income, color='blue', alpha=0.7)

# Set labels and title for the bar chart
plt.xlabel('Data Point')
plt.ylabel('Income')
plt.title('Bar Chart of Men\'s Income')

# Show the bar chart
plt.tight_layout()
plt.show()



df = pd.read_csv('C:\\Users\\MAZ YAFAI\\OneDrive\\Desktop\\10-1309-data-interim-impact-assessment-he-funding-table-10.csv', skiprows=1, encoding='ISO-8859-1', dtype=str)

# Convert the 'Estimated cost to business (£)' column to numeric
df['Estimated cost to business (£)'] = pd.to_numeric(df['Estimated cost to business (£)'], errors='coerce')

# Convert 'Size of firm (number of employees)' to strings
df['Size of firm (number of employees)'] = df['Size of firm (number of employees)'].astype(str)

# Create a scatter plot
plt.figure(figsize=(10, 6))

# Plot a scatter plot
plt.scatter(df['Size of firm (number of employees)'], df['Estimated cost to business (£)'], marker='o')

# Set plot labels and title
plt.xlabel('Size of Firm (Number of Employees)')
plt.ylabel('Estimated Cost to Business (£)')
plt.title('Scatter Plot of One-off Compliance Costs to Business')

# Customize the x-axis tick labels
plt.xticks(rotation=45)

# Show the scatter plot
plt.tight_layout()
plt.show()
