import math


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


class vector:
    vec = []

    def __init__(self, k):
        self.vec = k
        self.num = len(self.vec)

    def __add__(self, vector2):
        try:
            if len(self.vec) != len(vector2.vec):
                raise MyError("Error in add!")
            ret = []
            for j in range(len(self.vec)):
                ret.append(self.vec[j] + vector2.vec[j])
            return vector(ret)
        except MyError as mr:
            print(mr)

    def __sub__(self, vector2):
        ret = []
        try:
            if len(self.vec) != len(vector2.vec):
                raise MyError("Error in sub!")
            
            for j in range(len(self.vec)):
                ret.append(self.vec[j] - vector2.vec[j])
            return vector(ret)
        except MyError as mr:
            print(mr)

    def __mul__(self, cons):
        ret = []
        for j in range(len(self.vec)):
            ret.append(self.vec[j] * cons)
        return vector(ret)

    @staticmethod
    def scalar(vector1, vector2):
        try:
            if len(vector1.vec) != len(vector2.vec):
                raise MyError("Wrong vectors in scalar!")
            ret = 0
            for j in range(len(vector1.vec)):
                ret += vector1.vec[j] * vector2.vec[j]
            return ret
        except MyError as mr:
            print(mr)

    def __eq__(self, vector2):
        if len(self.vec) != len(vector2.vec):
            return False
        j = 0
        for i in self.vec:
            if i != vector2.vec[j]:
                return False
            j += 1
        return True

    def __getitem__(self, index):
        try:
            if len(self.vec) <= index:
                raise MyError("Wrong index!")
            j = 0
            for i in self.vec:
                if j == index:
                    return i
                j += 1
        except MyError as mr:
            print(mr)

    def __str__(self):
        s = ""
        for i in self.vec:
            s += str(i) + ','
        s = s[:len(s) - 1]
        return s

    def len(self):
        temp = 0
        for j in range(len(self.vec)):
            temp += self.vec[j] ** 2
        ret = math.sqrt(temp)
        return ret

    def __len__(self):
        return self.num

