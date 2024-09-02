# 비트 조작
"""
본래 비트를 조작하는 것은 하드웨어와 관련이 깊다.
  * 섀넌이 전기회로 스위치의 On/Off를 이용한 스위칭 회로를 연구한 것이 시초
  * True, False 2개 값으로 논리 연산을 설명하는 부울대수 (Boolean Algebra)를 회로에 적용해 논리 게이트를 만듬

부울 연산
  * AND, OR, NOT이 기본 부울 연산자로 서로 조합하여 대른 보조 연산 생성 가능
  * XOR가 대표적인 보조 연산에 해당됨 (x and not y) or (not x and y)
NOT
NOT F = T
NOT T = F

AND
F AND F = F
F AND T = F
T AND F = F
T AND T = T

OR
F OR F = F
F OR T = T
T OR F = T
T OR T = T

XOR
F XOR F = F
F XOR T = T
T XOR F = T
T XOR T = F

비트 연산자 (python)
"""

if __name__=="__main__":
    # 비트 연산
    True & False
    # False
    True | False
    # True
    True ^ False
    # False
    ~ True
    # -2

    # 비트 조작
    bin(0b1101 >> 2)
    # '0b11'
    bin(0b1101 << 2)
    # '0b110100'
    # ***
    bin(0b0101 ^ ~0b1100)
    # '-0b1010'

    # 자리수 제한 연산 (0b1100 -> 0b0011)
    """
    자릿수 만큼의 최대값을 지닌 비트마스크(MASK)를 만들어 XOR을 통해 자릿수 제한
    """
    bin(0b1100 ^ 0b1111)
    # '0b11'

    MASK = 0b1111
    bin(0b0101 ^ (0b1100 ^ MASK))

    # 파이썬의 진법 표현
    """
    파이썬이 이진수, 십진수, 16진수를 저장하고 표현하는 방법
    """
    bin(87) # -> '0b1010111'
    int('0b1010111', 2) # -> 87
    int('1010111', 2) # -> 87

    a = bin(87) # -> '0b1010111 TYPE: str'
    b = 0b1010111 # -> 87 TYPE: int

    hex(87) # -> '0x57'
    c = 0x57 # -> 87 TYPE: int

    # 2의 보수
    """
    2의 보수에 대해 개념이 정립되지 않은 경우 비트 조작이 어려움 특히 음수
    4비트 레지스터 기준으로 숫자 표현을 위해 사용되는 4비트 (0000 ~ 1111)
      * MSB (Most Significant Bit)를 사용하는 경우 아래와 같이 표현
        * 0XXX -> 양수 / 1XXX -> 음수

    수학적 2의 보수는 아래와 같이 나타낸다.
      1. '비트 연산자 NOT'은 2의 보수에서 1을 뺀 것
      2. '2의 보수 수학 연산'은 비트 연산자 NOT에서 1을 더한 것 
    """

    """
    bin(0b0101 ^ ~0b1100) -> '-0b1010'
      * 0b1100이 아닌 이유
      * 입력값이 4비트 포맷이 아니라는 점을 생각해야 함
      * 0b1100이 음수 -4여야 하는데, 실제로는 이 값을 양수 12로 가정했던 것
      * 이미 오버플로가 발생하여 전제조건에 문제가 있음
      * 위와 같은 연산 결과를 위해서는 8bit 포맷 또는 좀 더 큰 형태로 변환해야 됨


    """

    # XOR을 활용한 변수 스왑
    """
    임시 변수를 사용하지 않고 두 변수를 스왑하는 방법
    """
    x, y = 9, 4
    x = x + y   # 13
    y = x - y   # 9
    x = x - y   # 4
    # x, y = (4, 9)


    x, y = 9, 4 
    x = x^y     # 1001 ^ 0100 = 1101 (13)   
    y = x^y     # 1101 ^ 0100 = 1001 (9)
    x = x^y     # 1101 ^ 1001 = 0100 (4)
    # x, y = (4, 9)

    x, y = 10, 40
    # (x^y)^x = 40
    # (x^y)^y = 10

