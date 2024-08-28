theboard={'1':" ",'2':" ",'3':" ",
       '4':" ",'5':" ",'6':' ',
       '7':' ','8':' ','9':' '}
board_keys=[]
for key in theboard:
    board_keys.append(key)
def board(board):
    print(board['1']+'|'+ board['2']+'|'+ board['3'])
    print('_|_|_')
    print(board['4']+'|'+ board['5']+'|'+ board['6'])
    print('_|_|_')
    print(board['7']+'|'+ board['8']+'|'+ board['9'])
def game():
    turn='X'
    count=0
    for i in range(10):
        board(theboard)
        print("It's your turn:"+turn+".Move where?")
        move=input()
        if theboard[move]==' ':
            theboard[move]=turn
            count+=1
        else:
            print("This place is already taken. Try again pls!")
            continue
        if count>=5:
            if theboard['7']==theboard['8']==theboard['9']!=' ':
                board(theboard)
                print("\nGame Over!.\n")
                print("***"+turn+"Won.***")
                break
            elif theboard['4']==theboard['5']==theboard['6']!=' ':
                board(theboard)
                print("\nGame Over!.\n")
                print("***",turn," Won!!***")
                break
            elif theboard['1']==theboard['2']==theboard['3']!=' ':
                board(theboard)
                print("\nGame Over!.\n")
                print("***",turn," Won.***")
                break
            elif theboard['1']==theboard['4']==theboard['7']!=' ':
                board(theboard)
                print("\nGame Over!.\n")
                print("***"+turn+"Won.***")
                break
            elif theboard['2']==theboard['5']==theboard['8']!=' ':
                board(theboard)
                print("\nGame Over!.\n")
                print("***"+turn+"Won.***")
                break
            elif theboard['3']==theboard['6']==theboard['9']!=' ':
                board(theboard)
                print("\nGame Over!.\n")
                print("***"+turn+"Won.***")
                break
            elif theboard['3']==theboard['5']==theboard['7']!=' ':
                board(theboard)
                print("\nGame Over!.\n")
                print("***"+turn+"Won.***")
                break
            elif theboard['1']==theboard['5']==theboard['9']!=' ':
                board(theboard)
                print("\nGame Over!.\n")
                print("***"+turn+"Won.***")
                break
        if count==9:
            print("\nGame Over!.\n")
            print("Its a Tie!")
        if turn=='X':
            turn='O'
        else:
            turn='X'
    restart=input("Do you want to try again?(y/n)")
    if restart=='y' or restart=='Y':
        for key in board_keys:
            theboard[key]=' '
        game()

if __name__ == "__main__":
    game()           
                
                
    

    
    
    
