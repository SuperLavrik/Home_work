def sum_code(symbol_1,symbol_2):
    step = 1
    if ord(symbol_1) > ord(symbol_2):   # direction of counting
        step = -1                       # if first symbol bihind of second
    total = 0
    for i in range(ord(symbol_1),(ord(symbol_2) + step),step):
        total += i

    return total

first_symbol = "t"
second_symbol = "@"

print("Sum of number Unicode between symbol %s and %s  = %d" % \
      (first_symbol, second_symbol, sum_code(first_symbol,second_symbol)))
