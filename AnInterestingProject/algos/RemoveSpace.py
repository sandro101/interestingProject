class RemoveSpace:
    def remove(self, the_string):
        return the_string.replace(' ', '%20')


print(RemoveSpace().remove('a a') == 'a%20a')
print(RemoveSpace().remove('a a b') == 'a%20a%20b')
print(RemoveSpace().remove(' a a b') == '%20a%20a%20b')
