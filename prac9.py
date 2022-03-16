# 20ce147_prac9

#Aim :Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. The Student class has data members such as those representing rollNumber, Name, etc. Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects. Derive Result from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this relationship.

class Student:
    def __init__(self):  
        self.name = ""
        self.rollNo = 0

    def take_student_data(self): 
        self.name = input("Enter the name of student : ")
        print("Enter the roll number of", self.name, ": ", end="")
        self.rollNo = input()

    def student_data(self):  
        print("\nStudent name :", self.name)
        print("Roll number  :", self.rollNo)


class Exam(Student):  
    def __init__(self):  
        Student.__init__(self)
        self.arr = []

    def take_input(self): 
        for i in range(0, 6):
            print("Enter the marks of subject", i + 1, ":", end=" ")
            n = int(input())
            self.arr.append(n)

    def print_data(self):  
        print(self.name,"'s marks are ", end="")
        print(self.arr)


class Result(Exam):  
    def __init__(self):  
        Exam.__init__(self)
        self.total_marks = 0

    def calculate_avg(self): 
        self.check = True
        for i in range(0, 6):
     
            self.total_marks = self.total_marks + self.arr[i]

        if (self.check):
            print("Total marks:", self.total_marks)
            print(self.name, "Percentage:", self.total_marks / 6, "%")


st = Student()
exam = Exam()
result = Result()

result.take_student_data()
result.take_input()

result.student_data()
result.print_data()
result.calculate_avg()