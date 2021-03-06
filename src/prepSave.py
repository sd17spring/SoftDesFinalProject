"""
This module uses saveChoices moudle to store the traning data into CSV Files.

Project : Bomberman Bot with Machine Learning
Olin College Software Design Final Orject,  Spring 2017
By : TEAM AFK
"""


import saveChoices

# list of file names for our grid features
fileNames = ['training_data/wallsFULL.csv', 'training_data/bricksFULL.csv',
             'training_data/bombsFULL.csv', 'training_data/enemysFULL.csv']
fileDict = {'training_data/wallsFULL.csv': 1,
            'training_data/bricksFULL.csv': 2,
            'training_data/bombsFULL.csv': 9,
            'training_data/enemysFULL.csv': 7}


def convertFiles(myMat, x):
    '''
    Takes the array of places and convert them to a list of features
    The type of features will be determined by the parameter X
    '''
    listPlaces = []
    starty = 12
    endy = 21  # myMat.shape[1]
    startx = 16
    endx = 25  # myMat.shape[0]
    info = [10, 10, 10]

    # convert grid feature to a single line of features
    for i in range(starty, endy):
        for j in range(startx, endx):
            listPlaces.append(myMat.item((j, i)))
            # store bomb information
            if myMat.item((j, i)) == 9:
                dist = abs(20 - j) + abs(16 - i)
                if(info[0] == 10):
                    info[0] = dist
                elif(info[0] > dist):
                    info[0] = dist
            elif(myMat.item((j, i)) == 7):
                dist = abs(20 - j) + abs(16 - i)
                if(info[1] == 10):
                    info[1] = dist
                elif(info[1] > dist):
                    info[1] = dist
            elif(myMat.item((j, i)) == 2):
                dist = abs(20-j)+abs(16-i)
                if(info[2] == 10):
                    info[2] = dist
                elif(info[2] > dist):
                    info[2] = dist

    if(len(listPlaces) == 0):
        return

    # builds a list for each instance and add a 1 or 0 depending of the
    # presence of the object
    tempList = []
    for j in range(len(listPlaces)):
        if(listPlaces[j] == fileDict[fileNames[x]]):
            tempList.append(1)
        elif(x == 0 and (listPlaces[j] == 2 or listPlaces[j] == 7)):
            tempList.append(1)
        elif(x == 3 and listPlaces[j] == 8):
            tempList.append(1)
        else:
            tempList.append(0)

    return tempList, info


def saveFiles(tempList, info, i):
    '''
    Saves the feature list into csv for model training
    The file to save to will be determined by parameter i
    '''
    tempList = tempList + info
    saveChoices.addRow(fileNames[i], tempList)
