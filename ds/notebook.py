import datetime

last_id=0

class Note:
    def __init__(self,memo,tag=''):
        self.memo=memo
        self.tag=tag
        self.create_time=datetime.date.today()
        global last_id
        last_id+=1
        self.id=last_id
    
    def match(self, filters):
        return filters in self.memo or filters in self.tag

class Notebook:
    temp_value=10
    def lastid_info(self):
        global last_id
        print(last_id)

    def __init__(self):
        self.notes=[]
    def new_note(self,memo,tag):
        self.notes.append(Note(memo,tag))

    def list_notes(self):
        for n in self.notes:
            print(n.memo)
    def modify(self, note_id,memo):
        for note in self.notes:
            if note.id==note_id:
                note.memo=memo

