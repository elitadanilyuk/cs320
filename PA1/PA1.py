import math
import numpy as np
import argparse

# begin PROVIDED section - do NOT modify ##################################

count = 0

def getArgs() :
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type = str, help = 'File containing terrain')
    
    parser.add_argument('h', type = float, help = 'h value')
    
    parser.add_argument('theta', type = float, help = 'Angle of elevation for Sun')
    parser.add_argument('algorithm', type = str, help = 'naive | early | fast')
    return parser.parse_args()

def compare(x,y):
    global count
    count += 1
    if abs(x-y) < .000000000001 :
        return False
    if x < y :
        return True
    else:
        return False

def print_shade(boolean_array):
    for row in boolean_array:
        for column in row:
            if column == True:
                print ('*    ', end = '')
            elif column == False:
                print ('0    ', end = '')
        print('\n')
        
def read2Dfloat(fileName) : # read CSV of floats into 2D array
    array2D = []
    # Read input file
    f = open(fileName, "r")
    data = f.read().split('\n')
    
    # Get 2-D array
    for row in data[0:-1]:
        float_list = list(map(float, row.split(',')[0:-1]))
        array2D.append(float_list)

    return array2D

def runTest(args, terrain = None) :

    
    # Initialize counter
    global count
    count = 0

    theta = np.deg2rad(args.theta)
    
    if terrain == None :
      terrain = read2Dfloat(args.input_file)

    N     = len(terrain)
    shade = [[False] * N for i in range(N)]

    if args.algorithm == 'naive':
        result = naive(terrain, args.h, theta, N, shade)
    elif args.algorithm == 'early':
        result = earlyexit(terrain, args.h, theta, N, shade)
    elif args.algorithm == 'fast':
        result = fast(terrain, args.h, theta, N, shade)

    return result

# end PROVIDED section ##################################

# Fritz Sieker 

def isNotShady(elv_k, elv_j, h, angle):

    # if (elv_k - elv_j) == 0:
    #     return False
    # else:
        height = (elv_k - elv_j) / h
        tanTheta = math.tan(angle)

        # if compare(tanTheta, height):
        #     return False
        # else

        return compare(tanTheta, height)
    

###### Complete this function
def naive(image,h,angle,N,shade):
    # Loop with quadratic time (n^2)
    for x in range(N):
        for y in range(N):
            if compare(y, x):
                shade[x][y] = isNotShady(0, image[x][y], h, angle)
            else:
                shade[x][y] = isNotShady(image[x][y-1], image[x][y], h, angle)

    print()

    return shade

###### Complete this function
def earlyexit(image, h, angle, N, shade):
    # as soon as we find point that puts J in shade, exit
    # currentValue = image[0][0]
    maxValue = image[0][0]

    for x in range(N):
        maxValue = image[x][0]
        for y in range(N):
            if y==0:
                shade[x][y] = False
            elif compare(maxValue, image[x][y]):
                maxValue = image[x][y]
                shade[x][y] = isNotShady(maxValue, image[x][y], h, angle)
            else:
                shade[x][y] = isNotShady(image[x][y-1], image[x][y], h, angle)

    print()

    return shade

###### Complete this function
def fast(image, h, angle, N, shade):
    # exploit running max
    currentMax = 0
    maxValue = 0

    for x in range(N):
        for y in range(N):
            currentMax = image[x][y]
            if y==0:
                maxValue = image[x][y]
                shade[x][y] = isNotShady(0, image[x][y], h, angle)
            else:
                shade[x][y] = isNotShady(image[x][y-1], image[x][y], h, angle)

    print()

    return shade

    return shade
    
if __name__ == '__main__':
    answer = runTest(getArgs())
    print_shade(answer)
    print('Number of comparisons: ' + str(count))
