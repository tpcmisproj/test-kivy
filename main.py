import os
import sqlite3
import json
import requests
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
from kivy.clock import Clock
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class WaterMainMenu(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DeIonizedWater(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class GasMenu(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class WaterMenu(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class H2Gas(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class MainMenu(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DeIonizedWater(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DeepWellNo01(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DeepWellNo02(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiAcf(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiAnionBed01Regen(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiAnionBed02Regen(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiCationBed01Regen(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiCationBed02Regen(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiDualBed01(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiDualBed02(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiFilterReplacement(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiMixedBed01(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiMixedBed01Regen(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiMixedBed02(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiMixedBed02Regen(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiPolishingTankReplacement(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiTankBldg1PointOfUse(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiWaterAnalysisClassB(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class DiWaterAnalysisClassC(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class UvLightSterilizer(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class WaterConsumption(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class Wwtp(Screen):
    def change_screen(self, screen_name):
        self.manager.current = screen_name


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.setup_ui()
        self.test_if_theres_an_internet_connected()

    def test_if_theres_an_internet_connected(self):
        try:
            requests.get("http://www.google.com", timeout=3)
        except requests.ConnectionError:
            self.create_no_internet_connection_label()
            return False

    def create_no_internet_connection_label(self):
        self.no_internet_label = MDLabel(
            text="No internet connection,\nPlease use your username as password",
            size_hint_y=None,
            height=dp(48),
            color=(1, 0, 0, 1)  # Set text color to red
        )
        box_layout = MDBoxLayout(
            orientation="vertical",
            spacing="20dp",
            adaptive_height=True,
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5, "center_y": 0.6},
        )
        layout = RelativeLayout()
        box_layout.padding = dp(48)

        box_layout.add_widget(self.no_internet_label)

        layout.add_widget(box_layout)

        return self.add_widget(layout)

    def setup_ui(self):
        layout = RelativeLayout()

        box_layout = MDBoxLayout(
            orientation="vertical",
            spacing="20dp",
            adaptive_height=True,
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        box_layout.padding = dp(48)

        self.image = Image(
            source='static/tpc.jpg',
            size_hint=(None, None),
            size=(300, 200),
            pos_hint={"center_x": 0.5}
        )

        self.label_login = MDLabel(
            text="Please Log in using your HRIS Account", size_hint_y=None, height=dp(48))

        self.username = MDTextField(
            hint_text="Username", size_hint_y=None, height=dp(48))
        self.password = MDTextField(
            hint_text="Password", size_hint_y=None, height=dp(48), password=True)

        box_layout.add_widget(self.image)
        box_layout.add_widget(self.label_login)
        box_layout.add_widget(self.username)
        box_layout.add_widget(self.password)

        self.login_button = MDRaisedButton(
            text="Log In", on_release=self.on_login, size_hint_y=None, height=dp(48))
        box_layout.add_widget(self.login_button)

        layout.add_widget(box_layout)

        self.add_widget(layout)

    def on_login(self, *args):
        if self.is_internet_connected():
            response = self.log_in_function(
                self.username.text, self.password.text)
            if response['result'] is not False:
                self.logged_in_user_data = response['result']
                self.manager.current = 'menu'
            else:
                self.show_login_failure_dialog()
        else:
            self.log_in_local(self.username.text, self.password.text)

    def is_internet_connected(self):
        try:
            requests.get("http://www.google.com", timeout=3)
            return True
        except requests.ConnectionError:
            return False

    def log_in_local(self, username, password):
        local_data_file = "data/data.json"
        if os.path.exists(local_data_file):
            with open(local_data_file, "r") as file:
                data = json.load(file)
                for user_data in data.get("result", []):
                    if (user_data.get("username") == username and user_data.get("username") == password):
                        self.logged_in_user_data = user_data
                        self.manager.current = 'menu'
                        return

                self.show_login_failure_dialog()
        else:
            self.show_login_failure_dialog()

    def log_in_function(self, username, password):
        url = f"http://hris.teamglac.com/api/users/login?u={username}&p={password}"
        response = requests.get(url).json()
        return response

    def show_login_failure_dialog(self):
        dialog = MDDialog(
            title="Login Failed",
            text="Invalid username or password. Please try again.",
            buttons=[MDRaisedButton(
                text="OK", on_release=lambda _: dialog.dismiss())]
        )
        dialog.open()

    def go_to_home(self):
        self.root.current = 'login'


class ContentNavigationDrawer(MDBoxLayout):
    pass


def load_kv_files(directory):
    kv_files = [file for file in os.listdir(directory) if file.endswith('.kv')]
    kv_file_paths = [os.path.join(directory, kv_file) for kv_file in kv_files]
    loaded_files = [Builder.load_file(kv_file_path)
                    for kv_file_path in kv_file_paths]
    return loaded_files


class MainApp(MDApp):
    icons = list(md_icons.keys())[15:30]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_menu_kv_files()
        self.load_all_water_kv_files()
        self.load_all_gas_kv_files()

    def load_all_menu_kv_files(self):
        kv_files_directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'kv_path')
        return load_kv_files(kv_files_directory)

    def load_all_water_kv_files(self):
        kv_files_directory = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'kv_path/water')
        return load_kv_files(kv_files_directory)

    def load_all_gas_kv_files(self):
        kv_files_directory = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'kv_path/gas')
        return load_kv_files(kv_files_directory)

    def create_database(self):
        db_file = 'gas_data.db'
        if not os.path.exists(db_file):
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE h2gas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Date TEXT,
                    Shift TEXT,
                    Temperature TEXT,
                    Nitrogen TEXT,
                    Pressure TEXT,
                    NitrogenCylinderPressure TEXT,
                    PrimaryPressureGaugeBH2 TEXT,
                    Time TEXT,
                    PrimaryPressureGaugePallet TEXT,
                    Remarks TEXT,
                    SecondaryPressureGaugeBH2 TEXT
                )
            ''')

            conn.commit()
            conn.close()

    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.logout = [
            {
                "viewclass": "OneLineListItem",
                "icon": "android",
                "text": "LOG OUT",
                "height": dp(56),
                "on_release": lambda x="Item 2": self.menu_callback(x),
            }
        ]
        self.menu = MDDropdownMenu(
            items=self.logout,
            width_mult=4,
        )

        sm = ScreenManager()

        # MENUS

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(MainMenu(name="menu"))
        sm.add_widget(WaterMainMenu(name="water_main_menu"))
        sm.add_widget(GasMenu(name="gas"))

        # POWER

        # GAS

        sm.add_widget(H2Gas(name="h2gas"))

        # WATER

        sm.add_widget(WaterMenu(name="water"))
        sm.add_widget(DeIonizedWater(name="de_ionized_water"))
        sm.add_widget(DeepWellNo01(name="deep_well_no_01"))
        sm.add_widget(DeepWellNo02(name="deep_well_no_02"))
        sm.add_widget(DiAcf(name="di_acf"))
        sm.add_widget(DiAnionBed01Regen(name="di_anion_bed_01_regen"))
        sm.add_widget(DiAnionBed02Regen(name="di_anion_bed_02_regen"))
        sm.add_widget(DiCationBed01Regen(name="di_cation_bed_01_regen"))
        sm.add_widget(DiCationBed02Regen(name="di_cation_bed_02_regen"))
        sm.add_widget(DiDualBed01(name="di_dual_bed_01"))
        sm.add_widget(DiDualBed02(name="di_dual_bed_02"))
        sm.add_widget(DiFilterReplacement(name="di_filter_replacement"))
        sm.add_widget(DiMixedBed01(name="di_mixed_bed_01"))
        sm.add_widget(DiMixedBed01Regen(name="di_mixed_bed_01_regen"))
        sm.add_widget(DiMixedBed02(name="di_mixed_bed_02"))
        sm.add_widget(DiMixedBed02Regen(name="di_mixed_bed_02_regen"))
        sm.add_widget(DiPolishingTankReplacement(
            name="di_polishing_tank_replacement"))
        sm.add_widget(DiTankBldg1PointOfUse(
            name="di_tank_-_bldg_1_point_of_use"))
        sm.add_widget(DiWaterAnalysisClassB(
            name="di_water_analysis_-_class_b"))
        sm.add_widget(DiWaterAnalysisClassC(
            name="di_water_analysis_-_class_c"))
        sm.add_widget(UvLightSterilizer(name="uv_light_sterilizer"))
        sm.add_widget(WaterConsumption(name="water_consumption"))
        sm.add_widget(Wwtp(name="wwtp"))

        return sm

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Orange" else "Orange"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def change_screen(self, screen_name):
        self.root.current = screen_name

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        print('test')

    def change_screen_h2_gas(self, screen_name):
        self.menu.dismiss()
        self.root.current = screen_name

    def show_datetime_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.get_date)
        date_dialog.open()

    def get_date(self, instance, value, date_range):
        print(f"==>> date: {value}")
        self.selected_date = value
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        print(f"==>> time: {time}")
        datetime_str = f"{self.selected_date.strftime('%Y-%m-%d')} {time}"
        self.root.get_screen('gas').ids.datetime_text.text = datetime_str

    def show_drop_down(self, instance_textfield, instance_focus):
        if instance_focus:
            menu_items = [
                {"viewclass": "OneLineListItem", "text": "DAY 1",
                    "on_release": lambda x="DAY 1": self.set_item(x)},
                {"viewclass": "OneLineListItem", "text": "SWG 1",
                    "on_release": lambda x="SWG 1": self.set_item(x)},
                {"viewclass": "OneLineListItem", "text": "GRAVE 1",
                    "on_release": lambda x="GRAVE 1": self.set_item(x)},
                {"viewclass": "OneLineListItem", "text": "GRAVE 2",
                    "on_release": lambda x="GRAVE 2": self.set_item(x)},
            ]
            self.menu = MDDropdownMenu(
                caller=instance_textfield,
                items=menu_items,
                position="auto",
                width_mult=4,
            )
            self.menu.open()

    def set_item(self, text_item):
        self.menu.dismiss()
        self.root.get_screen('gas').ids.tech_shift.text = text_item

    def insert_to_database(self):
        self.create_database()

        conn = sqlite3.connect('gas_data.db')
        cursor = conn.cursor()

        date = self.root.get_screen('gas').ids.date.text
        tech_shift = self.root.get_screen('gas').ids.tech_shift.text
        temp = self.root.get_screen('gas').ids.temp.text
        n_pressure = self.root.get_screen('gas').ids.n_pressure.text
        p_pressure = self.root.get_screen('gas').ids.p_pressure.text
        n_cylinder_pressure = self.root.get_screen(
            'gas').ids.n_cylinder_pressure.text
        p_pressure_gauge_bhs2 = self.root.get_screen(
            'gas').ids.p_pressure_gauge_bhs2.text
        time = self.root.get_screen('gas').ids.time.text
        p_pressure_gauge_pallet = self.root.get_screen(
            'gas').ids.p_pressure_gauge_pallet.text
        remarks = self.root.get_screen('gas').ids.remarks.text
        s_pressure_gauge = self.root.get_screen(
            'gas').ids.s_pressure_gauge.text

        query = """
            INSERT INTO ShiftData
            (Date, Shift, Temperature, Nitrogen, Pressure, NitrogenCylinderPressure,
            PrimaryPressureGaugeBH2, Time, PrimaryPressureGaugePallet,
            Remarks, SecondaryPressureGaugeBH2)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        data = (date, tech_shift, temp, n_pressure, p_pressure, n_cylinder_pressure,
                p_pressure_gauge_bhs2, time, p_pressure_gauge_pallet,
                remarks, s_pressure_gauge)

        if date == '' or tech_shift == '' or temp == '' or n_pressure == '' or p_pressure == '' or n_cylinder_pressure == '' or p_pressure_gauge_bhs2 == '' or time == '' or p_pressure_gauge_pallet == '' or remarks == '' or s_pressure_gauge == '':
            dialog = MDDialog(
                title="Error Something went Wrong",
                radius=[20, 7, 20, 7],
                text="Error: Data fields cannot be empty.",
                buttons=[MDRaisedButton(
                    text="OK", on_release=lambda _: dialog.dismiss())]
            )
            dialog.open()
        else:
            try:
                cursor.execute(query, data)
                conn.commit()
                dialog = MDDialog(
                    title="Successfully Inserted!",
                    text="Data inserted into the database.",
                    radius=[20, 7, 20, 7],
                    buttons=[MDRaisedButton(
                        text="OK", on_release=lambda _: dialog.dismiss())]
                )

                dialog.open()

                print('Success')
            except Exception as e:
                dialog = MDDialog(
                    title="Error Something went Wrong",
                    radius=[20, 7, 20, 7],
                    text=f"Error: {str(e)}.",
                    buttons=[MDRaisedButton(
                        text="OK", on_release=lambda _: dialog.dismiss())]
                )
                dialog.open()

            finally:

                conn.close()


MainApp().run()
