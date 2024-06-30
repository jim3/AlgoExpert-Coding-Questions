# two number sum
def get_counter(arr):
    # initialize a hash map to store each number and its count
    counter = {}
    for num in arr:
        # check if num is a key in the hash map
        if num in counter:
            # update the count of num to increase by 1
            counter[num] += 1
        else:
            # set the count of num to 1
            counter[num] = 1
    return counter
