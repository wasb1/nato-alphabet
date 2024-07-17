import pandas

nato_d = pandas.read_csv("./nato_phonetic_alphabet.csv")
print(nato_d)

new_dict = {row.letter: row.code for (index, row) in nato_d.iterrows()}
print(new_dict)


word_input = input("Enter a word: ").upper()

repeat = True
while repeat:

    try:
        list_word = [code for (letter, code) in new_dict.items() if letter in word_input]
        if len(list_word) != len(word_input):
            raise TypeError("Enter only letters!")
        else:
            repeat = False
    except TypeError:
        word_input = input("Enter a word: ").upper()
    else:
        print(list_word)

