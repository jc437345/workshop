_author_ ="Rohit Targotra"
# Initialize the constants


def main():
	print("Reading List 1.0 - by Rohit Targotra ")
	list_book=[]

"""
		[['The Practice of Computing Using Python','Punch and Enbody',792,'r'],
			   ['The 360 Degree Leader','John Maxwell',369,'r'],
			   ['In Search of Lost Time','Marcel Proust',365,'c'],
					   ['Developing the Leader Within You','John Maxwell',225,'r']]
"""
#	BOOK_FILE="books.csv"
load_books(list_book)
displaymenu()
	 choice=input("enter your choice").upper()
	 while choice != 'Q':
		 if choice == 'R':
			 def list_requested():
		 elif choice == 'C':
			 def list_completebooks():
		 elif choice == 'A':
			 def add_book():
		 elif choice == 'M':
			 def mark_completebook():
		 else:
			 print("invalid input")
			 displaymenu()
			 choice=input("enter your choice").upper()




# end of main()
def displaymenu():
  print("Menu:")
print("R - List required books")
print("C - List completed books")
print("A - Add new book")
print("M - Mark a book as completed")
print("Q - Quit")
def load_books(list_book):
   temp_file = open("books.csv","r")
   for line in temp_file:
    line = line.strip().split(",")
    print(line)
   # temp_file.close()



# end of load_books()
def load_books(list_book):
	temp_file = open("book.csv","r")


#def complete_a_book():
    """

"""
print("complete a book")

# end of complete_a_book()

# Start the program
main()
