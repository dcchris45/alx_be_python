pattern = int(input("Enter the size of the pattern: "))
length = 0
while length < pattern:
    for _ in range(pattern):
        print("*", end="")
    print()
    length += 1
