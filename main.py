import os
import re


class NALTranslator:
    def __init__(self):
        self.copula_map = {  ##copula hashmap
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

    def readNalFile(self):
        filepath = input("Enter the path to your NAL file: ").strip()
        try:
            fileContent = self.translate(filepath)
            print(fileContent)
        except FileNotFoundError:
            print("NAL File could not be processed.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def translate(self, file):
        try:
            with open(file, 'r') as f:
                results = []
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('//'):  # Skip empty lines and comments
                        translated = self.translateInput(line)
                        results.append(translated)
                return "\n".join(results)
        except FileNotFoundError:
            return f"Error: File '{file}' not found."
        except Exception as e:
            return f"Error processing file: {str(e)}"

    def translateInput(self, task):
        task = task.strip()
        if not task:
            return "Empty input"

        has_period = task.endswith('.')
        if has_period:
            task = task[:-1]

        task, truth_phrase = self.truthValues(task)

        if "==>" in task:
            parts = task.split("==>")
            if len(parts) == 2:
                antecedent = self.translateSingleStatement(parts[0].strip())
                consequent = self.translateSingleStatement(parts[1].strip())
                translation = f"If {antecedent.lower()}, then {consequent.lower()}"
                if truth_phrase:
                    translation += f" {truth_phrase}"
                if has_period:
                    translation += "."
                return translation

        translation = self.translateSingleStatement(task)
        if truth_phrase:
            translation += f" {truth_phrase}"
        if has_period:
            translation += "."
        return translation

    def translateSingleStatement(self, statement):
        if statement.startswith('<') and statement.endswith('>'):
            statement = statement[1:-1]
            for copula in self.copula_map:
                if f" {copula} " in statement:
                    parts = statement.split(f" {copula} ")
                    if len(parts) == 2:
                        subject = self.clean_term(parts[0])
                        predicate = self.clean_term(parts[1])
                        return f"{subject} {self.copula_map[copula]} {predicate}"

        if "-->" in statement:
            parts = statement.split("-->")
            if len(parts) == 2:
                subject = self.clean_term(parts[0])
                predicate = self.clean_term(parts[1])
                return f"{subject} is a type of {predicate}"

        return self.clean_term(statement)

    def clean_term(self, term):
        term = term.strip()
        if term.startswith('{') and term.endswith('}'):
            term = term[1:-1]
        # Capitalize first letter
        if term:
            term = term[0].upper() + term[1:]
        return term

    def truthValues(self, sentence):
        truth = re.search(r'%([0-9.]+)(;[0-9.]+)?%$', sentence)

        if not truth:
            return sentence, ""

        frequency = float(truth.group(1))
        truth_phrase = ""

        if frequency == 0:
            truth_phrase = "(this is not true)"
        elif frequency <= 0.3:
            truth_phrase = "(this is very unlikely)"
        elif frequency <= 0.5:
            truth_phrase = "(this is unlikely)"
        elif frequency <= 0.7:
            truth_phrase = "(this is somewhat likely)"
        elif frequency <= 0.9:
            truth_phrase = "(this is likely)"
        elif frequency == 1.0:
            truth_phrase = "(this is certainly true)"
        else:
            truth_phrase = f"(confidence: {frequency})"

        return sentence[:truth.start()].strip(), truth_phrase


def main():
    translator = NALTranslator()
    while True:
        print("\nOptions:")
        print("1. Translate a NAL file")
        print("2. Enter NAL sentence")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            translator.readNalFile()
        elif choice == "2":
            task = input("Enter NAL sentence: ").strip()
            print("Translation:", translator.translateInput(task))
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()