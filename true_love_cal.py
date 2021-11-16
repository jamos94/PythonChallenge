# this program uses user input, lower(), and count()
# with the input and functions working, it moves to the conditional statments
# these statements print out whether your love is true or not.
# are you brave enough to find out?

print("Welcome to the Love Calculator!")
play = input("Are you ready to fin out if you\'re made for each other? Y/N: ").lower()


def lovescore():
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")

    # combine lowercase names
    combine_names = name1 + name2
    #convert combined names to lowercase
    lover_names = combine_names.lower()

    # count TRUE
    t = lover_names.count("t")
    r = lover_names.count("r")
    u = lover_names.count("u")
    e = lover_names.count("e")

    count_true = t + r + u + e

    # count LOVE
    l = lover_names.count("l")
    o = lover_names.count("o")
    v = lover_names.count("v")
    e = lover_names.count("e")

    count_love = l + o + v + e

    #an error was occuring here because I did not convert the score back into an integer to perform the condition checks
    love_score = int(str(count_true) + str(count_love))

    #if love score < 10 and > 90
    if (love_score < 10) or (love_score > 90):
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    #if love score is between 40 and 50
    elif (love_score >= 40) and (love_score <= 50):
        print(f"Your score is {love_score}, you are alright together.")

    else:
        print(f"Your score is {love_score}.")

if play == "y":
    lovescore()
# else: return to menu