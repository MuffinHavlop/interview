#người gõ code hoàng minh hiếu 
#tài khoản github: MuffinHavlop
#chương trình sau là một chương trình để chọn điểm bay, điểm đến và mẫu máy bay lặp lại vô số lần
#các địa điểm và thời gian bay là không chính xác vậy nên đừng để í
#do trình độ vãn còn có hạn nên code sẽ không được clean và tối ưu (sorry)


import math
import random
import time
#import random, math, time
print("your current location is: Ha Noi")
places = ['Los angeles', 'Houston', 'Bern', 'Geneva', 'Cairo', 'Beijing', 'Nanjing', 'HCMcity', 'Da Nang', 'Kiev', 'Odessa', 'Ha Noi']
types = ['Boeing 747', 'Airbus A380', 'Airbus A350', 'Boeing 777', 'sukhoi su-34' ,'sukhoi su-35', 'A10-Warthog']
#list của location và model máy bay
arrival_old = "Ha Noi"
while True:
    def viewing():
        global places
        global arrival
        global types
        global model
        exit = False
        while True: 
            if exit == True:
                break
            #exit = 1 để thoát khỏi loop chính
            option = input("which one do you like to check(locations, planes) if you have done viewing press (y): ")# (1)
            #chọn giữa xem các locations model planes hoặc nhấn y để chọn location và model 
            if option == "locations":
                with open('E:\python\interview\location.txt') as file:
                    print(file.read())
                    #xem location
            elif option == "planes":
                with open('E:\python\interview\planes.txt') as file:
                    print(file.read())
                    #xem model
            elif option == "y":  
                while True: 
                    arrival = input("select your destination(if you haven't viewed, press B): ")\
                    arrival = arrival.upper()
                    if arrival == "B":
                        break
                    #nhấn B để quay trở lại phần (1) xem lại location và model
                    else:
                        if arrival in places:
                            print(f"location chosen: {arrival}")
                            arrival_old = arrival
                    #chọn location
                        else:
                            print("Invalid syntax")
                            break
                        #nếu model hoặc location không đúng hoặc gõ sai thì quay lại loop
                    model = input("select your plane model(if you haven't viewed, press B): ")
                    if model == "B" or model == "b":
                        break
                    #nhấn B để quay trở lại phần (1) xem lại location và model
                    else:
                        if model in types:
                            print(f"plane model chosen: {model}")                    
                            exit = True
                            break
                    #chọn model, exit += 1 để thoát khỏi loop chính
                        else:
                            print("invalid syntax")
                            break
                        #nếu model hoặc location không đúng hoặc gõ sai thì quay lại loop
            else:
                pass
    viewing()
    def location():
        global x
        global y
        if arrival == "Bern":
            x =  -3064
            y = 256
        elif arrival == "Geneva":
            x =  -3257
            y = 126
        elif arrival == "Kiev":
            x =  -2075
            y = 300
        elif arrival == "Odessa":
            x =  -2200
            y = 75
        elif arrival == "Nanjing":
            x =  30
            y = 325
        elif arrival == "Beijing":
            x =  40
            y = 756
        elif arrival == "Los angeles":
            x =  4327
            y = 780
        elif arrival == "Houston":
            x =  4790
            y = 453
        elif arrival == "DaNang":
            x = 10
            y = -128
        elif arrival == "HCMcity":
            x = 5
            y = -256
        elif arrival == "Ha Noi":
            x = 0
            y = 0
    location()
    # Tọa độ của các thành phố
    def location_old():
        global x_old
        global y_old
        global arrival_old
        if arrival_old == "Bern":
            x_old =  -3064
            y_old = 256
        elif arrival_old == "Geneva":
            x_old =  -3257
            y_old = 126
        elif arrival_old == "Kiev":
            x_old =  -2075
            y_old = 300
        elif arrival_old == "Odessa":
            x_old =  -2200
            y_old = 75
        elif arrival_old == "Nanjing":
            x_old =  30
            y_old = 325
        elif arrival_old == "Beijing":
            x_old =  40
            y_old = 756
        elif arrival_old == "Los angeles":
            x_old =  4327
            y_old = 780
        elif arrival_old == "Houston":
            x_old =  4790
            y_old = 453
        elif arrival_old == "Da Bang":
            x_old = 10
            y_old = -128
        elif arrival_old == "HCM city":
            x_old = 5
            y_old = -256
        elif arrival_old == "Ha Noi":
            x_old = 0
            y_old = 0
        #Tọa độ của các thành phố cũ
    location_old()
    distance = math.sqrt((x-x_old)**2 + (y-y_old)**2)
    distance = math.ceil(distance)
    print(f"The travelling distance is: {distance} km")
    #khoảng cách phải bay
    if model == "Boeing 747":
        speed = 988
    elif model == "B0eing 777":
        speed = 1076
    elif model == "Airbus A380":
        speed = 1185
    elif model == "Airbus A350":
        speed = 945
    elif model == "sukhoi su-34":
        speed = 2200
    elif model == "sukhoi su-35":
        speed = 2778
    elif model == "A10-Warthog":
        speed = 676
    #Tốc độ của các mẫu máy bay
    bad_weather = random.randint(0,1)
    #khả năng xảy ra bão 50/50
    if bad_weather == 0:
        print("luckly the weather is good")
        fly_time = distance/speed
        fly_time = round(fly_time, 2)
        print(f"The time it would take from {arrival_old} to {arrival} is: {fly_time} hours")
        #không có bão
    else:
        print("due to the storm, we might have to fly slower")
        fly_time = distance/speed
        fly_time = round(fly_time, 2) + 1
        print(f"The time it would take from {arrival_old} to {arrival} is: {fly_time} hours")
        #có bão, tg bay +1h
    arrival_old = arrival
    print("flying...")
    time.sleep(fly_time)
    print("we've arrived at the location safely")
    print(f"your current location is:{arrival_old}")
    #bay đến địa điểm hiện tại





