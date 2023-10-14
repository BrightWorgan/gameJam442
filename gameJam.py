# The Theme is Flying Saucers


# print(", -''''''-,
#    .'         '.
#  _/_____________\_
# / _0_(_)_(_)_(_)_0_
#   \_ | _ | _ | __ | _ | _ | _ /
#     ''__'' __''
#     /
#    /
#   /
#  /
# / ")


def aliens():

    print("    ,-''''''-, ")
    print("  .'         '.")
    print("_/_____________\_")
    print(" /_0_(_)_(_)_(_)_0_\ ")
    print(" \_|_|_|__|_|_|_/")
    print("    ''__'' __''")
    print(" / ")
    print("        |    \ ")
    print(" / ")
    print(" /      |   ")
    print("/      |     \ ")


# set up athmosphere
def scene():
    print("Spooky is in the heart of the beholder, and this old  public house, or as they are called now, pub, rather enjoyed its less than traditional vibe.")

# get user's name


def nameFinder():
    print("It's a cold October night...")
    print(".....")
    print("Hello there mate What Can I get you?....")
    print(".....")
    print("What is your name?")
    username = input("Your Name:")
    print("AH,... Hello  " + username + " Here is yout pint of Guinness... ")


def leave():
    print("Maybe you should finish your drink and leave?")
    leave = input("Would you like to leave? Y or N ???")

    # while leave.upper() == "N":
    if leave.upper() == "Y":
        print("You drain the remainer of your pint and stand up to leave")

    elif leave.upper() == "N":
        print("You wave to the barman to order another drink....")
        nameFinder()

    else:
        print("Please anwser Y or N ....")


def pickDoor():
    print("You see a large heavy pair of dark wooden doors to your LEFT and a small signle plain wooden door to your RIGHT....")
    anwser = input("Pick a Door.... LEFT or RIGHT ????")

    if anwser.upper() == "LEFT":
        print("You place both of your hands on the large heavy pair of dark wooden doors and push ")
        print("You exit the pub via the large heavy pair of dark wooden doors")
        print("You find yourslef on a cobbledstoned lined side alley")
        print("It's very dark and very quiet....")
        print(" ..... a .... bit ... too ... quiet")
        print("You start walking towards home... feeling uneasy...")
        # direction = input(
        #     "Do you take the shortcut through the TOWN PARK or the much longer route via the CANAL WALK?")
        # if direction.upper() == "TOWN PARK":
        #     print("")
        aliens()
        print("OH NO!!!")
        print("IS THAT A FLYING SAUCER?!")

    elif anwser.upper() == "RIGHT":
        print("You exit through the small wooden door to your right")
        print("You find yourself outside the pub on a dark sidestreet")

    else:
        print("Please anwser Y or N ....")


#      , -''''''-,
#    .'         '.
#  _/_____________\_
# /_0_(_)_(_)_(_)_0_\
#   \_|_|_|__|_|_|_/
#     ''__'' __''
#     /          \
#    /            \
#   /              \
#  /                \
# /                  \

# Call all functions
scene()
leave()
pickDoor()
# nameFinder()
# aliens()
