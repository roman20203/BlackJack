from Deck import *
from Player import *
from Card import *


class BlackJack(object):
    '''
    classdocs
    '''
    gamedeck = Deck()

    def __init__(self, playerName):
        '''
        Initializes the game by
        - shuffling the deck
        - initializing a player1 (with given playerName) and dealer object (both are Player objects)
        '''
        self.gamedeck.shuffle()
        self.player1= Player(playerName)
        self.dealer= Player("Dealer")
    
    def getWinner(self):
        '''
        returns the player object (either the class's player1 or dealer object) that is the winner
        based on their hands (closest to 21 without going over)
        
        return - Player object
        ''' 
        if self.player1.score>21 and self.dealer.score<21 or self.dealer.score==21 and self.player1.score!=21 or self.player1.score<self.dealer.score and self.dealer.score<21:
          return "\nDealer Wins, Player 1 Loses"


        if self.player1.score<21 and self.dealer.score>21 or self.player1.score==21 and self.dealer.score!=21 or self.dealer.score<self.player1.score and self.player1.score<21:
          return "\nPlayer 1 Wins, Dealer Loses"
      

        if self.player1.score ==21  and self.dealer.score ==21:
          if len(self.player1.hand)<len(self.dealer.hand):
            return "\nPlayer 1 Wins, Dealer Loses"
          if len(self.player1.hand)>len(self.dealer.hand):
            return "Dealer Wins, Player 1 Loses"
        
        if self.player1.score>21 and self.dealer.score>21 or self.player1.score==self.dealer.score:
          return("\nPlayer1 and Dealer have tied!")
    
    def play(self):

        '''
        play the game using the class's deck, player1, and dealer objects
        '''
        
        '''
        initialize player1 and dealer hands (2 cards each)
        show player 1 hand
        player1 decision (hit or stand)
        dealer complete hand
        present game outcome - player1 win or lose
        '''
        again=True
        
        while again:

          for i in range(2):
            self.player1.addToHand(self.gamedeck.takeCard())
          print("\n")
          print(self.player1)

          hit=True

          while hit:
          
            decision=input("Hit or Stand:")

            if decision.lower()== "hit" or decision.lower()=="h":
              self.player1.addToHand(self.gamedeck.takeCard())
              print("\n")
              print(self.player1)
            
            if decision.lower()=="stand" or decision.lower()=="s" or self.player1.score>=21:
              print("\n")
              print("-"*30)
              print("Player1 Final")
              print("-"*30)
              print(self.player1)
              print("-"*30)
              hit=False
        

          for i in range(2):
            self.dealer.addToHand(self.gamedeck.takeCard())
            self.dealer.getBJScore()
          
          dealerHit=True

          while dealerHit:
            dealerHit=False
            if self.dealer.score<17:
              self.dealer.addToHand(self.gamedeck.takeCard())
              self.dealer.getBJScore()
              dealerHit=True
            if self.dealer.score>=17:
              dealerHit=False
              print("-"*30)
              print("Dealer Final")
              print("-"*30)
              print(self.dealer)
              print("-"*30)

          print(self.getWinner())
          print("\n")

          user_again=input("Would you like to play again?(y/n):")
          if user_again.lower()=="y":
            self.gamedeck.reset()
            self.__init__(self.player1.nameStr)
          if user_again.lower()=="n":
            again=False
            print("Goodbye!")


          

    
    def showWelcome(self):
        '''
        outputs a welcome message to the the player
        '''
        print("Welcome to BlackJack")
