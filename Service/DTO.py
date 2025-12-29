class NotaDTO:
    def __init__(self, nume_student, nota):
        self.__nume_student = nume_student
        self.__nota = nota

    #def get_nume(self):
       # return self.__nume_student

    #def get_nota(self):
        #return self.__nota

    def __str__(self):
        return f"Student: {self.__nume_student} | Nota: {self.__nota}"

class MediaDTO:
    def __init__(self, nume_student, media):
        self.__nume_student = nume_student
        self.__media = media

    #def get_nume(self):
        #return self.__nume_student

    def get_media(self):
        return self.__media

    def __str__(self):
        return f"Student: {self.__nume_student} | Media: {self.__media}"