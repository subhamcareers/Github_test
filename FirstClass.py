class person:
    counter=0
    def __init__(self,a='Ajay',b='Female'):
        self.name=a
        self.gender=b
        person.counter=person.counter+1
    def showinfo(self):
        print('Name:', self.name)
        print('Gender:', self.gender)
    @classmethod
    def ShowCount(cls):
        print('Number of Objects Created:',cls.counter)
