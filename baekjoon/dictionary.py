# 사전 자료형은 키 값의 쌍을 데이터로 가지는 자료형, 순서 X, 중괄호 {}
# 변경 불가능한 자료형을 키로 사용 가능 => (튜플)
# 해시 테이블을 사용하여 조회 및 수정 => O(1) 시간
# 데이터 저장 관리 효율 > 리스트

data = dict()
data['apple'] = 'sweet'
data['appley'] = 'sweety'
data['applee'] = 'sweete'
print(data)

# 키만 뽑기 벨류만 뽑기
key_list = list(data.keys())
value_list = data.values()

print(key_list)
print(value_list)
