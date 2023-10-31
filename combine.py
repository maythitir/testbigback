def generate_combinations(arrays):
    result = [[]]
    for array in arrays:
        result = [prev + [item] for prev in result for item in array]
    # return result
    for res in result:
        print(res)

# function for test in 3_test_combime.py


def generate_combinations_fortest(arrays):
    result = [[]]
    for array in arrays:
        result = [prev + [item] for prev in result for item in array]
    return result


# Example
source1 = [[1, 3, 4], [5, 6], [7, 8]]
source2 = [[1], [2, 3], [4, 5, 6], [7, 8, 9], [9, 10, 11]]
# Result
result1 = generate_combinations(source1)
result2 = generate_combinations(source2)
