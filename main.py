import random #import random library so the random parts of the code work
import time #imports time library so Bert and Ernie's alphabet game counter work

def generate_random_letter():   #creates function that gives the code a different random letter every time it starts
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return random.choice(alphabet)


def get_valid_integer(prompt): #it substitutes the int(input()), so the user gets a message to input a number and the code gets no errors
    while True:
        user_input = input(prompt)
        if user_input.isdigit():  # checks if the input is a digit
            return int(user_input)  # returns the input as an integer
        else:
            print(" ")
            print("[That's not a valid number. Please try again.]")
            print(" ")
            #OBS: I didn't put a valid one for strings because the code doesn't need it/won't crash without it.


def main_menu(): #the function that stores all the other game functions! It works as a menu

    select_char = get_valid_integer("""Which friend would you like to visit first? Select from the following numbers:
    Type '1' for Cookie Monster Search for Cookies Game
    Type '2' for Big Bird Shapes Game
    Type '3' for Elmo Colors Game
    Type '4' for Bert and Ernie Alphabet Game
    Type '5' for Bert and Ernie Opposites Game
    Type '6' for Count Von Count Math Games
    Type '7' for Groover Food Choices Game
    Type '8' for credits plus exit!
Choice: """)


    if select_char == 1:    #if user inputs 1, they get..
        cookie_monster_game() #..cookie monster's game, which is stored in that function.
    elif select_char == 2:
        big_bird_game()
    elif select_char == 3:
        elmo_game()
    elif select_char == 4:
        bert_ernie_alphabet_game()
    elif select_char == 5:
        bert_ernie_opposite_game()
    elif select_char == 6:
        count_von_count_math_game()
    elif select_char == 7:
        groover_game()
    elif select_char == 8:    #till here, all above where the same idea as the example of the input 1.
        say_goodbye() #but here the code will bring the user to the end plus credits
    else:
        print("Oops! Try again! Pick a number from the list.") #if user doesn't select a number from the list which would be from 1 to 8
        print(" ")
        main_menu() #then it returns the user to main_menu so they can select from the avaliable options

def cookie_monster_game(): 
        
        COOKIES = 0 #you start with 0 cookies, this variable can change depending on the choices made.
        print("You choose: Cookie Monster! Quick, hide your cookies, your fridge and your wall! The big boy is hungryyy!!")
        print(" ")
        print("You enter Hooper's Store. Cookie Monster is desperate for...Cookies! Alan decided to help his anxiety and also play a little fun game with him. The place smells like fresh baked goods.")
        print(" ")
        time.sleep(0.3) #delays the code
        print(f"Cookie Monster: OH! HELLO! ME COOKIE MONSTER. ME LOVE COOKIES AND ME MONSTER. SO ME COOKIE MONSTER. ARE {name} SOME FOOD MONSTER TOO?")
        food_cookie = str(input(f"Cookie Monster: WHICH IS {name} FAVORITE FOOD?:")) #stores input into variable. The f string makes the code more friendly to store variables/functions and show it to the user already formatted.
        print(f"Cookie Monster: GOT IT. {name} IS {food_cookie} MONSTER. LIKE ME. ME COOKIE MONSTER. BUT ME REAL NAME IS SID. ANYWAY, CAN {food_cookie} MONSTER HELP ME FIND THE COOKIES???? ME NEED COOKIEEEEEEES!!!") 
        time.sleep(0.5) #delays the code
        print("Cookie Monster: ...")
        time.sleep(0.5) #delays the code
        print("Cookie Monster: Thank you.")
        print("")
        time.sleep(0.2) #delays the code
        print("Let's search for Cookie Monster delicious cookies! ")
        print(" ")

        while True:  #while true means that piece of code will continue working in loop so it won't break even if the user keeps reselecting the options!
            cookie_choices() #calls the function with all the options for cookie monster's search game
            if cookie_choices_select == 1:  #if user input 1, they get the text .
                print(" ")
                print("Cookie Monster lifts the lid of the old purple cookie jar. There are some crumbles in there. Maybe if we put the crumbles together it will make one cookie?")
                time.sleep(0.3) #delays the code
                print("...")
                time.sleep(0.3) #delays the code
                print("No. But Cookie Monster ate the crumbles anyway.")
                time.sleep(0.3) #delays the code
            if cookie_choices_select == 2:
                print(" ")
                print("Cookie Monster is shaking the birdseed box. The box didn't do anything. Big Bird approached and traded a cookie with Cookie Monster for the birdseed box.")
                time.sleep(0.3) #delays the code
                print("Cookie Monster: COOOOOKIIIIIEEEEEEEEEEE! ON NOM NOM NOM")
                time.sleep(0.3) #delays the code
                COOKIES = COOKIES + 1  #It gives one more cookie for the amount the user already have!
                print(" ")
            if cookie_choices_select == 3:
                print(" ")
                print("Cookie Monster gets near the cashier where Alan is. Cookie Monster looks at him with pleading googly eyes.")
                time.sleep(0.3) #delays the code
                print("Cookie Monster: ALAN... ME HUNGRY. ME VERY, VERY HUNGRY MONSTER. ME STOMACH DOESN'T STOP GRUMBLING! COULD YOU PLEASE GIVE ME A COOKIE??? PLEASE?")
                time.sleep(0.3) #delays the code
                print("Alan sighs, and smiles.")
                print("Alan: Yes, Cookie Monster. I'll give you a cookie. But keep trying to find the others, okay?")
                time.sleep(0.3) #delays the code
                print("Cookie Monster: COOOOOOKIEEEEEEEEEEE!! ON NOM NOM")
                time.sleep(0.3) #delays the code
                print(" ")
                COOKIES = COOKIES + 1 #add one more cookie to the value the user got
            if cookie_choices_select == 4:
                print(" ")
                print("Cookie Monster starts to shout in the store dramatically.")
                time.sleep(0.3) #delays the code
                print("Cookie Monster:OOOOOH, ME SO SO HUNGRY! COOOOOKIEEEEES. WHERE IS THE COOKIES...")
                time.sleep(0.3) #delays the code
                print("Cookie Monster screams so much that a box falls out of the shelf. There are two cookies there.")
                time.sleep(0.3) #delays the code
                print(" ")
                COOKIES = COOKIES + 2 #add teo more cookie to the value of cookies the user has
            if cookie_choices_select == 5:
                print(" ")
                print("Cookie Monster got so hungry that it decided to munch on the wall. Alan is definitely concerned with the blue friend.")
                time.sleep(0.3) #delays the code
                print("Cookie Monster teeth shape is now permanently on the wall.")
                time.sleep(0.3) #delays the code
                print("Cookie Monster still thought the wall was delicious.")
                time.sleep(0.3) #delays the code
                print(" ")
            if cookie_choices_select == 6: #the option that ends the cooiie monster game
                print(" ")
                print(f"Cookie Monster got {COOKIES} Cookies!") #display the final cookies quantity that the user could get through this game
                print(f"THANK YOU TO HELP ME, {food_cookie} MONSTER! ME NOW WILL GIVE {food_cookie} MONSTER HALF THE COOKIES, ME AND YOU ARE FRIENDS!")
                cookie_half = int(COOKIES/2) #it divides the quantity of cookies by two
                print(f" You now have {cookie_half} cookies!") #cookie monster gave the user half of the cookies! 
                print(" ")
                print("[COOKIE MONSTER ENDING]")
                time.sleep(0.3) #delays the code
                main_menu() #returns to the character options menu
       
