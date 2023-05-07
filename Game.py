from deck import Deck
from hand import Hand

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
           
        while games_to_play <= 0:
            try:
                games_to_play = int(input("Enter number of games to play (0 or any key to exit): "))
                if games_to_play == 0:
                    print("Thank you! Hope to see you again!") 
                    return 0
            except:
                print("Thank you! Hope to see you again!")
                return 0

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            

            print()
            print("|--------------------" * 1)          
            print(f"| Game {game_number} of {games_to_play}")
            print("|--------------------" * 1)
            print()

            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand' (h/s): ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (h/s) ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
                    
            if self.check_winner(player_hand, dealer_hand):
                continue
          
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue
            
            self.show_values(player_hand,dealer_hand)
            # print("----- RESULT -----")
            # print("Your hand:", player_hand_value)
            # print("Dealer's hand:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)           
        print("\nThanks for playing!")

    def show_values(self, player_hand,dealer_hand):
        print("----- RESULT -----")
        print("PLAYER:", player_hand.get_value())
        print("DEALER:", dealer_hand.get_value())
        print("------------------")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                self.show_values(player_hand,dealer_hand)
                print("Busted! Dealer wins. 😭")
                return True
            elif dealer_hand.get_value() > 21:
                self.show_values(player_hand,dealer_hand)
                print("Dealer busted. You win! 😀🎉")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                self.show_values(player_hand,dealer_hand) 
                print("Push (Tie). Bets off. 😒")
                return True            
            elif player_hand.is_blackjack():
                self.show_values(player_hand,dealer_hand)
                print("Blackjack! You win! 😀🎉")
                return True
            elif dealer_hand.is_blackjack():
                self.show_values(player_hand,dealer_hand)
                print("Dealer has blackjack. Dealer wins. 😭")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win! 😀🎉")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Push (Tie). Bets off. 😒")
            else:
                print("Dealer wins. 😭")
            return True
        return False