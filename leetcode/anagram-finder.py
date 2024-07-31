

def find_anagram(src_str: str, target_str: str) -> bool:
    if len(src_str) != len(target_str):
        return False

    src_dict = {}
    target_dict = {}

    for char in src_str:
        if char in src_dict:
            src_dict[char] += 1
        else:
            src_dict[char] = 1

    for char in target_str:
        if char in target_dict:
            target_dict[char] += 1
        else:
            target_dict[char] = 1

    return src_dict == target_dict

def are_anagrams(frist_string, second_string) ->bool:
    return sorted(frist_string.lower()) == sorted(second_string.lower())

if __name__ == "__main__":
    print(find_anagram("listen", "silent")) #  Result: True
    print(find_anagram("Hello", "World")) # Result: False
    print(are_anagrams("listen", "silent")) #  Result: True
    print(are_anagrams("Hello", "World")) #  Result: False