def big_bird_game():
    
    print("You choose: Big Bird! Let's all be Birdketeers together!")
    print(" ")
    print("You're walking on Sesame Street when you see a really tall yellow bird just getting out of an equally as big nest! He seems very friendly. He approaches you. It's as tall as a tree.")
    print(" ")
    time.sleep(0.3) #delays the code
    print(f"Big Bird: Oh! Hello! I'm Big Bird.. You're the new neighbor, right? You could be a Birdketeer, {name}! Being a birdketeer means we play all the time and help each other!")
    time.sleep(0.3) #delays the code
    print("Big Bird: Would you like to play now? I have a fun game I play with Snuffleupagus!")
    print(" ")
    time.sleep(0.3) #delays the code
    print("Big Bird: In that game, I say an object and you need to say which shape it is. But it's very easy because the shapes will only be Circle, Square, or Triangle! ")
    time.sleep(0.3) #delays the code
    print(" ")
    big_bird_dict_game() 


def big_bird_dict_game():  #made a one more function so when user restarts the game they won't see Big Bird's introduction again
    
    shape_dict_bird = {
    "Ball" : "circle",
    "Ring" : "circle",
    "Sun" : "circle",
    "Eyes" : "circle",
    "Orange" : "circle",
    "Cookie" : "circle",
    "Bottlecaps" : "circle",
    "Wheel" : "circle",
    "Balloon" : "circle",
    "Box" : "square",
    "Window" : "square",
    "Ice cube" : "square",
    "Chessboard" : "square",
    "Dice" : "square",
    "Television" : "square",
    "Portrait" : "square",
    "Pillow" : "square",
    "Clothes Hanger" : "triangle",
    "Pizza slice" : "triangle",
    "Pyramid" : "triangle",
    "Traffic Cone" : "triangle",
    "Carrot" : "triangle",
    "House Roof" : "triangle",
    "Tent" : "triangle",
    "Party Hat" : "triangle"
    } #the dictionary is what makes the game since the code gives user the first part (keys), and the user has to give the answer matching the second one (values)
    
    for i in range(3):
        print(" ")
        random_word_bird = random.choice(list(shape_dict_bird.keys())) #it creates a variable that stores the code that gets the keys on the dictionary list, then gives a random one
        print(f"Big Bird: The object is {random_word_bird}!") #display the random key
        user_answer_shape = str(input("Big Bird: Which shape do you think it'll be? Remember that the answer is either Circle, Square, or Triangle! Answer: ")).lower() #the .lower() makes all letters to be converted into lower case so the user can answer in caps lock and the code will still work
        correct_bird_answer = shape_dict_bird[random_word_bird] #creates variable that stores the dictionary list with the given random key

        if shape_dict_bird[random_word_bird] == user_answer_shape: #checks if random key matches with the storaged value
            print(" ")
            print(f"Big Bird: Yes! The shape was {correct_bird_answer}! You got it right, Yay!") #the use of f string to show the user the correct answer
        else:
            print(" ")
            print(f"Big Bird: Aww, that's not it! The shape was: {correct_bird_answer}! But it's okay, let's play more!") #the use of f string to show the user the correct answer
    print(" ")
    big_end = str(input("Big Bird: Wow, that was fun! Want to play more? Select any key for yes, but 'q' to go home! "))

    if big_end.lower() == "q": #User types q, gets bye message and returns to main menu of characters choice. The .lower() makes all letters to be converted into lower case so the user can answer in caps lock and the code will still work
         print(" ")
         print("Big Bird: Oh, really? So soon? Well, now you're an honorary member of the Birdketeers! So come visit me anytime, okay? Bye!")
         print(" ")
         time.sleep(0.3) #delays the code
         main_menu()
    else: #if anything else is inputed, the game restarts
        print(" ")
        print("Big Bird: Yay! Let's learn more about shapes together! We can commemorate this with a delicious birdseed milkshake!")
        time.sleep(0.3) #delays the code
        print("[You received a Birdseed Milkshake. It has a lot of little chunks of seeds but is surprisingly good. Big Bird seems happy.]")
        time.sleep(0.3) #delays the code
        big_bird_dict_game()
        

def bert_ernie_alphabet_game(): #Function of Bert and Ernie Game of Alphabet
    
    print("You choose: Bert and Ernie Alphabet Game! Let's play with the alphabet!")
    print(" ")
    time.sleep(0.3) #delays the code
    print("You enter a nice cozy apartment on Sesame Street. The place has a mixture of its owners all around: The contrast of an entire shelf filled with books...with toys spread all around. A nice shared room, with one half organized neatly and the other, a mess with clothes on the floor.") 
    time.sleep(0.3) #delays the code
    print(" ")
    print("Ernie: Oh, hi! Welcome to Sesame Street! We're really happy to have you here, pal.")
    time.sleep(0.3) #delays the code
    print("Bert: Who are you talking with, Ernie? [Bert sighed before noticing that's not a play of Ernie, but YOU, the new neighbor.] Oh, Hi!")
    time.sleep(0.3) #delays the code
    print("Bert: Erniie! Why didn't you told me there were visitors? [Bert asked the shorter man.]")
    time.sleep(0.3) #delays the code
    print(f"Ernie: They just got there, Bert! [Ernie smiled.] You appeared in a great time, {name}! Bert and I were about to play an alphabetic name!.")
    time.sleep(0.3) #delays the code
    print("Bert: Yes. The game consists of writing only words that starts with the given letter. Is an amazing game.")
    time.sleep(0.3) #delays the code
    print("Ernie: It could be very boring though so I added a time counter to it!")
    time.sleep(0.3) #delays the code
    print(f"Bert: Erniie! It was not boring before. Also, {name}, we don't check if the word is correct, so me and Ern will trust you to play it without cheating, okay?")
    time.sleep(0.3) #delays the code
    print("Ernie: Yeah! That way is more fun! We're okay with you misspelling it, but don't create new words or Bert get mad.")
    time.sleep(0.3) #delays the code
    print("Bert: Of COURSE I get mad, Ernie! Duckiessaurus is not a real word!!!!")
    time.sleep(0.3) #delays the code
    print("Ernie: It could have been, Bert... maybe they discover a new dinosaur species..think about it, Bert...")
    time.sleep(0.3) #delays the code
    print("Bert: Uuugh, Ernie, no! [Bert groaned in annoyance, but he couldn't help the other shenanigans and ended up laughing. He couldn't get really mad with Ernie.]")
    time.sleep(0.3) #delays the code
    print(" ")
    print("Let's get started! In that game, we are going to put the maximum of words you can remember in 30 seconds. Try to put only real words and not new ones, no matter how creative! Bert likes it better that way. That way, you can try the game in English or in your mother language too. Fun, right? Also, if you put a word that's not the first letter given, the game ends.")
    time.sleep(0.3) #delays the code
    print(" ")
    # Pause introduced for the story
    bert_ernie_alphabet_game_start() 

