import random

class Student:
    educational_platform = 'udemy'

    def __init__(self,name:str,age:int=18):
        self.name = name
        self.age = age

    def greet(self):
        greeting_list = ['hii,my name is {}',
                         'hello,my name is {}. Nice to meet you!',
                         'hey,my name is {} and i am {} years old'
                         ]
        greeting_size = len(greeting_list)
        selected_greet = greeting_list[random.randint(0,greeting_size - 1)]

        if 'years old' in selected_greet:
            print(selected_greet.format(self.name,self.age))

        else:
            print(selected_greet.format(self.name))

def class_creator(names:list) -> list:
    return [Student(name) for name in names]

if __name__ == '__main__':

    students = ['breno','bruno','neide','janio']

    for student in (class_creator(students)):
        student.greet()
