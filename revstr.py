class class_reverse:

    def __init__(self,s):
        self.s = s

    def reverse_word(self):
        return self.s[::-1]
    
str= input("Enter the word to be reversed :")
revobj =  class_reverse(str)

print(f"reversed string :{revobj.reverse_word()}")