def bert_ernie_alphabet_game_start(): #Function created so if user wants to replay the game, the introduction will not show up again
    
    input("Press Enter to begin your adventure!")
    print(" ")
    print(" ")

    while True:  #the while true is what makes the code restart in a loop
        
        random_letter = random.choice('abcdefghijklmnopqrstuvwxyz') #it calls the random module that picks a random letter
        print(f"\nType words starting with the letter: {random_letter.upper()}") #gets a random letter to be displayed. The upper() makes all the letters to be converted into caps lock!
        
        print("That's the letter of the day, hey, heey, the letter of the day!") #little reference to the song "Letter of the Day"

        #start score + time limit
        score = 0 #score will change if the user get the answers right
        time_limit = 30  # 30 seconds is the time limit then the game ends
        start_time = time.time()  # Record the start time

        while True:
            # Check time that has passed
            current_time = time.time()
            passed_time = current_time - start_time
            remaining_time = time_limit - passed_time

            if remaining_time <= 0: #If the time is over, the text will be displayed and the game 'breaks', aka the loop stops
                print("Time's up!")
                break
            
            #get answer
            print(" ")
            word = input(f"Enter a word for the letter above! (Time left: {int(remaining_time)} seconds): ") #the f string helps the remaining time to be displayed for the user at each time the answer is sent
            print(" ")
            
            #check if word starts with the correct letter
            if word.lower().startswith(random_letter): 
                score += 1  # Update score so the user gets plus one
                print(" ")
                print(f"Ernie: Yay, you got another right!")
                print(f"Bert: Good job! Learning is so fun, hahaha")
                print(" ")
            else:
                # End the game if the user inputs a answer without the first letter being the given one
                print(f"Bert: Oh, I'm afraid it doesn't start with the correct letter, so the game is finished for now. But don't be sad, you can always play again with us!")
                print(" ")
                break
        
        print(f"Ernie: Hey! Your total Rubber Duckies is {score}!") #shows the user final score for the first time
        time.sleep(0.3) #delays the code
        print("Bert: 'Rubber Duckies', Ernie? Don't you mean 'score'??")
        time.sleep(0.3) #delays the code
        print(f"Ernie: I think Rubber Duckies make things better, Bert. I would rather win a lot of Rubber Duckies than another kind of little points!")
        time.sleep(0.3) #delays the code
        print(f"Bert:...Ernie...I give up trying to be rational. Okay, then, your total of, uh, Bottlecaps is {score}.")
        time.sleep(0.3) #delays the code
        print(f"Ernie: 'Bottlecaps', Bert? Noo, it should be 'total score is {score}' or the others will not understand, Bert.")
        time.sleep(0.3) #delays the code
        print(" ")
        print("Bert sighed exasperated because of Ernie's usual antics, while Ernie just chuckled.")
        print(" ")
        time.sleep(0.3) #delays the code

        play_again = input("Do you want to play again? Type any letter to play again, or hit 'q' to exit! ")
        if play_again.lower() == 'q': #if user types q they return to main menu
            print(" ")
            print("Ernie: Aw, really? Going so soon? Well, okay! Me and Bert can't wait to see you again, friend!")
            time.sleep(0.3) #delays the code
            print("Bert: Ern is right. Visit us anytime you want to. Thanks for playing!")
            time.sleep(0.3) #delays the code
            print("Bert and Ernie: Goodbye!!!")
            time.sleep(0.3) #delays the code
            print("While you exit the apartment, you can see the two are still laughing and playing with each other.")
            print(" ")
            time.sleep(0.3) #delays the code
            main_menu()
        else: #anything else restarts the game with a new first letter of the word
            print("Ernie: Yay! Let's play again!")
            print("Bert: It'll be wonderful to play another round!")
            time.sleep(0.3) #delays the code
            bert_ernie_alphabet_game_start()

def bert_ernie_opposite_game(): #Bert and Ernie function for the opposite game
    
    print("You choose: Bert and Ernie's Opposite Game! Have fun with the duo!")
    print(" ")
    time.sleep(0.3) #delays the code
    print("Ernie: It's good and great to have differences! Me and Bert for example, we get along so well and we are so different!")
    time.sleep(0.3) #delays the code
    print("Bert: Yeah! I like to read books while Ernie's upstairs playing his drums.")
    time.sleep(0.3) #delays the code
    print("Ernie: Bert likes plain foods and I like flavorful ones!")
    time.sleep(0.3) #delays the code
    print("Bert: I like organization, but Ernie doesn't seem to mind throwing his clothes all around the apartment.")
    time.sleep(0.3) #delays the code
    print("Ernie: Bert likes to take showers, and I appreciate taking baths and playing with my rubber duckie!! [Ernie squeezes a yellow duck made of rubber.]")
    time.sleep(0.3) #delays the code
    print("Bert: I like to sleep early, and SOMEONE likes to wake me up out of nowhere in the middle of the night because they're bored. [glares at Ernie]")
    time.sleep(0.3) #delays the code
    print("Ernie: Oh, I wonder who's that someone may be, Bert. [Ernie chuckles as Bert sighs exasperated.]")
    time.sleep(0.3) #delays the code
    print("Bert: Anyway, what we mean is, that being different from each other doesn't mean you can't get along. Ernie and I always find ways to do something we both like and to solve things by talking. We do care about each other and we think the differences are what make us, us.")
    time.sleep(0.3) #delays the code
    print("Ernie: That's why the game we'll play is to celebrate the differences! An opposite game!")
    print(" ")
    time.sleep(0.3) #delays the code
    print("Bert:But Ernie, different is, well, different from opposites. Opposites are usually directly the opposite.")
    time.sleep(0.3) #delays the code
    print("Ernie:... Oh! That makes sense, Bert. Makes sense.")
    time.sleep(0.3) #delays the code

    print("Bert: We'll give you a hint. The opposite of the sun would be the moon.")
    time.sleep(0.3) #delays the code
    print("Ernie: And the opposite of cookies is cookie monster.")
    time.sleep(0.3) #delays the code
    print("Bert: Cookie Monster, Erniie? They're not opposites!")
    time.sleep(0.3) #delays the code
    print("Ernie: Mm, I don't know, Bert..I mean, when Cookie Monster is near a cookie it ceases existing quickly.")
    time.sleep(0.3) #delays the code
    print("Bert: Yeah! But opposites don't mean they can't coexist at the same time!")
    time.sleep(0.3) #delays the code
    print("Ernie:...Then why when something is open, like a door, can't be closed?")
    time.sleep(0.3) #delays the code
    print("Bert: Because some things can't coexist at the same time while some can, Ernie. Open and Close are an opposites example that can't coexist at the same time.")
    time.sleep(0.3) #delays the code
    print("Ernie: Then Rubber Duckie and Bernice are opposites.")
    time.sleep(0.3) #delays the code
    print("Bert: Ernie, Rubber Duckie and my pet pigeon Bernice are not opposites!")
    time.sleep(0.3) #delays the code
    print("Ernie: They kinda are Bert. Rubber Duckie is a duck, and Bernice is a pigeon. They're different.")
    time.sleep(0.3) #delays the code
    print("Bert: But that logic doesn't apply to the game, Erniiie! Different and Opposites are not the same thing!")
    time.sleep(0.3) #delays the code
    print("Ernie:...but why, Bert?")
    time.sleep(0.3) #delays the code
    print("Bert: Ernie. Just..  [sigh]. Let's start the game..")
    time.sleep(0.3) #delays the code
    print(" ")
    print(" ")
    print("[THE OPPOSITE GAME]")
    print("The game of opposites is meant for you to say what is the direct opposite of the word we'll give you!")
    time.sleep(0.3) #delays the code
    print("Let's begin! ")
    time.sleep(0.3) #delays the code
    print(" ")
    bert_ernie_opposite_game_start()
    
