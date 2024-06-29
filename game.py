from blackjack import Player,Card,Deck,Dealer,Game

print("Welcome to Blackjack!")
player_name = input("Enter your name: ")
player = Player(player_name)
dealer = Dealer()
while True:
    game = Game()
    print(f"{player.name}'s chip balance: {player.chip_balance}")
    bet = int(input("Place your bet: "))
    player.place_bet(bet)
    game.deal_initial_cards(player, dealer)
    print(f"Dealer's hand: {dealer.hand[0]} and [hidden]")
    game.player_turn(player)
    if player.get_hand_value() <= 21:
        game.dealer_turn(dealer)
    result = game.check_winner(player, dealer)
    print(result)
    if result == f"{player.name} wins":
        player.chip_balance += bet * 2
    elif result == "It's a tie":
        player.chip_balance += bet
    if player.chip_balance <= 0:
        print("You're out of chips! Game over.")
        break
    play_again = input("Do you want to play another round? (y/n): ").lower()
    if play_again != 'y':
        break
print("Thank you for playing Blackjack!")

