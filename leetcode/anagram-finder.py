

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

print(find_anagram("listen", "silent")) # True
