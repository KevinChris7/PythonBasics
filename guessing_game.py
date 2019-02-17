

secret_word = "Rajini"
superstar = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while superstar != secret_word and not(out_of_guesses):
        if guess_count < guess_limit:
            superstar = input("Guess the Superstar: ")
            guess_count += 1
        else:
            out_of_guesses = True

if out_of_guesses:
    print("Guessed the Superstar Wrong,You Lose")

else:
    print("You Win")



