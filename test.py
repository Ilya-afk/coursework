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

    def get_view(self):
        self.cur.execute("SELECT * from info_view")
        rows = self.cur.fetchall()
        return rows

    def get_user_data(self):
        self.cur.execute("SELECT * from user_data")
        rows = self.cur.fetchall()
        return rows

    def get_tariff_period(self):
        self.cur.execute("SELECT * from tariff_period")
        rows = self.cur.fetchall()
        return rows

    def get_tariff(self):
        self.cur.execute("SELECT * from tariff")
        rows = self.cur.fetchall()
        return rows

    def get_payment(self):
        self.cur.execute("SELECT * from payment")
        rows = self.cur.fetchall()
        return rows

    def update_user(self, user_data_id, surname=None, first_name=None,
                    middle_name=None, phone_number=None, address=None, balance=None):
        surname = None if surname == "" else surname
        first_name = None if first_name == "" else first_name
        middle_name = None if middle_name == "" else middle_name
        phone_number = None if phone_number == "" else phone_number[:11]
        address = None if address == "" else address

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

    def update_payment(self, payment_id, user_data_id=None, payment_date=None,
                       payment_amount=None, tariff_id=None):
        payment_date = None if payment_date == "" else payment_date

        data = (payment_id, user_data_id, payment_date, payment_amount, tariff_id)
        self.cur.execute("SELECT * from update_payment(%s, %s, %s, %s, %s)", data)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def add_payment(self, user_data_id, payment_date, payment_amount, tariff_id):
        data = (user_data_id, payment_date, payment_amount, tariff_id)
        self.cur.execute("SELECT * from add_payment(%s, %s, %s, %s)", data)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def delete_payment(self, payment_id):
        self.cur.execute("SELECT * from delete_payment(%s)", (payment_id,))
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def update_tariff(self, tariff_id, tariff_name=None, price=None, cost_per_min=None,
                      number_of_free_min=None, tariff_period_id=None):
        tariff_name = None if tariff_name == "" else tariff_name

        data = (tariff_id, tariff_name, price, cost_per_min, number_of_free_min, tariff_period_id)
        self.cur.execute("SELECT * from update_tariff(%s, %s, %s, %s, %s, %s)", data)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def add_tariff(self, tariff_name, price, cost_per_min, number_of_free_min, tariff_period_id):
        data = (tariff_name, price, cost_per_min, number_of_free_min, tariff_period_id)
        self.cur.execute("SELECT * from add_tariff(%s, %s, %s, %s, %s)", data)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def delete_tariff(self, tariff_id):
        self.cur.execute("SELECT * from delete_tariff(%s)", (tariff_id,))
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def update_tariff_period(self, tariff_period_id, payment_id=None, start_date=None, end_date=None):
        start_date = None if start_date == "" else start_date
        end_date = None if end_date == "" else end_date

        data = (tariff_period_id, payment_id, start_date, end_date)
        self.cur.execute("SELECT * from update_tariff_period(%s, %s, %s, %s)", data)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def add_tariff_period(self, payment_id, start_date, end_date):
        data = (payment_id, start_date, end_date)
        self.cur.execute("SELECT * from add_tariff_period(%s, %s, %s)", data)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.con.commit()

    def delete_tariff_period(self, tariff_period_id):
        self.cur.execute("SELECT * from delete_tariff_period(%s)", (tariff_period_id,))
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

    db.add_tariff_period(None, "2000-01-01", "2000-01-01")
    print(db.get_tariff_period())
    db.update_tariff_period(6, start_date="1900-01-01")
    print(db.get_tariff_period())
    db.delete_tariff_period(6)
    print(db.get_tariff_period())
    db.close_con()
