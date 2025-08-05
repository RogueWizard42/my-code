# main_copy

from stats import word_count # Importing the function from the stats.py file
from stats import character_count # Importing the function from the stats.py file
from stats import sorting_hat # Importing the function from the stats.py file
import sys


def get_text_book(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as f:
        return f.read()
    
def main():
    
    if len(sys.argv) != 2:
        print("Enter the path to the book that you want to analyze. Use the format: python3 main.py <file_path>")
        #print("Usage: python3 main.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    
    text = get_text_book(file_path)
    letters = character_count(text) # Calling the function from the stats.py file
    print("============ BOOKBOT ============")
    print("Analyzing book found at book/frankenstein.txt")
    print("------------ Word Count ------------")
    number_of_words = word_count(text)
    print(f"Found {number_of_words} total words")
    print("------------ Character Count ------------")
    sorted_letters = sorting_hat(letters)
    for entry in sorted_letters:
        print(f"{entry['character']}: {entry['count']}")
    print("============ END ============")

main()
