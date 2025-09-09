# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up?

words = {
    "kella" : "Banana",
    "billi" : "Cat",
    "kitab" : "Book"
}

word = input("Enter one word of this three words (\" kella , billi , kitab\") return to this english meaning: ")
print(words[word])