board = list(range(1,10))

#создание поля на крестиков и ноликов
def draw_board(board): #функция
    print("." * 13)
    for i in range(3): #цикл
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("." * 13)

#ведение числа для хода и их проверка
def take_input(p_token): #функция
    valid = False
    while not valid: #тело-цикл, пока проверяймое условие истеное
        p_answer = input("куда поставм(X)" + p_token)
        try:
            p_answer = int(p_answer) #ведение числа
        except:
            print("нет такого числа!!! вы уверены что правильно вели???")
            continue #пропускает часть цикла
        if p_answer >=1 and p_answer <=9: #логическое сравнение (условие)
            if(str(board[p_answer-1]) not in "XO"): #логическое сравнение (условие)
                board[p_answer-1] = p_token
                valid = True #верное значение
            else:
                print("ты что гопник???")
        else:
            print("введите число от 1 до 9!!!")

#выйгрышные комбинации
def cheak_win(board): #функция
    win_coo = (0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)
    for each in win_coo:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

# кто выйграл
def main(board):
    coun = 0
    win = False
    while not win:
        draw_board(board) 
        if coun % 2 == 0: # если четное то выйграл X
            take_input("X") 
        else: # если не четное то выйграл O
            take_input("O") 
        coun +=1

        if coun >4: 
            thy = cheak_win(board)

            if thy:
                print(thy, "Вы выйграли))))")
                win = True
                break
        if coun ==9:
            print("ничья(((")
            break
    draw_board(board)
main(board)
