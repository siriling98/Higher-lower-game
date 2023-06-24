from art import logo, vs
from game_data import data
import random
from replit import clear


def get_data():
    return random.choice(data)


def generate_data(account, level):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    print(f"Compare {level} : {name}, a {description}, from {country}.")


def get_follower_count(account):
    return account["follower_count"]


def higher_account(account_1, account_2):
    if account_1 > account_2:
        return "a"
    else:
        return "b"


def start_game():
    game_on = True
    score = 0
    print(logo)

    account_1 = get_data()
    account_2 = get_data()

    while game_on:
        account_1 = account_2
        account_2 = get_data()

        if account_1 == account_2:
            account_2 = get_data()

        generate_data(account_1, 'A')
        print(vs)
        generate_data(account_2, 'B')

        count = get_follower_count(account_1)
        count2 = get_follower_count(account_2)

        higher = higher_account(count, count2)

        choice = input("Who has more followers? Type 'A' or 'B' : ").lower()

        if choice == higher:
            score += 1
            clear()
            print(logo)
            print(f"Your right! Current score : {score}")

        else:
            game_on = False
            print(f"Sorry that's wrong. Final score : {score}")


start_game()