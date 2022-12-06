class User:

    def login(self):
        print("Login")

    def reg(self):
        print("Register")


class Student(User):

    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")

class Instructor(User):

    def create_course(self):
        print("Create Course")

    def answer(self):
        print("Answer")
        
st1 = Student()

st1.enroll()
st1.login()
