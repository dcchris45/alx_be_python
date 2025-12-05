pattern = int(input("Enter the size of pattern: "))
length = 0
while length < pattern:
    for _ in range(pattern):
        print("*", end="")
    print()
    length += 1
    