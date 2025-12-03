from unittest import TestCase

from Repository.RepoLab import RepoLab
from Service.serviceLab import ServiceLab

class TestServiceLab(TestCase):
    def setUp(self):
        r = RepoLab()
        self.s = ServiceLab(r)
        self.s.adauga_problema(1, 1, "Introducere", "11.10.2025")

    def test_adauga_problema(self):
        self.assertEqual(self.s.get_toate_problemele()[0].get_descriere(), "Introducere")

    def test_sterge_problema(self):
        self.s.sterge_problema(1)
        self.assertEqual(self.s.get_toate_problemele(), [])

    def test_get_toate_problemele(self):
        pass

    def test_cauta_problema(self):
        pass

    def test_update_problema(self):
        pass
