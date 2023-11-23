#!/usr/bin/env python3
def return_evens(num_list):
    numbers = list(num_list)
    evens = list()
    for num in (numbers):
        if num % 2 == 0:
            evens.append(num)
    return(evens)
         
        
        
    

def make_exclamation(sentence_list):
    exclamation_sentences = []
    for sentence in sentence_list:
        if sentence != '':
            exclamation_sentence = sentence + '!'
            exclamation_sentences.append(exclamation_sentence)
    return exclamation_sentences


make_exclamation("")