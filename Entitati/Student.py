class Student:
    def __init__(self,student_id:int , nume: str ,grupa: int):
        self.student_id = student_id
        self.nume = nume
        self.grupa = grupa

    def get_student_id(self):
        return self.student_id

    def get_nume(self):
        return self.nume

    def get_grupa(self):
        return self.grupa

    def set_student_id(self,student_id):
        self.student_id = student_id

    def set_nume(self,nume):
        self.nume = nume

    def set_grupa(self,grupa):
        self.grupa = grupa

    def __str__(self):
        return f"Student( ID: {self.student_id} , Nume: {self.nume} , Grupa: {self.grupa})"

    #reprezentare mai frumoasa
    def __repr__(self):
        return f"Student(student_id={self.student_id}, nume={self.nume}, grupa={self.grupa})"

