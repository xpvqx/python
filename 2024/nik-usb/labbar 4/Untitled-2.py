#take in a series of temperatures, convert them to floats, and add them to a list. if 7 inputs in a row are positive temperatures, then return "spring is here", if there are no positive temperatures from the user input, return "spring is not here yet", if the temperatures are after 31th of july , return "spring cannot start after 3oth of july"

def spring_start_date():
    temperatures = input("enter temperature")
    temperatures = temperatures.split()
    temperatures = [float(i) for i in temperatures]
    print(temperatures)
    if temperatures[0] > 31:
        return "spring cannot start after 3oth of july"
    elif temperatures[0] < 31:
        return "spring is not here yet"
spring_start_date