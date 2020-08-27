from tkinter import *
from qm_minimizer import QM_Minimizer

class GUI:

	def __init__(self):
		window = Tk() # Create a window
		window.title("Quine-McKluskey Minimizer") # Set title																		#Window
		Label(window, text = "ENTER MINTERMS (seperated by comma e.g 3,4,5...): ").grid(row = 1, column = 1, sticky = W)    #Labels
		Label(window, text = "ENTER NUMBER OF VARIABLES (e.g 4):").grid(row = 3, column = 1, sticky = W)
		Label(window, text = ".").grid(row = 2, column = 1, sticky = W)
		Label(window, text = ".").grid(row = 5, column = 1, sticky = W)
		Label(window, text = ".").grid(row = 4, column = 1, sticky = W)
		Label(window, text = "MINIMIZED EXPRESSION: ").grid(row = 5, column = 1, sticky = W)
		self.mintermsVar = StringVar()
		Entry(window, textvariable=self.mintermsVar,justify=RIGHT).grid(row=1,column=3)
		self.variablesVar = StringVar()
		Entry(window, textvariable=self.variablesVar,justify=RIGHT).grid(row=3,column=3)
		self.expressionVar = StringVar()
		lblTotalPayment = Label(window, textvariable = self.expressionVar).grid(row = 5, column = 3, sticky=E)
		btMinimize = Button(window, text = "Minimize", command=self.minimize).grid(row = 6, column = 2, sticky=E)
		window.mainloop()

	def minimize(self):
			minterms = str(self.mintermsVar.get())
			no_of_vars = int(self.variablesVar.get())

			try:
				func = QM_Minimizer(minterms, no_of_vars).minimize()
				self.expressionVar.set(func)

			except Exception as InvalidInputException:

				self.expressionVar.set("Looks like your input is invalid")
				raise InvalidInputException

