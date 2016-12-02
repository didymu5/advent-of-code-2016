# call parse_coords('coord string') to get the result
def parse_coords(in_coords):
    # initialize the data
    x_coord = 0
    y_coord = 0
    cur_direction = "N"

    # information about parsing
    coord_list = [x.strip() for x in in_coords.split(',')]

    cartesian_list = [(0,0)]
    for coord in coord_list:
        cartesian_list += create_long_path(x_coord, y_coord, coord, cur_direction)
        moved_output = move_coords(x_coord, y_coord, coord, cur_direction)
        x_coord = int(moved_output[0])
        y_coord = int(moved_output[1])
        cur_direction = moved_output[2]
    return abs(x_coord) + abs(y_coord), find_duplicates(cartesian_list)


def create_long_path(xcord, ycord, coord, direction):
    # information
    directions = ['N', 'E', 'S', 'W']
    x_coord = xcord
    y_coord = ycord
    path_list = []
    directions_index = directions.index(direction)
    new_dir = direction
    num_steps = int(coord[1:])

    if coord[0] == "R":
        try:
            new_dir = directions[directions_index + 1]

        except IndexError:
            new_dir = directions[0]

    else:
        try:
            new_dir = directions[directions_index - 1]

        except IndexError:
            new_dir = directions[-1]

    if new_dir == 'N':
        for i in range(1, num_steps+1):
            path_list.append((x_coord, y_coord+i))
        y_coord += num_steps

    elif new_dir == 'S':
        for i in range(1, num_steps+1):
            path_list.append((x_coord, y_coord-i))
        y_coord -= num_steps

    elif new_dir == 'E':
        for i in range(1, num_steps+1):
            path_list.append((x_coord+i, y_coord))
        x_coord += num_steps

    else:
        for i in range(1, num_steps+1):
            path_list.append((x_coord-i, y_coord))
        x_coord -= num_steps

    return path_list


# returns the first duplicate in the list
def find_duplicates(input_list):
    dup_set = set([x for x in input_list if input_list.count(x) > 1])
    dup_dict = {}

    for coords in dup_set:
        dup_dict[input_list.index(coords)] = coords

    dup_coords = dup_dict[min(list(dup_dict.keys()))]
    print(dup_dict)
    return abs(dup_coords[0]) + abs(dup_coords[1])


def move_coords(xcord, ycord, coord, direction):
    # information
    directions = ['N', 'E', 'S', 'W']
    x_coord = xcord
    y_coord = ycord
    directions_index = directions.index(direction)
    new_dir = direction
    num_steps = int(coord[1:])

    if coord[0] == "R":
        try:
            new_dir = directions[directions_index + 1]

        except IndexError:
            new_dir = directions[0]

    else:
        try:
            new_dir = directions[directions_index - 1]

        except IndexError:
            new_dir = directions[-1]

    if new_dir == 'N':
        y_coord += num_steps

    elif new_dir == 'S':
        y_coord -= num_steps

    elif new_dir == 'E':
        x_coord += num_steps

    else:
        x_coord -= num_steps

    return [x_coord, y_coord, new_dir]
