import numpy as np


def middle_change(img):
    a = img
    a1 = a[15,15].astype(int)
    a2 = a[15,16].astype(int)
    a3 = a[16,15].astype(int)
    a4 = a[16,16].astype(int)

    middle_p_R = [a1[0],a2[0],a3[0],a4[0]]
    middle_p_G = [a1[1],a2[1],a3[1],a4[1]]
    middle_p_B = [a1[2],a2[2],a3[2],a4[2]]
    middle_average_R = int(np.mean(middle_p_R))
    middle_average_G = int(np.mean(middle_p_G))
    middle_average_B = int(np.mean(middle_p_B))

    difference_a1 = abs(a1[0]-middle_average_R) + abs(a1[1] - middle_average_G) + abs(a1[2] - middle_average_B)
    difference_a2 =abs(a2[0]-middle_average_R) + abs(a2[1] - middle_average_G) + abs(a2[2] - middle_average_B)
    difference_a3 =abs(a3[0]-middle_average_R) + abs(a3[1] - middle_average_G) + abs(a3[2] - middle_average_B)
    difference_a4 =abs(a4[0]-middle_average_R) + abs(a4[1] - middle_average_G) + abs(a4[2] - middle_average_B)

    if difference_a1 >= difference_a2 and difference_a1 >= difference_a3 and difference_a1 >= difference_a4:
        return [16,16,middle_average_R,middle_average_G,middle_average_B]
        
    if difference_a2 >= difference_a1 and difference_a2 >= difference_a3 and difference_a2 >= difference_a4:
        return [16,17,middle_average_R,middle_average_G,middle_average_B]
        
    if difference_a3 >= difference_a1 and difference_a3 >= difference_a2 and difference_a3 >= difference_a4:
        return [17,16,middle_average_R,middle_average_G,middle_average_B] 
        
    if difference_a4 >= difference_a1 and difference_a4 >= difference_a2 and difference_a4 >= difference_a3:
        return [17,17,middle_average_R,middle_average_G,middle_average_B]  
        


def middle_change_alter(img):
    a = img
    a1 = a[15,15].astype(int)
    a2 = a[15,16].astype(int)
    a3 = a[16,15].astype(int)
    a4 = a[16,16].astype(int)

    middle_p_R = [a1[0],a2[0],a3[0],a4[0]]
    middle_p_G = [a1[1],a2[1],a3[1],a4[1]]
    middle_p_B = [a1[2],a2[2],a3[2],a4[2]]
    middle_average_R = int(np.mean(middle_p_R))
    middle_average_G = int(np.mean(middle_p_G))
    middle_average_B = int(np.mean(middle_p_B))

    difference_a1 = abs(a1[0]-middle_average_R) + abs(a1[1] - middle_average_G) + abs(a1[2] - middle_average_B)
    difference_a2 =abs(a2[0]-middle_average_R) + abs(a2[1] - middle_average_G) + abs(a2[2] - middle_average_B)
    difference_a3 =abs(a3[0]-middle_average_R) + abs(a3[1] - middle_average_G) + abs(a3[2] - middle_average_B)
    difference_a4 =abs(a4[0]-middle_average_R) + abs(a4[1] - middle_average_G) + abs(a4[2] - middle_average_B)

    if difference_a1 >= difference_a2 and difference_a1 >= difference_a3 and difference_a1 >= difference_a4:
        return [16,16,255-middle_average_R,255-middle_average_G,255-middle_average_B]
        # print('a1')
    if difference_a2 >= difference_a1 and difference_a2 >= difference_a3 and difference_a2 >= difference_a4:
        return [16,17,255-middle_average_R,255-middle_average_G,255-middle_average_B]
        # print('a2') 
    if difference_a3 >= difference_a1 and difference_a3 >= difference_a2 and difference_a3 >= difference_a4:
        return [17,16,255-middle_average_R,255-middle_average_G,255-middle_average_B] 
        # print('a3')
    if difference_a4 >= difference_a1 and difference_a4 >= difference_a2 and difference_a4 >= difference_a3:
        return [17,17,255-middle_average_R,255-middle_average_G,255-middle_average_B]  
        # print('a4')

