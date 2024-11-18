#10. program to create flower class. 

class Flowers:
    def __init__(self):            
        self.Rose = 'red'  
        self.Lily = 'white'  
        self.Lotus = 'pink'  
  
    def displayit(self): 
        print("The Dictionary from object fields belongs to the class Flowers :") 
    
flower = Flowers()  
 
flower.displayit()  
print(flower.__dict__)  
