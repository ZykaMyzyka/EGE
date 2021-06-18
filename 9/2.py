for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((w and y) or ((x <= w) == (y <= z)))==False:
                    print(x,y,w,z)
