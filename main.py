
import cv2

## 영상 이미지 읽기
scr = cv2.imread('images/picture01.jpg')


## 영상 처리 알고리즘 구현##

dst1 = cv2.cvtColor(scr, cv2.COLOR_RGB2GRAY)
dst2 = scr.copy()
dst3 = cv2.add(src, (100, 100, 100, 0))



## 영상 디스플레이
cv2.imshow('scr', scr)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)



## 마무리
cv2.waitKey(0)
cv2.destroyAllWindows()
