#assuming same word is not strictly a rotation, so false
class WordRotation:
    def isRotation(self, the_string, rotation):
        if len(the_string) != len(rotation): return False
        for i, val in enumerate(the_string):
            match = rotation == the_string[-1*i:] + the_string[:len(the_string) - i]
            if match: return True
        return False
    
    def isSubstring(self, the_string, substring):
        return substring in the_string
          
print(WordRotation().isRotation('blahboo', 'booblah') == True);
print(WordRotation().isRotation('blahboo', 'ahboobl') == True);
print(WordRotation().isRotation('blahboo', 'booblah') == True);
print(WordRotation().isRotation('blahboo', 'blahboo') == False);
print(WordRotation().isRotation('blahboo', 'blah') == False);
print(WordRotation().isRotation('blahboo', 'booblhah') == False);
print(WordRotation().isRotation('blahboo', 'notsameword') == False);