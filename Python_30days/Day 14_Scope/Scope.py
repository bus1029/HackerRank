from itertools import combinations

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        # combs = list(set(combinations(self.__elements, 2)))
        # diffs = [abs(a-b) for (a, b) in combs]
        # self.maximumDifference = max(diffs)
        diffs = []

        for i in range(len(self.__elements)):
            for j in range(i+1, len(self.__elements)):
                diffs.append(abs(self.__elements[i] - self.__elements[j]))

        self.maximumDifference = max(diffs)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)