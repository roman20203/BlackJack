class Card(object):
    '''
    An object representing a card 
    '''
    def __init__(self, rank, suit):
        '''
        Create an instance of a card
        '''
        self.rank=rank
        self.suit=suit
     
    def getRank(self):
        '''
        Return the rank of the card
        '''
        string=""
        if self.rank==1:
          string="Ace"
        if self.rank==11:
          string="Jack"
        if self.rank==12:
          string="Queen"
        if self.rank==13:
          string="King"
        if self.rank<11 and self.rank>1:
          string=self.rank
        return str(string)

    def getSuit(self):
        '''
        Return the suit of the card
        '''
        strsuit=""
        if self.suit=="c":
          strsuit= "Clubs"
        if self.suit=="d":
          strsuit= "Diamonds"
        if self.suit=="h":
          strsuit= "Hearts"
        if self.suit=="s":
          strsuit= "Spades"
        return str(strsuit)

    def BJValue(self):
      '''
      Return the BlackJack rank of the card
      '''
      if self.rank in [11,12,13]:
        return 10
      if self.rank==1:
        return 1
      if self.rank>1 and self.rank<11:
        return self.rank
  
    def __str__(self):
      '''
      Return the card's suit and rank in a string
      '''
      return self.getRank() + " of " + self.getSuit()



