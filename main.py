import random

Possibilities = ["Rock", "Paper", "Scissors"]
print("Classic Rock Paper Scissors Game. How to play?\n"
      "Rock vs Paper: Paper Won\n "
      "Rock vs Scissors: Rock Win \n"
      "Paper vs Scissors: Scissors Win \n"
      "if you choose same option with computer, its draw. \n"
      "Lets Play!")

### For play Continiously###

while True:
    user_choose = input("Choose Rock, Paper, Scissors: ")
    user_choose = user_choose.capitalize()

    pc_choose_number = random.randint(0, 2)
    pc_choose = Possibilities[pc_choose_number]

    ### Break Loop and Draw option ###

    if user_choose == "Quit":
        print("Görüşürüz")
        break
    if user_choose == pc_choose:
        print("Draw")
    if user_choose not in Possibilities:
        print("Hatalı Seçim")

    ### Win Condition ###

    if user_choose =="Rock" and pc_choose== "Paper":
        print("I won.")
        print(f"ı Choose {pc_choose}")
    if user_choose == "Paper" and pc_choose == "Scissors":
        print("I won.")
        print(f"ı Choose {pc_choose}")
    if user_choose == "Scissors" and pc_choose == "Rock":
        print("I won.")
        print(f"ı Choose {pc_choose}")
    if user_choose =="Paper" and pc_choose== "Rock":
        print("You won.")
        print(f"ı Choose {pc_choose}")
    if user_choose == "Scissors" and pc_choose == "Paper":
        print("You won.")
        print(f"ı Choose {pc_choose}")
    if user_choose == "Rock" and pc_choose == "Scissors":
        print("You won.")
        print(f"ı Choose {pc_choose}")













