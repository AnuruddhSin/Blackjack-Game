import tkinter as tk
import random

# initialize the game
dealer_cards = []
player_cards = []

def deal_card():
    """Add a card to the player's hand"""
    card_value = random.randint(1, 11)
    player_cards.append(card_value)
    player_score = sum(player_cards)
    score_label.config(text="Score: {}".format(player_score))
    player_hand_label.config(text="Player Hand: {}".format(get_card_representation(player_cards)))

def deal_dealer():
    """Add a card to the dealer's hand"""
    card_value = random.randint(1, 11)
    dealer_cards.append(card_value)
    dealer_hand_label.config(text="Dealer Hand: {}".format(get_card_representation(dealer_cards)))

def get_card_representation(cards):
    """Return the actual representation of the cards"""
    card_representation = ""
    for card in cards:
        if card == 1:
            card_representation += "1 🂡 "
        elif card == 2:
            card_representation += "2 🂢 "
        elif card == 3:
            card_representation += "3 🂣 "
        elif card == 4:
            card_representation += "4 🂤 "
        elif card == 5:
            card_representation += "5 🂥 "
        elif card == 6:
            card_representation += "6 🂦 "
        elif card == 7:
            card_representation += "7 🂧 "
        elif card == 8:
            card_representation += "8 🂨 "
        elif card == 9:
            card_representation += "9 🂩 "
        elif card == 10:
            card_representation += "10 🂪 "
        elif card == 11:
            card_representation += "11 🂫 "
    return card_representation

def check_winner():
    """Check if there is a winner"""
    dealer_score = sum(dealer_cards)
    player_score = sum(player_cards)

    if player_score > 21:
        result_label.config(text="You went over. Dealer wins!", fg="red")
    elif dealer_score > 21:
        result_label.config(text="Dealer went over. You win!", fg="green")
    elif player_score == dealer_score:
        result_label.config(text="It's a tie!", fg="orange")
    elif player_score > dealer_score:
        result_label.config(text="You win!", fg="green")
    else:
        result_label.config(text="Dealer wins!", fg="red")

def hit():
    """Add a card to the player's hand"""
    deal_card()

def stand():
    """End the player's turn and start the dealer's turn"""
    while sum(dealer_cards) < 17:
        deal_dealer()

    check_winner()



def reset():
    global dealer_cards, player_cards, dealer_score, player_score

    # clear the previous cards and scores
    dealer_cards = []
    player_cards = []
    dealer_score = 0
    player_score = 0

    # update the GUI
    dealer_hand_label.config(text="Dealer Hand:")
    player_hand_label.config(text="Player Hand:")
    score_label.config(text="Score:")
    result_label.config(text="")
    deal_card()
    deal_dealer()
    deal_card()
    deal_dealer()
    # enable the deal button and disable the hit and stand buttons
    #deal_button.config(state=tk.NORMAL)
    # hit_button.config(state=tk.DISABLED)
    # stand_button.config(state=tk.DISABLED)


def new_card_king():
    king_spades_img = tk.PhotoImage(file="king_spades.png")

    # Create a Label and add the king of spades image to it
    king_spades_label = tk.Label(root, image=king_spades_img)
    king_spades_label.pack()
# create the window
root = tk.Tk()
root.title("Blackjack")

# set the window size and position
root.geometry("600x500+400+100")

# set the window background color
root.configure(bg="#192a56")

# set the font for all widgets
font = ("Arial", 14)

# create the frames
top_frame = tk.Frame(root, bg="#192a56")
top_frame.pack(side=tk.TOP, pady=10)

dealer_frame = tk.Frame(root, bg="#192a56")
dealer_frame.pack(side=tk.TOP, pady=10)

player_frame = tk.Frame(root, bg="#192a56")
player_frame.pack(side=tk.TOP, pady=10)

middle_frame = tk.Frame(root, bg="#192a56")
middle_frame.pack(side=tk.TOP, pady=10)


bottom_frame = tk.Frame(root, bg="#192a56")
bottom_frame.pack(side=tk.TOP)

# create the widgets for the top frame
title_label = tk.Label(top_frame, text="Blackjack", font=font, fg="white", bg="#192a56")
title_label.pack()

# create the game frame
game_frame = tk.Frame(root)
game_frame.pack()
# create the buttons frame
button_frame = tk.Frame(game_frame)
button_frame.pack()
# create the widgets for the bottom frame
result_label = tk.Label(bottom_frame, text="", font=font, fg="white", bg="#192a56")
result_label.pack()
# create the widgets for the dealer's frame
dealer_label = tk.Label(dealer_frame, text="Dealer", font=font, fg="white", bg="#192a56")
dealer_label.pack(side=tk.LEFT)

dealer_hand_label = tk.Label(dealer_frame, text="Dealer Hand: [?]", font=font, fg="white", bg="#192a56")
dealer_hand_label.pack(side=tk.LEFT)

# create the widgets for the player's frame
player_label = tk.Label(player_frame, text="Player", font=font, fg="white", bg="#192a56")
player_label.pack(side=tk.LEFT)

player_hand_label = tk.Label(player_frame, text="Player Hand: []", font=font, fg="white", bg="#192a56")
player_hand_label.pack(side=tk.LEFT)

score_label = tk.Label(player_frame, text="Score: 0", font=font, fg="white", bg="#192a56", padx=10)
score_label.pack(side=tk.LEFT)

# create the widgets for the middle frame
hit_button = tk.Button(middle_frame, text="Hit", font=font, bg="#eb2f06", fg="white", command=hit)
hit_button.pack(side=tk.LEFT, padx=10)

stand_button = tk.Button(middle_frame, text="Stand", font=font, bg="#44bd32", fg="white", command=stand)
stand_button.pack(side=tk.LEFT, padx=10)
reset_button = tk.Button(middle_frame, text="Reset",command=reset, font=font, bg="#eb2f06", fg="white")
reset_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(middle_frame, text="Exit", command=root.destroy, font=font, bg="black", fg="white")
exit_button.pack(side=tk.LEFT,padx=10)
def deal_dealer():
    """Add a card to the dealer's hand"""
    card_value = random.randint(1, 11)
    dealer_cards.append(card_value)
    dealer_hand_label.config(text="Dealer Hand: {}".format(get_card_representation(dealer_cards)))
# Create a PhotoImage object from the king of spades image

# deal the first four cards
deal_card()
deal_dealer()
deal_card()
deal_dealer()


# start the main loop
root.mainloop()
