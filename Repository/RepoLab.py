class RepoLab:
    def __init__(self):
        self.labs = []

    def addLab(self, lab):
        self.labs.append(lab)

    def getLabs(self):
        return list(self.labs)

    def getLabById(self, id):
        for lab in self.labs:
            if lab.id == id:
                return lab


    def getLabByName(self, name):
        for lab in self.labs:
            if lab.name == name:
                return lab

    def deleteLab(self, numar_laborator: int , numar_problrma: int):
        for lab in self.labs:
            if lab.numar_laborator == numar_laborator and lab.numar_problrma == numar_problrma:
                self.labs.remove(lab)
                return True
        return False

    def updateLab(self, numar_laborator: int , numar_problema: int, description: str, deadline: str):
        for lab in self.labs:
            if lab.numar_laborator == numar_laborator and lab.numar_problema == numar_problema:
                lab.description = description
                lab.deadline = deadline

    def getLabCount(self):
        return len(self.labs)

    def getLabByGrade(self, grade):
        labs = []

    def getLabByDeadline(self, deadline):
        labs = []

    def find_by_id(self,numar_laborator: int):
        for lab in self.labs:
            if lab.numar_laborator == numar_laborator:
                return (lab)
        return None

