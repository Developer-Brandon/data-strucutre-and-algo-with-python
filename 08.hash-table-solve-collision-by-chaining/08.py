hash_table = list([0 for i in range(8)])

print('해쉬테이블 틀 만들기', hash_table)

def get_hash_key(key):
    return hash(key)


def hash_func(key):
    return key % 8

def select_hash_code_by_key(key):
    return hash_func(get_hash_key(key))

def save_value(key, value):
    index_of_key = get_hash_key(key)
    hash_code = hash_func(index_of_key)
    if hash_table[hash_code] != 0:  # 방어 로직입니다. # 데이터는 [hash_code: [index_of_key, value],hash_code: [index_of_key, value],hash_code: [index_of_key, value],hash_code: [index_of_key, value] .... ] 이런식으로 삽입될 예정입니다.
        for index in range(len(hash_table[hash_code])):  # hash table을 순회합니다.
            if hash_table[hash_code][index][0] == index_of_key:  # 만약 index_of_key 값이 동일한 녀석이 있으면
                hash_table[hash_code][index][1] = value  # value의 자리에 value 값을 넣습니다.
                return
        hash_table[hash_code].append([index_of_key, value])  # 만약 키값이 동일한 녀석이 없으면 그대로 다음 row에 삽입하면 됩니다
    else:  # 만약 해당 hash_code로 이루어진 자리가 맨 처음 생성된 hash_table의 데에터라면 그대로 대입해주면 될 것입니다
        hash_table[hash_code] = [[index_of_key, value]]

def select_value_by_key(key):
    index_of_key = get_hash_key(key)
    hash_code = hash_func(index_of_key)
    if hash_table[hash_code] != 0:
        for index in range(len(hash_table[hash_code])):  # Linked list 안을 순회해줍니다
            if hash_table[hash_code][index][0] == index_of_key:
                return hash_table[hash_code][index][1]
        return None
    else:
        return None


# 실행할때마다 Hash 값이 다르게 나오실 것입니다. 아래의 값이 같게 나올때까지 돌리신 후, 결과를 확인합니다.
# 스크립트 언어의 특성상 같은 hashCode값을 가진 데이터라면 후반에 쓰인 BMD에 대한 value가 나올텐데 그렇지 않고 제대로 값이 출력되실 겁니다.
save_value("AMD", "저는 AMD입니다. 저는 제대로 호출되었을까요?")
print("저장된 key값의 hash code", select_hash_code_by_key("Db"))
save_value("BMD", "저는 BMD입니다. 저는 제대로 호출되었을까요?")
print("저장된 key값의 hash code", select_hash_code_by_key("Dd"))

print(select_value_by_key("AMD"))