def bert_ernie_opposite_game_start(): #new function for the actual game because if the user wants to replay they'll jump the introduction

    opposites_dict = {
    "happy": "sad",
    "sugar" : "salt",
    "day" : "night",
    "dog" : "cat",
    "sunny" : "rainy",
    "fast" : "slow",
    "less" : "more",
    "start" : "finish",
    "empty" : "full",
    "left" : "right",
    "up" : "down",
    "hot" : "cold",
    "early" : "late",
    "open" : "close",
    "young" : "old",
    "tall" : "short",
    "small" : "big",
    "weak" : "strong",
    "black" : "white",
    "low" : "high",
    "ask" : "answer",
    "above" : "bellow",
    "exciting" : "boring",
    "laugh" : "cry",
    "win" : "lose",
    "sweet" : "sour",
    "maximum" : "minimum",
    "indoor" : "outdoor",
    "inside" : "outside",
    "near" : "far",
    "dry" : "wet",
    "negative" : "positive",
    "clean" : "dirty"
   } #the game dictionary. the game will give keys and the user will need to input the right answers which is the key values.



    for i in range(3):
        print(" ")
        random_opposite = random.choice(list(opposites_dict.keys())) #creates variable that stores the dictionary list of the words, then pick a random key(first part) out of the dictionary.
        user_opposite_answer = str(input(f"What's the opposite of {random_opposite}?: ")).lower() #makes all letters be in lower case
        correct_opposite = opposites_dict[random_opposite] #creates variable that stores the dictionary of words and the random given key.

        if opposites_dict[random_opposite] == user_opposite_answer: #if the random key matches with the answer given by the user (which should be the value) they're right
            print(" ")
            print(f"Ernie: You're right! The answer was {correct_opposite}!! You know well about opposites!") #shows the correct answer/value of the key
            print(" ")
        else: 
            print(" ")
            print(f"Bert: Oops! Not quite. The correct answer for that is the opposite word: {correct_opposite}. But that was a great guess!") #shows the correct answer/value of the key
            print(" ")
    print(" ")
    time.sleep(0.3) #delays the code
    print("Ernie: What a great game!!")
    opposites_end = input("Bert: If you'd like to play again, press any key. If you want to return to the menu, press 'q'.") #stores user input into variable


    if opposites_end.lower() == "q": #if user input is equal to q, they'll return to main_menu
        print(" ")
        time.sleep(0.3) #delays the code
        print("Bert:Did you understand what is opposites now, Ernie? ")
        time.sleep(0.3) #delays the code
        print("Ernie: Now I do Bert! Different would be when we have the yellow and orange colors! They're colors, but not opposite like it would be with black and white.")
        time.sleep(0.3) #delays the code
        print("Bert: That's right, Ern. Different can be only different, like us.")
        time.sleep(0.3) #delays the code
        print("Ernie: And the opposite would be the fact I'm really fun, Bert. And the other opposite is you.")
        time.sleep(0.3) #delays the code
        print("Bert: That's right, Ern-.. Hey! What you meant by that?!")
        time.sleep(0.3) #delays the code
        print("[Ernie chuckles and leaves Bert totally flabbergasted]")
        time.sleep(0.3) #delays the code
        print("Bert: Ern, come back here! I'm fun! I'm plenty of fun!")
        time.sleep(0.3) #delays the code
        print("[You can hear Bert and Ernie in the distance, where Ernie's tease seems to work with Bert as always. Despite that, the two would be laughing with each other as soon as the tall notices it's just Ernie being playful as usual.]")
        time.sleep(0.3) #delays the code
        print(" ")
        main_menu()
    else: #any other input restarts that opposite game
        print(" ")
        time.sleep(0.3) #delays the code
        print("Ernie: Hooray! Let's play again! More differences!")
        time.sleep(0.3) #delays the code
        print("Bert: Opposites, Ernie- Wait, you're just teasing me now, aren't you?!")
        time.sleep(0.3) #delays the code
        print("[Ernie chuckles and Bert sighs.]")
        time.sleep(0.3) #delays the code
        print(" ")
        bert_ernie_opposite_game_start()

def count_von_count_math_game(): #Count function for the math games
    
    print("You choose: Count Von Count! Let's play with math on the not-so-scary vampire castle!")
    time.sleep(0.3) #delays the code
    print(" ")
    print("You enter a large castle in the high mountains of Sesame Street. A friendly vampire who has the personality of a sweet mathematician teacher greets you. The walls are old and antique, with little smiling living bats all around the ceiling and a big organ instrument in the living room. You feel strangely safe.")
    print(" ")
    time.sleep(0.3) #delays the code
    print("Count Von Count: Greetings! Oh, no, don't vorry abovt the bats! They're up to date with their vaccines and don't bite. How may I help you? Oh? Games?")
    time.sleep(0.3) #delays the code
    print("Count Von Count: Vat's vonderful! Ve could play math games, it can be so fun! I'll give you two values and you need to answer the right value, okay? Ve'll do Three tvrns! My bats vill play too!")
    time.sleep(0.3) #delays the code
    print(" ")
    print("Count Von Count: Vhat vould you like to play?")
    print(" ")
    count_von_menu() #displays a function so the user can choose which math game they want to play

    while True: #gets the code working everytime the user picks option
        if count_game == 1:
            print("ADDICTION GAME")
            count_addiction() #calls that function and start addiction game
        elif count_game == 2:
            print("SUBSTRACTION GAME")
            count_subtraction() #calls that function and start subtraction game
        elif count_game == 3:
            print("MULTIPLY GAME")
            count_multiply() #calls that function and starts multiplication game
        elif count_game == 4:
            print("DIVISION GAME")
            count_divide() #calls that function and starts division game
        else: #if any other number is selected, it'll make the user exit the count von count game code and return to main_mennu with all the characters games to choose
            print("Count Von Count: Thank you to visiting me. Please, come back anytime for more math games! Bye, Bye!!")
            time.sleep(0.3) #delays the code
            print("Leaving in 3...")
            time.sleep(1) #delays the code
            print("2...")
            time.sleep(1) #delays the code
            print("1...")
            time.sleep(1) #delays the code
            print("Ah! Ah! Ah! [Thunderbolt and Lightening noises. You left the castle behind.]")
            time.sleep(0.3) #delays the code
            print(" ")
            
        main_menu()

def count_addiction():
    for i in range(3):
        sum1 = random.randint(0,999) #picks random number from 0 to 999
        sum2 = random.randint(0,999) #picks random number from 0 to 999
        some = sum1 + sum2 #picks the given random numbers and some their values
        count_answer_some = get_valid_integer(f"Count Von Count: Vat's the value of {sum1} little bats Plus (+) {sum2} little bats? ") #get_valid_integer function so only numbers are accepted and the code gets no error

        if some == count_answer_some: #comparation of right answer with user given answer
            print(" ")
            print(f"Count Von Count: Vat's correct! {sum1} little bats plus {sum2} little bats is equal to {some} little bats! Ah! Ah! Ah! [Thunderbolt and Lightning sounds.]")
            print(" ")
        else:
            print(" ")
            print(f"Count Von Count: That vas a good try, but {sum1} bats plus {sum2} is equal to {some} little bats! Vat's ok! Keep playing and learning! Mistakes are a healthy part of the jovrney.")
        print("Count Von Count: Let's start again!")
        print(" ")
    count_quit_or_again = str(input("Count Von Count: Let's play again, press any key to continve or 'q' to return to the menu for more options! "))
    print(" ")
    

    if count_quit_or_again.lower() == "q":
        count_von_menu() #returns to count von count menu, to select a new math game or exit to main menu
    else:
        count_addiction() #restarts that addiction game

        
