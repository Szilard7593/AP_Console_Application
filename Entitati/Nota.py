from Entitati.ProblemaLaborator import ProblemaLaborator
from Entitati.Student import Student


class Nota:
    def __init__(self,id_stud, numar_lab,nota:int):
        self.id_stud = id_stud
        self.numar_laborator = numar_lab
        self.nota = nota


    def getId(self):
        return self.id_stud
    
    def setId(self):
        self.id_stud = id_stud
        
    def get_nota(self):
        return self.nota

    def set_nota(self,nota):
        self.nota = nota
        
    def getLab(self):
        return self.numar_laborator
    
    def setLab(self):
        self.numar_laborator = numar_lab

    def __repr__(self):
        return f"Nota(student={self.id_stud},problemaLab={self.numar_laborator},nota={self.nota})"