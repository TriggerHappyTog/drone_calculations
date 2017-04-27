import sys
import drone_calcs


print("What would you like to calculate? A = pressure altitude. B = Density Altitude.")
choice = str(sys.stdin.readline()).strip()
choice = str(choice.lower()).strip()


while choice != 'a' and choice != 'b':
    print('That aint a choice partner, try again.')
    choice = str(sys.stdin.readline()).strip().lower()

if str(choice) == "a":
        print("What's your QNH chief?")
        qnh = int(sys.stdin.readline())

        print("What's your airfield elevation (in feet)?")
        air_elev = int(sys.stdin.readline())

        answer = drone_calcs.pres_alt_calc(qnh, air_elev)
        print('Your pressure altitutde is %d feet, bub.' % answer)

elif str(choice) == "b":

        print("What's your QNH chief?")
        qnh = int(sys.stdin.readline())

        print("What's your airfield elevation (in feet)?")
        air_elev = int(sys.stdin.readline())

        print("What's your temp?")
        temp = int(sys.stdin.readline().strip())

        answer = drone_calcs.den_alt_calc(temp, qnh, air_elev)

        print('Your density altitude is %d feet, bub.' % answer)
