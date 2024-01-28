FILEPATH = 'myFile2.txt'

def read_myList(filepath=FILEPATH):
    """
    Read a text file and returns the content
    """
    with open(filepath, 'r') as file_local:
            myList_local = file_local.readlines()
    return myList_local

def write_myList(myList_args, filepath=FILEPATH):
    """
    Writes the user inputs to a txt file
    """
    with open(filepath, "w") as file:
        file.writelines(myList_args)

def count(phrase):
    return phrase.count('.')

if __name__ == "__main__":
    print(count("Trees are good. Grass is green."))