import sqlite3
import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ToDo(object):

    def __init__(self):
        self.table_name = None

    def create_table(self):
        conn = sqlite3.connect('todolist.db')
        curs = conn.cursor()
        curs.execute('''CREATE TABLE IF NOT EXISTS todo
                     (id integer primary key autoincrement, create_date datetime, title string ,
                      rank integer, deadline datetime)''')
        conn.commit()
        conn.close()

    def insert_data(self, create_date=datetime.datetime.now(), title=None, rank='1', deadline=None):
        logger.debug({
            'action': 'insert_data',
            'create_date': create_date,
            'title': title,
            'rank': rank,
            'deadline': deadline
        })
        if not title:
            return False
        deadline = datetime.date.today()+datetime.timedelta(days=int(deadline))
        conn = sqlite3.connect('todolist.db')
        curs = conn.cursor()
        curs.execute('''INSERT INTO todo (create_date, title, rank, deadline) 
        VALUES (?, ?, ?, ?)''', (create_date, title, rank, deadline))
        conn.commit()
        conn.close()

    def select_table(self):
        '''
        もっといい実装がありそう
        '''
        conn = sqlite3.connect('todolist.db')
        curs = conn.cursor()
        curs.execute('''SELECT * FROM todo''')
        rows = curs.fetchall()
        col_list = []
        res_list = []
        for i in curs.description:
            col_list.append(i[0])
        for row in rows:
            row_data = {}
            for i in range(len(row)):
                row_data[col_list[i]] = row[i]
            res_list.append(row_data)
        conn.close()
        return res_list

    def delete_todo(self, id):
        conn = sqlite3.connect('todolist.db')
        curs = conn.cursor()
        curs.execute('''DELETE FROM todo WHERE id=?''', (id, ))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    todo = ToDo()
    todo.create_table()
    todo.insert_data(
        create_date=datetime.datetime.now(),
        title='test title',
        rank='1',
        deadline=datetime.date.today()+datetime.timedelta(days=3))
    todo.select_table()
