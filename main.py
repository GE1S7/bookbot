text_file = open('books/frankenstein.txt', 'r')
prepared_file = text_file.read()

def count_words(text):
    wordlist = text.split()
    return len(wordlist)

def count_characters(text):
    letter_appeared = {}
    for i in text:
        if i.lower() not in letter_appeared.keys():
            letter_appeared[i.lower()] = 1
        else:
            letter_appeared[i.lower()] += 1
    return letter_appeared

def show_report(character_count, word_count):
    sorted_keys = sorted(character_count.keys())

    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{word_count} words found in the document")

    for i in sorted_keys:
        if i.isalpha():
            print(f"The '{i}' character was found {character_count[i]} times")
            
    
    print('--- End report ---')

show_report(count_characters(prepared_file), count_words(prepared_file))

