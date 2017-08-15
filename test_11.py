import random

def print_matrix(caption, matrix,string,column):
    print()
    print(caption)
    for i in range(string):
        for j in range(column):
            print(matrix[i][j], end="\t\t")
        print()
    return

number_column = 10
number_string = 9

lower_bound  = 1
upper_bound = 100

matrix = [[random.randint(lower_bound, upper_bound) for j in range(number_column)]
          for i in range(number_string)]

print_matrix("\tInitial matrix:",matrix,number_string,number_column)

transpod_matrix = [[matrix[i][j] for i in range (number_string)] for j in range (number_column)]

for j in range(number_column):
    transpod_matrix[j].sort()
    if (j+1)%2 :
        transpod_matrix[j].reverse()

sort_matrix = [[transpod_matrix[i][j] for i in range(number_column)] for j in range(number_string)]

print_matrix("\tSort matrix:",sort_matrix,number_string,number_column)

