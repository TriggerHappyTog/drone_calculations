import sys


def pres_alt_calc(qnh, air_elev):
    if qnh >= 1013.25:
        qnh = int(qnh) - 1013.25
        qnh = qnh * 30
        pres_alt = int(air_elev) - qnh

    else:
        qnh = int(qnh) + 1013.25
        qnh = qnh * 30
        pres_alt = int(air_elev) - qnh

    return pres_alt


def den_alt_calc(temp, qnh, air_elev):
    original_pres_alt = pres_alt_calc(qnh, air_elev)

    pres_alt = original_pres_alt * -0.002

    pres_alt = pres_alt + 15

    temp = temp - pres_alt

    temp = temp * 120

    answer = original_pres_alt + temp

    return answer


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

        answer = pres_alt_calc(qnh, air_elev)
        print('Your pressure altitutde is %d feet, bub.' % answer)

elif str(choice) == "b":
        # print("What is your pressure altitude chief?")
        # pres_alt = int(sys.stdin.readline().strip())

        print("What's your QNH chief?")
        qnh = int(sys.stdin.readline())

        print("What's your airfield elevation (in feet)?")
        air_elev = int(sys.stdin.readline())

        print("What's your temp?")
        temp = int(sys.stdin.readline().strip())

        answer = den_alt_calc(temp, qnh, air_elev)

        print('Your density altitude is %d feet, bub.' % answer)
