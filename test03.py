from bs4 import BeautifulSoup 

html = '''
<html>
    <head>
    </head>
    <body>
        <h1>스마트스토어</h1>
            <div class = 'sale'>
                <p id='notebook1' class='devices'>
                    <span class = 'name'> 맥북에어m1 </span>
                    <span class = 'price'> 980000원 </span>
                    <span class = 'inventory'> 5개 </span>
                    <span class = 'store'> 스마트컴퓨터 </span>
                    <a href = 'http://www.naver.com' > 홈페이지 </a>
                </p>
            </div>
            <div class = 'after'>
                <p id='notebook2' class='devices'>
                    <span class ='name'> 맥북프로 </span>
                </p>
            </div>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser') 

#id와 class로 찾기
# #뒤에 id를 입력해서 찾거나 .뒤에 class를 넣는 방법이 있다. 
# ids_notebook1 = soup.select('#notebook1')
# print(ids_notebook1)


# class_price = soup.select('.name')
# print(class_price)

# #태그가 span이면서 class명이 price인 것을 모두 찾는다. 
# tags_span_class_price = soup.select('span.price')
# print(tags_span_class_price)

# #상위 구조 활용
# #정보가 담긴 태그의 속성만으로는 찾기가 어려울 경우 부모 태그 아래에 있는지 등의 
# #정보를 추가해서 찾을 수 있다.
# #한단계 아래를 의미할 때는 '>'기호를 사용한다. 
# #상위 태그는 부모태그, 하위 태그는 자식 태그라고 부른다. 
# print("---상위 구조 사용---")
# tags_name = soup.select('span.name')
# print(tags_name)

# #이때 맥북프로를 제외하고 맥북에어만 찾기 위해 맥북에어가 포함된 
# #부모 태그 정보를 추가한다. 
# tags_notebook1 = soup.select('#notebook1 > span.name')
# print(tags_notebook1) 

# #태그 위치로 위치 찾기2 
# #결과는 동일하지만 첫번째 코드는 상위태그1(div.sale)
# #바로 아래에 있는 상위 태그2(#notebook1)을 찾고,
# #상위태그2(#notebook1) 바로 아래에 있는 태그(span.name)을 모두 찾았다. 
# #두번째 코드는 상위태그(div.sale) 바로 아래에 있는 태그뿐 아니라 
# #몇 단계 아래의 태그 중에서 태그 정보(span.name)를 모두 찾았다. 
tags_notebook2 = soup.select('div.sale > #notebook1 > span.name')
tags_notebook3 = soup.select('div.sale span.name')
print(tags_notebook2)
print(tags_notebook3)

# #태그 그룹에서 하나의 태그만 선택
# tags = soup.select('span.name')
# tag_1 = tags[0]
# print(tag_1)

# #반복구문
# tags = soup.select('span.name')
# for tag in tags:
#     print(tag)

# #선택한 태그에서 텍스트, 속성값 가져오기
# tags = soup.select('a')
# tag = tags[0]
# content = tag.text 
# print(content) 
# link = tag['href']
# print(link) 


