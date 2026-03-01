# example_usage.py
from db_manager import DatabaseManager

# 1. MySQL bilan ishlash
mysql_db = DatabaseManager(
    db_type='mysql',
    host='localhost',
    user='root',
    password='your_password',
    database='test_db'
)

if mysql_db.connect():
    # Foydalanuvchi yaratish
    user = mysql_db.create_user(chat_id=123456789, initial_balance=100.50)
    
    # Balansni tekshirish
    balance = mysql_db.get_balance(123456789)
    print(f"Balans: {balance}")
    
    # Pul qo'shish
    mysql_db.add_money(123456789, 50)
    
    # Pul ayirish
    mysql_db.subtract_money(123456789, 30)
    
    # Balansni o'rnatish
    mysql_db.set_money(123456789, 200)
    
    # Statistika
    stats = mysql_db.get_statistics()
    print(f"Jami foydalanuvchilar: {stats['total_users']}")
    print(f"Jami balans: {stats['total_balance']}")
    
    # Foydalanuvchini o'chirish
    mysql_db.delete_user(123456789)


# 2. PostgreSQL bilan ishlash
pg_db = DatabaseManager(
    db_type='postgresql',
    host='localhost',
    user='postgres',
    password='postgres',
    database='test_db'
)

if pg_db.connect():
    # Bir nechta foydalanuvchi yaratish
    pg_db.create_user(111111, 1000)
    pg_db.create_user(222222, 2000)
    pg_db.create_user(333333, 3000)
    
    # Pul o'tkazish
    pg_db.transfer_money(111111, 222222, 500)
    
    # Eng katta balansli foydalanuvchilar
    top_users = pg_db.get_top_users(5)
    for user in top_users:
        print(f"Chat ID: {user.chat_id}, Balans: {user.balans}")
