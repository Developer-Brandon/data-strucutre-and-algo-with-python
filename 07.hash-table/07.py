hash_table = list()


# 해쉬 테이블에 dummy data 를 넣어줍니다
def make_hash_table():
    global hash_table
    for i in range(10):
        hash_table.append(i)


def print_hash_table():
    print('\n\n')
    print('1. 해쉬테이블 틀 만들기\n', hash_table)


make_hash_table()
print_hash_table()

print('\n\n')
print('####################')
print('\n\n')

print('2. 해쉬함수 정의하기 & 키값을 아스키 코드로 hash code 만들기')


# 임의로 해쉬 함수를 정의 합니다
def hash_key_function(key):
    return key % 5


# 임의의 키값 만들기
def make_dummy_data_for_key():
    global key1, key2, key3
    key1 = 'brandon'
    key2 = 'harry'
    key3 = 'mac'


def print_ascii_code_of_key_datas():
    print('brandon ascii code', ord(key1[0]))
    print('harry ascii code', ord(key2[0]))
    print('mac ascii code', ord(key3[0]))
    print('\n')


def print_hash_code_of_key_datas():
    print('brandon hash code', hash_key_function(ord(key1[0])))
    print('harry hash code', hash_key_function(ord(key2[0])))
    print('mac hash code', hash_key_function(ord(key3[0])))
    print('\n')


make_dummy_data_for_key()
print_ascii_code_of_key_datas()
print_hash_code_of_key_datas()

print('\n\n')
print('####################')
print('\n\n')

print('3. 해쉬테이블에 저장하고싶은 데이터를 키와 같이 저장하기')


def save_value(key, value):
    # 예제로 입력된 Harry의 아스키 코드값을 hash_key_function 함수에 넣어서 hash_code를 구합니다
    hash_code = hash_key_function(ord(key[0]))
    # hash_table에 hash_code 주소로 이루어진 장소에 'who am i ?' value를 넣습니다.
    hash_table[hash_code] = value


def select_value_by_key(key):
    # 입력된 키값을 아스키 코드값으로 변경하고 다시 해시코드를 입력합니다.
    hash_code = hash_key_function(ord(key[0]))
    # 테이블에서 hash_code를 바라보게 하여 조회합니다.
    return hash_table[hash_code]


# 데이터를 저장 합니다.
save_value(key2, 'who am i?')

# 키값으로 데이터를 조회합니다.
print(select_value_by_key(key2))

print('\n\n')
print('####################')
print('\n\n')
