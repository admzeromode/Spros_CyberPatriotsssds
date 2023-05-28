import random

import csv
import numpy as np


def poisk_sezonov(arr, chast, tocn):
    """ 
    [ arr ] - данные 'x' и 'y' (тип 'list' [[x],[y]])\n
    [ chast ] - частота (тип 'int')\n
    [ tocn ] - погрешность (тип 'int' или 'float')\n
    \n
    возвращает 3 списка формата [[координаты 'x'], [координаты 'y']]
    """


    def create_chasti(arr, win):
        patterns = []
        k = 0
        j = 0
        rab = [[], []]
        for i in arr[1]:
            if (k % win == 0 and k != 0):
                patterns.append([[], []])
                patterns[j][0].append(rab[0])
                patterns[j][1].append(rab[1])
                rab.clear()
                rab.append([])
                rab.append([])
                j += 1

            rab[0].append(i)
            rab[1].append(k)
            k += 1
        else:
            patterns.append([[], []])
            patterns[j][0].append(rab[0])
            patterns[j][1].append(rab[1])

        
        return patterns

    pat_10 = create_chasti(arr, chast) ### ОКНО
    
    vozr_10 = []
    yb_10 = []
    norm_10 = []
    vsplesk_10 = []

    for i in pat_10:
        mean = np.mean(np.array(i[0][0], float))
        std = np.std(np.array(i[0][0], float))
        if (i[0][0][0] < i[0][0][-1] and i[0][0][-1] > mean):
            
            y_r = [i[0][0][0], i[0][0][-1]]
            x_r = [i[1][0][0], i[1][0][-1]]

            t1 = (float(i[0][0][-1]) - float(i[0][0][0]))
            t2_1 = ((float(i[0][0][-1]) - float(i[0][0][0]))**2) 
            t2_2 = ((float(i[1][0][-1]) - float(i[1][0][0]))**2)
            t2 = (t2_1 + t2_2)**0.5
            cos = t1 / t2

            
            vozr_10.append([x_r, y_r, cos])

        elif (i[0][0][0] > i[0][0][-1] and i[0][0][-1] < mean):
            
            y_r = [i[0][0][0], i[0][0][-1]]
            x_r = [i[1][0][0], i[1][0][-1]]

            t1 = (float(i[0][0][0]) - float(i[0][0][-1]))
            t2_1 = ((float(i[0][0][0]) - float(i[0][0][-1]))**2) 
            t2_2 = ((float(i[1][0][0]) - float(i[1][0][-1]))**2)
            t2 = (t2_1 + t2_2)**0.5
            cos = t1 / t2
            yb_10.append([x_r, y_r, cos])

        elif (len([*filter(lambda x: x < std+mean, i[0][0])]) > 0):
            y_r = i[0][0]
            x_r = i[1][0]
            norm_10.append([x_r, y_r])

        elif (len([*filter(lambda x: x < std+mean, i[0][0])]) < 1):
            y_r = i[0][0]
            x_r = i[1][0]

            vsplesk_10.append([x_r, y_r])

    rr = [vozr_10, yb_10]

    vozr_ = []

    for i in rr:
        for m in i:
            k = 0
            ra = []
            ra.append(m)
            for j in i:
                
                if m[2] > j[2]:
                    razn = j[2] / (m[2] / 100)
                elif m[2] < j[2]:
                    razn = m[2] / (j[2] / 100)
                else:
                    razn = 0
                
                if (m[0] != j[0] and k != 0 and razn <= tocn): ### ТОЧНОСТЬ
                    ra.append([j[0], j[1]])
                    #print(f'cos j = {j[2]} cos m = {m[2]} разница {razn}')
                    
                k += 1
            if len(ra) > 1:
                vozr_.append(ra)

    return vozr_, norm_10, vsplesk_10



