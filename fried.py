from threading import Thread
#from playsound import playsound


try:
    #Fried
    #(c) 2023 Erik's Gadgets

    import PySimpleGUI as sg #Imports GUI Library
    import os 
    #import playsound
    cutscene1_stage = 0
    
    frozen = 0
    
    login = os.getlogin()

    import random

    all_ratings = []

    rating = 0
    
    
    first_time = True

    file1 = open('save-file.txt', 'r')
    
    save_r_list = []    
        
    for i in file1:
        save_r_list.append(i.split())   

    print(save_r_list)
    
    multiplier = int(save_r_list[1][0])
    
    money = int(save_r_list[0][0])
    
    if save_r_list[2][0] == "False":
        done_tutorial = False
    else:
        done_tutorial = True

    sg.theme("DarkTeal12") #Sets theme
    print(done_tutorial)
    sg.Popup("Fried\n(c) 2023 Erik's Gadgets") #IP addition
    
    if done_tutorial == False:
        room = sg.Window(title="Fried", layout=[[sg.Image(filename="fried_title_screen.png")], [sg.Button("Start Tutorial"), sg.Button("Money"), sg.Button("Shop"), sg.Button("My Rating")]])
    else:
        room = sg.Window(title="Fried", layout=[[sg.Image(filename="fried_title_screen.png")], [sg.Button("Continue"), sg.Button("Money"), sg.Button("Shop"), sg.Button("My Rating")]])
    import winsound
    winsound.PlaySound("fried.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    
    while True:
        event, values = room.Read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Return":
            first_time = True
            room.close()
            winsound.PlaySound("fried.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            if done_tutorial == False:
                room = sg.Window(title="Fried", layout=[[sg.Image(filename="fried_title_screen.png")], [sg.Button("Start Tutorial"), sg.Button("Money"), sg.Button("Shop"), sg.Button("My Rating")]])
            else:
                room = sg.Window(title="Fried", layout=[[sg.Image(filename="fried_title_screen.png")], [sg.Button("Continue"), sg.Button("Money"), sg.Button("Shop"), sg.Button("My Rating")]])
        if event == "Buy Rating Multiplier":
            if money >= 5:
                room.close()
                money -= 5
                multiplier += 1
                room = sg.Window(title="Fried", layout=[[sg.Text(f"Money: ${money}")],[sg.Text("Rating Multiplier ($5.00) [Increases Multiplier by +1]"), sg.Button("Buy Rating Multiplier")],[sg.Text(f"Multiplier is currently {multiplier}")], [sg.Button("Return")]])
            else:
                sg.Popup("Not Enough Money")
        if event == "Shop":
            room.close()
            room = sg.Window(title="Fried", layout=[[sg.Text(f"Money: ${money}")],[sg.Text("Rating Multiplier ($5.00) [Increases Multiplier by +1]"), sg.Button("Buy Rating Multiplier")],[sg.Text(f"Multiplier is currently {multiplier}")], [sg.Button("Return")]])
        if event == "Money":
            sg.Popup(f"Current Money:\n${money}.00")
        if event == "My Rating":
            room.close()
            mysum = 0
            for i in all_ratings:
                mysum += i
            mysum2 = mysum
            if len(all_ratings) != 0:
                mysum /= len(all_ratings)
                print(mysum)
            mysum = round(mysum, None)
            print(mysum)
            if mysum == 0:
                if len(all_ratings) == 0:
                    room = sg.Window(title="Fried", layout=[[sg.Image(filename="my-rating-none.png")], [sg.Button("Return")]])
                else:
                    room = sg.Window(title="Fried", layout=[[sg.Image(filename="my-rating-0.png")], [sg.Button("Return")]])
            elif mysum == 1:
                room = sg.Window(title="Fried", layout=[[sg.Image(filename="my-rating-1.png")], [sg.Button("Return")]])
            elif mysum == 2:
                room = sg.Window(title="Fried", layout=[[sg.Image(filename="my-rating-2.png")], [sg.Button("Return")]])
            elif mysum == 3:
                room = sg.Window(title="Fried", layout=[[sg.Image(filename="my-rating-3.png")], [sg.Button("Return")]])
            elif mysum == 4:
                room = sg.Window(title="Fried", layout=[[sg.Image(filename="my-rating-4.png")], [sg.Button("Return")]])
            elif mysum == 5:
                room = sg.Window(title="Fried", layout=[[sg.Image(filename="my-rating-5.png")], [sg.Button("Return")]])
            else:
                room = sg.Window(title="Fried", layout=[[sg.Image(filename="my-rating-none.png")], [sg.Text("Your Rating Is" + str(mysum2 / len(all_ratings)))],[sg.Button("Return")]])
        if event == "Start Tutorial":
            if first_time == True:
                winsound.PlaySound("fried-cooking.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                first_time = False
            room.close()
            cutscene1_stage = 1
            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room.png")], [sg.Text("Welcome to YOUR brand new resturaunt\nThis is the kitchen!"), sg.Button("Continue")]])
        if event == "Continue":
            if first_time == True:
                winsound.PlaySound("fried-cooking.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                first_time = False
            if cutscene1_stage == 1:
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room.png")], [sg.Text("Let's buy a Fridge so that we have something to prevent the food from, well\nexpiring."), sg.Button("Continue")]])
                cutscene1_stage += 1
            elif cutscene1_stage == 2:
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room1.png")], [sg.Text("No one likes ugly, raw meat\n(including the fact that it gives you food poisoning)\nLet's buy a grill so that we can cook the meat!\n..and also to prevent Food Poisoning."), sg.Button("Continue")]])
                cutscene1_stage += 1
            elif cutscene1_stage == 3:
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room2.png")], [sg.Text("Alright! Let's Begin Cooking!!"), sg.Button("Continue")]])
                done_tutorial = True
                cutscene1_stage = 0
            elif cutscene1_stage == 0:
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room2.png")], [sg.Button("Fridge"),sg.Button("Grill")]])
                hasHotDogs = False
                hotDogsState = "Raw"
                ketchup = False
                orders = ["Hot Dog, Plain", "Hot Dog, with Ketchup"]
                random_num = random.randint(0,len(orders) - 1)
                sg.Popup(orders[random_num])
                if random_num == 0:
                    ketchupRequired = False
                elif random_num == 1:
                    ketchupRequired = True
                cutscene1_stage = -1
            elif cutscene1_stage == -1:
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room2.png")], [sg.Button("Fridge"),sg.Button("Grill")]])
            elif cutscene1_stage == -2:
                cutscene1_stage = -5
                if hotDogsState == "Raw":
                    room.close()
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-raw.png")], [sg.Button("Dress with Ketchup"),sg.Button("Continue")]])
                elif hotDogsState == "Cooked":
                    room.close()
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-cooked.png")], [sg.Button("Dress with Ketchup"),sg.Button("Continue")]])
                elif hotDogsState == "Burnt":
                    room.close()
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-burnt.png")], [sg.Button("Dress with Ketchup"),sg.Button("Continue")]])
            elif cutscene1_stage == -3:
                room.close()
                cutscene1_stage = -4
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-burnt-to-a-crisp.png")], [sg.Text("OH NO! You've burnt the hot dog! It's now a pile of ashes...")], [sg.Button("Continue")]])
            elif cutscene1_stage == -4:
                room.close()
                cutscene1_stage = -1
                all_ratings.append(0)
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-crisp.png")], [sg.Text("Oops... Maybe we should've done this some other way...")],[sg.Button("Continue")], [sg.Button("Return")]])
            elif cutscene1_stage == -5:
                ketchup_style = 0
                if hotDogsState == "Raw":
                    room.close()
                    cutscene1_stage = -7
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-raw-1.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                if hotDogsState == "Cooked":
                    room.close()
                    cutscene1_stage = -7
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-cooked-1.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                if hotDogsState == "Burnt":
                    room.close()
                    cutscene1_stage = -7
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-burnt-1.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
            elif cutscene1_stage == -6:
                if ketchup_style == 1:
                    if hotDogsState == "Raw":
                        room.close()
                        cutscene1_stage = -7
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-raw-2.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                    if hotDogsState == "Cooked":
                        room.close()
                        cutscene1_stage = -7
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-cooked-2.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                    if hotDogsState == "Burnt":
                        room.close()
                        cutscene1_stage = -7
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-burnt-2.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                elif ketchup_style == 2:
                    if hotDogsState == "Raw":
                        room.close()
                        cutscene1_stage = -7
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-raw-3.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                    if hotDogsState == "Cooked":
                        room.close()
                        cutscene1_stage = -7
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-cooked-3.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
                    if hotDogsState == "Burnt":
                        room.close()
                        cutscene1_stage = -7
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room7-burnt-3.png")], [sg.Text("Your Hot Dog is almost done!")],[sg.Button("Continue")]])
            elif cutscene1_stage == -8:
                cutscene1_stage = 0
                if ketchupRequired == False:
                    if hotDogsState == "Burnt":
                        if ketchup_style != 0:
                            room.close()
                            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-no-topping-burnt.png")], [sg.Text("Oops... Maybe we should've done this some other way...")],[sg.Button("Continue")], [sg.Button("Return")]])
                            all_ratings.append(1)
                        if ketchup_style == 0:
                            room.close()
                            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-toppings-burnt.png")], [sg.Text("Well, It's not BAD... It's not good either but it's not bad.")],[sg.Button("Continue")], [sg.Button("Return")]])
                            all_ratings.append(3)
                    if hotDogsState == "Cooked":
                        if ketchup_style != 0:
                            room.close()
                            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-cooked-bad-presentation.png")], [sg.Text("4 Stars! Pretty Good.")],[sg.Button("Continue")], [sg.Button("Return")]])
                            all_ratings.append(4)
                        if ketchup_style == 0:
                            room.close()
                            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-cooked-amazing-presentation.png")], [sg.Text("Great Job! All Five Stars!")],[sg.Button("Continue")], [sg.Button("Return")]])
                            all_ratings.append(5)
                    if hotDogsState == "Raw":
                        if ketchup_style != 0:
                            room.close()
                            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-raw.png")], [sg.Text("Oops... Maybe we should've done this some other way...")],[sg.Button("Continue")], [sg.Button("Return")]])
                            all_ratings.append(1)
                        if ketchup_style == 0:
                            room.close()
                            room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-raw-with-toppings.png")], [sg.Text("Two Stars are better than None... I guess...")],[sg.Button("Continue")], [sg.Button("Return")]])
                            all_ratings.append(2)
                if ketchupRequired == True and ketchup_style == 0:
                    if hotDogsState == "Burnt":
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-no-topping-burnt.png")], [sg.Text("Oops... Maybe we should've done this some other way...")],[sg.Button("Continue")], [sg.Button("Return")]])
                        all_ratings.append(1)
                    if hotDogsState == "Cooked":
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-no-topping-cooked.png")], [sg.Text("Two Stars are better than None... I guess...")],[sg.Button("Continue")], [sg.Button("Return")]])
                        all_ratings.append(2)
                    if hotDogsState == "Raw":
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-raw.png")], [sg.Text("Oops... Maybe we should've done this some other way...")],[sg.Button("Continue")], [sg.Button("Return")]])
                        all_ratings.append(1)
                if ketchupRequired == True and ketchup_style != 0 and hotDogsState == "Cooked":
                    if ketchup_style == 2:
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-cooked-amazing-presentation.png")], [sg.Text("Great Job! All Five Stars!")],[sg.Button("Continue")], [sg.Button("Return")]])
                        all_ratings.append(5)
                    if ketchup_style == 1:
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-cooked-bad-presentation.png")], [sg.Text("4 Stars! Pretty Good.")],[sg.Button("Continue")], [sg.Button("Return")]])
                        all_ratings.append(4)
                if ketchupRequired == True and ketchup_style != 0 and hotDogsState != "Cooked":
                    if hotDogsState == "Burnt":
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-toppings-burnt.png")], [sg.Text("Well, It's not BAD... It's not good either but it's not bad.")],[sg.Button("Continue")], [sg.Button("Return")]])
                        all_ratings.append(3)
                    if hotDogsState == "Raw":
                        room.close()
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="review-raw-with-toppings.png")], [sg.Text("Two Stars are better than None... I guess...")],[sg.Button("Continue")], [sg.Button("Return")]])
                        all_ratings.append(2)
                money += all_ratings[-1] * multiplier
            elif cutscene1_stage == -7:
                if ketchup_style == 0:
                    if hotDogsState == "Raw":
                        room.close()
                        cutscene1_stage = -8
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-raw-1.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                    if hotDogsState == "Cooked":
                        room.close()
                        cutscene1_stage = -8
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-cooked-1.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                    if hotDogsState == "Burnt":
                        room.close()
                        cutscene1_stage = -8
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-burnt-1.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                elif ketchup_style == 1:
                    if hotDogsState == "Raw":
                        room.close()
                        cutscene1_stage = -8
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-raw-2.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                    if hotDogsState == "Cooked":
                        room.close()
                        cutscene1_stage = -8
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-cooked-2.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                    if hotDogsState == "Burnt":
                        room.close()
                        cutscene1_stage = -8
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-burnt-2.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                elif ketchup_style == 2:
                    if hotDogsState == "Raw":
                        room.close()
                        cutscene1_stage = -8
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-raw-3.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                    if hotDogsState == "Cooked":
                        room.close()
                        cutscene1_stage = -8
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-cooked-3.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])
                    if hotDogsState == "Burnt":
                        room.close()
                        cutscene1_stage = -8
                        room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room8-burnt-3.png")], [sg.Text("Your Hot Dog is Complete!\nNow let's see the review you got!")],[sg.Button("Continue")]])        
        if event == "Grill":
            if hasHotDogs == False:
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room4.png")], [sg.Text("It appears you don't have anything to 'Grill' just yet."), sg.Button("Continue")]])
            elif hasHotDogs == True:
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room4.png")], [sg.Text("Cook the Hot Dogs for "), sg.Input(), sg.Text(" Minutes."), sg.Button("Cook")]])
        if event == "Dress with Ketchup":
            cutscene1_stage = -6
            random_num = random.randint(1, 2)
            if random_num == 1:
                if hotDogsState == "Raw":
                    room.close()
                    ketchup_style = 1
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-raw-ketchup1.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
                if hotDogsState == "Cooked":
                    room.close()
                    ketchup_style = 1
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-cooked-ketchup1.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
                if hotDogsState == "Burnt":
                    room.close()
                    ketchup_style = 1
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-burnt-ketchup1.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
            else:
                if hotDogsState == "Raw":
                    room.close()
                    ketchup_style = 2
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-raw-ketchup2.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
                if hotDogsState == "Cooked":
                    room.close()
                    ketchup_style = 2
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-cooked-ketchup2.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
                if hotDogsState == "Burnt":
                    room.close()
                    ketchup_style = 2
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room6-burnt-ketchup2.png")], [sg.Text("You have dressed the hot dog with ketchup."), sg.Button("Continue")]])
        if event == "Cook":
            if int(values[1]) < 10 and int(values[1]) > 0:
                hotDogsState = "Raw"
                hasHotDogs = 0
                room.close()
                cutscene1_stage = -2
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room5-raw.png")], [sg.Text("The Hot Dog has been cooked for " + str(values[1]) + " minutes."), sg.Button("Continue")]])
            elif int(values[1]) < 13 and int(values[1]) > 0:
                hotDogsState = "Cooked"
                hasHotDogs = 0
                room.close()
                cutscene1_stage = -2
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room5-cooked.png")], [sg.Text("The Hot Dog has been cooked for " + str(values[1]) + " minutes."), sg.Button("Continue")]])
            elif int(values[1]) < 30 and int(values[1]) > 0:
                hotDogsState = "Burnt"
                hasHotDogs = 0
                room.close()
                cutscene1_stage = -2
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room5-burnt.png")], [sg.Text("The Hot Dog has been cooked for " + str(values[1]) + " minutes."), sg.Button("Continue")]])
            elif int(values[1]) <= 0:
                hotDogsState = "Frozen"
                room.close()
                frozen += 1
                cutscne1_stage = 0
                print(frozen)
                if frozen < 20:
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="easter_egg_frozen.png")], [sg.Text("Well, if you want COLD Hot Dogs, don't put them on a grill. Put them in a freezer instead. Let's try this again now, shall we?"), sg.Button("Continue")]])
                elif frozen < 30:
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="easter_egg_too_many_hot_dogs.png")], [sg.Text("Stop it, there's too many hot dogs in the freezer."), sg.Button("Continue")]])
                else:
                    frozen = 0
                    room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="freezer-hot-dog-explosion.png")], [sg.Text("OH GOD- THE FREEZER EXPLODED WITH HOT DOGS! I'll go replace this fridge with an identical copy."), sg.Button("Continue")]])
            else:
                crisp = True
                hotDogsState = "Burnt"
                hasHotDogs = 0
                room.close()
                cutscene1_stage = -3
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room5-burnt.png")], [sg.Text("The Hot Dog has been cooked for " + str(values[1]) + " minutes."), sg.Button("Continue")]])
        if event == "Fridge":
            if hasHotDogs == False:
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room3.png")], [sg.Text("Let's Grab some Hot Dogs."), sg.Button("Continue")]])
                hasHotDogs = True
            elif hasHotDogs == True:
                room.close()
                room = sg.Window(title="Kitchen", layout=[[sg.Image(filename="room3_no_hotdogs.png")], [sg.Text("We ran out hotdogs!"), sg.Button("Continue")]])
                hasHotDogs = True
    room.close()
    winsound.PlaySound(None, winsound.SND_ASYNC)
    with open("save-file.txt",'r+') as file:
        file.truncate(0)
        file.write(str(money))
        file.write("\n")
        file.write(str(multiplier))
        file.write("\n")
        file.write(str(done_tutorial))

except Exception as err:
    import PySimpleGUI as sg
    sg.Popup(err)
