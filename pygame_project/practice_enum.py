lst = []
lst.append("a")
lst.append("b")
lst.append("c")

balls =[]
balls.append({
    "pos_x" : 50, # 공의 X 좌표
    "pos_y" : 50, # 공의 Y 좌표 
    "img_idx" : 0 , # 어느 공의 좌표 인지.. 0은 제일 큰공
    "to_x" : 3 ,# 공의 X축 이동방향 -3이면 왼쪽 +3이면 오른쪽
    "to_y" : -6 ,# Y축 이동방향
    "init_spd_y" : -18 # Y의 최초속도 
})

for lst_idx, lst_val in enumerate(lst):
    print(lst_idx, lst_val)

for ball_idx, ball_val in enumerate(balls):
     print(ball_idx, ball_val)