"""
Given a matrix
[[1,4,7,11,15],
 [2,5,8,12,19],
 [3,6,9,16,22],
 [10,13,14,17,24],
 [18,21,23,26,30]]
     
     Write a function to search for a target value in the matrix. 
     The function should return True if the target value is 
     found in the matrix, and False otherwise.
    target = 16 output = True
    target = 29 output = False
"""

from typing import List

def matrix_search(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False


if __name__ == "__main__":
    matrix = [[1,4,7,11,15],
              [2,5,8,12,19],
              [3,6,9,16,22],
              [10,13,14,17,24],
              [18,21,23,26,30]]
    
    target = 16
    print(matrix_search(matrix, target)) # True

    target = 29
    print(matrix_search(matrix, target)) # False


