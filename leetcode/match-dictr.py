from typing import Dict,Tuple

"""
Provided two dictionaries where the values are long string/sentence 
find mathing values in both dictionary. Solve with traditional way,
the result should be key and value from both dictionary.
Constaints the key can be different but the values could be same. 
Also solve with alternative approach such as using bag of words
"""


def find_matching_values(dict1 : Dict[str,str], dict2 :Dict[str,str]) -> Dict[Tuple[str,str],str]:
    result = {}
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if value1 == value2:
                result[(key1, key2)] = value1
    return result

# Example dictionaries
dict1 = {
    'a': 'The quick brown fox jumps over the lazy dog',
    'b': 'Hello world',
    'c': 'Python is great'
}

dict2 = {
    'x': 'Python is great',
    'y': 'The quick brown fox jumps over the lazy dog',
    'z': 'The book is great'
}

matching_values = find_matching_values(dict1, dict2)
print(matching_values)


def bag_of_words(sentence):
    return set(sentence.lower().split())

def find_matching_values_bow(dict1, dict2):
    result = {}
    for key1, value1 in dict1.items():
        bow1 = bag_of_words(value1)
        for key2, value2 in dict2.items():
            bow2 = bag_of_words(value2)
            if bow1 == bow2:
                result[(key1, key2)] = value1
    return result


matching_values_bow = find_matching_values_bow(dict1, dict2)
print(matching_values_bow)