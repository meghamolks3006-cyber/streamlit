

import mysql.connector


class BookListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.connection = mysql.connector.connect(
            user='root',
            password='megha',
            host='localhost',
            database='library_db'
        )

        print(self.connection)

        self.cursor = self.connection.cursor()

        print("successfully connected")

    def list(self):
        query = "SELECT * FROM book"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if records:
            return records
        else:
            return []
    def create(self, title, author, price, pages, language):
        # creating a new record
        query = """
        INSERT INTO book(title, author, price, pages, language)
        VALUES (%s, %s, %s, %s, %s)
        """

        data = (title, author, price, pages, language)

        self.cursor.execute(query, data)

        self.connection.commit()

        print("inserted data successfully")

    def retrieve(self, id):
        query = "SELECT * FROM book WHERE id = %s"

        data = (id,)

        self.cursor.execute(query, data)

        record = self.cursor.fetchone()

        if record:
            return record
        else:
            return None

    def delete(self, id):
        query = "DELETE FROM book WHERE id = %s"

        data = (id,)

        self.cursor.execute(query, data)

        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("deleted successfully")
            return True
        else:
            print("no records found")
            return False

    def update(self, id, title, author, price, pages, language):
        query = """
        UPDATE book
        SET title = %s,
            author = %s,
            price = %s,
            pages = %s,
            language = %s
        WHERE id = %s
        """

        data = (title, author, price, pages, language, id)

        self.cursor.execute(query, data)

        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("updated successfully")
        else:
            print("no records found")


# b = BookListCreateRetrieveUpdateDelete()
#
# b.list()

#b.create('ABC', 'john', 300, 500, 'english')

#b.retrieve(3)
#
# b.delete(3)
#
# b.update(5, 'STU', 'megha', 344, 344, 'english')
