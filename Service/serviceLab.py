from Entitati.ProblemaLaborator import ProblemaLaborator


class ServiceLab:
    def __init__(self,RepoLab):
        self.RepoLab = RepoLab

    def adauga_problema(self, numar_lab,numar_problema, descriere, deadline):
        problema = ProblemaLaborator(numar_lab,numar_problema, descriere, deadline)
        self.RepoLab.addLab(problema)

    def sterge_problema(self, numar_lab,numar_problema):
        self.RepoLab.deleteLab(numar_lab,numar_problema)

    def get_toate_problemele(self):
        return self.RepoLab.getLabs()

    def cauta_problema(self, numar_lab:int):
        problema = self.RepoLab.find_by_id(numar_lab)
        return problema

    def update_problema(self, numar_lab, numar_problema ,descriere, deadline):
        self.RepoLab.updateLab(numar_lab,numar_problema, descriere, deadline)