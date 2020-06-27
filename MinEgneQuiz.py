#Dette er en quiz game om noe særkunnskap om den fiksjonelle detektiv Sherlock Holmes, mer spesifikt sett en bestemt historie innen for novellesamlingen. 

print("Welcome.")

def correct(userAnswer, correctAnswer):
   if userAnswer == correctAnswer:
       print ("Congratulations!")
   else:
       print ("You are unfortunately wrong, my dear friend.")

def Question2andOnwards():
    Question2 = input("Who is Sherlock Holmes' only friend before he met Dr John Watson? \n>")
    correct(Question2, "Victor Trevor")

    Question3 = input("Where is the character Victor Laurence Trevor originated from? \n>")
    correct(Question3, "The Adventure of the Gloria Scott")

    Question4 = input("Which novel collection is The Adventure of the Gloria Scott from? \n>")
    correct(Question4, "The Memoirs of Sherlock Holmes")

    Question5 = input("Where is the hometown of Victor Trevor? \n>")
    correct(Question5, "Donnithorpe")


answer = input("Are you ready to start this? ")
if answer in ("yes", "Yes", "YES"):
    Question1 = input("What is the name of the detective that lives in 221B Baker Street, London, United Kingdom? \n>")
    if Question1 == "Sherlock Holmes":
        print("You bet it is!")
    else:
        print("guess not.")
    Question2andOnwards()
    print("\n")
    print("Thank you for your participation!")
else:
    print("See you next time!")
