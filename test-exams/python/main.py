# Questions 7 - 10 Multi-paradigm programming in Python


# 7a
import datetime
import math

import numpy as np


def sumImperative(list):
    sum = 0
    for number in list:
        sum = sum+number
    return sum

numLst = [1, 2, 3, 4, 5]
print(sumImperative(numLst))

# 7b
def evenNumbers():
    while (1):
        num = input("Give an input(number): ")

        if (int(num) % 2 == 0):
            print(num)
        elif (int(num) == 123):
            quit()
        else:
            print("Bye for now!")

# evenNumbers()

# Question 8

# 8a
data = [1, 2, 3, 4, 5]
add10 = lambda list: map(lambda num: num + 10, list)

print(list(add10(data)))

#8b
naturalNumbers = [0,1,2,3,4,5,6,7,8,9]
def getEvenNumbers(list):
    return filter(lambda x: x % 2 == 0, list)

print(list(getEvenNumbers(naturalNumbers)))

# Question 9

# 9a
def groupList(list, gLength):

    numOfLists = int(math.ceil(len(list) / gLength))
    resList = np.empty((numOfLists, gLength))
    counter = 0
    
    for i in range(numOfLists):
        for j in range(gLength):
            if len(list) > counter:
                resList[i][j] = list[counter]
                counter = counter+1

    return resList


list1 = [1,2,3,4,5,6]
res1 = groupList(list1, 2) # gives [ [1, 2], [3, 4], [5,6] ]
list2 = [1,2,3,4,5]
res2 = groupList(list2, 3) # gives [ [1, 2], [3, 4], [5,6] ]
print(res1)
print(res2)
    
    
# 9b
dkCities = ["Copenhagen", "Aarhus", "Aalborg", "Horsens", "Odense"]

def filterCities(cities: list): return filter(lambda city: city[:2] == "Aa", cities)

print(list(filterCities(dkCities)))

# Question 10

# 10a

class CourseNote():
    
    @property
    def jotting(self):
        return self.__jotting
    
    @jotting.setter
    def jotting(self, value):
        self.__jotting = value
        
    @property
    def creationDate(self):
        return self.__creationDate
    
    @creationDate.setter
    def creationDate(self, value: datetime.date):
        self.__creationDate = value
        
    @property
    def keywords(self):
        return self.__keywords
    
    @keywords.setter
    def keywords(self, value):
        self.__keywords = value
        
    def __init__(self, jotting, keywords):
        self.__jotting = jotting
        self.__keywords = keywords
        self.__creationDate = datetime.date.today()
        
    
    def isAmatch(self, searchFilter: str):
        return searchFilter in self.keywords or searchFilter in self.jotting
        
class Notebook():
    @property
    def courseNotes(self):
        return self.__courseNotes
    
    @courseNotes.setter
    def courseNotes(self, value: list[CourseNote]):
        self.__courseNotes = value
        
    def __init__(self):
        self.__courseNotes = []
        
    def search(self, strFilter: str):
        return filter(lambda note: note.isAmatch(strFilter) , self.courseNotes)
    
    def addNote(self, jotting: str, keywords: str):
        self.courseNotes.append(CourseNote(jotting, keywords))
        
        
        
course_note = CourseNote("This is a test jotting", "test")
print("Jotting:", course_note.jotting)
print("Keywords:", course_note.keywords)
print("Creation Date:", course_note.creationDate)

notebook = Notebook()
notebook.addNote("Another test jotting", "example")
notebook.addNote("This is a test jotting", "test")

search_results = notebook.search("test")
print("Search Results:")
for note in search_results:
    print("----------")
    print("Jotting:", note.jotting)
    print("Keywords:", note.keywords)
    print("Creation Date:", note.creationDate)
    print("----------")
    

# 10b
class Singer():
    def sing(self):
        print("kokot pica u holica chlpata ric a smradlava midza")
    
class SongWriter():
    def compose(self):
        print("pupu c pupu c, pupu c pupu c")

class SingerSongWriter(Singer, SongWriter):
    def strum(self):
        print("I'm so strumming wow")
        
    def actSensitive(self):
        print("Ah cmon man to co za picoviny trepes ty chod dopice skaredy si")
        
    def sing(self):
        Singer().sing()
        print("im singing some sensitive bullshit right now lalllalalala")
        
    def compose(self):
        SongWriter().compose()
        print("Maaan composing some sensitive stuff you know the blues and shit")


singer = Singer()
print("Singer is singing:")
singer.sing()

song_writer = SongWriter()
print("\nSongWriter is composing:")
song_writer.compose()

singer_song_writer = SingerSongWriter()
print("\nSingerSongWriter is singing:")
singer_song_writer.sing()
print("SingerSongWriter is composing:")
singer_song_writer.compose()
print("SingerSongWriter is strumming:")
singer_song_writer.strum()
print("SingerSongWriter is acting sensitive:")
singer_song_writer.actSensitive()


    