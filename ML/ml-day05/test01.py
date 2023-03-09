import cv2

# 读取图片
img = cv2.imread('./ML/ml-day05/1.png')

# 转为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 边缘检测
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# 轮廓检测
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 遍历所有轮廓
a = 0
for cnt in contours:
    # 计算轮廓面积和周长
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)

    # 如果轮廓面积和周长符合条件，则认为是缺口图片的轮廓
    if area > 500 and perimeter > 100:
        # 截取缺口图片
        x, y, w, h = cv2.boundingRect(cnt)
        captcha = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow('captcha', img)
        a += 1

print(f"找到了 {a}")

# cv2.waitKey(0)
cv2.destroyAllWindows()


