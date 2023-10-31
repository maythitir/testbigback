def compress(data):
    compressed = ""
    count = 1

    # Iterate through the input string
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed += str(count) + data[i - 1]
            count = 1

    # Handle the last character
    compressed += str(count) + data[-1]

    return compressed


def decompress(data):
    decompressed = ""
    i = 0

    # Iterate through the compressed string
    while i < len(data):
        count = int(data[i])
        char = data[i + 1]
        decompressed += count * char
        i += 2

    return decompressed


# Example
input_data1 = "HELLOOO"
input_data2 = "BWAAALAAA"

compressed_data1 = compress(input_data1)
decompressed_data1 = decompress(compressed_data1)

compressed_data2 = compress(input_data2)
decompressed_data2 = decompress(compressed_data2)

print(f"Original 1: {input_data1}")
print(f"Compressed 1: {compressed_data1}")
print(f"Decompressed 1: {decompressed_data1}")

print(f"\nOriginal 2: {input_data2}")
print(f"Compressed 2: {compressed_data2}")
print(f"Decompressed 2: {decompressed_data2}")
