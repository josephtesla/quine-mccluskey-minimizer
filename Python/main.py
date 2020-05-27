"""
  DRIVER PROGRAM

"""

from qm_minimizer import QM_Minimizer
from GUI import GUI


def main():
	print("|-----------------------------------------------|")
	print("|																				|")
	print("|																				|")
	print("|		QUINE-McKluskey Minimizer      	|")
	print("|																				|")
	print("|		SELECT AN ENVIRONMENT:          |")
	print("|																				|")
	print("|		ENTER '1' FOR GUI               |")
	print("|																				|")
	print("|		ENTER '2' FOR CONSOLE           |")
	print("|																				|")
	print("|																				|")
	print("|-----------------------------------------------|")


	env = input("Enter here: ")

	while env not in ['1', '2']:
		print("!INVALID INPUT!")
		env = input("Enter here: ")


	if env == "1":
		GUI() #RUN GUI instance

	elif env == "2":
		print("\n|-------------- CONSOLE MODE -------------| \n")

		invalid = True


		while invalid:
			try:

				print("|-----ENTER MINTERMS SEPERATED BY COMMA (e.g 3,2,5,12...) ------|")
				minterms = input("minterms: ")

				print("\n\n|-----ENTER NUMBER OF VARIABLES (e.g 4) ------|")
				no_of_vars = int(input("no of variables: "))

				func = QM_Minimizer(minterms, no_of_vars).minimize()

				print("|------ MINIMIZED EXPRESSION -------| \n")
				print("\t " + func)

				invalid = False

			except Exception as InvalidInputException:
				print("\n\n!----- ERROR: INVALID FUNCTION INPUT------|\n\n")
				
				invalid = True
				

main()