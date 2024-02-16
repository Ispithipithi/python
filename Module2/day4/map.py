# my_string = "this is a Ccollege where new prin is appointed"
# upper_string = my_string.upper()
# upper_string_lambda = lambda x : x.upper()

# def func_upper(word):
#     if word.startsswith("c"):
#         word.title()
#     else:
#         word.upper()
#     return word
    
# splited_list =my_string.split(" ")
# final_ans = list(map(my_string, splited_list))
# print(splited_list)
# print(final_ans)


jpt_list="THIS IS WORLD Where WE LIVE AND SLEEP"
def func_jpt(word,index):
    if index % 2 == 0:
        result_word = word.upper()
    else:
        result_word = word.title()
    return result_word
result = [func_jpt(word, index) for index, word in enumerate(jpt_list.split())]
print(result)
print(" ".join(result))
print("-".join(result))
