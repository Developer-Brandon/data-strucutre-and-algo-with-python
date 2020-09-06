def sum_all_with_for(data):
    sum = 0
    for i in range(data+1):
       sum += i
    print('\n\n')
    print('for문을 이용한 1~10까지의 합', sum)

sum_all_with_for(10)


def sum_all_without_for(data):
    sum = int(data * (data+1) / 2)
    print('\n\n')
    print('for문을 이용하지 않은 1~10까지의 합',sum)


sum_all_without_for(10)
