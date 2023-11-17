from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
import sqlite3


class InsertData:
    def __init__(self, data):
        self.conn = sqlite3.connect('data/fac_monitoring.db')
        self.cursor = self.conn.cursor()
        self.data = data

    def error_handler(self):
        dialog = MDDialog(
            title="Error Something went Wrong",
            radius=[20, 7, 20, 7],
            text="Error: Data fields cannot be empty.",
            buttons=[MDRaisedButton(
                text="OK", on_release=lambda _: dialog.dismiss())]
        )
        dialog.open()

    def success_handler(self):
        dialog = MDDialog(
            title="Successfully Inserted!",
            text="Data inserted into the database.",
            radius=[20, 7, 20, 7],
            buttons=[MDRaisedButton(
                text="OK", on_release=lambda _: dialog.dismiss())]
        )
        dialog.open()

    def exception_handler(self, error_message):
        dialog = MDDialog(
            title="Error Something went Wrong",
            radius=[20, 7, 20, 7],
            text=f"Error: {str(error_message)}.",
            buttons=[MDRaisedButton(
                text="OK", on_release=lambda _: dialog.dismiss())]
        )
        dialog.open()

    def insert_h2_gass(self):
        date = self.data['date']
        time = self.data['time']
        tech_shift = self.data['tech_shift']
        emp_no = self.data['emp_no']
        date_time_encode = self.data['date_time_encode']
        temp = self.data['temp']
        n_pressure = self.data['n_pressure']
        p_pressure = self.data['p_pressure']
        n_cylinder_pressure = self.data['n_cylinder_pressure']
        p_pressure_gauge_bhs2 = self.data['p_pressure_gauge_bhs2']
        p_pressure_gauge_pallet = self.data['p_pressure_gauge_pallet']
        remarks = self.data['remarks']
        s_pressure_gauge = self.data['s_pressure_gauge']
        print(f"==>> s_pressure_gauge: {s_pressure_gauge}")

        query = """
                INSERT INTO gas_data
                (date, time, tech_shift, emp_no, date_time_encode, temp, n_pressure, p_pressure,
                n_cylinder_pressure, p_pressure_gauge_bhs2, p_pressure_gauge_pallet,
                remarks, s_pressure_gauge)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """

        data = (date, time, tech_shift, emp_no, date_time_encode, temp, n_pressure, p_pressure,
                n_cylinder_pressure, p_pressure_gauge_bhs2, p_pressure_gauge_pallet,
                remarks, s_pressure_gauge)

        if date == '' or tech_shift == '' or emp_no == '' or temp == '' or n_pressure == '' or p_pressure == '' or n_cylinder_pressure == '' or p_pressure_gauge_bhs2 == '' or time == '' or p_pressure_gauge_pallet == '' or remarks == '' or s_pressure_gauge == '':
            self.error_handler()
        else:
            try:
                self.cursor.execute(query, data)
                self.conn.commit()
                self.success_handler()
            except Exception as e:
                self.exception_handler(e)

            finally:
                self.conn.close()
