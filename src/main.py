import random

questions = {
    "category1": {
        "1001": {
            "Q": "The atmoic number of sodium is 20.",
            "A": False
        },
        "1002": {
            "Q": "The black box in a plane is black.",
            "A": False
        },
        "1003": {
            "Q": "In a deck of cards, the king has a mustache.",
            "A": False
        },
        "1004": {
            "Q": "Hippos sweat a red substance.",
            "A": True
        },
        "1005": {
            "Q": "The black box in a plane is black.",
            "A": False
        },
        "1006": {
            "Q": "In a deck of cards, the king has a mustache.",
            "A": False
        },
        "1007": {
            "Q": "Hippos sweat a red substance.",
            "A": True
        }
    },
    "category2": {
        "1001": {
            "Q": "The atmoic number of sodium is 20.",
            "A": False
        },
        "1002": {
            "Q": "The black box in a plane is black.",
            "A": False
        },
        "1003": {
            "Q": "In a deck of cards, the king has a mustache.",
            "A": False
        },
        "1004": {
            "Q": "Hippos sweat a red substance.",
            "A": True
        },
        "1005": {
            "Q": "The black box in a plane is black.",
            "A": False
        },
        "1006": {
            "Q": "In a deck of cards, the king has a mustache.",
            "A": False
        },
        "1007": {
            "Q": "Hippos sweat a red substance.",
            "A": True
        }
    },
    "category3": {
        "1001": {
            "Q": "The atmoic number of sodium is 20.",
            "A": False
        },
        "1002": {
            "Q": "The black box in a plane is black.",
            "A": False
        },
        "1003": {
            "Q": "In a deck of cards, the king has a mustache.",
            "A": False
        },
        "1004": {
            "Q": "Hippos sweat a red substance.",
            "A": True
        },
        "1005": {
            "Q": "The black box in a plane is black.",
            "A": False
        },
        "1006": {
            "Q": "In a deck of cards, the king has a mustache.",
            "A": False
        },
        "1007": {
            "Q": "Hippos sweat a red substance.",
            "A": True
        }
    }
}


def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1", "y")


class Quiz:
    def init():
        """Initialize the quiz"""
        global IncorrectScore
        global CorrectScore 
        
        IncorrectScore = 0
        CorrectScore = 0

        category = Quiz.showCatalogs()
        quizQues = Quiz.pickRandomQuestions(category)
        Quiz.startTest(quizQues)
        Quiz.endTest()

    def showCatalogs():
        """Shows the availaboe categories to the user and allows them to pick one among them"""
        global categories
        categories = list(questions.keys())
        for i in range(0, len(categories)):
            print("%d. %s"%(i+1, categories[i]))
        n = int(input(("Choose a category (1-%d): "%(len(categories)))))

        if n < 1 or n > len(categories)+1:
            print("Please select a valid categories in range 1 to %d.", len(categories))
            Quiz.showCatalogs()
        else:
            return categories[n]

    def pickRandomQuestions(category):
        """Picks 5 random questions from the category mentioned as first parameter."""
        ques = questions[category]
        qIds = list(ques.keys())
        totalQues = len(qIds)

        pickedQues = random.sample(range(0, totalQues), 5)

        quesData = list()
        for i in range(0, len(pickedQues)):
            question = ques[qIds[i]]["Q"]
            answer = ques[qIds[i]]["A"]

            templist = list()
            templist.append(question)
            templist.append(answer)
            quesData.append(templist)

        return quesData
    
    def startTest(question):
        """Starts the test and ask user each questions as passed in list as first parameter."""
        for ques in question:
            response = input("%s\nTrue/False (T/F): "%(ques[0]))
            global IncorrectScore
            global CorrectScore
            if(str2bool(response) == ques[1]):
                CorrectScore += 1
            else:
                IncorrectScore += 1
    
    def endTest():
        """Ends the test and displays the score. Also asks the user for a rematch."""
        global IncorrectScore
        global CorrectScore

        print("Score: %.1f"%((CorrectScore / (CorrectScore+IncorrectScore)) * 100)+"%")
        print("Correct Score:", CorrectScore)
        print("Incorrect Score:", IncorrectScore)

        replay = input("Do you want to play again? (Y/N): ")
    
        if(str2bool(replay) == True):
            Quiz.init()
        else:
            print("Thanks for playing our quiz game. Have a nice day!")




            

Quiz.init()




