from homework1.task1 import say_hi

# https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html 
# pass capsys to test; this is a pytest fixture that captures output in console, which we want.
def test_say_hi(capsys):
    # call func
    say_hi()
    # get output
    greeting = capsys.readouterr() 
    # when testing equivalence, make sure to strip the greeting of newline character 
    assert greeting.out.strip() == "Hello, World!"
