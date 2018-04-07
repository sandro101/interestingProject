from collections import Counter
# (u,v), (v,w), and (w,u) - makes a triangle


class TriangleEasy:
    def find(self, a, b):
        if len(a) == 0:
            return 3
        pos_a = {v for k, v in Counter(a).items() if v >= 2}
        pos_b = {v for k, v in Counter(b).items() if v >= 2}
        if len(pos_a) == 0 and len(pos_b) == 0:
            return 2

        if self._can_form_triangle(pos_a, a, b) or self._can_form_triangle(pos_b, b, a):
            return 0
        else:
            return 1

    @staticmethod
    def _can_form_triangle(ns_that_may_form_tri, a, b):
        connected = set(zip(a, b))
        for n in ns_that_may_form_tri:
            pos_of_ns_that_may_form_tri = {i: v for i, v in enumerate(a) if v == n}
            pos_of_ns_connected_to_ns_that_may_form_tri = {b[k] for k, v in pos_of_ns_that_may_form_tri.items()}
            for connection in connected:
                n1, n2 = connection
                if n1 in pos_of_ns_connected_to_ns_that_may_form_tri and n2 in pos_of_ns_connected_to_ns_that_may_form_tri:
                    return True
            return False


a = [16,4,15,6,1,0,10,12,7,15,2,4,8,1,10,15,13,10,1,16,3,19,8,7,13,1,15,15,15,5,16,7,5,6,4,18,3,8,6,2,16,8,19,14,17,16,4,6,9,17,4,10,8,12,2,3,18,9,13,17,4,7,10,0,13,11,15,17,11,15,11,19,19,4,10,14,16,6,3,17,1,4,14,9,7,18,10,11,5,0,5,9,9,7,16,12,4,10,17,3]
b = [17,18,6,16,18,6,11,2,15,10,1,15,17,8,5,9,7,0,0,4,16,1,9,0,9,5,17,14,1,12,14,11,9,18,0,12,11,3,19,14,7,6,3,19,0,1,19,5,11,19,2,13,12,0,6,2,14,16,14,18,5,5,19,3,6,14,12,5,17,3,1,12,7,11,8,8,10,11,13,2,13,13,0,18,2,7,2,12,14,9,3,19,2,8,12,13,8,18,13,18]
print(TriangleEasy().find(a, b))

a = [0,2,1,2]
b = [3,0,2,3]
print(TriangleEasy().find(a, b))
