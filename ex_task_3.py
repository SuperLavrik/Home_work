def solution(snake_style):
    split_style = snake_style.split("_")
    camelizedstyle =""
    for i in split_style:
        camelizedstyle += str(i).title()
    print (camelizedstyle)

snake_style = "this_is_var_name"
print(snake_style)
solution(snake_style)

