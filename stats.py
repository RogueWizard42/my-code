# a file to read and analyze the text from a file

def word_count(book_text): 
    words = book_text.split()
    num_words = len(words)
    #print(f"{num_words} words found in the document")
    return num_words
    
def character_count(book_text):
    characters = book_text.lower()
    counting = {}
    for char in characters:
        if char in counting:
            counting[char] +=1 
        else:
            counting[char] = 1
    return counting

def sorting_hat(letters):
    alphabet = []
    for letter, count in letters.items():
        if letter.isalpha():
            alphabet.append({"character" : letter, "count" : count})
    alphabet.sort(reverse = True, key = lambda x: x["count"])
    return alphabet
