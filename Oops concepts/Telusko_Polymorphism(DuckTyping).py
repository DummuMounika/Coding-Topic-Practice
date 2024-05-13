#Integerated development environment
#Duck Typing: the dynamic variable is utlize in each class

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")
class Myeditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")
class Laptop:
     def code(self,ide):
         ide.execute()


#ide =PyCharm()
ide= Myeditor()

lap1 = Laptop()
lap1.code(ide)

