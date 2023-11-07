def count_word_in_sentence(sentence, word):
    words = sentence.split()
    count = 0

    for w in words:
        if w == word:
            count += 1

    return count

sentence = input("Enter a sentence: ")
word_to_find = input("Enter the word to search for: ")

word_count = count_word_in_sentence(sentence, word_to_find)

if word_count > 0:
    print(f"The word '{word_to_find}' is included in the sentence.")
    print(f"It appears {word_count} time(s) in the sentence.")
else:
    print(f"The word '{word_to_find}' is not found in the sentence.")
