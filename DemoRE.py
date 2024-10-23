# DemoRE.py
#정규표현식 사용

import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")
print(result.group())

result = re.search("\d{4}", "올해는 2024년")
print(result.group())

result = re.search("\d{5}", "우리동네는 52300")
print(result.group())



def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# 테스트 샘플
test_emails = [
    "user@example.com",
    "user.name@example.co.kr",
    "user+tag@example.org",
    "user123@sub.example.com",
    "user@example",  # 잘못된 이메일
    "user@.com",  # 잘못된 이메일
    "user@example.",  # 잘못된 이메일
    "@example.com",  # 잘못된 이메일
    "user@example.c",  # 잘못된 이메일 (최상위 도메인이 너무 짧음)
    "user name@example.com"  # 잘못된 이메일 (공백 포함)
]

# 테스트 실행
for email in test_emails:
    if is_valid_email(email):
        print(f"{email}: 유효한 이메일 주소입니다.")
    else:
        print(f"{email}: 유효하지 않은 이메일 주소입니다.")