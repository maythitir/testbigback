def generate_combinations(arrays):
    result = [[]]
    for array in arrays:
        result = [prev + [item] for prev in result for item in array]
    # return result
    for res in result:
        print(res)


# Example
source1 = [[1, 3, 4], [5, 6], [7, 8]]
source2 = [[1], [2, 3], [4, 5, 6], [7, 8, 9], [9, 10, 11]]
# Result
result1 = generate_combinations(source1)
result2 = generate_combinations(source2)
