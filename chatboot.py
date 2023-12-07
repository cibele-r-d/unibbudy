from sys import exit


def exit_or_continue():
    user_choice = input("Would you like to ask another question? (Yes/No): ")
    if user_choice.strip().lower() in ("no", "n"):
        exit("See you later, Unibudy is alway here to help.")

    elif user_choice.strip().lower() in ("yes", "y"):
        return True


def faq():
    print(
        """Here are some frequent questions about the campus:\n 
◦ Where is the dining hall?(for this question type 'dining')
◦ Where is the library? (for this question type 'library')
◦ Where is the Art & Design Department? (for this question type 'art')
◦ Where is the Computing Department? (for this question type 'computing')
◦ Where is the Information Centre? (for this question type 'information')
◦ If you don't have an enquire type "exit"\n"""
    )
    while True:
        question = input("Type your question: ")
        if question.strip().lower() == "dining":
            print(
                "The Dining Hall is located in Block C, near the entrance gate 1. Please refer to the map for directions."
            )
            exit_or_continue()

        if question.strip().lower() == "library":
            print(
                "The library is located in Block D, behind the Information Center building. Please refer to the map for directions."
            )
            exit_or_continue()

        if question.strip().lower() == "art":
            print(
                "The Art & Design Department is located in Block A, besides Information Center building. Please refer to the map for directions."
            )
            exit_or_continue()

        if question.strip().lower() == "computing":
            print(
                "The Computing Department is located in Block B, near the Entrance Gate 2. Please refer to the map for directions."
            )
            exit_or_continue()

        if question.strip().lower() == "information":
            print(
                "You are located in the Information Center, the desk for Student Support is located on the 2nd floor. Please refer to the direction signs."
            )
            exit_or_continue()

        if question.strip().lower() == "exit":
            exit("See you later, Unibudy is alway here to help.")

        else:
            print("I didn't get that, could you try again?")


print(
    """Hello! Greetings from the virtual world 
      I'm UniBuddy your guide to help you find your way around the campus.
      To get started, could you please provide your credentials?"""
)
name = input("Please enter your full name: ")
while True:
    if len(name) == 0:
        name = input("Sorry I didn't catch that, could you type your first name: ")
        continue

    else:
        break

name = name.lower().capitalize().strip()
first_name = name.split()[0]

while True:
    try:
        age = int(input(f"Your age: "))
        if 16 < age < 100:
            break
        else:
            print("I need your actual age. Try again :)")

    except ValueError:
        print("I need your actual age. Try again :)")
        continue


while True:
    fav_color = input("What color do you prefer, blue, red, yellow or green: ")
    if fav_color.lower().strip() in ("blue", "red", "yellow", "green"):
        break

    else:
        print("Sorry, I didn't get that, could you try again")


yes_or_no_suggest = input(
    f"""\nWelcome to the campus, {first_name}! 
We are trilled to have you here with us. 
Would you like to hear some suggestions? (Yes/No): """
)


if yes_or_no_suggest.strip().lower() in ("no", "n"):
    faq()

elif yes_or_no_suggest.strip().lower() in ("yes", "y"):
    print("\nGreat! I have some suggestions for you based on you preferences.\n")
    if fav_color == "blue":
        print(
            "I think you would love the Blue Ocean Swim Club, it's located in the Gymnasium, please refer to the map for directions."
        )

    if fav_color == "red":
        print(
            "After a long day of hard work why not enjoy some fun time in The Big Red Bar, it's located in the Block C, please refer to the map for directions."
        )

    if fav_color == "yellow":
        print(
            "I think you would love the The Yellow Gym, it's located in the Gymnasium, please refer to the map for directions."
        )

    if fav_color == "green":
        print(
            "I think you would love the Green Readers Book Club, it's located in the Block A, please refer to the map for directions."
        )

    print("")
    faq()

#this is the first task Data Science HyperionDev suggested to upload on the portfolio. 
#It's requests are a chat boot (Unibudy) that requests pre determined questions.  