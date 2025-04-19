import os

def main():
    print(translate("Nal-1.txt"))


def translate(file):
    path = os.path.join("Nal Examples", file)
    f = open(path, 'r')
    content = f.read()
    return(content)

if __name__ == "__main__":
    main()

def translateInput(task):
    return 0


def translateFile(file):
    return 0

def copulas(copula):
    return 0

def getSentenceType(sentence):
    return 


##Allow for users to input their own NAL file.
def readNalFile():
    filepath = input("Enter the path to your NAL file: ").strip()
    try:
        fileContent = translate(filepath)
        print(fileContent)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
