import random, math

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    tries = 0
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        tries = tries + 1
        if guess == item:
            return mid, tries
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1 
    return None


my_list = list(range(-100000, 7821803))

#print(binary_search(my_list, 6))
#print(binary_search(my_list, -1))

# Recursive Version
# Getting a low and a high, with a goal number
def binary_search_two2(arr, goal_num=None, tries=0):
    low = 0
    high = len(arr) - 1
    mid = math.ceil((len(arr) / 2) - 1)
    if goal_num == None:  # If the there is not goal(on init).
        goal_num = random.randint(low, high + 1)  # actual num from lo to hi
        print("The goal num is {}".format(goal_num))
    print("Guessing number between {} and {}".format(arr[low], arr[high]))
    print()
    tries += 1
    if arr[mid] > goal_num:
        print("too high {}".format(goal_num))
        arr = arr[low:mid + 1]
    elif arr[mid] < goal_num:
        print("too low, {}".format(goal_num))
        arr = arr[mid:high + 1]
    elif arr[mid] == goal_num:
        print("you won")
        return "It took {} tries".format(tries)
    print("tries {}".format(tries))
    binary_search_two2(arr, goal_num, tries)


binary_search_two2(list(range(1, 3999999999)))
