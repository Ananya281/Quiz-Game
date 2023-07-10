print("Welcome to Quiz Game")
print("There are 10 questions in this game\nEach carries 10 marks")
score=0
ques=0

correct=["charles babbage","kevin systrom","linda yaccarino","uniform resource locator","c","python","douglas engelbart","dr vijay p bhatkar","cpu","federico faggin"]

i=1
while True:
    try:
        ask=input("Are you ready to play?\n(yes/no)")
        if(ask.lower()=="yes"):
            print("Okay, Let's play!!!")
            print("Write complete answer! Do not write option")        
            print("Q-1: Who is the father of computer?")
            print("Your options are:")
            print("a : Charles Babbage\nb : Douglas Engelbart\nc : Alan Turing\nd : Blaise Pascal")
            ans=input("Answer is ")
            if ans.lower()==correct[0]:
                score=score+10
                ques=ques+1
                print("Correct")
                print("You gained 10 marks")
                print("Now your score is ",score)
            else:
                print("Incorrect")
            print("Q-2: Who is the founder of instagram?")
            print("Your options are:")
            print("a : Mark Zuckerberg\nb : Will Cathcart\nc : Kevin Systrom\nd : Sunder Pichai")
            ans=input("Answer is ")
            if ans.lower()==correct[1]:
                score=score+10
                ques=ques+1
                print("Correct")
                print("You gained 10 more marks")
                print("Now your score is ",score)
            else:
                print("Incorrect")
            print("Q-3: Who is the ceo of twitter?")
            print("Your options are:")
            print("a :Andy Jassy\nb : Linda Yaccarino\nc : Neal Mohan\nd : Will Cathcart")
            ans=input("Answer is ")
            if ans.lower()==correct[2]:
                score=score+10
                ques=ques+1
                print("Correct")
                print("Oops! You gained 10 more marks")
                print("Now your score is ",score)
            else:
                print("Incorrect")
            print("Q-4: What is the full form of url?")
            print("Your options are:")
            print("a : Uniform Resource Locator\nb : Universe Resource Locator\nc : Uniform Reverse Locator\nd : Uniform Resource Location")
            ans=input("Answer is ")
            if ans.lower()==correct[3]:
                score=score+10
                ques=ques+1
                print("Correct")
                print("You gained 10 more marks")
                print("Now your score is ",score)
            else:
                print("Incorrect")
            print("Q-5: Which language is mother of all computer language")
            print("Your options are:")
            print("a : Python\nb : Java\nc : C++\nd : C")
            ans=input("Answer is ")
            if ans.lower()==correct[4]:
                score=score+10
                ques=ques+1
                print("Correct")
                print("You gained 10 more marks")
                print("Now your score is ",score)
            else:
                print("Incorrect")
            print("Q-6: Which is the best programming language")
            print("Your options are:")
            print("a : Python\nb : Java\nc : C++\nd : C")
            ans=input("Answer is ")
            if ans.lower()==correct[5]:
                score=score+10
                ques=ques+1
                print("Correct")
                print("You gained 10 more marks")
                print("Now your score is ",score)
            else:
                print("Incorrect")
            print("Q-7: Who is father of GUI")
            print("Your options are:")
            print("a : Charles Babbage\nb : Alan Kay\nc : Henry Edward Roberts\nd : Douglas Engelbart")
            ans=input("Answer is ")
            if ans.lower()==correct[6]:
                score=score+10
                ques=ques+1
                print("Correct")
                print("You gained 10 more marks")
                print("Now your score is ",score)
            else:
                print("Incorrect")
            print("Q-8: Who is the father of Indian computing?")
            print("Your options are:")
            print("a : Sunder Pichai\nb : Dr Vijay P Bhatkar\nc : Rangaswamy Narasimhan\nd : Boris Babayan") 
            ans=input("Answer is ")       
            if ans.lower()==correct[7]:
                score=score+10
                ques=ques+1
                print("Correct")
                print("You gained 10 more marks")
                print("Now your score is ",score)
            else:
                print("Incorrect")
            print("Q-9: What is the brain of computer?")
            print("Your options are:")
            print("a : Mouse\nb : Keyboard\nc : Monitor\nd : CPU")
            ans=input("Answer is ")
            if ans.lower()==correct[8]:
                score=score+10
                ques=ques+1
                print("Correct")
                print("You gained 10 more marks")
                print("Now your score is ",score)
            else:
                print("Incorrect")
            print("Q-10: Who invented CPU?")
            print("Your options are:")
            print("a : Ada Lovelace\nb : Federico Faggin\nc : Guido van Rossum\nd : Adam Osborne")
            ans=input("Answer is ")
            if ans.lower()==correct[9]:
                score=score+10
                ques=ques+1
                print("Correct")
                print("You gained 10 more marks")
                print("Now your score is ",score)
            else:
                print("Incorrect")
            print("You give",ques,"answers correct")
            print("Your total score is ",score)
            print("Thanks for playing")
            break
        elif(ask.lower()=="no"):
            print("Okay, please play next time.")
            break
        else:
            print("Invalid number.Please write yes/no")
    except Exception as e:
        i=i+1
with open("myscore.txt","r") as f:
    myscore=int(f.read())
if(myscore<score):
    print("You have just broken the high score, Congrats!")
    with open("myscore.txt","w") as f:
        f.write(str(score))
        




    
    
    
