#Dette er en quiz game om noe særkunnskap om den fiksjonelle detektiv Sherlock Holmes, mer spesifikt sett en bestemt historie innen for novellesamlingen. 

print("Welcome.")

#nede er mitt forsøk om å unngå gjentakelse i koden min, men det fungerte ikke helt da jeg prøvde å sette det inn i funksjonen 'Question2andOnwards', det hadde vært flott hvis jeg kan få noe forslag i hva jeg kan gjøre for å forbedre på den :)
#def correct():
#    Questions = [Question2, Question3, Question4, Question5]
#    i = 0
#    Question2 = "Victor Trevor"
#    Question3 = "The Adventure of the Gloria Scott"
#    Question4 = "The Memoirs of Sherlock Holmes"
#    Question5 = "Donnithorpe"
#    while i < len(Questions):
#        x = Question[i]
#        if x:
#            print ("Congratulations!")
#        else:
#            print ("You are unfortunately wrong, my dear friend.")
#        i += 1


#CORRECT
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

#def Question2andOnwards():
#    Question2 = input("Who is Sherlock Holmes' only friend before he met Dr John Watson? \n>")
#    if Question2 == "Victor Trevor":
#        print ("Congratulations!")
#    else:
#        print ("You are unfortunately wrong, my dear friend.")
#
#    Question3 = input("Where is the character Victor Laurence Trevor originated from? \n>")
#    if Question3 == "The Adventure of the Gloria Scott":
#        print ("Congratulations!")
#    else:
#        print ("You are unfortunately wrong, my dear friend.")
#
#    Question4 = input("Which novel collection is The Adventure of the Gloria Scott from? \n>")
#    if Question4 == "The Memoirs of Sherlock Holmes":
#        print ("Congratulations!")
#    else:
#        print ("You are unfortunately wrong, my dear friend.")
#
#    Question5 = input("Where is the hometown of Victor Trevor? \n>")
#    if Question5 == "Donnithorpe":
#        print ("Congratulations!")
#    else:
#        print ("You are unfortunately wrong, my dear friend.")


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
