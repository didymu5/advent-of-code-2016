# use cartesian coordinates

grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

def less_one(in_var):
        if in_var - 1 < 0:
                return in_var
        else:
                return in_var - 1


def more_one(in_var):
        if in_var + 1 > 2:
                return in_var
        else:
                return in_var+1

def find_number(cur_x, cur_y, line_dir):
        out_x = cur_x
        out_y = cur_y
        for let in line_dir:
                if let == 'L':
                        out_x = less_one(out_x)
                elif let == 'R':
                        out_x = more_one(out_x)
                elif let == 'U':
                        out_y = less_one(out_y)
                else:
                        out_y = more_one(out_y)
        return (out_x, out_y)


def find_code(input_str):
        cur_x = 1
        cur_y = 1
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