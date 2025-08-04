x, y, w, h = map(int,input().split())

result_x_1 = w - x
result_x_2 = x - int(0)
result_y_1 = h - y
result_y_2 = y - int(0)

print(min(result_x_1,result_x_2,result_y_1,result_y_2))