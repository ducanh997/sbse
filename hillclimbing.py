import random


def init_solution(mat):
    """
    Initialize a random candidate solution
    :param mat:
    :return: Random init solution
    """
    cities = list(range(len(mat)))
    random.shuffle(cities)
    return cities


def calculate_route_length(mat, solution):
    """
    For example, if mat is
        [0, 400],
        [400, 0]

    and solution is [0, 1]
    then this function should return 400 (0 -> 1) + 400 (1 -> 0) = 800

    :param mat: Edge matrix
    :param solution: A  solution
    :return: Distance if this solution is 
    """
    result = 0
    for i in range(len(solution)):
        result += mat[solution[i - 1]][solution[i]]
    return result


def generate_neighbours(solution):
    result = []
    for i in range(len(solution) - 1):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            result.append(neighbour)
    return result


def get_best_neighbour(mat, neighbours):
    best_route_length = calculate_route_length(mat, neighbours[0])
    best_neighbour = neighbours[0]
    for neighbour in neighbours:
        current_route_length = calculate_route_length(mat, neighbour)
        if current_route_length < best_route_length:
            best_route_length = current_route_length
            best_neighbour = neighbour
    return best_neighbour, best_route_length


def hill_climbing(mat):
    current_solution = init_solution(mat)
    print(f'Init solution: {current_solution}')
    current_route_length = calculate_route_length(mat, current_solution)

    neighbours = generate_neighbours(current_solution)
    best_neighbour, best_neighbour_route_length = get_best_neighbour(mat, neighbours)

    while best_neighbour_route_length < current_route_length:
        current_solution = best_neighbour
        current_route_length = best_neighbour_route_length
        neighbours = generate_neighbours(current_solution)
        best_neighbour, best_neighbour_route_length = get_best_neighbour(mat, neighbours)

    return current_solution, current_route_length


def generate_mat(n_city):
    result = []
    for i in range(n_city):
        distances = []
        for j in range(n_city):
            if j == i:
                distances.append(0)
            elif j < i:
                distances.append(result[j][i])
            else:
                distances.append(random.randint(10, 1000))
        result.append(distances)
    return result


def print_mat(mat):
    print('Adjacency matrix:')
    for row in mat:
        print(row)


if __name__ == '__main__':
    mat = generate_mat(10)
    print_mat(mat)

    print('_________________________')
    for i in range(10):
        solution, length = hill_climbing(mat)
        print(f'Result: {solution}, length: {length}')
