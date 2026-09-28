from models import Base, engine, SessionLocal, init_db, Vehicle, Order, Location

def seed_data():
    \ \\Заполняем базу тестовыми данными, чтобы проект не был пустым\\\
    db = SessionLocal()
    
    # 1. Добавляем склад
    warehouse = Location(name=\Main Distribution Center\, latitude=59.9343, longitude=30.3351, location_type=\warehouse\)
    db.add(warehouse)
    
    # 2. Добавляем транспорт
    v1 = Vehicle(plate_number=\A123BC77\, capacity=500.0, vehicle_type=\truck\, status=\available\)
    v2 = Vehicle(plate_number=\B456DE77\, capacity=100.0, vehicle_type=\bike\, status=\available\)
    db.add_all([v1, v2])
    
    # 3. Добавляем тестовые заказы
    o1 = Order(customer_name=\Ivanov\, address=\Nevsky Ave 1\, latitude=59.9389, longitude=30.3145, weight=10.5)
    o2 = Order(customer_name=\Petrov\, address=\Rubinshteyna 10\, latitude=59.9350, longitude=30.3220, weight=5.0)
    o3 = Order(customer_name=\Sidorov\, address=\Liteyny 20\, latitude=59.9320, longitude=30.3300, weight=20.0)
    db.add_all([o1, o2, o3])
    
    db.commit()
    db.close()
    print(\Database seeded successfully!\)

if __name__ == \__main__\:
    init_db()
    seed_data()
