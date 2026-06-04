# I BUILT A LIBRARY CATALOGUE AND TRIED 
# 1. PRINTING THE BOOKS & 2. PRINTING AVAILABLE BOOKS 
# 2. SEARCHING FOR A BOOK AND PRINTING AN ERROR MESSAGE IF NOT FOUND 
# 3.ADDING A BOOK & SORTING BOOKS ACCORDING TO THE YEAR
#**********WHAT I LEARNT FROM MY MISTAKES******
#Using nested dictionaries, applying .key, .values and .items(). 
# Using the .get() function to avoid crashing in cse a value is missing
#I  can access the inner dictionary directly after declaring it in the for loop , eg accessing status , i dont need to go back to library

# A library catalogue — each book maps to its details
library = {
    "The Pragmatic Programmer": {"author": "Hunt & Thomas", "year": 1999, "available": True},
    "Clean Code":               {"author": "Robert Martin",  "year": 2008, "available": False},
    "Automate the Boring Stuff": {"author": "Al Sweigart",    "year": 2015, "available": True},
    "Python Crash Course":       {"author": "Eric Matthes",   "year": 2019, "available": True},
    "Fluent Python":             {"author": "Luciano Ramalho", "year": 2015, "available": False},
}

#Printing every book title and its author using .items()
for book, writer in library.items():
   print(f"{book} : {writer['author']}")

#Printing only the books that are currently available
for book, status in library.items():
    if status['available']:
        print(book)

#Using .get() to safely look up "The Hobbit" — print its details or "not in catalogue" if missing
search = library.get('The Hobbit', 'not in catalogue')
print(search)

#Add a new book of your choice to the library with all three fields, then print the updated total count
library['Learn with Simon'] = {"author": "Simon", "year": 2026, "available": True}
print(len(library))
#Building a new dictionary called by_year that maps each year to a list of book titles published that year
by_year = {}
for book, time in library.items():
    year  =  time['year']
    if year not in by_year:
        by_year[year] = []
    by_year[year].append(book)
print(by_year)

