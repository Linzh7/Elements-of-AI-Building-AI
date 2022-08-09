import random


def main():
    prob = random.random()
    if prob < 0.1:
        favourite = "bats"
    elif prob >= 0.1 and prob < 0.2:
        favourite = "cats"
    elif prob >= 0.2:
        favourite = "dogs"
    print("I love " + favourite)


main()