def count_subtraction(): #function for the subtraction game
    for i in range(3):
        sub1 = random.randint(0,999) #gives random number from 0 to 999
        sub2 = random.randint(0,999) #gives random number from 0 to 999
        subtract = sub1 - sub2 #subtract those two random values
        print("Count Von Count: Remember! Sometimes, the nvmbers can be negative, so put a - (minus) sign in front of them if vat's the case!")
        print(" ")
        count_answer_subtr = get_valid_integer(f"Count Von Count: Now, Ve have {sub1} little bats. How many ve vould have if {sub2} little bats got subtracted? ")#get_valid_integer function so only numbers are accepted and the code gets no error

        if subtract == count_answer_subtr: #if user answer is equal to the right answer
            print(" ")
            print(f"Count Von Count: Vat's absolutely correct! {sub1} bats minus {sub2} bats is eqval to {subtract} little bats! They all flew away! Ah, Ah, Ah! [Thunderbolt and Lightning sounds. Little wings of bats can be heard flying in the background happily.]")
            print(" ")
        else: #if user answer is different from right answer
            print(" ")
            print(f"Count Von Count: Ah, not qvite! Bvt a good try, mistakes happen and are part of learning! {sub1} bats minus {sub2} bats eqvals to {subtract} bats! They decided to go play!")
            print(" ")
    
    count_quit_or_again = str(input("Count Von Count: Let's play again? Press any key to continve or 'q' to return to the menu for more options! "))
    print(" ")

    if count_quit_or_again.lower() == "q":
        count_von_menu() #if selected q,the user will return to count menu to choose between a new math game or to exit to main_menu
    else:
       count_subtraction() #restart the subtraction game

def count_multiply(): #game of the multiplication
    for i in range(3):

        mult1 = random.randint(0,99) #picks random number from 0 to 99
        mult2 = random.randint(0,99) #picks random number from 0 to 99
        multiply = mult1 * mult2 #multiply the two random values given above
        count_answer_mult = get_valid_integer(f"Count Von Count: So let's begin! Vat's is the mvltiplication of {mult1} bats and {mult2} bats? ")#get_valid_integer function so only numbers are accepted and the code gets no error

        if multiply == count_answer_mult: #if user answer is equal to right answer
            print(" ")
            print(f"Count Von Count: You've got it! The mvltiplication of {mult1} bats and {mult2} bats is {multiply}! A lot of new baby bats! Ah! Ah! Ah! [Thunder and Lightning sounds.]")
            print(" ")
        else: #if user answer is different from right answer
            print(" ")
            print(f"Count Von Count: Great try, bvt not qvite! {mult1} bats multiplied with {mult2} bats are equal to {multiply}! Mistakes happen, keep learning!")
            print(" ")
    count_quit_or_again = str(input("Count Von Count: Vant to play again? press any key to continve or 'q' to return to the menu for more options! "))
    print(" ")

    if count_quit_or_again.lower() == "q":
        count_von_menu() #if user selects q they will return to count menu where the math games are 
    else: 
        count_multiply() #if anything else is selected, restarts the multiply game

def count_divide():
    for i in range(3):

        divis1 = random.randint(1,999) #picks random number from 1 to 999
        divis2 = random.randint(1,40) #picks random number from 1 to 40
        divisions = int(divis1  / divis2) #divide the two random numbers from above
        print("Count Von Count: A hint! The nvmbers answers are rounded! They're integers!")
        print(" ")
        count_answer_divide = get_valid_integer(f"Count Von Count: If you have {divis1} apples to divide for {divis2} little bats. How many apples can you give to the bats? ")#get_valid_integer function so only numbers are accepted and the code gets no error
    
        if divisions == count_answer_divide: #if user answer is equal as the right answer
            print(" ")
            print(f"Vat's vonderful! That's exactly it, {divis1} apples to divide for {divis2} bats means you give them {divisions} apples! Vat cute little hvngry bats! Ah! Ah! Ah! [Lightning and Thunder sounds. Bats munching on apples can be heard nearby.]")
            print(" ")
        else: #if user answer is different from the right answer
            print(" ")
            print(f"Oh, not really! If you have {divis1} apples and vants to share vit the little {divis2} bats, you need to give them {divisions} apples! Keep trying, mistakes are okay and ve learn that vay!")
            print(" ")
    print(" ")
    count_quit_or_again = str(input("Count Von Count: Let's play again, press any key to continve or 'q' to return to the menu for more options! "))
    print(" ")
    
    if count_quit_or_again. lower() == "q":
        count_von_menu() #if user selects q, they'll return to count menu so they choose another math game or quit to main_menu
    else:
        count_divide() #any other input will restart the division game

def groover_game(): #created the groover game function 


#Food chart for reference, it doesnt change nothing in the code and it could be deleted
    cookie = 2 
    chocolate_breakfast = 1
    chocolate_middle_day = 3
    salad_bowl = 3
    banana = 3
    oatmeal = 6 #The higher score because 1. it's breakfast, 2. It's Bert's recommendation.
    lollipop = 1
    chips = 1
    balanced_meal = 4
    ethnic_meal = 4
    skip_snack = -1
    skip_breakfast = -6 #The most important meal of the day!
    skip_lunch = -5
    skip_dinner = -2
    birdseed_milkshake = 5
    apple = 5
    pasta = 3
    hamburger_fries = 3


    health = 0 #the health starts with 0. It can increases or decreases depending on the meal choices.
    #the health value is what decides one of the three endings

###the Introduction plus Breakfast scene.
    print("You choose: Groover! We're gonna have food adventures!")
    time.sleep(0.3) #delays the code
    print(" ")
    print(" ")
    print("It's a beautiful day on Sesame Street! Your friend Groover wants help on what to eat during the day.")
    time.sleep(0.3) #delays the code
    print("Groover: Oh, hello! It's me, your furry lovable favorite monster Groover! I want to play Super Groover tomorrow but I need to eat super healthy to go through the day with energy! Can you help me pick foods to go through the day? ")
    time.sleep(0.3) #delays the code
    print(" ")
    print(" ")
    print("GROOVER's BREAKFAST")
    answer_break = input("""Choose an option for Groover breakfast!: 
    type 'a' for oatmeal [Bert's recommendation!]
    type 'b' for a banana
    type 'c' for a chocolate
    type anything to skip the breakfast
    Choice: """) #gets user input

    #The lower() transforms letters into lower case.

    if answer_break.lower() == "a": #if user chooses a. 
        health += 6 #add six to health counter
        print(" ")
        print("Groover: I just ate a healthy oatmeal! Yum!")
        print(" ")
    elif answer_break.lower() == "b":
        health += 3 #add three to health counter
        print(" ")
        print("Groover: I ate a banana! Healthy and nutritious.")
        print(" ")
    elif answer_break.lower() == "c":
        health += 1 #add one to health counter. To eat is better than not.
        print(" ")
        print("Groover: An odd choice for breakfast but still delicious!")
        print(" ")
    else:
        health += -6 #Decreases six from the health counter. Breakfast is the most important meal of the day
        print(" ")
        print("Groover: My little stomach feels empty now...")
        print(" ")

