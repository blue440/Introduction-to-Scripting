# Cody Beck


# Initial game title.
def welcome():
    print("\n    Welcome to the\n Lich Text Adventure Game\n")


# User command directions.
def directions():
    print(" Collect 6 items to win the game, or become the Lich's undead minion.\n")
    print(' To explore use the following commands.\n', 'go North\n', 'go South\n',
          'go East\n', 'go West\n', '\n', "To collect items use.\n", "get 'item name'\n")
    print(" Type 'Directions' to view command list.\n")
    print(" Type 'exit' to quit the game.\n")


# Ask user to play again
def play_again():

    play = input(' Would you like to play again?\n Type yes or no\n>')
    if play.lower() == 'no':
        return False
    elif play.lower() == 'exit':
        return False
    elif play.lower() == 'yes':
        return True
    else:
        print(' Try again.')


# End text to let user know that they have left the game.
def end_text():
    print(' Thanks for playing!')


# Main game function.
def main():

    # Dictionary of room connections.
    rooms = {
        'Sanctuary': {'North': 'Kitchen', 'South': 'Catacombs', 'East': 'Vestry', 'West': 'Chancel'},
        'Chancel': {'East': 'Sanctuary', 'item': 'Blessing'},
        'Kitchen': {'West': 'Larder', 'South': 'Sanctuary', 'item': 'Holy Water'},
        'Larder': {'East': 'Kitchen', 'item': 'Torch'},
        'Vestry': {'West': 'Sanctuary', 'North': 'Sacristy', 'item': 'Magic Sigil'},
        'Sacristy': {'South': 'Vestry', 'item': 'Cross'},
        'Catacombs': {'North': 'Sanctuary', 'East': 'Crypt', 'item': 'Chant'},
        'Crypt': {'West': 'Catacombs', 'item': 'Lich'}
    }

    # Define variables.
    location = 'Sanctuary'
    inventory = []
    action = ""
    target = ""

    # Status function to detect if room has an available item and which sentence to use.
    def status():

        # Test to see if there is an item in the room and format accordingly.
        if 'item' in rooms[location]:
            print(' You are in the {}'.format(location))
            print(' Inventory: {}'.format(inventory))

            # statements to choose proper sentence for output.
            if rooms[location]['item'] == 'Holy Water':
                print(' You see some {}'.format(rooms[location]['item']))
                print(' Enter your move.')

            elif rooms[location]['item'] == 'Blessing':
                print(' You can receive a {}'.format(rooms[location]['item']))
                print(' Enter your move.')

            elif rooms[location]['item'] == 'Chant':
                print(' You can learn a {}'.format(rooms[location]['item']))
                print(' Enter your move.')

            else:
                print(' You see a {}'.format(rooms[location]['item']))
                print(' Enter your move.')

        # Output format with no items in the room.
        else:
            print(' You are in the {}'.format(location))
            print(' Inventory: {}'.format(inventory))
            print(' Enter your move.')

    # Main game loop.
    while action != 'exit':

        # Test for win / loss conditions

        # Loss condition
        if location == 'Crypt':
            if len(inventory) != 6:

                print(' Bzzztt....   Game Over!')
                answer = play_again()

                if answer is True:
                    location = 'Sanctuary'
                    welcome()
                    directions()
                    main()
                    break
                else:
                    break

            # Win Condition
            elif len(inventory) == 6:

                print(' You have defeated the Lich!')
                answer = play_again()

                if answer is True:
                    location = 'Sanctuary'
                    welcome()
                    directions()
                    main()
                    break

                else:
                    break

        # Main game loop
        else:
            status()

            # Set variables to user input.
            direction = input('>')
            direction_list = direction.split(maxsplit=1)

            # Test for valid input
            if len(direction_list) > 0:
                action = direction_list[0].lower()

            if len(direction_list) == 2:
                target = direction_list[1].title()

            # Check for movement input
            if action == 'go':

                # Use input to change rooms
                if target in rooms[location]:
                    location = rooms[location][target]

                else:  # Display error message
                    print(" You can't go that way!")

            # Check for get 'item' input
            elif action == 'get':

                # Display error message
                if 'item' not in rooms[location]:
                    print(" There is nothing here.")

                elif target not in rooms[location]['item']:
                    print(" There is no {} here".format(target))

                # Use input to collect items
                elif target in rooms[location]['item']:
                    inventory.append(rooms[location]['item'])
                    del rooms[location]['item']  # Remove items from the dictionary to prevent confusion

            # User access to game instructions
            elif action == 'directions':
                directions()

            # Exit to break game loop
            elif action == 'exit':
                break

            else:  # Display error message
                print(' Try a different command.')


# Function calls to begin the game
welcome()
directions()
main()
end_text()

