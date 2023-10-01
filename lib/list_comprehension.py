#!/usr/bin/env python3

def return_evens(num_list):
    even_elements = [n for n in num_list if n % 2 == 0]
    return even_elements

#Example usage
num_list = [0, 1, 3, 5, 7, 8, 9]
result = return_evens(num_list)
print(result)

def make_exclamation(sentence_list):
    exclamation_sentence = [sentence + "!" for sentence in sentence_list]
    return exclamation_sentence

#Example

input_sentence = ["Hello", "I'm doing great", "Python is fun"]
result = make_exclamation(input_sentence)

print(result)