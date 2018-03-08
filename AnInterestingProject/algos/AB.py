import math


class AB:

    def createString(self, N, K):
        if (N / 2) ** 2 < K:
            return ""
        solution = ["B" for i in range(0, int(math.ceil(N / 2)))] + ["A" for i in range(0, N - int(math.ceil(N / 2)))]
        while True:
            if self._check(solution, K):
                return "".join(solution)
            else:
                solution = self._shiftB(solution)

    def _check(self, solution, K):
        counter = 0
        for pos, char in enumerate(solution):
            if counter == K:
                return True
            if char == "A":
                if pos + 1 >= len(solution):
                    return False
                for i in range(pos + 1, len(solution)):
                    if solution[i] == "B":
                        counter += 1

    def _shiftB(self, solution):
        for pos, char in enumerate(solution):
            if char == "B":
                if (pos + 1 < len(solution)) & (solution[pos + 1] == "A"):
                    solution[pos] = "A"
                    solution[pos + 1] = "B"
                    return solution

a = AB()
print(a.createString(3, 2))