import os
import re

class NALTranslator:
    def __init__(self):
        self.copula_map = { ##copula hashmap
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



    def translate(self, file):
        try:
            with open(file, 'r') as f:
                results = []
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('//'):  # Skip empty lines and comments
                        translated = self.translateInput(line)
                        results.append(f"{translated}\n")
                return "\n".join(results)
        except FileNotFoundError:
            return f"Error: File '{file}' not found."
        except Exception as e:
            return f"Error processing file: {str(e)}"

    def translateInput(self, task):
        ##Translate a single NAL sentence
        task = task.strip()
        if not task:
            return "Empty input"
        
        task, truth_phrase = truthValues(task)


    def translateFile(self, file_path):
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            return self.translateInput(content)
        except FileNotFoundError:
            return f"Error: File not found at {file_path}"
        except Exception as e:
            return f"Error processing file: {str(e)}"

    def getSentenceType(sentence):
        return 


    def truthValues(sentence):
        ##Extract the truth value from Narsese sentence using tuple statements
        truth = re.search(r'%([0-9.]+)(;[0-9.]+)?%$', sentence)

        if not truth:
            return sentence, "", None, None
        
        frequency = float(truth.group(1))
        
        if frequency == 0:
            truth_phrase = " is not"
        elif frequency != 0 and frequency <= 0.3:
            truth_phrase = "is most likely not"
        elif frequency > 0.3 and frequency <= 0.5:
            truth_phrase = "is probably not"
        elif frequency > 0.5 and frequency <= 0.8:
            truth_phrase = "is probably"
        elif frequency > 0.8 and frequency != 1.0:
            truth_phrase = " is most likely"
        elif frequency == 1.0:
            truth_phrase = " is"


        return sentence[:truth.start()].strip(), truth_phrase, frequency


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




def main():
    while True:
        print("\nOptions:")
        print("1. Translate a NAL file")
        print("2. Enter NAL sentence")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            readNalFile()
        elif choice == "2":
            task = input("Enter NAL sentence: ").strip()
            print("Translation:", translateInput(task))
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()