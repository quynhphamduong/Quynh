def main():
    scores = []

    # Collect 10 test scores
    for i in range(1, 11):
        score = float(input(f"Enter score {i}: "))
        scores.append(score)

    # (a) Print out the highest and lowest scores
    highest_score = max(scores)
    lowest_score = min(scores)
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")

    # (b) Print out the average of the scores
    average_score = sum(scores) / len(scores)
    print(f"Average score: {average_score:.2f}")

    # (c) Print out the second largest score
    sorted_scores = sorted(scores, reverse=True) # Sap xep so tu lon den be
    second_largest_score = sorted_scores[1]
    print(f"Second largest score: {second_largest_score}")

    # (d) Check if any score is greater than 100 and print a warning
    if any(score > 100 for score in scores):
        print("Warning: A value over 100 has been entered.")

    # (e) Drop the two lowest scores and print the average of the rest
    sorted_scores = sorted(scores)
    remaining_scores = sorted_scores[2:]
    average_remaining_scores = sum(remaining_scores) / len(remaining_scores)
    print(f"Average after dropping the two lowest scores: {average_remaining_scores:.2f}")


if __name__ == "__main__":
    main()