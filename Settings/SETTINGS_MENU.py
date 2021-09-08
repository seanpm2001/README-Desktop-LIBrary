# Start of script
# This script was going good until I had to add type checking, then it turned into really bad code. There are other problems with this script, and lots of optimization is needed.
""" About
This is the settings menu for the README desktop library. It is the UI version of the settings for the README desktop extension.
The settings are stored in a separate file. Multiple interface versions are included, one with a GUI and one with a CLI
"""
def cli_SettingsMenu():
  # Command line settings
  print ("Settings for the README desktop library extension")
  print ("You are using the command line version of the settings menu. If you desire a GUI version, go [here](link unavailable)")
  xLoop = int(1)
  while (xLoop == 1):
    consoleCA1 = str(input("Input here: "))
  elif (xLoop is not == 1):
    print ("The settings changer has crashed.")
    noMore = input("Press [ENTER] to quit the program")
    break
  # Divider
def gui_SettingsMenu():
  # Graphical User Interface setting
  print ("Settings for the README desktop library extension")
  print ("You are using the graphical user interface version of the settings menu. If you desire a CLI version, go [here](link unavailable)")
  print ("This version does not have graphics yet.")
  xLoop = int(1)
  while (xLoop == 1):
    consoleCA1 = str(input("Input here: "))
  elif (xLoop is not == 1):
    print ("The settings changer has crashed.")
    noMore = input("Press [ENTER] to quit the program")
    break
  # Divider
def main():
  print ("Settings menu for README desktop library (extension)")
  try:
    getModeInt = int(input("Which version of the settings would you like to use?\nCLI (Command Line Interface) - All text, no images (ID: 0)\nGUI (Graphical User Interface) - Text but with graphics (ID: 1)\n>>>"))
  except ValueError:
    print("Please enter an integer between 0 and 1!")
    break
  if (getModeInt == 0):
    return cli_SettingsMenu()
    break
  elif (getModeInt == 1):
    return gui_SettingsMenu()
    break
  elif (getModeInt is not == 0 or 1):
    except ValueError:
      print("Please enter an integer between 0 and 1!")
      break
# Divider
# Start of settings
return main()
break
''' File info
File type: Python 3 source file (*.py)
File version: 1 (Wednesday, 2021 September 8th at 3:05 pm)
Line count (including blank lines and compiler line): 59
'''
# End of script
