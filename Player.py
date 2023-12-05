from Card import *

class Player(object):
    #represents a player object
    nameStr =""
    def __init__(self, nameStr):
      self.hand=[]
      self.score=0
      self.nameStr=nameStr

    #nameStr - the name of the player, i.e 'Player 1' or 'Dealer'
  
        #add your code here
        
    def addToHand(self,newCard):
        #appends a card object to the players hand and updates the score
        self.hand.append(newCard)

        if self.score!=1:
          self.score+= newCard.BJValue()
      
        if newCard.BJValue()==1:
          new_value=self.score
          if new_value+11<=21:
            self.score+=10
          else:
            self.score+=0


    def getBJScore(self):
        '''
        returns the score of the players hand
        
        return int
        '''
        return self.score
        
    
    def getName(self):
        #returns the name of the player
        return self.nameStr
        
    def __str__(self):
        #returns the string representation of the object, that includes the 
        #name, score, and cards in the hand
        #presents on screen

        string=""

        for i in range(len(self.hand)):
          string+=str(self.hand[i]) + ", "
    
        return("Player: "+ self.getName() + "\nScore:"+ str(self.getBJScore()) + "\nHand: "+ string)

