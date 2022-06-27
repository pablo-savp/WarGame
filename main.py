import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
  
  def __init__(self,type,rank):
    self.tipo=type
    self.rango=rank
    self.value=values[rank]
    
  def __str__(self):
    return self.rank + " of " + self.type

class Deck:
  def __init__(self):
    self.all_cards=[]
    for suit in suits:
      for rank in ranks:
        
        createdCard=Card(suit,rank)
        self.all_cards.append(createdCard)

  def shuffleDeck(self):
    random.shuffle(self.all_cards)

  def deal_one(self):
    return self.all_cards.pop()

class Player:
  
  def __init__(self,name):
    self.name=name
    self.all_cards=[]

  def removeOne(self):
    return self.all_cards.pop(0)

  def addCards(self,new_cards):
    if type(new_cards) == type([]):
      self.all_cards.extend(new_cards)
    else:
      self.all_cards.append(new_cards)
    

  def __str__(self):
    return f"Player {self.name} has {len(self.all_cards)} cards"


#MAIN
#Game Set-up
player_one=Player("One")
player_two=Player("Two")

gameDeck= Deck()
gameDeck.shuffleDeck()

for x in range(26):
  player_one.addCards(gameDeck.deal_one())
  player_two.addCards(gameDeck.deal_one())

game_on= True
roundNumber=0

while game_on:
  roundNumber+=1
  print(f"Round {roundNumber}")

  if len(player_one.all_cards) ==0:
    print("Player one is out of cards! Player Two Wins")
    game_on = False
    break

  if len(player_two.all_cards) ==0:
    print("Player two is out of cards! Player One Wins")
    game_on = False
    break

  #Start of round
  playerOneTableCards = []
  playerOneTableCards.append(player_one.removeOne())
  
  playerTwoTableCards = []
  playerTwoTableCards.append(player_two.removeOne())

  at_war=True

  while at_war:
    
    if playerOneTableCards[-1].value > playerTwoTableCards[-1].value:   

      player_one.addCards(playerOneTableCards)
      player_one.addCards(playerTwoTableCards)
      at_war=False

    elif playerTwoTableCards[-1].value > playerOneTableCards[-1].value:   

      player_two.addCards(playerOneTableCards)
      player_two.addCards(playerTwoTableCards)
      at_war=False

    else:
      print("War has Started!")

      if len(player_one.all_cards) < 5:
        print("Player one is unable to declare War due to lack of cards")
        print("Player Two Wins!")
        game_on = False
        break

      elif len(player_two.all_cards) < 5:
        print("Player two is unable to declare War due to lack of cards")
        print("Player One Wins!")
        game_on = False
        break

      else:
        for num in range(5):
          playerOneTableCards.append(player_one.removeOne())
          playerTwoTableCards.append(player_two.removeOne())
          
          
      
  
  
  

  
    
    
        
    
  
  
  