import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the CSV file
file_path = '/Users/manishmaharjan/Downloads/dataanalytics/Data_Analytics_Work/week_10/Sample_Data_for_Activity.csv'
data = pd.read_csv(file_path, header=None)

# Extract columns
x = data[0]
y = data[1]
z = data[2]

# Ensure 'categories' is numerical
categories = pd.to_numeric(data[3], errors='coerce')

# Create a scatter plot
plt.scatter(x, y, c=categories, cmap='viridis', label='Data Points')
plt.colorbar(label='Categories')
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.title('Scatter Plot of Sample Data')
plt.legend()
plt.show()