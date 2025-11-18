from unittest import TestCase

from Entitati.ProblemaLaborator import ProblemaLaborator


class TestProblemaLaborator(TestCase):
    def test_get_numar_laborator(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        assert l1.get_numar_laborator() == 1

    def test_get_numar_problema(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        assert l1.get_numar_problema() == 1

    def test_get_descriere(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        assert l1.get_descriere() == "Introducere"

    def test_get_deadline(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        assert l1.get_deadline() == "11.10.2025"

    def test_set_numar_laborator(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        l1.set_numar_laborator(2)
        assert l1.get_numar_laborator() == 2

    def test_set_numar_problema(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        l1.set_numar_problema(2)
        assert l1.get_numar_problema() == 2

    def test_set_descriere(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        l1.set_descriere("Problema 2")
        assert l1.get_descriere() == "Problema 2"

    def test_set_deadline(self):
        l1 = ProblemaLaborator(1, 1, "Introducere", "11.10.2025")
        l1.set_deadline("12.12.1015")
        assert l1.get_deadline() == "12.12.1015"