###The lunch time
    print(" ")
    time.sleep(0.3) #delays the code
    print("GROOVER's LUNCH")
    print(" ")
    print(" ")
    time.sleep(0.3) #delays the code
    print("[It's the middle of the day now. After playing, Groover decided it was great to take a pause and rest, and while doing so, the lunch was just ready!]")
    time.sleep(0.3) #delays the code
    print("Groover: Oh, I love lunchtime. It's a perfect hour of the day. I wonder what I'll eat today.")
    time.sleep(0.3) #delays the code

    answer_lunch = input("""What will Groover eat today for lunch? Help him with that great task!
    Type 'a' for a balanced meal with rice, salad, protein and fiber!
    Type 'b' for chips, delicious packaged chips.
    Type 'c' for a delicious ethnic meal!
    Type anything else to skip lunch.
    """)

    if answer_lunch.lower() == "a":
        health += 4 #add four to health counter
        print(" ")
        print("Groover: Oh, that balanced meal was just delicious!")
        print(" ")
    elif answer_lunch.lower() == "b":
        health += 1 #add one to health counter
        print(" ")
        print("Groover: How can chips be so good? I can even lick the leftovers off my fingers!")
        print(" ")
    elif answer_lunch.lower() == "c":
        health += 4 #add four to health counter
        print(" ")
        print("Groover: Wow! What a delicious food! I feel so energized!")
        print(" ")
    else:
        health += -5 #decreases five from the health counter. Don't skip meals.
        print(" ")
        print("Groover: I wish I hadn't skipped the lunch...")
        print(" ")
    
###Middle of the day snack
    time.sleep(0.3) #delays the code
    print("GROOVER's MIDDLE OF THE DAY SNACK")
    print(" ")
    print(" ")
    time.sleep(0.6) #delays the code
    print("[After the lunchtime, Groover returned outside. It was just in time for his part-time job as a waiter. While Mr. Johnson waited impatiently for his meal, Groover planned his own. After all, it was the middle of the day! It had been a while since Groover had eaten.]")
    time.sleep(0.6) #delays the code
    print("Groover: I'm going to Hooper's Store while Mr. Johnson's food is being made! I'm sure it'll give me plenty of time to go, eat, and come back!")
    time.sleep(0.6) #delays the code
    print("[Groover walks out of the restaurant and follows Hooper's Store direction. There, he can see Cookie Monster shaking a birdseed box while Big Bird looks at him, puzzled and curious. Groover looked at Alan, who was talking with Gordon.]")
    time.sleep(0.6) #delays the code
    print("Groover: Hello Alan, Hello Gordon! Alan, I'm hungry and would like to eat something!!!")
    time.sleep(0.6) #delays the code
    print("Alan: Oh, we have plenty of delicious and also healthy options here at Hooper's Store!")
    time.sleep(0.6) #delays the code
    print("Help Groover decide which snack he should eat right now.")

    answer_middle_day = input("""
    Type 'a' for a birdseed milkshake (if Cookie Monster ever stops shaking the birdseed box.)
    Type 'b' for a small chocolate bar
    Type 'c' for a chocolate chip cookie...
    Type anything else to change Groover's mind and go away, eating nothing at all.
    """) #gets user input 

    if answer_middle_day.lower() == "a":
       health += 5 #add five to health counter
       print(" ")
       print("[Groover watches as Big Bird gently trades a cookie for the birdseed box. He gives Alan the item and the friendly Asian man makes birdseed milkshakes for everyone.]")
       print(" ")
    if answer_middle_day.lower() == "b":
        health += 3 #add three to health counter. its okay to eat junk food sometimes.
        print(" ")
        print("Groover: Oh! I don't know if I should eat chocolate though because everyone says it's not healthy, but I really wanted one..")
        time.sleep(0.3) #delays the code
        print("Gordon: There's nothing wrong with eating a delicious but not healthy snack once in a while! We just can't eat it all the time and eat it in small quantities. [Gordon smiled.] ")
        time.sleep(0.3) #delays the code
        print("Alan: Yeah! Don't feel bad, Groover. You can enjoy your chocolate without guilt. You won't substitute any big meal of the day with it.")
        time.sleep(0.3) #delays the code
        print("[Groover eats his chocolate without guilt. Balance is important and it can include unhealthy but delicious junk food.]")
        print(" ")
    if answer_middle_day.lower() == "c":
        health += 5 #add 5 to the health counter
        print(" ")
        print("[Groover lifts his chocolate chip cook-]")
        time.sleep(0.3) #delays the code
        print("[COOOOOKIIIIEEEE! ON NOM NOM NOM!]")
        time.sleep(0.3) #delays the code
        print("[...]")
        time.sleep(0.3) #delays the code
        print("[Cookie Monster just ate the cookie before Groover's eyes.]")
        time.sleep(0.3) #delays the code
        print("Cookie Monster: OH NO! ME SORRY! ME BE SORRY MONSTER! I HAVE A RED FRESH APPLE. PLEASE, ACCEPT IT AS A TOKEN OF MY...SORRYNESS.")
        time.sleep(0.3) #delays the code
        print("[Groover accepts the fruit and forgives Cookie Monster.]")
        time.sleep(0.3) #delays the code
        print("Groover: Oh, an apple is also really good! We just need to remind that Cookie Monster really loves cookies.")
        print(" ")
    else:
       health += -1 #decreases one from health counter since it's only a middle of the day snack and not a really major meal of the day
       print(" ")
       print("[Everyone at Hooper's Store looks with worry as Groover decides to not eat anything at all. It's definitely healthier to eat something than anything at all...]")
       print(" ")
    time.sleep(0.3) #delays the code
    
    print("[Groover returns to the restaurant. He picks Mr. Johnson's meal out of the stove and brings it to him on a silver plate.]")
    time.sleep(0.3) #delays the code
    print("Groover: Here's your meal, Mr. Johnson! Done by me, the furry lovable monster Groover.")
    time.sleep(0.3) #delays the code
    print("[... The food is all burned.]")
    time.sleep(0.3) #delays the code

    print(" ")
    print(" ")

