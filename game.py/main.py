# this is the predefine questions
questions = [
    ["What is the capital of India?", "Delhi", "New Delhi", "Mumbai", 1],
    ["Who is most likely to win a dance-off on Mars?", "Elon Musk", "A Martian with 6 legs", "Neil Armstrong's hologram", 1],
    ["Which planet is known for its spicy tacos?", "Venus", "Planet Taco-47", "Earth (sometimes)", 1],
    ["What do aliens use to power their spaceships?", "Solar panels", "Quantum burritos", "Dark matter smoothies", 2],
    ["If time travel were real, what would be the best year to visit?", "3025", "1999 (for the parties)", "The year dinosaurs got Wi-Fi", 2],
    ["What is the official language of robots?", "Binary", "Beepish", "Sarcasm", 0],
    ["Which superhero is most likely to be an undercover alien?", "Batman", "Iron Man", "Shaktimaan", 2],
    ["What happens if you press Ctrl+Alt+Universe?", "You reboot reality", "You summon a tech god", "You get a free pizza", 0],
    ["Which fruit is secretly a time machine?", "Banana", "Pineapple", "Avocado", 1],
    ["What do astronauts do for fun in zero gravity?", "Play floating chess", "Juggle planets", "Moonwalk (literally)", 2]
]
amount_of_questions = [100,200,300,400,500,600,700,800,900,1000]
total_amount = 0
# loops for showing all the questions and options
i=0
for question in questions:
    print(f"The question is : {question[0]} ")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
  

    # error handling to do not program stop 
    try:
        answer = int(input("Enter the number which option you like to choose: "))
    except ValueError:
        print("Invalid input. Please enter a number.")

    if answer == question[4]:
        print("You got it right! you win the prize! ")
        total_amount += amount_of_questions[i]
        # total_amount.append(amount_of_questions[i])
        i += 1
    else:
        print("Sorry, that's incorrect. Total amount won: ", total_amount)
        break