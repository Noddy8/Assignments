#EX-2. Get_str() and Print_str() in upper case:
class string:
    def get_str(self,s):
        self.s = s
    def print_str(self):
        r = self.s.upper()
        print(r)
    
s = input("Enter Something :")
a = string()
a.get_str(s)
a.print_str()


        
