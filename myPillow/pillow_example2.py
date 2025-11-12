# import PIL
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

# 이미지 열기 (상대 경로와 절대 경로)
img = Image.open("./photo/cat.jpg")


#이미지 적용
img = img.transpose(Image.FLIP_TOP_BOTTOM)

#이미지 출력
img.show()

#이미지 닫기
img.close()
