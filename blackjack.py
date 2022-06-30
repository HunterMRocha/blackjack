import random

values = [1,2,3,4,5,6,7,8,9,10,10,10,10]
suits = ["♠", "♣", "♥", "♦"]

class Card:
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

  def str(self):
    return self.value + " " + self.suit


    

class Deck:
  def __init__(self):
    self.deck = []
    for val in values:
      for suit in suits:
        card = Card(str(val),suit).str()
        self.deck.append(card)
      
  
  def str(self):
    deck_str = ""
    for card in self.deck:
     deck_str += "\n" + card.str()
    return deck_str

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    return self.deck.pop()



    

class Hand:
  def __init__(self, player):
    self.hand = []
    self.aces = 0
    self.hvalue = 0 # -1:Blackjack, -2:Bust
    self.player = player
    self.status = "playing"

  def addCard(self,card):
    self.hand.append(card)
    self.hvalue += int(card.split()[0])

  def show(self):
    print(f"Dealer: UNKNOWN, {self.hand[0]}\n")


  def getHand(self):
    return self.hand
  
  def updateStatus(self):
    if self.hvalue > 21:
      self.status = 'bust'
    elif self.hvalue == 21: 
      self.status = 'blackjack'
    else:
      return self.hvalue

  def hit_or_stand(self, hand, deck):
    if hand.player != "Dealer":
      choice = input("Hit or Stand? ").lower()
      if choice == "stand":
        self.status = "stand"
      else:
        hand.addCard(deck.deal())
        hand.updateStatus()
    else: 
      hand.addCard(deck.deal())
      hand.updateStatus()

  def show_all(self, hand):
    for card in hand:
      print(f'{card} ', end='' )
    print("\n")

  def summary(self, hand):
    print(f'{hand.player}\'s Hand: {hand.getHand()}\nTotal: {hand.hvalue}\nStatus: {hand.status}\n')
  
  