# use cartesian coordinates

grid = [[None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None]]

def move_coord(in_x, in_y, x_move, y_move):
    out_x = in_x + x_move
    out_y = in_y + y_move
    if out_x < 0 or out_y < 0:
        print('less than 0')
        return (in_x, in_y)
    elif out_x > 4 or out_y > 4:
        print('too big')
        return (in_x, in_y)
    elif grid[out_y][out_x]==None:
        print('nonetype problem')
        return (in_x, in_y)
    else:
        print('actually worked')
        return (out_x, out_y)

def find_number(cur_x, cur_y, line_dir):
        out_x = cur_x
        out_y = cur_y
        for let in line_dir:
                if let == 'L':
                    new_coord = move_coord(out_x, out_y, -1, 0)
                    out_x = new_coord[0]
                    out_y = new_coord[1]
                elif let == 'R':
                    new_coord = move_coord(out_x, out_y, 1, 0)
                    out_x = new_coord[0]
                    out_y = new_coord[1]
                elif let == 'U':
                    new_coord = move_coord(out_x, out_y, 0, -1)
                    out_x = new_coord[0]
                    out_y = new_coord[1]
                else:
                    new_coord = move_coord(out_x, out_y, 0, 11)
                    out_x = new_coord[0]
                    out_y = new_coord[1]
        return (out_x, out_y)


def find_code(input_str):
        cur_x = 0
        cur_y = 2
        code = []
        input_dir = input_str.splitlines()

        # naming: dir for directions
        for line_dir in input_dir:
                print(line_dir)
                line_info = find_number(cur_x, cur_y, line_dir)
                cur_x = line_info[0]
                cur_y = line_info[1]
                print (cur_x, cur_y, 'coords')
                code.append(grid[cur_y][cur_x])

        return code