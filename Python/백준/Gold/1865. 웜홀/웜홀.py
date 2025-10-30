import sys
input = sys.stdin.readline

# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스 반복
for _ in range(T):

    # 지점(정점), 도로(양방향), 웜홀(단방향, 음의 가중치)
    n, m, w = map(int, input().split())

    # 간선 정보를 저장할 리스트
    edges = []

    # 도로 정보 입력 (양방향)
    for _ in range(m):
        # 시작 정점, 도착 정점, 걸리는 시간
        s, e, t = map(int, input().split())
        edges.append((s, e, t))   # 정방향
        edges.append((e, s, t))   # 역방향
    
    # 웜홀 정보 입력 (단방향, 음의 가중치)
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # 최단 거리 배열 초기화
    dist = [0] * (n + 1)

    # 음의 사이클 존재 여부를 판별하기 위한 Bool
    negative_cycle = False

    # 벨만-포드 알고리즘 수행
    for i in range(1, n + 1):
        updated = False

        # 모든 간선을 확인
        for u, v, cost in edges:

            # 더 짧은 경로를 발견한 경우
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                updated = True
                
                # n번째 반복에서도 값이 갱신된다면 음의 사이클 존재
                if i == n:
                    negative_cycle = True
                    break

        # 더 이상 갱신이 없으면 종료
        if not updated:
            break

    # 결과 출력
    print("YES" if negative_cycle else "NO")