import json
class Homelib:                                      
    def __init__(self):
        try:
            with open("homelib.json", "r") as f:  
                self.homelib = json.load(f)
                for index in range(len(self.homelib)):
                    self.homelib[index]['id'] = index       
        except FileNotFoundError:
            self.homelib = []                     
 


    def all(self): 
        return self.homelib                       

    def get(self, id):  
        return self.homelib[id]
        
    def create(self, data): 
        self.homelib.append(data)                  

    def save_all(self): 
        with open("homelib.json", "w") as f:       
            json.dump(self.homelib, f)              


    def update(self, id, data):
        homelibrary = self.get(id)
        if homelibrary:
            index = self.homelib.index(homelibrary)
            self.homelib[index] = data
            self.save_all()
            return True
        return False


    def delete(self, id): 
        homelibrary = self.get(id)
        if homelibrary:
            self.homelib.remove(homelibrary)
            self.save_all()
            return True 
        return False     

homelib = Homelib()                                 
