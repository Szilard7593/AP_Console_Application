from unittest import TestCase

from Entitati.Nota import Nota
from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student


class TestNota(TestCase):
    def test_get_nota(self):
        s = Student(1, "Mihai", 321)
        p = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        s1 = Nota(s, p, 1)
        assert s1.get_nota() == 1
        assert s1.get_student() == s
        assert s1.get_problema_lab() == p
        assert s1.get_student_id() == 1
        assert s1.get_nume() == "Mihai"
        assert s1.get_grupa() == 321


    def test_set_nota(self):
        s = Student(1, "Mihai", 321)
        p = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        s1 = Nota(s, p, 1)
        s1.set_nota(2)
        assert s1.get_nota() == 2

    def test_get_student(self):
        s = Student(1, "Mihai", 321)
        p = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        s1 = Nota(s, p, 1)
        assert s1.get_student() == s
        assert s1.get_student_id() == 1
        assert s1.get_nume() == "Mihai"

    def test_get_problema_lab(self):
        s = Student(1, "Mihai", 321)
        p = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        s1 = Nota(s, p, 1)
        assert s1.get_problema_lab() == p

    def test_set_student(self):
        s = Student(1, "Mihai", 321)
        p = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        s3 = Student(3, "Ana", 456)
        s1 = Nota(s, p, 1)
        s1.set_student(s3)
        assert s1.get_student() == s3

    def test_set_problema_lab(self):
        s = Student(1, "Mihai", 321)
        p = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        q = ProblemaLaborator(1, 2, "Problema 2", "12.12.1015")
        s1 = Nota(s, p, 1)
        s1.set_problema_lab(q)
        assert s1.get_problema_lab() == q

    def test_get_student_id(self):
        s = Student(1, "Mihai", 321)
        p = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        s1 = Nota(s, p, 1)
        assert s1.get_student_id() == 1

    def test_get_nume(self):
        s = Student(1, "Mihai", 321)
        p = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        s1 = Nota(s, p, 1)
        assert s1.get_nume() == "Mihai"

    def test_get_grupa(self):
        s = Student(1, "Mihai", 321)
        p = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        s1 = Nota(s, p, 1)
        assert s1.get_grupa() == 321
