import random
import os

# Variables- Deck, player, computer
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
p_cards = [0, 0]
p_score = 0
c_cards = [0, 0]
c_score = 0
hit = True


# If hand has an ace and the total goes above 21 will change the ace from 11 to 1
def change_ace():
    ace = False
    if 11 in p_cards or 11 in c_cards:
        ace = True
    if ace and score(p_cards) > 21:
        p_cards.remove(11)
        p_cards.append(1)
    if ace and score(c_cards) > 21:
        c_cards.remove(11)
        c_cards.append(1)

# Prints out the final results of the round
def result():
    if score(c_cards) == score(p_cards):
        print("It's a draw")
    elif score(p_cards) > score(c_cards) and score(p_cards) < 22 or score(c_cards) > 21:
        print("You win")
    else:
        print("You lose")

# deals two random cards to the player and computer, from the list above L5
def deal_cards():
    p_cards[0] = cards[random.randrange(9)]
    p_cards[1] = cards[random.randrange(9)]
    c_cards[0] = cards[random.randrange(9)]
    c_cards[1] = cards[random.randrange(9)]

# calculates the score of the player or computer based on input
def score(a):
    score = sum(a)
    return score


# gives the player an extra card at random and adds it to the score
def extra_card():
    p_cards.append(cards[random.randrange(9)])
    score(p_cards)
    change_ace()

# checks if player or computer gets a blackjack
def blackjack():
    if 11 in c_cards and 10 in c_cards and score(c_cards) == 21:
        print(f"Computer\'s final hand {c_cards}, final score: {score(c_cards)}\nComputer Gets Blackjack, You Lose")
        return True
    elif 11 in p_cards and 10 in p_cards and score(p_cards) == 21:
        print(f"BlackJack You Win \nComputer\'s final hand {c_cards}, final score: {score(c_cards)}")
        return True

# prints out players hand and current score, as well as the first card of the dealer
def prints():
    print(f'Your cards:{p_cards}, current score: {score(p_cards)} \nComputer\'s first card: {c_cards[0]}')

# computer will pick up cards if it's score is less than 17
def comp_play():
    while score(c_cards) < 17:
        c_cards.append(cards[random.randrange(9)])
        score(c_cards)
        change_ace()

# full game
def game():
    in_play = True
    while in_play:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play == 'y':
            os.system("clear")
            from Art import logo
            print(logo)
            again = True
            deal_cards()
            change_ace()
            prints()
            bl = blackjack()
            if bl:
                return
            else:
                while again:
                    another = input("Press y for another card or n to pass")
                    if another == 'y':
                        extra_card()
                        prints()
                        if score(p_cards) > 21:
                            again = False
                            print("Bust")
                    elif another == 'n':
                        again = False
                        comp_play()
                    else:
                        print("Invalid input, try again")
                print(
                    f"Your final hand:{p_cards}, final score: {score(p_cards)} \nComputer\'s final hand {c_cards}, "
                    f"final score: {score(c_cards)}")
                result()
        elif play == 'n':
            in_play = False
        else:
            print("invalid input, try again")


game()
