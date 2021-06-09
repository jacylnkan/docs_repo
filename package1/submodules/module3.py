class Person:
    """Person superclass.
    """
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        """Prints the person's first and last name.
        """
        print(self.firstname, self.lastname)

class Student(Person):
    """Student subclass.

    Args:
        Person (Person): A person.
    """
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        """Prints a welcome statement for the student.
        """
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
