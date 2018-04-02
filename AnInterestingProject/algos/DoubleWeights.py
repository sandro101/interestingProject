import sys
from AnInterestingProject.jcollection.stack import Stack


class DoubleWeights:
    @staticmethod
    def minimal_cost(self, weights1, weights2):
        weight1 = [[int(val) if val is not "." else sys.maxsize for val in row] for row in weights1]
        weight2 = [[int(val) if val is not "." else sys.maxsize for val in row] for row in weights2]

        sum1 = [sys.maxsize] * len(weight1)
        sum2 = [sys.maxsize] * len(weight1)
        stack = Stack((0, 0, 0, 0))

        while stack.hasNext():
            node, s1, s2, prev_node = stack.pop()
            test_path_cost = s1 * s2
            current_path_cost = sum1[node] * sum2[node]

            if test_path_cost < current_path_cost:
                sum1[node] = s1
                sum2[node] = s2
                print("From node: " + str(prev_node))
                print("To node: " + str(node) + " costs: " + str(test_path_cost))

                for next_node in reversed(range(len(weight1))):
                    # Add all possible moves and total cost including previous moves
                    stack.push((
                        next_node,
                        sum1[node] + weight1[node][next_node],
                        sum2[node] + weight2[node][next_node],
                        node,  # just for logging, not needed in algo
                    ))

        if sum1[-1] == sys.maxsize:  # conform to problem
            return -1

        return sum1[1] * sum2[1]


weights1 = ["..14", "..94", "19..", "44.."]
weights2 = ["..94", "..14", "91..", "44.."]
print(DoubleWeights().minimalCost(weights1, weights2))

weights1 = ["..", ".."]
weights2 = ["..", ".."]
print(DoubleWeights().minimalCost(weights1, weights2))
