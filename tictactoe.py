'''
this is the game of tic tac toe where one has to get 3 consecutive X's or O's to win the game
'''
def get_symbol_of_player():
    answer =  str(raw_input("Player1, Choose your symbol: 'X' or 'O'\n"))
    return answer
def show_board(positionList):
    emptyline = ((' '*3 + "|" )*2 + ' '*3)
    dashedline = '-' *11
    print (emptyline)
    print (' ' + positionList[0] + ' ' + '|' + ' ' + positionList[1] + ' ' + '|' + ' ' + positionList[2] + ' ')
    print (emptyline)
    print (dashedline)
    print (emptyline)
    print (' ' + positionList[3] + ' ' + '|' + ' ' + positionList[4] + ' ' + '|' + ' ' + positionList[5] + ' ')
    print (emptyline)
    print (dashedline)
    print (emptyline)
    print (' ' + positionList[6] + ' ' + '|' + ' ' + positionList[7] + ' ' + '|' + ' ' + positionList[8] + ' ')
    print (emptyline)
 

def end_of_game(posList,player1_turn):
    
    if (posList[0] == posList[1] == posList[2] != ' ' or
        posList[3] == posList[4] == posList[5] != ' ' or
        posList[6] == posList[7] == posList[8] != ' ' or
        posList[0] == posList[4] == posList[8] != ' ' or
        posList[2] == posList[4] == posList[6] != ' ' or
        posList[0] == posList[3] == posList[6] != ' ' or
        posList[1] == posList[4] == posList[7] != ' ' or
        posList[2] == posList[5] == posList[8] != ' '):
        print ('GAME OVER')
        if not player1_turn:
            print ('PLAYER 1 WINS!!')  
        else:
            print ('PLAYER 2 WINS!!')
        return True
    
    elif not ' ' in posList:
        print ('GAME HAS ENDED IN A DRAW')
        return True
    
    else:
        return False
    
 
def play_game(position,filledPlaces,p1_sign, p2_sign,player_dict,player1_turn):
    
    def check_for_valid_position(index,filled):
        return (not index in filled) and (not index > 9)
    
    if player1_turn:
        print ("Player1's turn")
        pos = input('enter the position you want to mark (1-9)')
        if check_for_valid_position(pos,filledPlaces):
            position[pos-1]=p1_sign
            filledPlaces.append(pos)
            player1_turn = False
            show_board(position)
        else:
            print ('enter position of an empty space')
            play_game(position,filledPlaces,p1_sign, p2_sign,player_dict,player1_turn)
    else:
        print ("Player2's turn")
        pos = input('enter the position you want to mark (1-9)')
        if check_for_valid_position(pos,filledPlaces):
            position[pos-1]=p2_sign
            filledPlaces.append(pos)
            player1_turn = True
            show_board(position)
        else:
            print ('enter position of an empty space')
            play_game(position,filledPlaces,p1_sign, p2_sign,player_dict,player1_turn)
    while not end_of_game(position,player1_turn):
        play_game(position,filledPlaces,p1_sign, p2_sign,player_dict,player1_turn)
    play_again = str(raw_input("Would you like to play another game? Type 'Yes' or 'No'"))
    if play_again.lower() == 'yes':
        main()
    else:
        quit() 
 
def main():
    print ('Let us start the game\n')
    player1_sign = get_symbol_of_player()
    if not (player1_sign == 'X' or player1_sign == 'O'):
        print ("Please choose only among 'X' and 'O'\n")
        player1_sign = get_symbol_of_player()

    player_dict={}        
    if player1_sign == 'X' :
        player_dict['X'] = 'player1'
        player2_sign = 'O'
        player_dict['O'] = 'player2'
    else:
        player_dict['O'] = 'player1'
        player2_sign = 'X'
        player_dict['X'] = 'player2' 
    
    print ('Let us begin. {} starts'.format(player_dict['X']))
    positionList=[' ' for num in range(0,9)]
    show_board(positionList)
    filledPlaces=[]
    player1_turn = True if player_dict['X'] == 'player1' else False
    play_game(positionList,filledPlaces, player1_sign,player2_sign,player_dict,player1_turn)

if __name__=="__main__":
    main()