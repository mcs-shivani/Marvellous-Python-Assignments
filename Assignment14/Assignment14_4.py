
class Student :
    School_Name = "SJV"

    def __init__(self , A, B):
        self.roll_no = A
        self.name = B

    def Display(self):
        print("School Name : "+Student.School_Name)
        print("Roll No : ", self.roll_no)
        print("Name : "+self.name)
    
    @classmethod
    def setSchoolName(cls, new_school_name):
        Student.School_Name = new_school_name
        print("Updated School Name : "+new_school_name)

def main():
    Obj1 = Student(101 , "Ashish")
    Obj1.Display()
    Obj1.setSchoolName("Kanya")
    Obj1.Display()

if __name__ == "__main__":
    main()