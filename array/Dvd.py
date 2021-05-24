
# Definition of dvd
class Dvd:
    def __init__(self, name, releaseYear, director):
        self.name = name
        self.releaseYear = releaseYear
        self.director = director

# print elements of array
dvdCollection=[]
dvdCollection.append(Dvd("test1",1990,"Jennie"))
dvdCollection.append(Dvd("test2",1991,"Tang"))

for ele in dvdCollection:
    print(str(ele.name) + ", " + str(ele.releaseYear) + ", " + (ele.director))
