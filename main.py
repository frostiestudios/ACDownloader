from appJar import gui
import json
import webbrowser
DWN="\u2193"
def settings(btn):
    if btn=="View on GitHub":
        webbrowser.open("https://github.com/frostiestudios/ACDownloader")
    if btn=="Settings":
        webbrowser.open("https://github.com/frostiestudios/ACDownloader")
def install():
    print("Installing")
    mod=app.getOptionBox("Mod")
    print(mod)
app=gui("ACDownloader")
#Tabs
app.startTabbedFrame("Tabs")
#Main Tab
app.startTab("Main")
app.startLabelFrame("ACDownloader",2,1)
app.addOptionBox("Mod",["CSP","Content Manager"],1,1)
app.addButtons([DWN],install,1,2)
app.stopLabelFrame()
app.stopTab()
#Settings Tab
app.startTab("Settings")
app.addLabel("Settings")
app.addButton("Help",settings)
app.addButton("View on GitHub",settings)
app.stopTab()
app.stopTabbedFrame()
app.go()