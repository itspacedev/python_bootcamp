import pandas

data = pandas.read_csv("squirrel_data.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(gray_squirrels)

red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(red_squirrels)

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels)

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
# print(new_data)
