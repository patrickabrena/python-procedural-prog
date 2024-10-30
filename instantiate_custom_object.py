#notes on instantiating a custom object


#define a new class called "Recipe"
#class is like a blueprint for creating objects that will have similar characteristics (attributes) and behaviours (methods)
class Recipe():
    #This is the constructor method, "__init__" which is automatically called whenever a new object of the Recipe Class is created
    #"self" is a param that represents the instance of tyhe class being created. It gives access to the instance's attributes and methods.
    #dish, items, and time are additional parameters passed when an object is created. These will be used to intialize the instance's attributes
    def __init__(self, dish, items, time) -> None: # need the self param because it represents the instance of the class that will be created when the class is instantiated
        self.dish = dish
        self.items = items
        self.time = time
        #all 3 variables above are instance variables meaning that each Recipe object will have its own unique values for these attributes
    

    #defining a method named "contents" inside Recipe class.
    #self is used again here, allowing the method to access the instance's attributes 
    def contents(self):
        print(f"The {self.dish} has {str(self.items)} and takes {str(self.time)} to prepare")


#INSTANTIATING OBJECTS
#the lines below create 2 new Recipe objects named pizza and pasta
pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["Bowtie Pasta", "tomato sauce", "garlic"], 30)

#now that there are 2 instances of of the recipe class, I can try to access the attributes and methods.
#can do this by writing two print statements for pizza.items and pasta.itmes
print(pizza.items)
print(pasta.items)

#now try the printing the instance method, "contents" over pizza
print(pizza.contents())
print(pasta.contents())
#run code to see output