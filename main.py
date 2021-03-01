from replit import db
from re import findall

class Term:
  def __init__(self, strTerm):
    #strTerm = 4Fe3CO2
    splitTerm = findall(r'[A-Z][a-z]+|[A-Z]|\d+', strTerm)
    debug(splitTerm)
    fIndex = 0
    self.elements = []
    for f in splitTerm:
      try:
        int(f)
        if fIndex == 0:
          self.co = int(f)
        else:
          self.elements[-1][1] = int(f)                          
      except:
        self.elements.append([f,1])
      fIndex+=1
    debug(self.elements)

class Equation:
  pass
def debug(*args):
  if bDebug:
    print("[DEBUG] " + ''.join(str(arg) for arg in args))
bDebug = True
if bDebug: print("[DEBUG] In debug mode; extra info wil be printed")
print("Welcome to my Chemistry Calculator!\nFirst, enter your chemical equation. It must be in this specific format:\nFe2O3 + 3CO -> 2Fe + 3CO2 (spaces optional)")
strEq = input("\nType the equation here and press Enter: ")
if strEq == "debug":
  bDebug = True
  print("[DEBUG] In debug mode; extra info will be printed")
  strEq = input("Type the equation here and press Enter: ")
if strEq == '' and bDebug:
  debug("Assuming test equation above")
  strEq = "Fe2O3 + 3CO -> 2Fe + 3CO2"
  
#Check if this is a valid equation, and if so, split it into equal parts
#ele = {"H":1.01,"He":4.00,"Li":6.94,"Be":9.01,""}
strEq.replace(' ', '')
reactants = strEq.split("->")[0].split("+")
for r in reactants: Term(r)
products = strEq.split("->")[1].split("+")
for p in products: Term(p)