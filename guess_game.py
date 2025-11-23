
from random import randint

easy_level=10
hard_level=5


#checking answer is currect or not
def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too high.")
        return turns-1
    elif guess<answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}.")


#setteing the diffuculty level
def set_difficulty():
    input_level=input("choose a difficulty level --> 'easy' or 'hard' : ")
    if input_level=='easy':
        return easy_level
    else:
        return hard_level


#main funciton
def game():
    print("wellcome to gussing game:")
    print("as i am thinking of a number between 1 and 100")
    print("you have to guss it")

    answer=randint(1,100)
    turn =set_difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turn } attempts remaining to guss the number.")
        guess=int(input("make a guss:"))
        turn=check_answer(guess,answer,turn)
        if turn==0:
            print("you have no more attempts and you lose the game and correct answer is { answer}.")
            return 
        elif guess!=answer:
            print("guess again.")

#starting game function
game()