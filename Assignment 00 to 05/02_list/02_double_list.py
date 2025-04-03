
def test(num):
    num = [1,2,3,7]
    display_list = []
    for i in range(len(num)):
        display_list = num[i]
        num[i] = display_list*2
    print("number = ["+num+"]")


test(list)