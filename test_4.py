count_digit = 5
multip_odd = 0

print("Input %d-digit number  - " % count_digit, end="")
x = str(input())

for i in range(count_digit):
    if i >= len(x):             # if input number less counn_digit
        x +="1"
    if   int(x[i])%2:
        if not multip_odd:      #  when we have fist odd number
            multip_odd = 1
        multip_odd *= int(x[i])

print ("Multiplication odd digit in %d - digit number = %d" % (count_digit, multip_odd))