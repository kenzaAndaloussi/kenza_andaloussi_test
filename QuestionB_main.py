# Import the class StringCompare
from QuestionB import StringCompare

if __name__ == '__main__':
    try:
        # Ask the user to enter two strings of floats
        flt1 = input('Enter a first string of floats\n')
        flt2 = input('Enter a second string of floats \n')
        # Apply the comparisons methods of the class StringCompare
        compare = StringCompare(flt1, flt2)
        if flt1 == flt2:
            print(compare.equal())

        else:
            print(compare.greater())
            print(compare.lesser())
    # Print an error if the user enters something different to numbers
    except ValueError:
        print("Characters are not allowed, please Enter only numbers \n")
