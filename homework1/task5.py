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

def first_three_items(a_list):
    return a_list[:3]

# testing with pytest
class TestClass:
    def test_first_three_items(self):
        assert first_three_items(favorite_books) == ["Alias Grace by Margaret Atwood", "Milkweed by Jerry Spinelli", "Quiet by Susan Cain"]

    def test_list_1(self):
        assert len(favorite_books) == 8

    def test_list_2(self):
        assert favorite_books[0] == "Alias Grace by Margaret Atwood"

    def test_list_3(self):
        assert favorite_books[-1] == "Stolen by Lucy Christopher"

    def test_dictionary_1(self):
        assert len(student_database) == 6

    def test_dictionary_2(self):
        assert student_database["Piper DeHoyos"] == 9999

    def test_dictionary_3(self):
        assert student_database["Harry Styles"] == 1111


    
