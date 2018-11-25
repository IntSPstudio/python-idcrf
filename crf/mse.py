#|==============================================================|#
# Made by IntSPstudio
# IDcrf
# Thank you for using this software!
# ID: 980003008
#
# Twitter: @IntSPstudio
#|==============================================================|#

#LIBRARIES
import it8c
import json
#import scrt
#SETTINGS
typeHistory ={}
ptia = {
  "pages": {
    "0": "Menu",
		"1": "Encrypt string",
    "2": "Encrypt file",
		"3": "Decrypt string",
		"4": "Decrypt file",
    "5": "Exit"
  },
	"settings": {
		"titlePrefix": "Crf",
	},
	"visuals": {
		"stMark": "==]",
		"contentLine": it8c.vslTerminalLine(0,"")
	}
}
#EXIT
def dumbHistory():
	aFile = open("history.json", "w")
	json.dump(typeHistory, aFile, indent=2, sort_keys=True)
	aFile.close()
#MAIN
def userInput(rawInput):
  rawInput = str(rawInput)
  if rawInput !="":
    #ENCRYPT STRING
    if rawInput == "1":
      print("")
      ap =  ptia["visuals"]["stMark"]
      bp = ap + "Input: "
      cp = it8c.lettersdigits(input(bp),"") #User input
      if cp !="":
        dp = cp #scrt.fidCrt(cp) #Encrypt
        ep = ap +"Result: "+ dp +" ?"
        fp = input(ep) #Show result
        fp = it8c.lettersdigits(fp,"") #Comment
        hp = str(len(typeHistory)) #History json length
        ip ={} #Per result array
        ip["A"] = cp #Input
        #ip["B"] = dp #Output
        if fp !="":
          ip["C"] = fp #Comment
        #ip["D"] = it8c.dataPrintList(scrt.aidCrt(cp,1),"") #A
        typeHistory[hp] = ip #Save