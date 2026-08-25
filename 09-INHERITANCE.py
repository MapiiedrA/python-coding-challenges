"""
Inheritance Exercise
"""

# Superclasses

class Animal:

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass


# Subclasses

class Dog(Animal):

    def sound(self):
        print("Woof!")

class Cat(Animal):

    def sound(self):
        print("Meow!")

def print_sound(animal: Animal):
    animal.sound()

my_animal = Animal("Animal")
my_animal.sound()
my_dog = Dog("Dog")
print_sound(my_dog)
my_cat = Cat("Cat")
print_sound(my_cat)

"""
EXTRA CHALLENGE
* Implement the hierarchy of a software development company composed of Employees 
 * who can be Managers, Project Managers, or Programmers.
 * Each employee has an ID and a name.
 * Depending on their role, they have properties and functions exclusive to their 
 * activity, and store the employees reporting to them.
 """

class Employee:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)
    
class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} is coordinating all company projects.")

class ProjectManager(Employee):

    def __init__(self, id, name, project):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} is coordinating their project.")

class Programmer(Employee):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}")

    def add(self, employee: Employee):
        print(
            f"A programmer has no employees reporting to them. {employee.name} will not be added.")

my_manager = Manager(1, "MapiDev")
my_project_manager = ProjectManager(2, "Mauricio", "Project 1")
my_project_manager2 = ProjectManager(3, "Brais", "Project 2")
my_programmer = Programmer(4, "MoureDev", "Python")
my_programmer2 = Programmer(5, "Ros", "Swift")
my_programmer3 = Programmer(6, "Bushi", "Kotlin")
my_programmer4 = Programmer(7, "Nasos", "Bash")

my_manager.add(my_project_manager) 
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2)

my_programmer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()