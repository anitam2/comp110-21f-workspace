counts: dict[str, int] = {}

example_string: str = "The quick brown fox jumped over the lazy dog. Then, Kyle petted the dog and called him Fluffernutter."

for letter in example_string.lower():
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

print(counts)