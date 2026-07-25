# use the world list(file name=word.py) for world generation
from word import word

length_of_word = len(word)
print(f"Length Of Word = {length_of_word}")

letters = list(word)
copy_letters = ["0"] * length_of_word

for _ in range(length_of_word):
    input_str = input()
    input_list = list(input_str)
    
    if len(input_str)>length_of_word:
        print("the length of word is to long")
        
    for i in range(length_of_word):
        if letters[i] == input_list[i]:
            copy_letters[i] = "1"

    print(letters)
    print(copy_letters)