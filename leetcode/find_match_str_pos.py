"""
Given a string s and a non-empty string p, 
find the position where p occurs in s with start
and end index.

"""

def find_match_str_pos(s: str, p: str) -> tuple:
    start_index = s.find(p)
    
    if start_index != -1:
        end_index = start_index + len(p)
        return (start_index, end_index)
    else:
        return (-1, -1)


s = "hello world, this is a test string"
p = "test"
result = find_match_str_pos(s, p)
print(result)