print("Крестики нолики")
pole = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
win = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
       [0, 3, 6], [1, 4, 7], [2, 5, 8],
       [0, 4, 8], [2, 4, 6]]

def b_pole():
        
    print(pole[0], pole[1], pole[2])
    print(pole[3], pole[4], pole[5])
    print(pole[6], pole[7], pole[8])
def check_win():
    res = ""
    for i in range(0,len(win)):

        if pole[win[i][0]] == 'x' and pole[win[i][1]] == 'x' and pole[win[i][2]] == 'x':
            #print("Победа Х")
            res = "X"
            
        if pole[win[i][0]] == '0' and pole[win[i][1]] == '0' and pole[win[i][2]] == '0':
            #print("Победа 0")
            res = "0"
            

    return res            
game_over = False  
while game_over == False:
        
    b_pole()
    step = int(input("Введи число "))
    ind = pole.index(step)
    
    pole[ind] = 'x'
    res = check_win()
    if res != "":
        
        game_over = True
        b_pole()
        print("Game Over, Winner is ", res)
        break
    b_pole()
    step = int(input("Введи число"))
    ind = pole.index(step)

    
    pole[ind] = '0'
    res = check_win()
    if res != "":
        game_over = True
        b_pole()
        print("Game Over, Winner is ", res)
        break
