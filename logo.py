

dictList = list()
logoName = [" "]
sameList = list()

while True:

    sameDict = {
        "nameOfSame":"",
        "sameControl":""
    }


    dict = {
        "fcommand": "",
        "logoNme": "",
        "logoDirect": ""

    }

    print("Please enter your command ('q' for quit the program') :")

    komut =input()

    control = list(komut.split())

    if control[0] == "q":
        print("Exiting the program...")
        break

    elif control[0] == "LOGO":

            if len(control)>3 or len(control)<3:
                print("Entered too much or less command! Please Try again.")



            elif control[1] not in logoName:

                flag = False
                temp_list = list(control[2])
                #print(temp_list)
                for m in temp_list:
                    if m not in ["U","D","L","R"]:
                        flag = True
                        break

                if flag == True:
                    print("You entered wrong letter! Please try again")
                else:

                    logoName.append(control[1])
                    dict["fcommand"]=control[0]
                    dict["logoNme"]=control[1]
                    dict["logoDirect"]=control[2]
                    dictList.append(dict)
                    #print(dict)
                    #print("liste: ",dictList)
                    #print(dictList[0]["fcommand"])
                    print(control[1], "defined")
                    #print(logoName)
                    #print(dictList)


            else:

                print("This name already exist")

            firstInp = 0
            secondInp = 0

            matrix = [
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " "],
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " "],
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " "],
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " "],
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " "],
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " "],
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " "],
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " "],
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " "],
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " "],
                [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ",
                 "."]]


            def change(matrix, i, j, element):
                if element == "D":
                    matrix[i * 2 - 1][j * 2 - 2] = "|"

                elif element == "U":
                    matrix[i * 2 - 3][j * 2 - 2] = "|"

                elif element == "R":
                    matrix[i * 2 - 2][j * 2 - 1] = "-"

                elif element == "L":
                    matrix[i * 2 - 2][j * 2 - 3] = "-"
                return matrix


            for y in range(len(dictList)):

                if control[1] == dictList[y]["logoNme"]:

                    # print(dictList[y]["logoNme"])
                    a = dictList[y]["logoDirect"]
                    v = 0

                    while v < len(dictList[y]["logoDirect"]):

                        if a[v] in ["U", "D", "R", "L"]:
                            if a[v] == "U":
                                change(matrix, firstInp, secondInp, "U")
                                firstInp -= 1
                            elif a[v] == "D":
                                change(matrix, firstInp, secondInp, "D")
                                firstInp += 1
                            elif a[v] == "R":
                                change(matrix, firstInp, secondInp, "R")
                                secondInp += 1
                            elif a[v] == "L":
                                change(matrix, firstInp, secondInp, "L")
                                secondInp -= 1

                        v += 1
                    #print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
                    sameDict["nameOfSame"] = control[1]
                    sameDict["sameControl"] = str(firstInp)
                    sameList.append(sameDict)

                    break




    elif control[0] == "ENGRAVE":
        k = 0


        firstInp = int(control[2])
        secondInp = int(control[3])



        matrix =   [[".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."],
                    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", ".", " ", "."]]


        def change(matrix, i, j, element):
            if element == "D":
                matrix[i * 2-1][j * 2-2 ] = "|"

            elif element == "U":
                matrix[i * 2 - 3][j * 2 - 2] = "|"

            elif element == "R":
                matrix[i * 2 - 2][j * 2 - 1] = "-"

            elif element == "L":
                matrix[i * 2 - 2][j * 2 - 3] = "-"
            return matrix





        for y in range(len(dictList)):

            if len(control) > 4:
                print("Entered too much command!")
                break
            if int(control[2]) < 1 or int(control[3]) < 1:
                print("Your grid should start [1,1] or higher")
                break
            if control[1]==dictList[y]["logoNme"]:

               # print(dictList[y]["logoNme"])
                a=dictList[y]["logoDirect"]
                v=0


                while v<len(dictList[y]["logoDirect"]):

                    if a[v] in ["U","D","R","L"]:
                        if a[v] == "U":
                            change(matrix, firstInp, secondInp,"U")
                            firstInp -= 1
                        elif a[v] == "D":
                            change(matrix, firstInp, secondInp, "D")
                            firstInp +=1
                        elif a[v] == "R":
                            change(matrix, firstInp, secondInp, "R")
                            secondInp +=1
                        elif a[v] == "L":
                            change(matrix, firstInp, secondInp, "L")
                            secondInp -= 1

                    v += 1
                print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
                #sameDict["nameOfSame"]=control[1]
                #sameDict["sameControl"]=str(firstInp)
                #sameList.append(sameDict)

                break




    elif control[0]=="SAME":

        #print(len(sameList))
        #print(sameList[0]["nameOfSame"])
        for t in range(len(sameList)):

            if sameList[t]["nameOfSame"]==control[1]:
                a_index = next((index for (index,d) in enumerate(sameList) if d["nameOfSame"] == control[1]), None)
                b_index = next((index for (index, d) in enumerate(sameList) if d["nameOfSame"] == control[2]), None)
                if sameList[a_index]["sameControl"] == sameList[b_index]["sameControl"] or abs(int(sameList[a_index]["sameControl"])) == abs(int(sameList[b_index]["sameControl"])):
                    print("yes")

                else:
                    print("no")






    else:
        print("Please enter a valid comment...")