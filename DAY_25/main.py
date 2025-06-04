# Read file contents
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# Use csv library to read data from the file
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Use pandas to access the data
import pandas

data = pandas.read_csv("weather_data.csv")
# Check the type of data
print(type(data))

# Check the type of a column
print(type(data["temp"]))

# Print one series
print(data["temp"])

# Convert data to a dictionary
data_dict = data.to_dict()
print(data_dict)

# Convert series to a python list
temp_list = data["temp"].to_list()
print(temp_list)

# Calculate average temperature
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

# Get average temperature using Pandas
avg_temp_p = data["temp"].mean()
print(avg_temp_p)

# Get maximum temperature using Pandas
max_temp_p = data["temp"].max()
print(max_temp_p)

# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in a row
print(data[data["day"] == "Monday"])

# Get a row with the maximum temperature
print(data[data["temp"] == data["temp"].max()])

monday = data[data["day"] == "Monday"]
print(monday)
print(monday["condition"])

monday_temp = monday["temp"][0]
print(monday_temp)
monday_temp_f = monday_temp * (9/5) + 32
print(monday_temp_f)

# Create a dataframe from scratch
example_data = {
    "students": ["Alice", "Bobb", "TommyX"],
    "scores": [76, 56, 49],
}
e_df = pandas.DataFrame(example_data)
print(e_df)

# Convert(Save) a dataframe to a csv file
e_df.to_csv("example_dataframe_to_csv.csv")
