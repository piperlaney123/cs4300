"""
This program creates a list of book titles and authors, and uses list slicing to print the first three books in the list. 
The program also creates a dictionary that represents a basic student database that includes student names and corresponding IDs. 
It uses pytest to verify correctness.
"""

# a list of some of my favorite books ʕ·ᴥ·ʔ
favorite_books = ["Alias Grace by Margaret Atwood", "Milkweed by Jerry Spinelli", "Quiet by Susan Cain", "A Separate Peace by John Knowles",
 "To Kill a Mockingbird by Harper Lee", "The Hobbit by J. R. R. Tolkien", "Bright Young Women by Jessica Knoll", "Stolen by Lucy Christopher"]

# dictionary of basic student database
student_database = {"John Doe": 1234, "Jane Doe": 5678, "Piper DeHoyos": 9999, "Harry Styles": 1111, "Rami Malek": 2323, "Light Yagami": 4444}

# returns first 3 items from a list using list slicing; recieves a list
def first_three_items(a_list):
    return a_list[:3]


    