def another_middle_change(img):
    a = img
    a1 = a[15,15].astype(int)
    a2 = a[15,16].astype(int)
    a3 = a[16,15].astype(int)
    a4 = a[16,16].astype(int)

    R = []
    G = []
    B = []
    for i in range(32):
        for j in range(32):
            R.append(a[i][j][0])
            G.append(a[i][j][1])
            B.append(a[i][j][2])


    average_R = int(np.mean(R))
    average_G = int(np.mean(G))
    average_B = int(np.mean(B))

    difference_a1 = abs(a1[0]-average_R) + abs(a1[1] - average_G) + abs(a1[2] - average_B)
    difference_a2 =abs(a2[0]-average_R) + abs(a2[1] - average_G) + abs(a2[2] - average_B)
    difference_a3 =abs(a3[0]-average_R) + abs(a3[1] - average_G) + abs(a3[2] - average_B)
    difference_a4 =abs(a4[0]-average_R) + abs(a4[1] - average_G) + abs(a4[2] - average_B)

    if difference_a1 >= difference_a2 and difference_a1 >= difference_a3 and difference_a1 >= difference_a4:
        return [16,16,average_R,average_G,average_B]
        
    if difference_a2 >= difference_a1 and difference_a2 >= difference_a3 and difference_a2 >= difference_a4:
        return [16,17,average_R,average_G,average_B]
        
    if difference_a3 >= difference_a1 and difference_a3 >= difference_a2 and difference_a3 >= difference_a4:
        return [17,16,average_R,average_G,average_B] 
        
    if difference_a4 >= difference_a1 and difference_a4 >= difference_a2 and difference_a4 >= difference_a3:
        return [17,17,average_R,average_G,average_B]  


def another_middle_change_alter(img):
    a = img
    a1 = a[15,15].astype(int)
    a2 = a[15,16].astype(int)
    a3 = a[16,15].astype(int)
    a4 = a[16,16].astype(int)

    R = []
    G = []
    B = []
    for i in range(32):
        for j in range(32):
            R.append(a[i][j][0])
            G.append(a[i][j][1])
            B.append(a[i][j][2])


    average_R = int(np.mean(R))
    average_G = int(np.mean(G))
    average_B = int(np.mean(B))

    difference_a1 = abs(a1[0]-average_R) + abs(a1[1] - average_G) + abs(a1[2] - average_B)
    difference_a2 =abs(a2[0]-average_R) + abs(a2[1] - average_G) + abs(a2[2] - average_B)
    difference_a3 =abs(a3[0]-average_R) + abs(a3[1] - average_G) + abs(a3[2] - average_B)
    difference_a4 =abs(a4[0]-average_R) + abs(a4[1] - average_G) + abs(a4[2] - average_B)

    if difference_a1 >= difference_a2 and difference_a1 >= difference_a3 and difference_a1 >= difference_a4:
        return [16,16,255-average_R,255-average_G,255-average_B]
        
    if difference_a2 >= difference_a1 and difference_a2 >= difference_a3 and difference_a2 >= difference_a4:
        return [16,17,255-average_R,255-average_G,255-average_B]
        
    if difference_a3 >= difference_a1 and difference_a3 >= difference_a2 and difference_a3 >= difference_a4:
        return [17,16,255-average_R,255-average_G,255-average_B] 
        
    if difference_a4 >= difference_a1 and difference_a4 >= difference_a2 and difference_a4 >= difference_a3:
        return [17,17,255-average_R,255-average_G,255-average_B]  


def get_average(img):
    a = img
    R = []
    G = []
    B = []
    for i in range(32):
        for j in range(32):
            R.append(a[i][j][0])
            G.append(a[i][j][1])
            B.append(a[i][j][2])


    average_R = int(np.mean(R))
    average_G = int(np.mean(G))
    average_B = int(np.mean(B))

    average = []
    average.append(average_R)
    average.append(average_G)
    average.append(average_B)
    return average