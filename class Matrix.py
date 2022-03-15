a = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
b = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]

class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str,c))
        return Matrix

matrixa = Matrix(a)
matrixb = Matrix(b)

print(matrixa, '\n')
print(matrixb, '\n')
print(matrixa + matrixb)
