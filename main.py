import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def choose_card(card_list):
    card_list.append(random.choice(cards))
    return card_list


def calculate_score(card_score_list):
    if len(card_score_list) == 2 and sum(card_score_list) == 21:
        return 0
    if 11 in card_score_list and card_score_list > 21:
        card_score_list.remove(11)
        card_score_list.append(1)
    return sum(card_score_list)


def compare_card(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_card = []
    computer_card = []
    is_game_over = False

    for i in range(0, 2):
        choose_card(user_card)
        choose_card(computer_card)

    while not is_game_over:
        computer_score = calculate_score(computer_card)
        user_score = calculate_score(user_card)
        print(f"   Your cards: {user_card}, current score: {user_score}")
        print(f"   Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                choose_card(user_card)
            else:
                is_game_over = True

        # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        choose_card(computer_card)
        computer_score = calculate_score(computer_card)

    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare_card(user_score, computer_score))

    # Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # clear()
    play_game()
