
def solve_part_one(map_data: str) -> int:
    directions, *cords = map_data.split("\n")
    cords_map = {}
    for cord in cords:
        if cord:
            split = cord.split(" = ")
            cords_map[split[0]] = (list(map(str, split[1].removeprefix('(').removesuffix(")").split(', '))))
    steps = 0
    last_pos = ''

    index = 0
    while index < len(directions):
        if steps == 0:
            lookup = cords_map["AAA"]
        else:
            lookup = cords_map[last_pos]

        if directions[index] == "R":
            next = lookup[1]
        if directions[index] == "L":
            next = lookup[0]

        last_pos = next



        steps += 1

        if last_pos == "ZZZ":
            break
        
        if (index == len(directions) - 1):
            index = 0
            continue
        else:
            index += 1
    return steps

def solve_part_two(map_data: list) -> int:
    directions, *cords = map_data.split("\n")
    cords_map = {}
    for cord in cords:
        if cord:
            split = cord.split(" = ")
            cords_map[split[0]] = (list(map(str, split[1].removeprefix('(').removesuffix(")").split(', '))))
    steps = 0


    starting_nodes = [key for key, value in cords_map.items() if key[-1] == "A"]


    index = 0
    current_nodes = []
    while index < len(directions):

        current_nodes = []
        for node in starting_nodes:
            lookup = cords_map[node]
            if directions[index] == "R":
                next = lookup[1]
            if directions[index] == "L":
                next = lookup[0]

            current_nodes.append(next)


        check = 0
        for node in current_nodes:
            if node[-1] == "Z":
                check += 1
        
        if check == len(current_nodes):
            steps += 1
            break


        starting_nodes = []
        starting_nodes.extend(current_nodes)


        new_count = 0


        steps += 1

        for new_node in current_nodes:
            if new_node[-1] == 'Z':
                new_count += 1

        if (index == len(directions) - 1):
            index = 0
            continue
        else:
            index += 1

        


    
    return steps



if __name__ == "__main__":
    with open('input.txt', 'r') as cords:
        map_data = cords.read()
        # assert solve_part_one(map_data) == 16343
        # assert solve_part_two(race_data) == 34454850
        # print(solve_part_one(map_data))
        print(solve_part_two(map_data))
