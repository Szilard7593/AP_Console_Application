class RepoNota:
    def __init__(self):
        self.note = []

    def addNote(self, note):
        self.note.append(note)

    def getNote(self):
        return list(self.note)

    def getNoteById(self, note):
        for note in self.note:
            if note.note == note:
                return note

    def delete(self,id):
        for note in self.note:
            if note.student_id == id:
                self.note.remove(note)
                return True
            
    def getall(self):
        return list(self.note)
        