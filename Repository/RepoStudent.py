class RepoStudent:
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def getStudents(self):
        return self.students

    def getAllStudents(self):
        return list(self.students)

    def getStudentById(self, id):
        for student in self.students:
            if student.student_id == id:
                return student
        return None

    def getStudentByName(self, name):
        for student in self.students:
            if student.name == name:
                return student

    def deleteStudent(self, id):
        for student in self.students:
            if student.student_id == id:
                self.students.remove(student)
                return True
        return False

    def updateStudent(self, student_id, name, grupa):
        for student in self.students:
            if student.student_id == id:
                student.name = name
                student.grupa = grupa

    def getStudentCount(self):
        return len(self.students)

    def getStudentByAge(self, age):
        students = []

    def getStudentByGrade(self, grade):
        students = []




