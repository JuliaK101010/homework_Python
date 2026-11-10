import pytest  # noqa
from sqlalchemy import create_engine, text

# Ваша строка подключения к базе QA
DB_URL = "postgresql+psycopg2://postgres:123@localhost:5432/QA"

engine = create_engine(DB_URL)


@pytest.fixture
def db_connection():
    """Фикстура для подключения, создания тестовой таблицы и очистки."""
    connection = engine.connect()

    # Создаем временную таблицу для тестов, чтобы колонки точно совпадали
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS test_students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """))
    connection.commit()

    yield connection

    # Удаляем тестовую таблицу после завершения тестов
    connection.execute(text("DROP TABLE IF EXISTS test_students"))
    connection.commit()
    connection.close()


def test_add_student(db_connection):
    """Тест на добавление (INSERT) студента в БД."""
    query = text(
        "INSERT INTO test_students (name, email) "
        "VALUES (:name, :email) RETURNING id"
    )
    result = db_connection.execute(
        query,
        {"name": "Ivan Testov", "email": "ivan.test@test.com"}
    )
    db_connection.commit()
    student_id = result.fetchone()[0]

    assert student_id is not None

    # Очистка созданной записи
    cleanup_query = text("DELETE FROM test_students WHERE id = :id")
    db_connection.execute(cleanup_query, {"id": student_id})
    db_connection.commit()


def test_update_student(db_connection):
    """Тест на изменение (UPDATE) данных студента в БД."""
    insert_query = text(
        "INSERT INTO test_students (name, email) "
        "VALUES (:name, :email) RETURNING id"
    )
    res = db_connection.execute(
        insert_query,
        {"name": "Old Name", "email": "old@test.com"}
    )
    db_connection.commit()
    student_id = res.fetchone()[0]

    # Обновляем данные
    update_query = text(
        "UPDATE test_students SET name = :new_name WHERE id = :id"
    )
    db_connection.execute(
        update_query,
        {"new_name": "New Name", "id": student_id}
    )
    db_connection.commit()

    # Проверяем, что имя изменилось
    select_query = text("SELECT name FROM test_students WHERE id = :id")
    row = db_connection.execute(select_query, {"id": student_id}).fetchone()
    assert row[0] == "New Name"

    # Очистка
    cleanup_query = text("DELETE FROM test_students WHERE id = :id")
    db_connection.execute(cleanup_query, {"id": student_id})
    db_connection.commit()


def test_delete_student(db_connection):
    """Тест на удаление (DELETE) студента из БД."""
    insert_query = text(
        "INSERT INTO test_students (name, email) "
        "VALUES (:name, :email) RETURNING id"
    )
    res = db_connection.execute(
        insert_query,
        {"name": "To Delete", "email": "delete@test.com"}
    )
    db_connection.commit()
    student_id = res.fetchone()[0]

    # Удаляем студента
    delete_query = text("DELETE FROM test_students WHERE id = :id")
    db_connection.execute(delete_query, {"id": student_id})
    db_connection.commit()

    # Проверяем, что запись удалена
    select_query = text("SELECT * FROM test_students WHERE id = :id")
    row = db_connection.execute(select_query, {"id": student_id}).fetchone()
    assert row is None
