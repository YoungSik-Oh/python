# 레벤슈타인 거리 구하기

def calc_distance(a, b):
    if a == b: 
        return 0    # 레벤슈타인 거리 계산
    
    a_len = len(a)
    b_len = len(b)
    if a == "": return b_len
    if b == "": return a_len
    # 2차원 표 (a_len+1, b_len+1) 준비하기 --- 
    matrix = [[] for i in range(a_len + 1)]
    
    for i in range(a_len+1):     # 0으로 초기화
        matrix[i] = [0 for j in range(b_len + 1)]
    
    # 0일 때 초깃값을 설정
    for i in range(a_len + 1):
        matrix[i][0] = i
    
    for j in range(b_len + 1):
        matrix[0][j] = j
    
    # 표 채우기 --- 
    for i in range(1, a_len + 1):
        ac = a[i-1]
        print("ac : ", ac)
        for j in range(1, b_len + 1):
            bc = b[j - 1]
            cost = 0 if (ac == bc) else 1
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # 문자 삽입
                matrix[i][j-1] + 1,     # 문자 제거
                matrix[i-1][j-1] + cost # 문자 변경
            ])
        print("matrix:", matrix)
    return matrix[a_len][b_len]

# "가나다라"와 "가마바라"의 거리 --- 
print(calc_distance("가나다라","가마바라"))
    # ac :  가
    # matrix: [[0, 1, 2, 3, 4], [1, 0, 1, 2, 3], [2, 0, 0, 0, 0], [3, 0, 0, 0, 0], [4, 0, 0, 0, 0]]
    # ac :  나
    # matrix: [[0, 1, 2, 3, 4], [1, 0, 1, 2, 3], [2, 1, 1, 2, 3], [3, 0, 0, 0, 0], [4, 0, 0, 0, 0]]
    # ac :  다
    # matrix: [[0, 1, 2, 3, 4], [1, 0, 1, 2, 3], [2, 1, 1, 2, 3], [3, 2, 2, 2, 3], [4, 0, 0, 0, 0]]
    # ac :  라
    # matrix: [[0, 1, 2, 3, 4], [1, 0, 1, 2, 3], [2, 1, 1, 2, 3], [3, 2, 2, 2, 3], [4, 3, 3, 3, 2]]
    # 2

print("\n\n---실행 예-------------------")
samples = ["강남역","신사동","강남역삼동"]
#samples = ["강남역","강감찬장군묘역","강나루","신사동","강남역삼동"]
base = samples[0]
r = sorted(samples, key = lambda n: calc_distance(base, n))
for n in r:
    print(calc_distance(base, n), n)

# ---실행 예-------------------
# ac :  강
# matrix: [[0, 1, 2, 3], [1, 1, 2, 3], [2, 0, 0, 0], [3, 0, 0, 0]]
# ac :  남
# matrix: [[0, 1, 2, 3], [1, 1, 2, 3], [2, 2, 2, 3], [3, 0, 0, 0]]
# ac :  역
# matrix: [[0, 1, 2, 3], [1, 1, 2, 3], [2, 2, 2, 3], [3, 3, 3, 3]]
# ac :  강
# matrix: [[0, 1, 2, 3, 4, 5], [1, 0, 1, 2, 3, 4], [2, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0]]
# ac :  남
# matrix: [[0, 1, 2, 3, 4, 5], [1, 0, 1, 2, 3, 4], [2, 1, 0, 1, 2, 3], [3, 0, 0, 0, 0, 0]]
# ac :  역
# matrix: [[0, 1, 2, 3, 4, 5], [1, 0, 1, 2, 3, 4], [2, 1, 0, 1, 2, 3], [3, 2, 1, 0, 1, 2]]
# 0 강남역
# ac :  강
# matrix: [[0, 1, 2, 3, 4, 5], [1, 0, 1, 2, 3, 4], [2, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0]]
# ac :  남
# matrix: [[0, 1, 2, 3, 4, 5], [1, 0, 1, 2, 3, 4], [2, 1, 0, 1, 2, 3], [3, 0, 0, 0, 0, 0]]
# ac :  역
# matrix: [[0, 1, 2, 3, 4, 5], [1, 0, 1, 2, 3, 4], [2, 1, 0, 1, 2, 3], [3, 2, 1, 0, 1, 2]]
# 2 강남역삼동
# ac :  강
# matrix: [[0, 1, 2, 3], [1, 1, 2, 3], [2, 0, 0, 0], [3, 0, 0, 0]]
# ac :  남
# matrix: [[0, 1, 2, 3], [1, 1, 2, 3], [2, 2, 2, 3], [3, 0, 0, 0]]
# ac :  역
# matrix: [[0, 1, 2, 3], [1, 1, 2, 3], [2, 2, 2, 3], [3, 3, 3, 3]]
# 3 신사동