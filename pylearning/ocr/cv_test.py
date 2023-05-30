import cv2

img = cv2.imread('./source/cat.jpg', cv2.IMREAD_COLOR)
cv2.imshow('cat', img)
#cv2.waitKey(2000)  # 2초간 대기, 0-계속 대기
cv2.waitKey(0)

# 파일 쓰기
cv2.imwrite('./source/cat_copy.jpg', img)

# gray 로 변경 - cvtColor() 함수 사용, RGB가 아닌 BGR임
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('cat', img_gray)
cv2.waitKey(0)




