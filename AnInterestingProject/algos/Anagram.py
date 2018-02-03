#In reality just sort both strings and then check they are equal
class Anagram:
    def isAnagram(self, the_string, anagram):
        if len(the_string) != len(anagram): return False
        the_string = list(the_string)
        anagram = list(anagram)
        for letter in the_string:
            try:
                anagram.remove(letter)
            except ValueError:
                return False
        return True;
             
print(Anagram().isAnagram('a', 'a'));
print(Anagram().isAnagram('a', 'ab'));
print(Anagram().isAnagram('ba', 'ab'));
print(Anagram().isAnagram('aa', 'ab'));