###Dinner time
    print("GROOVER's DINNER")
    time.sleep(0.3) #delays the code
    print(" ")
    print(" ")
    print("[At night, Groover went back home. He thought about what he could eat now to finally finish his day and go to sleep, so tomorrow he could go and play all friends and save Sesame Street as Super Groover!!!]")
    time.sleep(0.3) #delays the code
    print("Oh, I wonder what I'll eat now!")

    answer_dinner = input("""
    Groover walks to his kitchen as he wonders what he'll eat now.
    Type 'a' to eat some pasta meal
    Type 'b' to eat some hamburger and fries
    Type 'c' to eat a full bowl of salad with protein and a lot of assorted vegetables
    Type anything else to skip the dinner.
    """) #get user input 

    if answer_dinner.lower() == "a":
        health += 3 #add three to health counter
        print(" ")
        print("Groover: Oh, that pasta meal was delicious!")
        print(" ")
    elif answer_dinner.lower() == "b":
        health += 3 #add three to health counter
        print(" ")
        print("Groover: Soo good! I really like the combo of hamburgers and fries!")
        print(" ")
    elif answer_dinner.lower() == "c":
        health += 3 #add three to health counter
        print(" ")
        print("Groover: Salad is always so fresh and healthy! And I ate a lot!")
        print(" ")
    else:
        health += -2 #decreases two from health counter
        print(" ")
        print("[Groover skips dinner...]")
        print(" ")
    
    time.sleep(0.3) #delays the code 
    print("[Groover brushes his teeth and after a while, he goes to his bed, ready to sleep. He can't wait for tomorrow..]")
    print(" ")
    print(" ")
    time.sleep(0.3) #delays the code
    print("[Another sunny day on Sesame Street! No clouds! A blue pretty sky, perfect to go and play. Groover costume was hanging there, ready for him to use and save everyone as Super Groover!]")
    time.sleep(0.3) #delays the code

    if health <= 0: #If you skip all meals you WILL get a bad ending.
        print(" ")
        print("[Groover feels really bad. He felt his stomach in pain. So, he told his momma and they went to the doctor.]")
        time.sleep(0.5) #delays the code
        print("[The doctor explained how we need to eat food and balance our meals so we won't get sick and keep being healthy and strong, with the energy to do the things we like and even the daily simple ones.]")
        time.sleep(0.5) #delays the code
        print("[Groover can't go play and get to be Super Groover today...]")
        time.sleep(0.5) #delays the code
        print("[Oh no! Do you think you could make better choices to change Groover's day fate?]")
        time.sleep(0.5) #delays the code
        print(" ")
    elif health < 10: #here's a good ending
       print(" ")
       print("Groover: I'm not feeling my best but I think I can play a bit today!")
       time.sleep(0.5) #delays the code
       print("Groover went outside dressed as Super Groover and played with the Sesame Street neighbors for a bit. He wanted to play more, but he was feeling a bit more tired than normal.")
       time.sleep(0.5) #delays the code
       print("[Great choices!! Groover could go and play with his friends. But maybe Groover could had even more energy if he had made different food choices...? Eating a meal is always better than not eating anything.]")
       time.sleep(0.5) #delays the code
       print(" ")
    else: #that's the best ending!
       print(" ") 
       print("[Groover woke up feeling amazing. He jumped out of bed and went to brush his teeth, wash his face, and run to dress up as Super Groover. Of course, he didn't skip his breakfast before going outside to play on the street!]")
       time.sleep(0.5) #delays the code
       print("Groover: I feel absolutely great today!!! Oh wow! I can't wait to play all day with everyone! Super Groover iiiis ready!")
       time.sleep(0.5) #delays the code
       print("[Groover played with his neighbor friends on Sesame Street. He ran, he jumped, he laughed, he fell and got up! He even helped to save a little kitty cat, with all his clumsiness and big heart. Groover had a lot of fun today.]")
       time.sleep(0.5) #delays the code
       print("Wonderful! The meals chosen made Groover have a really fun and great day on Sesame Street, with plenty of energy to do so! Remember, you don't need to give up on a treat once in a while, just remember to also eat healthy!")
       time.sleep(0.5) #delays the code
       print(" ")
    print("[GROOVER FOOD AVENTURES END!]")
    groover_quit_or_again = str(input("Press any key to continue or 'q' to quit to the main menu! ")) #creates the variable that stores the user answer (if they want to quit or not)
    print(" ")

    if groover_quit_or_again.lower() == "q":  #if user selects q, they return to main_menu to select another character game
        print("Groover: Thank you for helping me, furry lovable monster Groover with meal choices!") #first that phrase will be displayed to the user
        main_menu() #then the user gets back at the main menu
    else:
       groover_game() #if any other key is pressed the game restarts
    

def elmo_game(): #Creates the function of Elmo's game
    
        print("You choose: Elmo! Lalala, lalala, Elmo's world!♪")
        print(" ")
        time.sleep(0.3) #delays the code
        print("You enter a room on Sesame Street. The walls are sky blue colored and there are fluffy clouds drawn all over in white crayons. There are toys all around the place, a golden fish inside an aquarium bowl and a little red furry monster in the middle of the room, lying down in the tapestry while confused about how to start coloring the blank paper.")
        print(" ")
        time.sleep(0.3) #delays the code
        print(f"Elmo: Hi, {name}! Welcome to Elmo's world! Elmo's been wondering about the rainbow today! The rainbow is pretty and Elmo's like it a lot, so Elmo's decided to draw it today. But Elmo's only three and a half! So Elmo's can't remember the seven colors of the rainbow arc! Will you help Elmo today??? Hoooray! Let's do that!") #f strings let us use variables inside the code
        print(" ")
        time.sleep(0.3) #delays the code
        print("Elmo: Elmo's will help. The first color of the rainbow is the same color as Elmo fur!!")
        print(" ")
        first_rainbow() #calls function so user can input answer
        while first_rainbow_color.lower() != "red": #if the answer is different from red the user will get the same hint again till they type the correct answer
            print("Elmo: Oops! Try again! Remember, it's the same color as Elmo's fur!")
            first_rainbow() #calls function so user can input answer again
        print(" ")
        print("Elmo: Hoorayy! You got it! Let's go to the second rainbow color! Elmo's been wondering about the second rainbow color! It's the same name as a citrus fruit! Also, Elmo's little goldfish Dorothy.")
        print(" ")
        second_rainbow() #calls function so user can input answer
        while second_rainbow_color.lower() != "orange": #if the answer is different from orange the user will get the same hint again till they type the correct answer
            print("Elmo: Mm, not quite! It has the same name as a citric fruit and Ernie's skin color!")
            second_rainbow() #calls function so user can input answer again
        print(" ")
        print(f"Elmo: You got it, {name}! Now we're heading to the third color. Elmo's say it's as bright as the SUN!")
        print(" ")
        third_rainbow() #calls function so user can input answer
        while third_rainbow_color.lower() != "yellow": #if the answer is different from yellow the user will get the same hint again till they type the correct answer
            print("Elmo: Another hint! You know Big Bird? He has feathers of that same color!")
            third_rainbow() #calls function so user can input answer again
        print(" ")
        print("""
Elmo: Just four more!!! It's four, right?
Count Von Count: Yes! Fovr, fovr more, Ah, Ah Ah! [Thunder and lightning sounds]""")
        print("Elmo: The next color, the fourth one, is the same color as the grass!")
        print(" ")
        fourth_rainbow()#calls function so user can input answer
        while fourth_rainbow_color.lower() != "green": #if the answer is different from green the user will get the same hint again till they type the correct answer
            print("Elmo: Ooh! Ooh! Elmo knows that one! It's Oscar the grouch fur color!")
            fourth_rainbow() #calls function so user can input answer again
        print(" ")
        print("Elmo: What's the color five of the rainbow? Elmo's wonder and It reminds of Cookie Monster!")
        five_rainbow()#calls function so user can input answer
        while five_rainbow_color.lower() != "blue": #if the answer is different from blue the user will get the same hint again till they type the correct answer
            print(f"Elmo: No worries, {name}! It's also the color of the sky and the ocean!")
            five_rainbow()#calls function so user can input answer again
        print(" ")
        print("Elmo: We're almost there! That one has a fun name that confuses Elmo. It has the same color as Super Grover, but it's not dark blue. It starts with the letter I. ")
        sixth_rainbow()#calls function so user can input answer
        while sixth_rainbow_color.lower() != "indigo": #if the answer is different from indigo the user will get the same hint again till they type the correct answer
            print("Elmo: It starts with the letter I and finishes with GO. ")
            sixth_rainbow()#calls function so user can input answer again
        print(" ")
        print("Elmo: Now we have the last color! It's the name of a purple flower!")
        seventh_rainbow()#calls function so user can input answer
        while seventh_rainbow_color.lower() != "violet": #if the answer is different from violet the user will get the same hint again till they type the correct answer
            print(f"Elmo: Did {name} know about the UV rays? Sunscreen helps Elmo and you from those!!")
            seventh_rainbow() #calls function so user can input answer again
        print(" ")
        time.sleep(0.3) #delays the code
        print("Elmo: We did it!!! Hooray! Thanks for helping Elmo! Elmo's so happy, it makes Elmo want to daance!")
        print(" ")
        time.sleep(0.3) #delays the code
        print("Happy Happy dance, dance!♫ Happy, happy, dance, dance!♫ When we learn something new we do a happy dance, dance!!!♫ Hooray! Keep learning! Elmo loves you!") #Elmo's World ending song and phrases
        print(" ")
        time.sleep(0.3) #delays the code
        print("[ELMO'S END.]")
        time.sleep(0.3) #delays the code
        main_menu()


