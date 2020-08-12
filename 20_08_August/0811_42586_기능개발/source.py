from collections import deque

def solution(progresses, speeds):
    answer = []
    
    # progress, speeds를 순차적으로 꺼낼 queue 생성
    q = deque(zip(progresses, speeds))

    # 모든 progress를 다 사용할 때까지
    while q:
        # q의 가장 첫 진행 꺼내기
        p, s = q.popleft()
        
        # 필요한 개발 기간 구하기
        # 7.3일이라면 8일이 되어야 한다 -> 음수로 정수화 시키면 절댓값 기준 올림이 실행.
        # -7.3 // 1 = -8
        # ※ 정수화는 현재 실수에서 가장 낮은 정수로 만든다.
        days = -(100 - p) // s
        
        cnt = 1
        
        # 현재 q에 요소가 있고, 현재 q에 있는 작업의 진도가
        # 방금 꺼낸 진도보다 빠르거나 같았던 경우는 함께 처리되니 개수를 같이 센다.
        while q:
            prog, spd = q[0] # 현재 남은 가장 첫 요소
            
            tmp_days = -(100 - prog) // spd

            # 방금 꺼낸 요소와 같이 빌드할 수 있다면, 같이 개수세고 queue에서 제거
            if tmp_days >= days:
                cnt += 1
                q.popleft()
            else:
                break
        
        answer.append(cnt)

    return answer

