import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


new_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter your name: ").upper()
output = [new_dictionary[letter] for letter in word]
print(output)