import random
def multiplication_game():
    for i in range(1, 11):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2

        print(f"Question {i}: {num1} x {num2} = ", end="")
        user_answer = int(input())

        if user_answer == correct_answer:
            print("Right!")
        else:
            print(f"Wrong. The answer is {correct_answer}.")
    print("Game Over. Well done!")
def main():
multiplication_game()
if __name__ == "__main__":
    main()