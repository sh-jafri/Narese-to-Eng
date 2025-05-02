import os
import re

def main():
    print(translate("Nal-1.txt"))


def translate(file):
    path = os.path.join("Nal Examples", file)
    f = open(path, 'r')
    content = f.read()
    return content

if __name__ == "__main__":
    main()

def translateInput(task):

    return 0


def translateFile(self, file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return self.translateInput(content)
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except Exception as e:
        return f"Error processing file: {str(e)}"

def copulas(copula):
    hashmap = {
        "-->": "is a type of",
        "<->": "is similar to",
        "{--": "is an instance of",
        "--]": "is a property of",
        "{-]": "is an instance with property",
        "~": "is not",
        "-": "not",
        "|": "and",
        "&": "that are",
        "/": "or",
        "*": "product of",
        "==>": "implies that",
        "=/>": "predicts that",
        "=|>": "expects that",
        "=\\>": "retrospects that",
        "<=>": "is equivalent to",
        "<?>": "whether",
        "_": "with",
        "\\": "the operation",
        ",": "and",
        "?": "is it true that",
        "!": "it is certain that",
        ".": "it is possible that"
    }
    return 0

def getSentenceType(sentence):
    return 


def truthValues(sentence):

    """Extract the truth value from Narsese sentence using hashmapping"""

    truth = re.search(r'%([0-9.]+)(;[0-9.]+)?%$', sentence)

    if not truth:
        return sentence, "", None, None
    
    frequency = float(truth.group(1))
    
    if frequency == 0:
        truth_value = " is not"
    elif frequency != 0 and frequency <= 0.3:
        truth_value = "is most likely not"
    elif frequency > 0.3 and frequency <= 0.5:
        truth_value = "is probably not"
    elif frequency > 0.5 and frequency <= 0.8:
        truth_value = "is probably"
    elif frequency > 0.8 and frequency != 1.0:
        truth_value = " is most likely"
    elif frequency == 1.0:
        truth_value = " is"


    return sentence[:truth.start()].strip(), truth_value, frequency


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
