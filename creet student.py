class Student:

    def __init__(self, name, age, number, gender, tutor):

        self._name = name
        self._age = age
        self._number = number
        self._gender = gender
        self._tutor = tutor
        student_list.append(self)

    def get_name(self):
        return self._name

    def get_age(self):

        return self._age

    def get_number(self):
        return self._number

    def get_gender(self):
        return self._gender
    
    def get_tutor(self):
        return self._tutor
    
def show_all():
    ''' This function displays details of all enemies. '''
    for student in student_list:
        print(student.get_name(), student.get_age(), student.get_number(), student.get_gender(), student.get_tutor())
        create_student()


def create_student():
    new_name = input("name: ")
    new_age = int(input("age: "))
    new_number = int(input("number: "))
    new_gender = input("M or F: ")
    #while 
    #if new_gender = "M" or "F":
    new_tutor = input("What tutor are you in: ")
    Student(new_name, new_age, new_number, new_gender, new_tutor)
        
    #else:
        #print("Please reply with M or F")
        #new_gender = input("M or F: ")
        


 
student_list = []

create_student()

show_all()
