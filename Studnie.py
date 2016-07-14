import numpy as np
import itertools


class Path:
    def __init__(self):
        self.path_start = []
        self.path_end = []

    def set_coordinates(self, i):
        i += 1
        start_x = int(input())
        start_y = int(input())
        end_x = int(input())
        end_y = int(input())

        self.path_start = [start_x, start_y]
        self.path_end = [end_x, end_y]


def det(path_start, path_end, point_cords):
    matrix = [
        [path_start[0], path_start[1], 1],
        [path_end[0], path_end[1], 1],
        [point_cords[0], point_cords[1], 1],
    ]
    return np.linalg.det(np.array(matrix))


def collect_all_paths():
    L = int(input())
    paths = []

    for i in range(L):
        path = Path()
        path.set_coordinates(i)
        paths.append(path)

    return paths


def two_secments_cut(p, q, a, d):
    return (np.sign(det(p, q, d)) != np.sign(det(p, q, a)) and
            np.sign(det(a, d, p)) != np.sign(det(a, d, q)) or

            np.sign(det(p, q, a)) == 0 and
            p[0] <= a[0] <= q[0] and
            p[1] <= a[1] <= q[1] or

            np.sign(det(p, q, d)) == 0 and
            p[0] <= d[0] <= q[0] and
            p[1] <= d[1] <= q[1] or

            np.sign(det(a, d, p)) == 0 and
            a[0] <= p[0] <= d[0] and
            a[1] <= p[1] <= d[1] or

            np.sign(det(a, d, q)) == 0 and
            a[0] <= q[0] <= d[0] and
            a[1] <= q[1] <= d[1])


def studnie():
    paths = collect_all_paths()
    counter = 0

    # print(paths)
    combinations = list(itertools.combinations(paths, 2))

    for combination in combinations:
        p = combination[0].path_start
        q = combination[0].path_end
        a = combination[1].path_start
        d = combination[1].path_end

        if two_secments_cut(p, q, a, d):
            counter += 1

    print(counter)


def main():
    studnie()

main()
