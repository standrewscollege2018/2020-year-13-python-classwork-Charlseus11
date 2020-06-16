''' This program demonstrates how to use classes and objects. '''

class Enemy:
    ''' The enemy class has life, name and functions that do something. '''

    def __init__(self, name, life):
        ''' The init function runs on instaantiation and sets up all attributes'''
        self._life = life
        self._name = name

    def get_name(self):
        return self._name

    def get_life(self):
        ''' This function returns the amount of life remaining '''

        return self._life

    

    def attacked(self):
        '''this function subtracts 1 from the objects health. '''
        print("ouch")
        self._life -= 1

#create an enenmy object and store in variable called enemy1
enemy1 = Enemy("gaming addiction", 20)
enemy2 = Enemy("Alchoholism", 50)
enemy1.attacked()
#call the get life function and print out the life
print(enemy1.get_life(),enemy1.get_name())
    
