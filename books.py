from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///books.db')

with engine.connect() as conn:
    conn.execute(text('''CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT
    )'''))
    
    conn.execute(text('''INSERT INTO book (title, author) VALUES
        ('The Great Gatsby', 'F. Scott Fitzgerald'),
        ('To Kill a Mockingbird', 'Harper Lee'),
        ('1984', 'George Orwell'),
        ('Pride and Prejudice', 'Jane Austen'),
        ('The Catcher in the Rye', 'J.D. Salinger')
    '''))
    
    conn.commit()
    print('Database created successfully!')