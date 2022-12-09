from sys import argv, exit

# your countInv code must be based on merge sort and must run in O(n log n) time, where n is the input size


# provided
#
# Read integers from the given filename.
#
# Return value: list of integers
def read_array(filename):
    try:
        with open(filename) as f:
            return [int(n) for n in f.read().split()]
    except:
        exit("Couldn’t read numbers from file \""+filename+"\"")


# implement
#
# Return the number of inversions in the given list,
# by doing a merge sort and counting the inversions.
#
# Return value: number of inversions
def count_inversions(in_list):
    lenList = len(in_list)

    if lenList <= 1:
        return 0
    else:
        # dividing list into two halves
        halfLen = lenList // 2
        l_list = in_list[:halfLen]
        r_list = in_list[halfLen:]

        # call each half to count_inversions & merge_i
        l_half = count_inversions(l_list)
        r_half = count_inversions(r_list)
        merge_list = merge_i(l_list, r_list, in_list)

    numInv = l_half + r_half + merge_list

    return numInv


# implement
#
# Merge the left & right lists into in_list.  in_list already contains
# values--replace those with the merged values.
#
# Return value: inversion count
def merge_i(l_list, r_list, in_list):
    invCount = 0
    in_list.clear()

    while len(l_list) !=0 and len(r_list)!=0:
        if l_list[0] > r_list[0]:
            # put smallest (Rj) in list
            in_list.append(r_list.pop(0))

            # Rj is smallest so add num of elements remaining in L to out
            invCount += len(l_list)
        else:
            # put smallest (Li) in list
            in_list.append(l_list.pop(0))

    if l_list or r_list == 0:
        # 'append the other one to list'
        if l_list == 0:
            in_list.extend(r_list)
        else:
            in_list.extend(l_list)

    return invCount


# provided
if __name__ == '__main__':
    if len(argv) != 2:
        exit("usage: python3 "+argv[0]+" datafile")
    in_list = read_array(argv[1])
    print(count_inversions(in_list))
