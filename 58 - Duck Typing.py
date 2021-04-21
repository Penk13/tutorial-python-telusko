# 58 - DUCK TYPING

# “If it looks like a duck and quacks like a duck, it’s a duck”

# We dont care whether the object is a duck or not
# We only care if it behaves like a duck or not

class Duck:
    def fly(self):
        print("flap, flap, flap")
    def quack(self):
        print('quack, quack, quack')

class Human:
    def fly(self):
        print("im flapping my arms")
    def quack(self):
        print('im quacking like a duck')

for animal in (Duck(), Human()):
    animal.fly()
    animal.quack()
#Akan mengeksekusi duck dan human, tidak hanya duck
#Karena dalam duck typing, tidak peduli apa objeknya