
board = list(range(1,10))
win_coard = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
def draw_board():
   for i in range(3):
       print(board[0+i*3],board[1+i*3],board[2+i*3])


def input_token(token):
   while True:
       value = input('куда поставить '+token+'? ')
       if not (value in '123456789'):
           print('ошибочный ввод')
           continue
       value = int(value)
       if str(board[value-1]) in 'XO':
           print('клиетка уже занята')
           continue
       board[value - 1] = token
       break


def win():
   for each in win_coard:
       if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
           return board[each[1]-1]
   else:
       return False


def main():
   count = 0
   while True:
       draw_board()
       if count % 2 == 0:
           input_token('X')
       else:
           input_token('O')
       if count>=3:
           winner = win()
           if winner:
               draw_board()
               print(winner, "победил")
               break
       count += 1
       if count > 8:
           draw_board()
           print("ничья")
           break


main()
