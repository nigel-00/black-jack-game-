#import the random module 
import random 

#Create a deal_card function 
def deal_card():
    #deal card list: Every card has an equal chance of being selected
    cards  = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    #Select a random card from the cards list
    card  = random.choice(cards)
    #return a random card from the cards list 
    return card 
#Create the calculate score function 
def calculate_score(cards):
    #Check for a black jack 
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #Check for an ace, removes the value 11 and replaces with 1 if the user has more than 21 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    #returns the total value of the cards 
    return sum(cards)
#Compare the scores 
def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose!"
    if user_score == computer_score:
            return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose!"


def play_game():
    #Start out with creating two empty lists that keep track of the dealer and the user cards drawn
    user_cards  = []
    computer_cards =  []
    #Check if the game is over
    is_game_over  = False
    #run the for loop twice to get two cards 
    for _ in range(2):
        #returns  a new card using the deal card function 
        new_card  = deal_card()
        #Add the cards to the user_card list 
        user_cards.append(new_card)
        #Add the card to the computer_list 
        computer_cards.append(new_card)
    #While the game is playing
    while not is_game_over:

        #Calculate the user and computer score
        user_score = calculate_score(user_cards)
        computer_score  = calculate_score(computer_cards)
        #Print computer`s first card and user cards 
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer`s first card: {computer_cards[0]}")
        #Checks for a black jack from both the user and the computer and also if the user has a score more than 21 
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over =  True 
        else:
            #Ask the user to deal again 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            #If they type y then deal a card and add it to the user cards 
            if user_should_deal == "y":
                user_cards.append(deal_card())
            #else the game is over
            else:
                is_game_over = True
    #Computer draws a card if its score is not 0 and less than 17
    while computer_score != 0 and  computer_score < 17:
        #Add a new card to the computer list 
        computer_cards.append(deal_card())
        #Calculate the computer score 
        computer_score = calculate_score(computer_cards)
        #Display the final score for the computer and user
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer`s final hand: {computer_cards}, final score {computer_score} ")
    #call the compare function and print the final winner
    print(compare(user_score, computer_score))
#If they want to play the game call the game function 
while input("Do you want to play a game of Blackjack? Type 'y' or 'no': ") == "y":
    play_game()

