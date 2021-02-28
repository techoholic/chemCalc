#from mendeleev import element
def debug(*args):
  if bDebug:
    print("[DEBUG] " + ''.join(str(arg)+' ' for arg in args))
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
strEq.strip() #remove whitespace
e = [[],[]]
reactants = strEq.split("->")[0].split("+")
rCnt = 0
for r in reactants:
  e[0].append([''])
  currentlyReading = "co"
  for c in r: #c for character; iterating through string to extact element, coefficients, and subscripts
    debug("c:",c)
    if currentlyReading == "co":
      try:
        int(c)
        debug(c)
        e[0][rCnt][0]+=c
      except:
        debug("got to except")
        e[0][rCnt][0] = 1 if e[0][rCnt][0] == '' else int(e[0][rCnt][0])
        currentlyReading = "el"
  debug("e:",e)
  rCnt+=1
products = strEq.split("->")[1].split("+")
for p in products: pass