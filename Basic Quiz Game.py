class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def check_answer(self, user_input):
        """
        
        """
        return self.options[user_input - 1] == self.answer

    def display_question(self):
        """
        Displays the question and its options.
        """
        print(self.prompt)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        """
        Starts the quiz and processes each question.
        """
        for question in self.questions:
            question.display_question()
            user_input = self.get_user_input(len(question.options))
            if question.check_answer(user_input):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer was: {question.answer}\n")
        self.display_final_score()

    def get_user_input(self, options_length):
        """

        """
        while True:
            try:
                user_input = int(input("Please enter the number of your answer: "))
                if 1 <= user_input <= options_length:
                    return user_input
                else:
                    print("Invalid choice. Please choose a valid option number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_final_score(self):
        """
        Displays the user's final score.
        """
        print(f"Quiz Complete! Your final score is: {self.score}/{len(self.questions)}")

def main():
    """
    Main function to set up the quiz.
    """

    # ASCII art welcome message
    print("""
 __          __  _                            _            ____       _    _  ___  _______
 \ \        / / | |                          | |         /  __  \    | |  | |  |   |__ __|
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___    | |  | |    | |  | |  |     | |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   | |  | |    | |  | |  |    |  |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |  | |__| |    | |__| |  |   |  |
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \ ____\ \   \ ____ / _|_ |_______|
                                                                \_\            
    """)

    # Define the quiz questions
    questions = [
        Question("Which of the following is a valid Python keyword?", ["function", "define", "global", "module"], "global"),
        Question("What is the correct extension of Python files?", [".pyth", ".pt", ".pyt", ".py"], ".py"),
        Question("Which of the following is the correct way to import the math module in Python?", ["import Math", "import math", "import maths", "import mathematics"], "import math"),
        Question("Which of the following methods is used to add an element to the end of a list in Python?", ["insert()", "append()", "add", "extend"], "append()"),
        Question("Which of the following is not a standard Python data type?", ["List", "Dictionary", "Tuple", "Array"], "Array")
    ]

    # Create a quiz instance and start it
    quiz = Quiz(questions)
    quiz.start()

if __name__ == "__main__":
    main()
