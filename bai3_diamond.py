def print_diamond(n):
    # Top half of the diamond
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    # Bottom half of the diamond
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
def main():
    height = int(input("Enter the height of the diamond: "))
    print_diamond(height)

if __name__ == "__main__":
    main()