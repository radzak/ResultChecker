import numpy as np


class Stick:
    def __init__(self):
        self.stick_start = []
        self.stick_end = []

    def set_coordinates(self, i):
        i += 1
        start_x = int(input("Podaj współrzedną x początku {0}. bierki: ".format(i)))
        start_y = int(input("Podaj współrzedną y początku {0}. bierki: ".format(i)))
        end_x = int(input("Podaj współrzedną x końca {0}. bierki: ".format(i)))
        end_y = int(input("Podaj współrzedną y końca {0}. bierki: ".format(i)))

        self.stick_start = [start_x, start_y]
        self.stick_end = [end_x, end_y]


def det(stick_start, stick_end, point_cords):
    matrix = [
        [stick_start[0], stick_start[1], 1],
        [stick_end[0], stick_end[1], 1],
        [point_cords[0], point_cords[1], 1],
    ]
    return np.linalg.det(np.array(matrix))


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


def collect_all_sticks():
    L = int(input("Podaj liczbę bierek: "))
    sticks = []

    for i in range(L):
        stick = Stick()
        stick.set_coordinates(i)
        sticks.append(stick)

    return sticks


def bierki():
    sticks = collect_all_sticks()

    while True:
        stick1_index = int(input()) - 1
        stick2_index = int(input()) - 1

        if [stick1_index, stick2_index] == [-1, -1]:
            break

        p = sticks[stick1_index].stick_start
        q = sticks[stick1_index].stick_end
        a = sticks[stick2_index].stick_start
        d = sticks[stick2_index].stick_end
        print("TRUE") if two_secments_cut(p, q, a, d) else print("FALSE")


def main():
    bierki()


if __name__ == '__main__':
    main()
