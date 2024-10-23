import sqlite3
import random

class FoodBeverageDatabase:
    def __init__(self, db_name='food_beverage.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_product(self, name, price):
        self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        self.connection.commit()

    def update_product(self, product_id, name=None, price=None):
        if name and price:
            self.cursor.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (name, price, product_id))
        elif name:
            self.cursor.execute('UPDATE products SET name = ? WHERE id = ?', (name, product_id))
        elif price:
            self.cursor.execute('UPDATE products SET price = ? WHERE id = ?', (price, product_id))
        self.connection.commit()

    def delete_product(self, product_id):
        self.cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        self.connection.commit()

    def select_all_products(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

def generate_sample_data(num_samples=100):
    sample_names = [
        '커피', '차', '주스', '탄산음료', '생수', '에너지 드링크', '스무디',
        '샌드위치', '햄버거', '피자', '파스타', '샐러드', '스테이크', '치킨',
        '아이스크림', '케이크', '쿠키', '초콜릿', '과자', '캔디'
    ]
    sample_data = []
    for _ in range(num_samples):
        name = random.choice(sample_names)
        price = round(random.uniform(1000, 30000), -2)  # 1,000원에서 30,000원 사이의 가격, 100원 단위로 반올림
        sample_data.append((name, price))
    return sample_data

if __name__ == '__main__':
    db = FoodBeverageDatabase()

    # 100개의 샘플 데이터 생성 및 삽입
    sample_data = generate_sample_data(100)
    for name, price in sample_data:
        db.insert_product(name, price)

    # 모든 제품 조회
    print("모든 제품 목록:")
    products = db.select_all_products()
    for product in products:
        print(product)

    # 예시: ID가 1인 제품의 정보를 수정
    db.update_product(1, name="프리미엄 커피", price=5000)

    # 예시: ID가 2인 제품을 삭제
    db.delete_product(2)

    print("\n수정 및 삭제 후 제품 목록:")
    products = db.select_all_products()
    for product in products:
        print(product)

    db.close()