from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///books.db')

with engine.connect() as conn:
    result = conn.execute(text('SELECT title FROM book ORDER BY title'))
    for row in result:
        print(row[0])