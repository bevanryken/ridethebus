# RIDE THE BUS card game by Bevan Ryken
# Friday, 14 October 2022
# My fist proper python program. 
# If you wish, please inform me any pointers to optimize the coding.
# This will be udpated in due course.

import time, random, os

inv = "   Have a drink for an invalid entry and try again!\n"
exit = stop1 = stop2 = stop3 = stop4 = False
colours = ["red", "black"]
os.system('clear')
# Deck of ranked cards set up below...
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["diamonds", "hearts", "clubs", "spades"]
deck = []
value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " + suit, value])
    value = value + 1
random.shuffle(deck)
card1 = card2 = card3 = deck.pop(0)
# Start of the game
name = input("\nHey there, what's your name? ").title()
print(f"\nHi there {name}, let's play RIDE THE BUS!\n")
time.sleep(1.5)

while exit == False:
    user_play = input("Do you still wish to play? (yes or no): ")
        
    if any(user_play.lower() == e for e in ["yes", 'y', '1', 'ye']):
        time.sleep(1)
        print("   Let's keep the bus rolling! \n")
        # To reset the stops to False, if you have already played 1+ rounds
        stop1 = stop2 = stop3 = stop4 = False
    elif any(user_play.lower() == e for e in ['no', 'n', '0']):
        break
    else:
        print(inv)
        time.sleep(2)
        continue

    #Stop1: Red or black
    while stop1 == False: 
        print("Bus stop 1...")
        time.sleep(2)
        user_choice1 = str(input(f"   What will it be {name}? Red card or Black card: ")).lower()

        if any(user_choice1.lower() == a for a in ["red", "r", "re"]):
            user_choice1 = "red"
        elif any(user_choice1.lower() == a for a in ['black', 'b', 'bla']):
            user_choice1 = "black"
        else:
            print(inv)
            time.sleep(2)
            continue

        computer_input = random.choice(colours)

        if user_choice1 == computer_input:
            print(f"\n   {name} has chosen: {user_choice1}... ")
            time.sleep(1.5)
            print(f"   The computer has chosen: {computer_input}... \n")
            time.sleep(1.5)
            print("   CORRECT! Go to Bus Stop 2!\n")
            stop1 = True   
        if user_choice1 not in computer_input:   
            print(f"\n   {name} has chosen {user_choice1}... ")
            time.sleep(1.5)
            print(f"   The computer has chosen {computer_input}...\n")
            time.sleep(1.5)
            print(f"   WRONG! No match {name} - Have 1 drink, and try again!\n")
            time.sleep(1.5)

    # Stop2: Higher or lower
    while stop2 == False:
        print("Bus stop 2...")
        time.sleep(2)
        print(f"   The card drawn is:", card1[0])
        user_choice2 = input(f"\n   {name}, will you choose Higher card or Lower card? ")
        card2 = deck.pop(0)
        time.sleep(2)
        if any(user_choice2.lower() == b for b in ["h", "hi", "high", "higher"]):
            user_choice2 = "higher"
        elif any(user_choice2.lower() == b for b in ["l", "lo" "low", "lower"]):
            user_choice2 = "lower"
        else:
            print(inv)
            time.sleep(2)
            continue

        correct_guess = 'h' if card2[1] > card1[1] else 'l'

        if user_choice2[0].lower() != correct_guess:
            print(f"   You drew the {card2[0]}... ")
            print(f"   Wrong! Have 2 drinks {name}, and try again!\n")
            time.sleep(2)
        elif user_choice2[0].lower() == card2[1] == card1[1]:
            print(f"   The numbers are EQUAL!")
            time.sleep(2)
            print(f"   {card2[0]} is the same as {card1[0]} - Try again {name}!")
            time.sleep(2)
        else:
            print(f"   You drew the {card2[0]}... ")
            time.sleep(2)
            print("   CORRECT! Goto Bus Stop 3")
            time.sleep(2)
            stop2 = True


    # Stop3: Inside or outside (Possible math error)
    while stop3 == False:
        print("\nBus stop 3...")
        time.sleep(2)
        print(f"   The cards drawn previously were: ")
        time.sleep(2)
        print(f"\n   Card 1: {card1[0]}")
        print(f"   Card 2: {card2[0]}")
        time.sleep(2)
        user_choice3 = input(f"\n   {name}, will you pick an Inside card or Outside card? (i/o) ")
        card3 = deck.pop(0)
        print(f"\n   You drew the {card3[0]}")
        
        #If user chose inside option
        if user_choice3 == "i":
            print(f"   You selected the INSIDE option")
            time.sleep(2)
            if card1[1] > card3[1] > card2[1] or card2[1] > card3[1] > card1[1]:
                print(f"   Your card, {card3[0]}, is on INSIDE of {card1[0]} and {card2[0]}")
                time.sleep(2)
                print(f"   CORRECT! Goto the final Bus Stop 4...\n")                
                stop3 = True
            else:
                print(f"   Your card, {card3[0]}, is OUTSIDE of {card1[0]} and {card2[0]}")
                time.sleep(2)
                print(f"   WRONG! have 3 drinks {name} and try again!")
                time.sleep(2)    
                
        # If user chose the outside option
        elif user_choice3 == "o":
            print(f"   You selected the OUTSIDE option")
            time.sleep(2)
            if card1[1] > card3[1] < card2[1] or card2[1] > card3[1] < card1[1]:
                print(f"   Your card, {card3[0]}, is OUTSIDE {card1[0]} and {card2[0]}")
                time.sleep(2)
                print(f"   CORRECT, Goto the final Bus Stop 4...\n")
                stop3 = True
                time.sleep(2)
            else:
                print(f"   {card3[0]} is INSIDE of {card1[0]} and {card2[0]}")
                time.sleep(2)
                print(f"   WRONG! have 3 drinks {name} and try again!")               
        else:
            print(inv)

    # Stop4: Suits
    while stop4 == False:
        print("\nBus Stop 4...")
        time.sleep(2)
        print(f"   Choose a suit: ")
        time.sleep(2)
        print(f"   Diamonds,\n   Hearts,\n   Clubs,\n   Spades ")
        user_choice4 = input("\n   Which suit do you choose? ").lower()
        
        if any(user_choice4 == d for d in ["diamonds", "d", "dia"]):
            user_choice4 = "diamonds"
        elif any(user_choice4 == d for d in ["hearts", "h", "hea"]):
            user_choice4 = "hearts"
        elif any(user_choice4 == d for d in ["clubs", "c", "clu"]):
            user_choice4 = "clubs"
        elif any(user_choice4 == d for d in ["spades", "s", "spa"]):
            user_choice4 = "spades"
        else:
            print(inv)
            time.sleep(2)
            continue
        
        computer_choice4 = random.choice(suits)
        
        if user_choice4 == computer_choice4:
            print(f"\n   {name} has chosen {user_choice4}")
            time.sleep(2)
            print(f"   The computer has chosen {computer_choice4}")
            time.sleep(2)
            print("   CORRECT! You have conquered ...RIDE THE BUS!!!...\n")
            print("   EVERYONE ELSE HAS 4 DRINKS!!!")
            stop4 = True

        elif user_choice4 not in computer_choice4:
            print(f"\n   {name} has chosen {user_choice4}")
            time.sleep(2)
            print(f"   The computer has chosen {computer_choice4}")
            time.sleep(2)
            print(f"   Tough luck {name} - Have 4 drinks, and start all over again! \n")
            time.sleep(2)
            stop4 = True

print(f"\nThe game has ended. Cheers {name} for playing RIDE THE BUS! \n")
exit = True