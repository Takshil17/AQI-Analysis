import pandas as pd
import matplotlib.pyplot as plt

# Load the AQI data
aqi_data = pd.read_csv("D:\\COLLEGE DESKTOP\\BDA\\aqi_pune_2024.csv")


# Convert 'Date' column to datetime type
aqi_data['Date'] = pd.to_datetime(aqi_data['Date'])

# Extract the month from the 'Date' column
aqi_data['Month'] = aqi_data['Date'].dt.month_name()

# Define AQI categories
categories = ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe']
bins = [0, 50, 100, 200, 300, 400, 500]

# Cut AQI data into the categories
aqi_data['Category'] = pd.cut(aqi_data['AQI Level'], bins=bins, labels=categories)

# Group by month and category with observed=True to silence the warning
monthly_aqi = aqi_data.groupby(['Month', 'Category'], observed=True).size().unstack(fill_value=0)


# Plot pie chart for each month
for month in monthly_aqi.index:
    category_counts = monthly_aqi.loc[month]
    
    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90, colors=['#009966', '#ffde33', '#ff9933', '#cc0033', '#660099', '#7e0023'])
    plt.title(f'AQI Levels Distribution in Pune ({month} 2024)')
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.show()