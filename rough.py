# # binary search
# def binary_search(array,search_value):
#     first_index = 0 
#     last_index = len(array) -1 

#     while first_index <= last_index :
#         mid = (first_index + last_index)//2
#         value_at_mid = array[mid]

#         if value_at_mid == search_value :
#             return mid 
#         elif search_value > value_at_mid :
#             first_index = mid + 1 
#         elif search_value < value_at_mid :
#             last_index = mid  - 1


# array = [1,2,3,4,5,6]
# search_value = 10

# print(binary_search(array,search_value))

# # is prime number 
# def is_prime(number):
#     for i in range(2,number):
#         if number%i ==0 :
#             return False 
#     return True 
# number = int(input("please enter the number: "))
# print(is_prime(number))


# # leap year 

# def is_leap_year(year):
#     if year % 100 == 0 :
#         if year %400 == 0 :
#             return False 
#         return True 
#     return year % 4 == 0 

# year = int(input("enter the year to check leap year or not "))

# print(is_leap_year(year))

# # chess board 

# def chess_board(number_of_grains):
#     placed_grain = 1 
#     chess_board_space = 1 

#     while placed_grain < number_of_grains:
#         placed_grain *= 2 
#         chess_board_space += 1 
    
#     return chess_board_space 

# number_of_grains = int(input("enter the number of grains "))

# print(chess_board(number_of_grains))
    
# def chess_board_2(chess_board_space):
#     placed_grain = 1
#     inital_chess_board_space = 1 

#     while inital_chess_board_space < chess_board_space:
#         placed_grain *= 2 
#         inital_chess_board_space += 1 
#     return placed_grain

# chess_board_space = int(input("enter the board space "))

# print(chess_board_2(chess_board_space))

# bubble sort 

# def bubble_sort(array):
#     first_pointer = 0
#     second_pointer = 1
#     loop_count = len(array) -1 

#     for i in range(len(array) - 1):

#         while second_pointer <= loop_count: 
#             if array[first_pointer] > array[second_pointer] :
#                 array[first_pointer],array[second_pointer] = array[second_pointer],array[first_pointer]
#                 first_pointer = second_pointer 
#                 second_pointer += 1 
#             else :
#                 first_pointer = second_pointer
#                 second_pointer += 1 
    
#         loop_count -= 1 
#         first_pointer = 0 
#         second_pointer = 1 


    
#     return array 

# array = [7,4,123,10,3,2,1]

# print(bubble_sort(array))


# def bubble_sort(array):
#     unsorted_until_index = len(array) - 1 
#     sorted = False 

#     while not sorted :
#         sorted = True 
#         for i in range(unsorted_until_index):
#             if array[i] > array[i+1]:
#                 array[i],array[i+1] = array[i+1],array[i]
#                 sorted = False 
#         unsorted_until_index -= 1 
    
#     return array 


# def has_dups(array):
#     for i in range(len(array)-1):
#         for j in range(i+1,len(array)):
#             if array[i] == array[j]:
#                 return "dups exists"
    
#     return "dups does not exists"

# array = [1,5,3,11,9,1]

# print(has_dups(array))


# def has_dups(array):
#     numbers = set()

#     for num in array :
#         if num not in numbers :
#             numbers.add(num)
#         else:
#             return "dups exist"
        
#     return "dups does not exist"

# array = [1,5,3,11,9]

# print(has_dups(array))


## single greatest number 

# def sing_greatest_number(array):

#     current_greatest = float('-inf')

#     for num in array :
#         if num > current_greatest :
#             current_greatest = num 
    
#     return current_greatest 

# array = [10,12,5,44,1]

# print(sing_greatest_number(array))

# def selection_sort(array):
#     for i in range(len(array)-1):
#         starting_index = i 
#         lowest_index_so_far = i
#         lowest_value_so_far = array[i]

#         for j in range(starting_index+1,len(array)):
#             if array[j] < lowest_value_so_far:
#                 lowest_value_so_far= array[j]
#                 lowest_index_so_far = j 
        
#         array[starting_index],array[lowest_index_so_far] = array[lowest_index_so_far],array[starting_index]
    
#     return array 

        


# array = [4,2,7,1,3]

# print(selection_sort(array))

## Insertion sort 

# def insertion_sort(array):
#     for index in range(1,len(array)):
#         temp_value = array[index]
#         position = index - 1 

#         while position >= 0 :
#             if array[position] > temp_value :
#                 array[position +1] = array[position]
#                 position = position - 1 
#             else:
#                 break 
        
#         array[position+1] = temp_value 
#     return array 


# array = [4,2,7,1,3]


# print(insertion_sort(array))

# word builder 


# def word_builder(array):
#     words = []

#     for char in array :
#         for char_2 in array :
#             if char != char_2:
#                 words.append(char + char_2)
    
#     return words

# # array = ['a','b','c','d']
# # print(word_builder(array))

# def merge_array(array_1,array_2):
#     new_array = []
#     array_1_pointer = 0 
#     array_2_pointer = 0 
#     while array_1_pointer <= (len(array_1) -1) and array_2_pointer <= (len(array_2) - 1):
#         if array_1[array_1_pointer] < array_2[array_2_pointer] :
#             new_array.append(array_1[array_1_pointer])
#             array_1_pointer += 1 
#         else:
#             new_array.append(array_2[array_2_pointer])
#             array_2_pointer += 1 

#     if array_1_pointer <= (len(array_1) - 1) :
#         new_array.extend(array_1[array_1_pointer:])
#     elif array_2_pointer <= (len(array_2) -1) :
#         new_array.extend(array_2[array_2_pointer:])
    
#     return new_array 


# array_2 = [2,4]
# array_1 = [1,3,5,6]

# print(merge_array(array_1,array_2))

# # needle and haystack 


# def find_needle(needle,haystack):
#     list_1 = []

#     for i in range(len(haystack)):
#         if needle[0] == haystack[i]:
#             list_1.append(i)
    
#     indeces = []
#     for num in list_1:
#         if haystack[num:num+len(needle)] == needle :
#             return True 
    
#     return False 
        



# needle = 'def'
# haystack = 'abdecdefghi'


# print(find_needle(needle,haystack))


# def greatest_product(array):
#     sorted_array = sorted(array)
#     condition_1 = sorted_array[0] * sorted_array[1] * sorted_array[-1]
#     condition_2 = sorted_array[-1] * sorted_array[-2] * sorted_array[-3]

#     return max(condition_1,condition_2)

# array = [-88,-99,10,4,2]

# print(greatest_product(array))


def greatest_product(array):
    max1 = max2 = max3 = float("-inf")
    min1 = min2 = float("inf")

    for num in array :
        if num > max1 :
            max1,max2,max3 = num,max1,max2 
        elif num > max2 :
            max2,max3 = num,max2 
        elif num > max3 :
            max3 = num 
    
    for num in array :
        if num < min1 :
            min1,min2 = num,min1 
        elif num < min2:
            min2 = num
    
    return max(max1*max2*max3,min1*min2*max1)



array = [-88,-99,10,4,2]

print(greatest_product(array))
