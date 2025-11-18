from unittest import TestCase

from Repository.RepoStudent import RepoStudent
from Service.serviceStudent import serviceStudent


class TestserviceStudent(TestCase):
    def test_adauga_student(self):
        repo = RepoStudent()
        s2erviceStudent = serviceStudent(repo)
        s2erviceStudent.adauga_student(1,"Mihai",1)
        toti = s2erviceStudent.get_toti_studentii()
        assert len(toti) == 1

    def test_sterge_student(self):
        #Incercam sa stergem ceva inexistent
        repo = RepoStudent()
        s2erviceStud = serviceStudent(repo)
        s2erviceStud.sterge_student(3)
        toti = s2erviceStud.get_toti_studentii()

        assert len(toti) == 0

        #Stergem un student actual din repo
        s2erviceStud.adauga_student(1, "John",3)
        s2erviceStud.sterge_student(1)
        n = s2erviceStud.get_toti_studentii()

        assert len(n) == 0

    def test_cauta_student(self):
        repo = RepoStudent()
        s2erviceStudent = serviceStudent(repo)
        s2erviceStudent.adauga_student(1, "Mihai", 1)
        student2 = s2erviceStudent.cauta_student(1)
        assert student2.get_student_id() == 1
        assert student2.get_nume() == "Mihai"
        assert student2.get_grupa() == 1

    def test_update_student(self):
        repo = RepoStudent()
        s2erviceStudent = serviceStudent(repo)
        s2erviceStudent.adauga_student(1, "Mihai", 1)
        s2erviceStudent.update_student(1, "Ana", 2)
        student2 = s2erviceStudent.cauta_student(1)
        assert student2.get_student_id() == 1
        assert student2.get_nume() == "Ana"
        assert student2.get_grupa() == 2
