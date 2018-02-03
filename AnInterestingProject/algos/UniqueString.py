class UniqueString:
    def isUinque(self, the_string):
        if len(the_string) < 2: return True
        for letter in the_string:
            hits = 0
            for check in the_string:
                if letter == check: hits += 1
                if hits > 1: return False
        return True


print(UniqueString().isUinque('a'))
print(UniqueString().isUinque('aa'))
print(UniqueString().isUinque('aab'))
print(UniqueString().isUinque('baa'))
print(UniqueString().isUinque('akjwebfkw'))
print(UniqueString().isUinque('qwrjhgfds'))
