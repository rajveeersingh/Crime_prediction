from pymongo import MongoClient

class Testmongo:
    
    def __init__(self):
        # create connection with mongo server
        client = MongoClient('mongodb://localhost:27017')
        # get the database
        db = client['project']
        # get the collection
        self.books = db['books']

    def execute1(self,critaria):
        cur = self.books.find({},{ critaria:True })
        return list(cur)    
    
    def execute(self,critaria,critaria2):
        cur = self.books.find({},{critaria:True,critaria2:True })
        return list(cur)
        # print(dict(cur))
    # x = []
# Tm = Testmongo()
# Tm.execute1('crime_type')
#x.append(cur['Area_name'])
# y = []

# for b in cur:
# x.append(b)
   # y.append(b['Year'])
   # print(b['crime_type'])
# print(len(x))
  