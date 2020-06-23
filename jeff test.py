''' This program demonstrates how to use classes and objects. '''

class Enemy:
    ''' The enemy class has life, name and functions that do something. '''

    def __init__(self, name, life):
        ''' The init function runs on instaantiation and sets up all attributes'''
        self._life = life
        self._name = name
        #add new enemy object
        enemy_list.append(self)
        
    #make a get function for all attributes
    def get_name(self):
        return self._name

    def get_life(self):
        ''' This function returns the amount of life remaining '''

        return self._life

    

    def attacked(self):
        '''this function subtracts 1 from the objects health. '''
        print("ouch")
        self._life -= 1


def show_all():
    ''' This function displays details of all enemies. '''
    #for i in range
    for enemy in enemy_list:
        print(enemy.get_name(), enemy.get_life())

def life_check():
    health = int(input("how much health: "))
    for enemy in enemy_list:
        if enemy.get_life() >= health:
            print(enemy.get_life(),enemy.get_name())

def create_enemy():
    ''' This function allows the user to create a new enemy, entering the name
    life for it '''
    new_name = input("name: ")
    new_life = int(input("life: "))
    #create the new enemy object
    Enemy(new_name, new_life)


#the enemy_list stores all enemy objects
enemy_list = []


#create an enenmy object and store in variable called enemy1
enemy1 = Enemy("gaming addiction", 20)
enemy2 = Enemy("Alchoholism", 50)
enemy1.attacked()


#call the get life function and print out the life
print(enemy1.get_life(),enemy1.get_name())

create_enemy()
show_all()
