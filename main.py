from blackjack import Deck, Hand

  
def main():
  # Step 1: Create a deck & shuffle it
  deck = Deck()
  deck.shuffle()
 
  # Step 2: Create a player hand & dealer hand, then deal
  player = input("enter your name: ")
  players_hand = Hand(player)
  dealers_hand = Hand("Dealer")
  for i in range(2):
    players_hand.addCard(deck.deal())
    dealers_hand.addCard(deck.deal())
 
  # Step 3: Show both your cards & 1 of the dealers
  print(f'{players_hand.player}: ', end='')
  players_hand.show_all(players_hand.getHand())
  dealers_hand.show()

  # Step 4: Player goes first
  while players_hand.status == 'playing':
    players_hand.hit_or_stand(players_hand, deck)
    players_hand.show_all(players_hand.getHand())
    if players_hand.hvalue > 21:
      players_hand.updateStatus()
      # print("Game Over. You Lose.")
  

  # Step 5: Dealers Turn
  print("\nDealers Turn... ")
  dealers_hand.show_all(dealers_hand.getHand())
  while dealers_hand.hvalue < 15 and dealers_hand.status == 'playing': 
    dealers_hand.hit_or_stand(dealers_hand, deck)
    dealers_hand.show_all(dealers_hand.getHand())
    dealers_hand.updateStatus()
   
  # Step 6: Summary Report 
  players_hand.summary(players_hand)
  dealers_hand.summary(dealers_hand)

  # Step 7: Repeat

main()