###THE START OF THE ALL! MAIN MENU
def main():
    text = "Sesame Street Adventures Game!!" #title of the game
    Width = 50   #how the title will be spaced
    print(text.center(Width))  #title is now displayed more on the center
    print(" ") #space for aesthetic
    time.sleep(0.3) #delays the code
    print("An original code by Bianca Clara Correia Kusunoki!") #who programmed it
    time.sleep(0.3) #delays the code
    print("Made with love for Sesame Street.") # <3

    print(" ")
    letter_of_the_day = generate_random_letter() #it generates a random letter with the function at the beginning of the code
    number_of_the_day = random.randint(0,20) #generates a number from 0 to 20
    time.sleep(0.3) #delays the code
    print(f"Sesame Street has been brought to you today by the letter {letter_of_the_day} and by the number {number_of_the_day}." )
    print(" ")
    print(" ")
    time.sleep(0.3) #delays the code
    print("Hi, welcome to Sesame Street! Today we're going to learn about colors, shapes, numbers, letters and healthy meal choices!")
    print(" ")
    name_pick()  #calls the function to get user name
    main_menu()  #calls the main menu which you can choose the character's game.
    

######THE END OF IT ALL: Credits plus End
def say_goodbye():    #function that gets called when you choose number 8 at the main_menu function
    print("""
    Come on and move your body and use your mind ♫
    'Cause you know you are growing all the time!
    You're getting smarter! stronger! kinder!
    On Sesame Street!
    Kind at home and when you play ♪
    Try some sharing and caring every day ♪
    You're getting smarter (smarter)! Stronger (stronger)! Kinder (kinder)!
    On Sesame Street!
    Kinder and stronger and smarter ♬
    On Sesame Street!!!
    Yeah!""")  #Sesame Street ending song!! "Smarter, Stronger, Kinder")
    print(" ")
    time.sleep(0.5) #delays the code

    Width = 50
    ascii = """
                   ⣠⢖⢛⠛⡲⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                 ⠀⣼⣁⣀⣐⣀⣃⣈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣾⠉⣉⡉⣉⡉⣉⡉⢉⡉⢉⠉⡉⣉⡉⠉⢉⡉⣉⣉⢉⡉⢉⣉⢉⣉⢉⣉⠉⣷
    ⣿⠀⣏⠁⣏⡁⣧⠁⣸⡇⣿⣴⡇⣿⡁⠀⢻⡉⢸⡏⣿⣹⢸⣏⢸⣏⠈⡏⠀⣿
    ⣿⠀⣌⡇⣏⡀⣌⡧⡷⣧⣿⠟⡇⣿⡀⠀⢤⣻⢸⡇⣿⢻⢸⣇⢸⣇⡀⡇⠀⣿
    ⢻⣄⣈⣀⣉⣁⣈⣀⣁⣈⣀⣀⣁⣈⣁⣀⣈⣁⣀⣀⣈⣈⣈⣉⣈⣉⣀⣁⣠⡟
    """
    print(ascii.center(Width))  #it displays the ascii above more centered than the other printed words
    print(" ")
    print(" ")
    time.sleep(0.3) #delays the code
    print("Sesame Street is owned by Sesame Street Workshop. All rights reserved.")
    print(" ")
    print(" ")
    time.sleep(0.3) #delays the code
    print("""This code was made with love by Bianca Clara Correia Kusunoki, a huge Sesame Street fan.
    Thinking of all the personality aspects of the characters I came up with the ideas myself as I mimicked what an actual game from Sesame Street Workshop would be,
    focusing on teaching and learning, mixing with some fun.
    This code was submitted as the final project of 'Code In Place' by Stanford University, a text-based game entirely made in Python language, in April/June of 2025. 
    """) #Quickly about




########COOKIE MONSTER IS HUNGRY!

def cookie_choices(): #creating the function to store the searching options for Cookie Monster's game.
    global cookie_choices_select
    cookie_choices_select = get_valid_integer("""There are some places to search for, where do you want to search first? 
    Type '1' to Check inside the purple cookie jar.
    Type '2' to Check behind Big Bird's birdseed box on the shelf.
    Type '3' to Politely ask Alan for a cookie.
    Type '4' to Shout in hungriness. 
    Type '5' to Eat Hooper's Store wall.
    Type '6' to End the Adventure.
Choice: """) #the get_valid_integer substitutes int(input()) so the user input numbers and the code get no errors
    return cookie_choices_select



######### Elmo's little variables!!! 

        #seven colors of the rainbow, in order, are: Red, Orange, Yellow, Green, Blue, Indigo, and Violet. 

def first_rainbow(): #asks for user answer
    global first_rainbow_color
    first_rainbow_color = str(input("What's the first color of the rainbow?: "))
    return first_rainbow_color

def second_rainbow(): #asks for user answer
    global second_rainbow_color
    second_rainbow_color = str(input("What's the second color of the rainbow?: "))
    return second_rainbow_color

def third_rainbow(): #asks for user answer
    global third_rainbow_color
    third_rainbow_color = str(input("The third color now!: "))
    return third_rainbow_color

def fourth_rainbow(): #asks for user answer
    global fourth_rainbow_color
    fourth_rainbow_color = str(input("Now let's go to the number four of the rainbow! What's the color?: "))
    return fourth_rainbow_color

def five_rainbow(): #asks for user answer
    global five_rainbow_color
    five_rainbow_color = str(input("What's the color number five of the rainbow?: "))
    return five_rainbow_color

def sixth_rainbow(): #asks for user answer
    global sixth_rainbow_color
    sixth_rainbow_color = str(input("We're almost done! What's the sixth color of the rainbow?: "))
    return sixth_rainbow_color

def seventh_rainbow(): #asks for user answer
    global seventh_rainbow_color
    seventh_rainbow_color = str(input("Last color, what it is?: "))
    return seventh_rainbow_color


#############COUNT VON COUNT MENU
def count_von_menu():  #It stores the menu from count von count math games
    global count_game
    count_game = get_valid_integer("""Count Von Count: Velcome! To start a fun math game, vrite any of the following:
    Type '1' for Addiction!
    Type '2' for Svbtraction!
    Type '3' for Mvltiplication!
    Type '4' for Division!
    Type any other number (0 or from 5-9) to retvrn to the menv!
    Choice: """) #get_valid_integer applied so the user inputs numbers and the code gets no error
    return count_game

###########USER NAME
def name_pick(): #Gets the name of the user and stores it to use on all the code since we made it global
    global name 
    name = str(input("First, Sesame Street wants to know about their new neighbor! What would you like to be called, friend? "))
    return name


if __name__ == "__main__":
    main()