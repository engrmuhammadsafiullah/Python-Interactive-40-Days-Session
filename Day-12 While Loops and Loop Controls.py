# A simple guessing game loop
secret_number = 7
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret_number:
        print("Correct!")
        break # Ends the loop immediately
    else:
        print("Try again!")
        
