#! /usr/bin/env python
class Matrix:
    def __init__(self, matrix_string):
        self.rows = [x.split(" ") for x in matrix_string.split("\n")]

    def row(self, index):
        return list(map(int, self.rows[index-1]))

    def column(self, index):
        return list(map(int, [row[index-1] for row in self.rows]))