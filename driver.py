from Tkinter import *

class State:
	def __init__(self, bux=10000, timer=0, stuff=[0,0,0,0,0], loc=0):
		self.cash=bux
		self.time=timer
		self.inv=stuff
		self.location=loc
	
		
root=Tk(className="gunRun: Mhacks Edition")
root.withdraw()
mainwin=Toplevel()

def startGame(root, troot):
	game=State()
	root.withdraw()
	troot.destroy()

def loadGame(root):
	pass

def quitGame(root):
	root.destroy()

nw=Button(mainwin, text="New Game", command=lambda: startGame(mainwin, root))
ld=Button(mainwin, text="Load Game", command=lambda: loadGame(mainwin))
qt=Button(mainwin, text="Exit Game", command=lambda: quitGame(rt))

nw.pack()
ld.pack()
qt.pack()

mainwin.mainloop()
