first_string = "123456"
second_string = "abcdefijkl"

half_of_first_str = int(len(first_string)/2)
half_of_second_str = int(len(second_string)/2)

new_second_string = second_string[:half_of_second_str] + first_string + second_string[(-half_of_second_str):]
new_first_string = first_string[:half_of_first_str] + new_second_string + first_string[(-half_of_first_str):]

print("Первая строка \f%s" %(first_string))
print("Вторая строка \f%s" %(second_string))

print("\nПервая новая строка \f%s" %(new_first_string))
print("Вторая новая строка \f%s" %(new_second_string))
