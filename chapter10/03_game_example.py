
'''
isLeftPressed kasaree kaam garirako chha tyo dekhnu jarurat hunna meaning its abstraction and 
Player ko sabai function player maa gayo Remote kaa sabai functions aafno Remote maa hunchha teslai encaptulation bhanchha
# '''
class Remote:
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
    def moveButtom(self):
        pass

player1 = Player()
remote1 = Remote()
if(remote1.isLeftPressed()): 
    player1.moveLeft()


'''
Modeling a broblem in OOPs
We define the following in our problem

Noun ->         Class       -> Employee
Adjective ->    Attribute   -> name, age, salary
Verbs ->        Method      -> work(), getPaid()


'''