# Use the word list (file name=word.py) for word generation
from word import word

length_of_word = len(word)
print(f"Length Of Word = {length_of_word}")

letters = list(word)
count = 0

for _ in range(length_of_word):
    input_str = input(f"Enter a {length_of_word}-letter word: ")
    
    # Check if the length matches before processing
    if len(input_str) != length_of_word:
        print(f"Invalid input! Word must be exactly {length_of_word} characters long.")
        continue  # Skip to the next trial without crashing
    
    count += 1
    print(f"Trial NO. {count}")
    
    input_list = list(input_str)
    copy_letters = ["0"] * length_of_word
            
    for i in range(length_of_word):
        if letters[i] == input_list[i]:
            copy_letters[i] = "1"
        else:
            copy_letters[i] = "0"

    print("Input: ", input_list)
    print("Match: ", copy_letters)
    
    # Optional: Stop early if they guess correctly
    if copy_letters == ["1"] * length_of_word:
        print("Congratulations! You guessed the word!")
        break