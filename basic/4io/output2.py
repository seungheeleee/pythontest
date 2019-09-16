print('삼각형 넓이 계산기')
width = int(input('밑변의 길이를 입력해주세요: '))
height = int(input('높이의 길이를 입력해주세요: '))
area = width * height / 2
print('밑변: {}, 높이: {}인 삼각형의 넓이는 {}입니다.'.format(width, height, area))