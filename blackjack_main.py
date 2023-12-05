from BlackJack import*

# Main game function
def main():
    # Initialize a game object with player name
    game = BlackJack(input("Please Enter Your Name:"))
    # Run game
    game.play()
main()
