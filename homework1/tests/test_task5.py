from homework1.task5 import *

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