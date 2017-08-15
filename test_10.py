import random

number_column = 3
number_string = 8

lower_bound  = 1
upper_bound = 100

matrix = [[random.randint(lower_bound, upper_bound) for j in range(number_column)]
          for i in range(number_string)]

print (" Initial matrix:")
for i in range (number_string):
    for j in range (number_column):
        print (matrix[i][j], end = "\t\t" )
    print()

transp_matrix = [[matrix[i][j] for i in range (number_string)] for j in range (number_column)]

print ("\n Transposed matrix:")
for k in range (number_column):
    for l in range (number_string):
        print (transp_matrix[k][l], end = "\t\t" )
    print()