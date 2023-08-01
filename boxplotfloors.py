import matplotlib.pyplot as plt
import pandas as pd

# Define the filename and sheet name of your Excel data
filename = 'datax.xlsx'
sheetname = 'boxplot'

# Define the columns to be compared
a_col = 'f0'  # Column A contains the x-axis data
b_col = 'f1'  # Column B contains the y-axis data
c_col = 'f2'
d_col = 'f3'
e_col = 'f4'

# Read data from Excel
df = pd.read_excel(filename, sheet_name=sheetname)
data0 = df[a_col]
data1 = df[b_col]
data2 = df[c_col]
data3 = df[d_col]
data4 = df[e_col]

# Combine the data into a list for the box plot
data = [data0, data1, data2, data3, data4]

# Labels for each data set
labels = ['0','1','2','3','4']

# Create the box plot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('Average RSSI Floorwise', fontweight="bold")
plt.xlabel('Floors',fontweight="bold")    
plt.ylabel('RSSI (dBm)', fontweight="bold")
#plt.ylim(-120, -40)  # Set the y-axis limits from 0 to 100

# Show the plot
plt.grid(True)
plt.savefig("plot.png", dpi=300)
plt.show()
#plt.xlim(0, 10)  # Set the x-axis limits from 0 to 10
