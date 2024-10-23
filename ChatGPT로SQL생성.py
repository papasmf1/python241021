import sqlite3
import random

class ProductDatabase:
    def __init__(self, db_name='electronics.db'):
        # 데이터베이스 연결
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # 제품 정보를 저장할 테이블 생성
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_product(self, name, price):
        # 제품 추가
        self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        self.connection.commit()

    def update_product(self, product_id, name=None, price=None):
        # 제품 정보 수정
        if name and price:
            self.cursor.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (name, price, product_id))
        elif name:
            self.cursor.execute('UPDATE products SET name = ? WHERE id = ?', (name, product_id))
        elif price:
            self.cursor.execute('UPDATE products SET price = ? WHERE id = ?', (price, product_id))
        self.connection.commit()

    def delete_product(self, product_id):
        # 제품 삭제
        self.cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        self.connection.commit()

    def select_all_products(self):
        # 모든 제품 조회
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def close(self):
        # 데이터베이스 연결 종료
        self.connection.close()

# 샘플 데이터를 위한 제품명 및 가격 생성 함수
def generate_sample_data(num_samples=100):
    sample_names = [
        'Smartphone', 'Laptop', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Headphones', 'Speaker', 'Camera', 'Smartwatch',
        'Printer', 'Scanner', 'Hard Drive', 'USB Drive', 'Router', 'Projector', 'Graphics Card', 'Motherboard', 'CPU', 'RAM'
    ]
    sample_data = []
    for _ in range(num_samples):
        name = random.choice(sample_names)
        price = round(random.uniform(50.0, 1500.0), 2)  # 가격은 50 ~ 1500 사이 랜덤 생성
        sample_data.append((name, price))
    return sample_data

# 전자제품 데이터베이스 클래스 사용 예시
if __name__ == '__main__':
    # 데이터베이스 객체 생성
    db = ProductDatabase()

    # 100개의 샘플 데이터 생성 및 삽입
    sample_data = generate_sample_data(100)
    for name, price in sample_data:
        db.insert_product(name, price)

    # 모든 제품 조회
    products = db.select_all_products()
    for product in products:
        print(product)

    # 예시: ID가 1인 제품의 정보를 수정
    db.update_product(1, name="Updated Laptop", price=1200.00)

    # 예시: ID가 1인 제품을 삭제
    db.delete_product(1)

    products = db.select_all_products()
    for product in products:
        print(product)
        
    # 데이터베이스 종료
    db.close()
