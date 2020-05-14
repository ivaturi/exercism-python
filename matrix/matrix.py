#! /usr/bin/env python
class Matrix:
    def __init__(self, matrix_string):
        r, n = matrix_string.split("\n"), matrix_string.count("\n") + 1
        self.rows = [list(map(int, r[i].split(" "))) for i in range(0, n)]
        self.cols = list(map(list,zip(*self.rows)))

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.cols[index-1]

