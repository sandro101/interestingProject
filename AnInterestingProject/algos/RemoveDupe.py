# Assume we do care about order, otherwise just convert it to a set and then back to a string
# This implementation is a very bad idea given that it is updating the list which was initially
# used to set the parameters
class RemoveDupe:
    def remove(self, the_string):
        if len(the_string) < 2: return the_string
        initial_len = len(the_string)
        removed = 0
        for ipos in range(initial_len):
            for jpos in range(initial_len):
                if ipos >= jpos: continue;
                if the_string[ipos - removed] == the_string[jpos - removed]:
                    the_string.pop(ipos - removed)
                    removed += 1
                    break
        return the_string


print(RemoveDupe().remove(list('a')) == list('a'))
print(RemoveDupe().remove(list('aa')) == list('a'))
print(RemoveDupe().remove(list('aaab')) == list('ab'))
print(RemoveDupe().remove(list('baaab')) == list('ab'))
print(RemoveDupe().remove(list('bacaabc')) == list('abc'))
print(RemoveDupe().remove(list('badcdadabc')) == list('dabc'))
print(RemoveDupe().remove(list('ebadcdadabc')) == list('edabc'))
