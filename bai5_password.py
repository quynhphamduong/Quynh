def password_check():
    correct_password = "securepassword"  # Set your correct password here
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        user_input = input("Enter the password: ")
        if user_input == correct_password:
            print("You are logged in to the system.")
            return
        else:
            print("Wrong password.")
            if attempt < max_attempts:
                print(f"Try again. You have {max_attempts - attempt} attempts left.")
            else:
                print("You are kicked off the system.")

password_check()
