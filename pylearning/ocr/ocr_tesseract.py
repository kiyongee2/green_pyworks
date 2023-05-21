"""
이미지에 있는 텍스트 추출
Tesseract - OCR 프로그램 중 하나
다양한 운영체제에서 사용할 수 있는 엔진
"""

from PIL import Image
from pytesseract import pytesseract

pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
img_file = Image.open("images/cold.png")
text = pytesseract.image_to_string(img_file, lang="kor")
# print(text)
print(text.replace(" ", ""))

# 변환된 데이터를 파일에 쓰기
# 인코딩(encoding) 속성 'utf8'
with open("output/cold.txt", 'w', encoding='utf8') as f:
    # f.write(text)
    f.write("\n")
    f.write(text.replace(' ', ''))

