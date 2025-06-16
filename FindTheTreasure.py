print("Welcome to Treasure Island.\nYour mission is to find treasure.")
direction = input("You have two directions.. which will you choose? Left or Right : ")
if direction == "Left":
    print("Nice! You reached to the Lake!\n\nThere is Island at the center of the lake.")
    swim_wait = input("Do you wanna wait for the boat or swim for the Island? Wait or Swim : ")
    if swim_wait == "Wait":
        print("Good! You reached to the Island...")
        door = input("\nNow you have three doors, which will you choose? Red or Blue or Yellow : ")
        if door == "Yellow":
            print("Congrats! You got the treasure...\nYou win!!!")
        else:
            print("You choose wrong door...\nGame Over!")
    else:
        print("You choose wrong way to go...\nGame Over!")
else:
    print("You choose wrong direction...\nGame Over!")