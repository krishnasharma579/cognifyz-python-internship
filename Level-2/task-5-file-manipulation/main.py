import os

#get the current project directory
BASE_DIR = os.path.dirname(__file__)
#create the full path to the sample text file
file_path = os.path.join(BASE_DIR, "sample.txt")

#function to read the file and display its statistics
def file_manipulation():
    try:
        #open the file in read mode
        with open(file_path, "r") as file:
            #read the entire file content
            content = file.read()

            #count total characters, words, and lines
            characters = len(content)
            words = len(content.split())
            lines = len(content.splitlines())

    #handle the case when the file does not exist
    except FileNotFoundError:
        print("File not found. Please make sure 'sample.txt' exists.")
        return
    
    #check if the file is empty
    if not content:
        print("The file is empty.")
        return
    
    #display the file statics
    print(f"Total Lines: {lines}")
    print(f"Total Words: {words}")
    print(f"Total Characters: {characters}")

#run the program
if __name__ == "__main__":
    file_manipulation()