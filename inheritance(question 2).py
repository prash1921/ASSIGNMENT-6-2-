import sys
class dog:
      def __init__(self,name,age,coatcolour):
          self.name=name
          self.age=age
          self.coatcolour=coatcolour
          
print("dog initalized!")
def description(self):
     return f"{self.name} is {self.age} years old"
def get_info(self,coatcolour):
    return f"{self.name} has {self.coatcolour} fur"
class jackrussellterrier(dog):
     def breed(self,breed="jack russel terrier"):
          return f"{self.name} is a {breed}"
     def mood(self,mood="happy and energetic"):
          return f"{self.name} is {mood}"
     def attention(self,attention="moderate"):
          return f"{self.name} needs {attention}"
     def height(self,height="13-15 years"):
          return f"{self.name} has a {height}"
     def characterstics(self,chataterstics="double coat,flat,hard coat"):
          return f"{self.name} has {characterstics}"
class Bulldog(dog):
     def breed(self,breed="bull dog"):
          return f"{self.name} is a {breed}"
     def mood(self,mood="friendlybut dignified"):
          return f"{self.name} is {mood}"
     def attention(self,attention="moderate"):
          return f"{self.name} needs {attention} attention"
     def height(self,height="8-10"):
          return f"{self.name} has a {height}"
     def characterstic(self,characterstics="straight coat"):
          return f"{self.name} has {characterstics}"
          
          
          Rex=dog("rex",5,"brown")
          print(rex.description())
          print(rex.get_info())
          leo=dog("daisy",6,"fawn")
          print(leo.description())
          print(leo.get_info())
          print("************")
     rex=jackrussellterrier("rex",5,"brown")
     print(rex.breed())
     print(rex.mood())
     print(rex.attention())
     print(rex.height())
     print(rex.characterstics())
     print("********************")


     leo=bulldog("leo",7,"black")
     print(leo.breed())
     print(leo.mood())
     print(leo.attention())
     print(leo.height())
     print(leo.characterstics())
     print("********************")