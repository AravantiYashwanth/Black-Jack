import random
import art

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(cards):
     return random.sample(cards,2)


user_cards = deal_card(cards)
computer_cards = deal_card(cards)

print(f"your cards are: {user_cards}")


def calculate_score(cards):

    # Check for blackjack (ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    score = sum(cards)
    # Calculate score with possible ace adjustment
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
       
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your score is: {user_score}")
end = True

if user_score == 0 or user_score >21 or computer_score == 0 :
    print("Game has ended.")
    end = False

while end :
    ans = input("Do you want to draw another card? Type 'yes' or 'no': ")
    if ans == "yes":
        user_cards.append(random.choice(cards))
        user_score = calculate_score(user_cards)
        print(f"Your cards are now: {user_cards}")
        print(f"Your score is now: {user_score}")
        if user_score >= 21:
            print("You have reached 21 or more.")
            end = False
        
    else:
        print("You chose to stop drawing cards.")
        break

# Computer's turn
while computer_score < 17:
    computer_cards.append(random.choice(cards))
    computer_score = calculate_score(computer_cards)

print(f"Computer's final cards: {computer_cards}")
print(f"Computer's final score: {computer_score}")

def compare(u_s, c_s):
    if u_s == c_s:
        print("It's a draw.")
    elif c_s == 0 or (u_s > 21 ):
        print("You lose.")
    elif u_s == 0 or (c_s > 21 ):
        print("You win.")
    elif u_s > c_s:
        print("You win.")
    else:
        print("You lose.")

compare(user_score, computer_score)