import random


neighbours = (
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
)


def get_random_generation(columns, rows):
    result = []
    for outer_index in range(rows):
        inner_list = []
        for inner_index in range(columns):
            inner_list.append(random.choice((True, False)))
        result.append(inner_list)
    return result


def compose_out(a_list):
    return "".join(["#" if alive else "." for alive in a_list])


def draw(world):
    for a_list in world:
        print(compose_out(a_list))


def offset(value, limit):
    if value in range(limit):
        return value
    elif value < 0:
        return value + limit
    else:
        return value - limit


def count_alive_neighbours(ancestry, cell_x, cell_y):
    y_limit, x_limit = len(ancestry), len(ancestry[0])
    count = 0
    for neighbour in neighbours:
        x = offset(cell_x + neighbour[0], x_limit)
        y = offset(cell_y + neighbour[1], y_limit)
        if ancestry[y][x]:
            count += 1
    return count


def get_next_generation(ancestry):
    next_generation = []
    for y, a_list in enumerate(ancestry):
        new_inner = []
        for x, alive in enumerate(a_list):
            alive_neighbours_count = count_alive_neighbours(ancestry, x, y)
            if alive and alive_neighbours_count not in (2, 3):
                new_inner.append(False)
            elif not alive and alive_neighbours_count == 3:
                new_inner.append(True)
            else:
                new_inner.append(alive)
        next_generation.append(new_inner)
    return next_generation


if __name__ == '__main__':
    width, height, steps = 20, 10, 20
    generation = get_random_generation(width, height)
    print("draw initial generation")
    draw(generation)
    for index in range(steps):
        print("draw generation #{}".format(index + 1))
        generation = get_next_generation(generation)
        draw(generation)