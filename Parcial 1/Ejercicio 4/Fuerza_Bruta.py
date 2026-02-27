n = int(input())
s = input()

best = n  # worst case: remove all stones

# iterate through all possible subsets of stones to remove
# mask represents which stones are removed (bit = 1 means removed)
for mask in range(1 << n):

    remaining = []

    # build the remaining string after removals
    for i in range(n):
        if not (mask & (1 << i)):  # if this stone is NOT removed
            remaining.append(s[i])

    # check if the remaining stones have no equal neighbors
    valid = True
    for i in range(1, len(remaining)):
        if remaining[i] == remaining[i - 1]:
            valid = False
            break

    # if configuration is valid, update minimum removals
    if valid:
        removed = n - len(remaining)
        best = min(best, removed)

print(best)

#note, for the last codeforce test this will evaluate O(2^n) = 2^50 ≈ 1,125,899,906,842,624 operations due to n=50, so the last test will not be passed
