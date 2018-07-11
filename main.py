import Game

print('Welcome to Tic Tac Toe!')

while True:
    #reset board
    theBoard = [" "]*100
    player1_marker , player2_marker = Game.player_input()
    turn = Game.choose_first()
    print (turn + ' will go first!')
    
    playgame = input("Would you like to start the game? ").upper() 
    
    if playgame[0] == "Y":
        game_on = True
    else:
        game_on = False
    
    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            
            Game.display_board(theBoard)
            position = Game.player_choice(theBoard)
            Game.place_marker(theBoard, player1_marker, position)

            if Game.win_check(theBoard, player1_marker):
                Game.display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if Game.full_board_check(theBoard):
                    Game.display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.
            
            Game.display_board(theBoard)
            position = Game.player_choice(theBoard)
            Game.place_marker (theBoard, player2_marker, position)
                
            if Game.win_check(theBoard, player2_marker):
                Game.display_board(theBoard)
                print('Congratulatiuons! You have won the game!')
                game_on = False
            else:
                if Game.full_board_check(theBoard):
                    Game.display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not Game.replay():
        break