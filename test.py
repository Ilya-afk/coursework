import psycopg2


class Database:
    def connection(self, user, password):
        try:
            self.con = psycopg2.connect(
              database="cursovaya",
              user=user,
              password=password,
              host="127.0.0.1",
              port="5432"
            )
            self.cur = self.con.cursor()
        except:
            print('error')
            return 'error'
        return 'success'

    def get_user_data(self):
        self.cur.execute("SELECT * from user_data")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def get_view(self):
        self.cur.execute("SELECT * from info_view")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def get_tariff_period(self):
        self.cur.execute("SELECT * from tariff_period")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def update_user(self, user_data_id, surname=None, first_name=None,
                    middle_name=None, phone_number=None, address=None, balance=None):
        data = (user_data_id, surname, first_name, middle_name, phone_number, address, balance)
        self.cur.execute("SELECT * from update_user(%s, %s, %s, %s, %s, %s, %s)", data)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def add_user(self, surname, first_name, middle_name, phone_number, address, balance):
        data = (surname, first_name, middle_name, phone_number, address, balance)
        self.cur.execute("SELECT * from add_user(%s, %s, %s, %s, %s, %s)", data)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def delete_user(self, user_data_id):
        self.cur.execute("SELECT * from delete_user(%s)", (user_data_id,))
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def close_con(self):
        self.con.close()


def try_connection(user, password):
    try:
        con = psycopg2.connect(
          database="cursovaya",
          user=user,
          password=password,
          host="127.0.0.1",
          port="5432"
        )
        cur = con.cursor()
    except:
        return False
    return True


if __name__ == '__main__':
    db = Database()
    is_ok = 'error'
    while is_ok == 'error':
        u = input()
        p = input()
        is_ok = db.connection(u, p)

    db.delete_user(6)
    db.get_user_data()
    db.close_con()
