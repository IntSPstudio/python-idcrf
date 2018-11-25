#|==============================================================|#
# Made by IntSPstudio
# IDcrf
# Thank you for using this software!
# Version: 0.0.1.20182611
# ID: 980003008
#
# Twitter: @IntSPstudio
#|==============================================================|#

#LIBRARIES
import ptia as scr
import mse
#SETTINGS
continuity =1
#LOOP
if __name__ == "__main__":
  #EXIT KEY
  exitKey =""
  for page, pages in mse.ptia["pages"].items():
    if pages == "Exit":
      exitKey = page
  #MAIN
  while continuity == 1:
    #MENU
    result = str(scr.main(mse.ptia))
    #CHECK EXIT
    if result !="":
      if result == exitKey:
        mse.dumbHistory()
        continuity =0
      else:
        mse.userInput(result)