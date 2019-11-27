n = int(input())
unsorted = []

for _ in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)

print(sorted(unsorted, key=lambda x: int(x)))