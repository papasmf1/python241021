# Person 클래스: 사람에 대한 기본 정보를 담는 클래스
class Person:
    def __init__(self, id, name):
        # id: 사람의 고유 ID
        self.id = id  
        # name: 사람의 이름
        self.name = name

    # printInfo 메서드: 사람의 ID와 이름을 출력하는 함수
    def printInfo(self):
        # f-string을 사용하여 ID와 이름을 문자열로 반환
        return f"ID: {self.id}, Name: {self.name}"

# Manager 클래스: Person 클래스를 상속받으며, 추가적으로 직함(title)을 저장
class Manager(Person):
    def __init__(self, id, name, title):
        # 부모 클래스(Person)의 __init__ 메서드를 호출하여 id와 name을 초기화
        super().__init__(id, name)  
        # title: 관리자의 직함(예: 팀 리더, 프로젝트 매니저 등)
        self.title = title

    # printInfo 메서드: 관리자 정보(ID, 이름, 직함)를 출력하는 함수
    def printInfo(self):
        # f-string을 사용하여 ID, 이름, 직함을 문자열로 반환
        return f"ID: {self.id}, Name: {self.name}, Title: {self.title}"

# Employee 클래스: Person 클래스를 상속받으며, 추가적으로 기술(skill)을 저장
class Employee(Person):
    def __init__(self, id, name, skill):
        # 부모 클래스(Person)의 __init__ 메서드를 호출하여 id와 name을 초기화
        super().__init__(id, name)  
        # skill: 직원의 기술(예: 파이썬, 자바 등)
        self.skill = skill

    # printInfo 메서드: 직원 정보(ID, 이름, 기술)를 출력하는 함수
    def printInfo(self):
        # f-string을 사용하여 ID, 이름, 기술을 문자열로 반환
        return f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}"

# 테스트 코드를 작성하여 각 클래스가 올바르게 작동하는지 확인
def test_person_classes():
    # 테스트 결과를 저장할 리스트
    test_results = []

    # Test 1: Person 클래스의 기본 정보 테스트
    person = Person(1, "Alice")
    # person 객체의 정보가 예상한 문자열과 일치하는지 확인
    test_results.append(person.printInfo() == "ID: 1, Name: Alice")

    # Test 2: 다른 Person 객체의 정보 테스트
    person2 = Person(2, "Bob")
    # person2 객체의 정보가 예상한 문자열과 일치하는지 확인
    test_results.append(person2.printInfo() == "ID: 2, Name: Bob")

    # Test 3: Manager 클래스의 정보 테스트
    manager = Manager(3, "Charlie", "Team Lead")
    # manager 객체의 정보가 예상한 문자열과 일치하는지 확인
    test_results.append(manager.printInfo() == "ID: 3, Name: Charlie, Title: Team Lead")

    # Test 4: 다른 Manager 객체의 정보 테스트
    manager2 = Manager(4, "David", "Project Manager")
    # manager2 객체의 정보가 예상한 문자열과 일치하는지 확인
    test_results.append(manager2.printInfo() == "ID: 4, Name: David, Title: Project Manager")

    # Test 5: Employee 클래스의 정보 테스트
    employee = Employee(5, "Eve", "Python")
    # employee 객체의 정보가 예상한 문자열과 일치하는지 확인
    test_results.append(employee.printInfo() == "ID: 5, Name: Eve, Skill: Python")

    # Test 6: 다른 Employee 객체의 정보 테스트
    employee2 = Employee(6, "Frank", "Java")
    # employee2 객체의 정보가 예상한 문자열과 일치하는지 확인
    test_results.append(employee2.printInfo() == "ID: 6, Name: Frank, Skill: Java")

    # Test 7: Manager 객체의 직함 변경 테스트
    manager2.title = "Senior Project Manager"
    # 직함이 변경된 manager2 객체의 정보가 예상한 문자열과 일치하는지 확인
    test_results.append(manager2.printInfo() == "ID: 4, Name: David, Title: Senior Project Manager")

    # Test 8: Employee 객체의 기술 변경 테스트
    employee2.skill = "JavaScript"
    # 기술이 변경된 employee2 객체의 정보가 예상한 문자열과 일치하는지 확인
    test_results.append(employee2.printInfo() == "ID: 6, Name: Frank, Skill: JavaScript")

    # Test 9: 직함이 없는 Manager 객체 테스트 (직함에 빈 문자열 사용)
    manager3 = Manager(7, "Grace", "")
    # 직함이 없는 manager3 객체의 정보가 예상한 문자열과 일치하는지 확인
    test_results.append(manager3.printInfo() == "ID: 7, Name: Grace, Title: ")

    # Test 10: 기술이 없는 Employee 객체 테스트 (기술에 빈 문자열 사용)
    employee3 = Employee(8, "Hannah", "")
    # 기술이 없는 employee3 객체의 정보가 예상한 문자열과 일치하는지 확인
    test_results.append(employee3.printInfo() == "ID: 8, Name: Hannah, Skill: ")

    # 테스트 결과 리스트 반환 (각 테스트가 성공했는지 여부가 True 또는 False로 저장됨)
    return test_results

# 테스트 실행
test_results = test_person_classes()
# 테스트 결과 출력 (모든 테스트가 성공하면 True 리스트가 출력됨)
print(test_results)
