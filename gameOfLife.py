import random

board_state = [[]]


def random_state(width, height):
    outer_list = []
    for i in range(height):
        inner_list = []
        for j in range(width):
            inner_list.append(random_dead_or_alive(2))
        outer_list.append(inner_list)

    change_board_state(outer_list)


def random_dead_or_alive(random_numbers):
    number = random.randint(0, (random_numbers - 1))
    if (number == 0):
        return 1
    else:
        return 0

life_cycle_num = 1


def print_pretty(width, height):
    print("\n")
    global life_cycle_num
    life_cycle_num = life_cycle_num + 1
    output_string_list = []
    temp = " -"*width
    output_string_list.append(temp)
    for i in range(height):
        output_string = "|"
        for j in range(width):
            if(board_state[i][j] == 1):
                output_string = output_string + "# "
            else:
                output_string = output_string + "  "
        output_string = output_string + "|"
        output_string_list.append(output_string)
    output_string_list.append(temp)

    print_string = "Life cycle number: " + str(life_cycle_num) + "\n-------------------------------------\n"
    for str_out in output_string_list:
        print_string = print_string + str_out + "\n"

    print_string = print_string + "\n\nType 'exit' to quit: "

    print(print_string)


def check_neighbors(width, height):
    tempBoard = [[0 for i in range(width)]for j in range(height)]
    for a in range(width):
        for b in range(height):
            tempBoard[b][a] = board_state[b][a]
    for x in range(width):
        for y in range(height):
            blah = 0
            live_neighbors = 0
            if(x-1 >= 0):
                if(y-1 >= 0):
                    live_neighbors = live_neighbors + fuckYou(x-1, y-1)
                live_neighbors = live_neighbors + fuckYou(x-1,y)
                if(y+1 < height):
                    live_neighbors = live_neighbors + fuckYou(x-1, y+1)
            if(y-1 >= 0):
                live_neighbors = live_neighbors + fuckYou(x, y-1)
            if(y+1 < height):
                live_neighbors = live_neighbors + fuckYou(x, y+1)
            if(x+1 < width):
                if(y-1 >= 0):
                    live_neighbors = live_neighbors + fuckYou(x+1, y-1)
                live_neighbors = live_neighbors + fuckYou(x+1, y)
                if(y+1 < height):
                    live_neighbors = live_neighbors + fuckYou(x+1, y+1)
            tempBoard[y][x] = live_or_die(live_neighbors, x, y)
            #print(x,y)
            #print("live neighbors: ", live_neighbors)
            #print("=======================")
    change_board_state(tempBoard)


def fuckYou(x, y):
    if(board_state[y][x] == 1):
        return 1
    else:
        return 0


def live_or_die(neighbors, x, y):
    if(fuckYou(x, y) == 1):
        if((neighbors == 3) or (neighbors == 2)):
            return 1
        else:
            return 0
    else:
        if(neighbors == 3):
            return 1
        else:
            return 0

def change_board_state(new_board):
    global board_state
    board_state = new_board

def run_game(width, height):
    key = ''
    while not(key == "exit"):
        print_pretty(width, height)
        check_neighbors(width, height)
        key = input()



def main():
    what_start = input("'load' file, or 'new' game: ")
    board_width = 0
    board_height = 0
    key = True
    while(key):
        if(what_start == "new"):
            while(True):
                try:
                    width = input("What width would you like: ")
                    board_width = int(width)
                    height = input("What height would you like: ")
                    board_height = int(height)
                    break
                except:
                    print("Invalid input")
            random_state(board_width, board_height)
            run_game(board_width, board_height)
            key = False
        elif(what_start == "load"):
            board_file = ''
            key2 = True
            while(key2):
                try:
                    data = []
                    board_file = input("type in the name of your saved board: ")
                    file_path_string = r"C:\Users\gabri\OneDrive\Documents\Coding\Python\LearnPythonDotIO\gameOfLife_Boards\\"
                    file_path_string = file_path_string + board_file + ".txt"
                    with open(file_path_string, 'r') as file:
                        data = file.read().split('\n')
                    board_height = len(data)
                    board_width = len(data[0])

                    loaded_board = []
                    for row in data:
                        board_row = []
                        for char in row:
                            board_row.append(int(char))
                        loaded_board.append(board_row)

                    change_board_state(loaded_board)
                    run_game(board_width, board_height)
                    key2 = False
                except:
                    if(board_file == "exit"):
                        #exit the inner while loop
                        key2 = False
                    else:
                        print("There is no saved board with that name. Try again, or type 'exit' to quit")
            key = False
        elif(what_start == "exit"):
            #exit while loop
            key = False
        else:
            board_start = input("Invalid input. Type 'exit' to quit, or try again: ")
    

if(__name__ == "__main__"):
    main()
