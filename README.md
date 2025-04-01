# credit-card-model
Trying to find the optimum strategy for playing the playing card game, credit card

The game is:

* Each player gets four cards face down
* The first player picks up a card from the deck and can either choose to discard it or
swap the card with the first of their face down cards
* If they choose to swap, they can then again decide to swap with the second card in their pile or discard the newly 
picked up card
* This continues until they discard, or swap with their last card in which case they have to discard the picked up card
* Once they finish their turn, it is the other players turn who repeats the same process
* When one player thinks that they have a lower score than the opponent, they can call credit card, then the other player
has one more turn
* You add up the count of your face down cards (Ace being one point, picture cards being 10) and the player with the
lowest total wins the round.