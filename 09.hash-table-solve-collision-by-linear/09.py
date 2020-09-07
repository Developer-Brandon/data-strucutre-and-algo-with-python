hash_table = list([0 for i in range(8)])


def get_hash_key(key):
    return hash(key)


def hash_func(key):
    return key % 8


def save_value(key, value):
    index_of_key = get_hash_key(key)
    hash_code = hash_func(index_of_key)

    if hash_table[hash_code] != 0:
        for index in range(hash_code, len(hash_table)):  # hash_code(해쉬코드에 해당하는 수)에서 부터 전체 hash_table의 수만큼 순회합니다
            if hash_table[index] == 0:  # 순회하다가 만약 해당 hash_code 자리에 아무것도 없다면 값을 삽입하고
                hash_table[index] = [index_of_key, value]
                return
            elif hash_table[index][0] == index_of_key:  # index의 key값이 현재 입력한 key값과 동일한 데이터를 찾았다면
                hash_table[index][1] = value  # 덮어 씌워 줍니다
                return
    else:
        hash_table[hash_code] = [index_of_key, value]


def select_value_by_key(key):
    index_of_key = get_hash_key(key)
    hash_code = hash_func(index_of_key)

    if hash_table[hash_code] != 0:
        for index in range(hash_code, len(hash_table)):
            if hash_table[index] == 0:  # 비어있으면 아무것도 꺼내지말고
                return None
            elif hash_table[index][0]:  # 있으면 value 값을 꺼냅니다.
                return hash_table[index][1]
    else:
        return None


save_value('AMD', '저는 AMD 입니다.')
save_value('AMD', '저는 두번쨰 AMD 입니다.')
save_value('BMD', '저는 BMD 입니다.')
print(select_value_by_key('AMD'))
