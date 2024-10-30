#Exercise: Instantiate a Custom Object

#Step 1:
    #Define a class MyFirstClass
    #Add print statement inside it: "Whoe wrote this?"

class MyFirstClass:

    
    print("Who wrote this?")
    #Step 2: Create string variable named index and initialize it with a string "Author-Book"
    index = "Author-Book"

    #Step 3: Define a function called hand_list()
        #Pass the self param into it as well as philopsher param and book param
        #Write a print statement that will give output such as "Plato wrote the book: Republic"
    def hand_list(self, philospher, book):
        #Step 4
        #Write a print statement using the print() function and pass the class variable by accessing it
            #can access the index class variable directly using MyFirstClass.index
            #This line will display "Author-Book" from the index variable
        print(MyFirstClass.index)

        #Write a print statement that outputs: "Plate wrote the book: republic" using philosopher and book.
        print(f"{philospher} wrote the Book: {book}")

#Step 5
#Create and instantiate an object of the class MyFirstClass called whodunnit
whodunnit = MyFirstClass()
#Call the hand_list() method on whodunnit with values "Sun Tzu" and "The Art of War"
    #"Sun Tzu" and "The Art of War" are passed as arguments for the philosopher and book parameters
    #This will print the class variable and the message "Sun Tzu wrote the book: The Art of War"
whodunnit.hand_list("Sun Tzu", "The Art of War")
#run the code to see the output

#rewrite the code to include a "year" of publication in the output

class MyFirstClassReloaded:
    print("Who wrote this and what year was it pubished?")
    index = "Author-Book-Year"

    def hand_list(self, philosopher, book, year):
        print(MyFirstClassReloaded.index)
        print(f"{philosopher} wrote the Book: {book}, Year Published: {str(year)}")
whodunnit = MyFirstClassReloaded()
whodunnit.hand_list("The Prince", "Machiavelli", 1532)