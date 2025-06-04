import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(df)

# Convert dataframe to a dictionary
nato_dict = {row["letter"]: row["code"] for (index, row) in df.iterrows()}
print(nato_dict)

word = input("Please enter a word: ").upper()

# Generate a phonetic code
nato_list = [nato_dict[letter] for letter in word]
print(nato_list)
