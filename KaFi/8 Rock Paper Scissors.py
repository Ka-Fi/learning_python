player_one = 0
player_two = 0
point_one = 0
point_two = 0
while player_one != 4 and player_two != 4:
    player_one = int(input("Rock:1 Paper:2 Scissors:3, EXIT : 4 "))
    player_two = int(input("Rock:1 Paper:2 Scissors:3, EXIT : 4 "))
    if player_one == player_two:
        print("you choose the same {}:{}".format(point_one, point_two))

    if player_one == 1:
        if player_two == 2:
            print("point for player 2")
            point_two +=1
        elif player_two == 3:
            print("point for player 1")
            point_one +=1
    elif player_one  == 2:
        if player_two == 1:
            print("point for player 2")
            point_two+=1
        elif player_two == 3:
            print("point for player 1")
            point_one+=1
    elif player_one == 3:
        if player_two == 1:
            print("point for player 2")
            point_two+=1
        elif player_two == 2:
            print("point for player 1")
            point_one+=1
    print("ueser one have {} points, user two have {} points".format(point_one,point_two))