def main():
    print("Enter a college class: ", end="")
    name = input()
    print("Enter an adjective: ", end="")
    adjective = input()
    print("Enter an activity", end="")
    activity = input()
    print(
        f"{name} class was really {adjective} today. We learn how to {activity} today in class. I can't wait for tomorrow's class")


if __name__ == "__main__":
    main()