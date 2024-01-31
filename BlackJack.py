import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


computer_initial_hand = random.choices(cards, k=2)
computer_score = sum(computer_initial_hand)
while computer_score < 17:
    computer_initial_hand.append(random.choice(cards))
    computer_score = sum(computer_initial_hand)
print(computer_initial_hand)
    

def my_cards():
    play_game = True
    option = input("Do you want to play a game of BlackJack? 'y' or 'n' ")
    clear()
    if option == 'n':
        play_game = False
    elif play_game:
        print(logo)
        my_initial_hand = random.choices(cards, k=2)
        current_score = sum(my_initial_hand)
        another_card = True
        while another_card and current_score <= 21:
            print(f"Your cards {my_initial_hand}, current score: {current_score}")
            print(f"Computer's first card: {computer_initial_hand[0]}")
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "n":
                another_card = False
            else:
                my_initial_hand.append(random.choice(cards))
                current_score = sum(my_initial_hand)
        print(f"Your final hand: {my_initial_hand}, final score: {current_score}")
        print(f"Computer's final hand: {computer_initial_hand}, final score: {computer_score}")
        if current_score > 21:
            print("You went over.You lose")
        elif computer_score > 21:
            print("Opponent went over. You win")
        elif current_score > computer_score:
            print("You win")
        elif current_score < computer_score:
            print("You lose")
        elif current_score == computer_score:
            print("Draw")
        my_cards()

my_cards()
                 
