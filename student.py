class Student:

    school_name = "Programming Pathshala"   # class variable

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("---------------------------------")
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print(f"Grade   : {self.calculate_grade()}")
        print("---------------------------------")

    @staticmethod
    def validate_marks(marks):
        return 0 <= marks <= 100