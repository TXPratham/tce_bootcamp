import random

card_ranks=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
card_suits=["Hearts","Diamonds","Clubs","Spades"]
deck=[rank+" "+suit for rank in card_ranks for suit in card_suits]
random.shuffle(deck)

while True:
    try:
        players=int(input("Enter number of players= "))

        if players>0 and 52%players==0:
            break
        else:
            print("Invalid number of players.")
    except ValueError:
        print("Please enter a number.")

cards_per_player=52//players
hands=[]

for i in range(players):
    player_cards=[]
    for j in range(cards_per_player):
        card=deck.pop()
        player_cards.append(card)
    hands.append(player_cards)

scores=[]
for i in range(players):
    scores.append(0)

print("Game Started")
print(f"Each player gets {cards_per_player} cards.")
for round_number in range(cards_per_player):
    print("\nRound",round_number+1)
    for i in range(players):
        card=random.choice(hands[i])
        hands[i].remove(card)
        print(f"Player {i+1} : {card}")
    while True:
        try:
            winner=int(input("Enter the winning player number: "))
            if winner>=1 and winner<=players:
                scores[winner-1]=scores[winner-1]+1
                break
            else:
                print("Invalid player number.")
        except ValueError:
            print("Please enter a number.")
print("\nFinal Scores")
for i in range(players):
    print(f"Player {i+1}:{scores[i]} rounds won")
highest_score=max(scores)
winner=scores.index(highest_score)
print(f"\nOverall Winner: Player {winner+1}")
print(f"Rounds won:{highest_score}")