# 슬라이딩 윈도우 (Sliding window)
"""
고정 사이즈의 윈도우가 이동하면서, 윈도우 내에있는 데이터를 이용해 문제를 풀이하는 알고리즘
    * 네트워크에서 사용되던 알고리즘을 문제 풀이 사용하는 것
    * 본래, 네트워크 호스트 간 패킷 흐름을 제어하기 위한 기법으로 사용
        * 패킷을 전송할 떄, 고정사이즈의 윈도우가 옆으로 이동하면서 패킷 전송하는 방식

    * Two-pointer 기법과 유사한 면이 존재함
    * Two-pointer
        윈도우 사이즈 변동 / 주로, 정렬된 배열 대상 / 좌우 포인터 양방향 이동
    * Sliding-window
        윈도우 사이즈 고정 / 배열 정렬 여부 상관 없음 / 좌, 우 단방향 이동
"""
