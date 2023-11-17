import os
import sqlite3


class CreateDatabase:
    def __init__(self, db_file='data/fac_monitoring.db'):
        self.db_file = db_file

    def create_database(self):
        if not os.path.exists(self.db_file):
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.executescript('''
                    CREATE TABLE gas_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        time TIME,
                        tech_shift TEXT,
                        emp_no INTEGER,
                        date_time_encode DATETIME,
                        temp INTEGER,
                        n_pressure INTEGER,
                        p_pressure INTEGER,
                        n_cylinder_pressure INTEGER,
                        p_pressure_gauge_bhs2 INTEGER,
                        p_pressure_gauge_pallet INTEGER,
                        s_pressure_gauge INTEGER,
                        remarks TEXT  -- Remove the comma here
                    );
                    CREATE TABLE n2_liquid (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        n2_level_mm_of_h2o INTEGER,
                        inventory_gallons DECIMAL(10, 2),
                        inventory_m3 DECIMAL(10, 2),
                        pressure_psi INTEGER,
                        volume_percentage INT,
                        ppm DECIMAL(10, 2),
                        vaporizer_use_no_1_no_2 VARCHAR(1),
                        time TIME,
                        remarks TEXT
                    );
                    CREATE TABLE de_ionized_water (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        di_water_gallons INTEGER,
                        di_flow_gpm INTEGER,
                        resistivity_bdg1 DECIMAL,
                        resistivity_bdg2 DECIMAL,
                        time TIME,
                        remarks TEXT
                    );
                    CREATE TABLE deep_well_no_01 (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        voltage INTEGER,
                        current INTEGER,
                        hour_meter DECIMAL,
                        water_draw DECIMAL,
                        time TIME,
                        remarks TEXT
                    );
                    CREATE TABLE deep_well_no_02 (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        voltage REAL,
                        current INTEGER,
                        hour_meter DECIMAL,
                        water_draw DECIMAL,
                        time TIME,
                        remarks TEXT
                    );
                    CREATE TABLE di_acf (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        time TIME,
                        pump_number INTEGER,
                        initial_meter_reading INTEGER,
                        final_meter_reading INTEGER,
                        rinse_start_time TIME,
                        rinse_finish_time TIME,
                        pressure_psi INTEGER,
                        micron_filter_pressure_psi INTEGER,
                        remarks TEXT
                    );
                    CREATE TABLE di_anion_bed_01_regen (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        back_wash_flowrate INTEGER,
                        back_wash_time INTEGER,
                        settling_time INTEGER,
                        chem_water_injection_flowrate INTEGER,
                        chem_water_injection_time INTEGER,
                        slow_rinse_flowrate INTEGER,
                        slow_rinse_time INTEGER,
                        fast_rinse_flowrate INTEGER,
                        fast_rinse_time INTEGER,
                        ph DECIMAL(4,2),
                        conductivity_microsiemens INTEGER,
                        amount_of_chemical_used INTEGER,
                        remarks TEXT
                        
                    );
                    CREATE TABLE di_anion_bed_02_regen (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        back_wash_flowrate INTEGER,
                        back_wash_time INTEGER,
                        settling_time INTEGER,
                        chem_water_injection_flowrate INTEGER,
                        chem_water_injection_time INTEGER,
                        slow_rinse_flowrate INTEGER,
                        slow_rinse_time INTEGER,
                        fast_rinse_flowrate INTEGER,
                        fast_rinse_time INTEGER,
                        ph DECIMAL(4,2),
                        conductivity_microsiemens INTEGER,
                        facilities_monitoring INTEGER,
                        amount_of_chemical_used INTEGER,
                        remarks TEXT
                    );
                    CREATE TABLE di_cation_bed_01_regen (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        back_wash_flowrate INTEGER,
                        back_wash_time INTEGER,
                        settling_time INTEGER,
                        chem_water_injection_flowrate INTEGER,
                        chem_water_injection_time INTEGER,
                        slow_rinse_flowrate INTEGER,
                        slow_rinse_time INTEGER,
                        fast_rinse_flowrate INTEGER,
                        fast_rinse_time INTEGER,
                        amount_of_chemical_used FLOAT,
                        remarks TEXT
                    );
                    CREATE TABLE di_cation_bed_01_regen (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        back_wash_flowrate INTEGER,
                        back_wash_time INTEGER,
                        settling_time INTEGER,
                        chem_water_injection_flowrate INTEGER,
                        chem_water_injection_time INTEGER,
                        slow_rinse_flowrate INTEGER,
                        slow_rinse_time INTEGER,
                        fast_rinse_flowrate INTEGER,
                        fast_rinse_time INTEGER,
                        amount_of_chemical_used FLOAT,
                        remarks TEXT
                    );
                    CREATE TABLE di_dual_bed_01 (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        flow_rate INTEGER,
                        acf_pressure_in INTEGER,
                        cation_pressure_in INTEGER,
                        cation_pressure_out INTEGER,
                        cation_pH DECIMAL(4,2),
                        anion_tank_conductivity_micro_mhos INTEGER,
                        anion_tank_pH DECIMAL(4,2),
                        remarks TEXT
                    );
                    CREATE TABLE di_dual_bed_02 (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        flow_rate INTEGER,
                        facilities_monitoring INTEGER,
                        acf_pressure_in INTEGER,
                        cation_pressure_in INTEGER,
                        cation_pressure_out INTEGER,
                        cation_pH DECIMAL(4,2),
                        anion_tank_conductivity_micro_mhos INTEGER,
                        anion_tank_pH DECIMAL(4,2),
                        remarks TEXT
                    );
                    CREATE TABLE di_filter_replacement (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        filter_location TEXT,
                        quantity_replaced INTEGER,
                        size_of_filter_cartridge INTEGER,
                        remarks TEXT
                    );
                    CREATE TABLE di_mixed_bed_01 (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        back_wash_flowrate_gpm INTEGER,
                        back_wash_time_min INTEGER,
                        settling_time_min INTEGER,
                        caustic_draw_flowrate_gpm INTEGER,
                        caustic_draw_time_min INTEGER,
                        slow_rinse_1_flowrate_gpm INTEGER,
                        slow_rinse_1_time_min INTEGER,
                        acid_draw_flowrate_gpm INTEGER,
                        acid_chem_draw_time_min INTEGER,
                        slow_rinse_2_flowrate_gpm INTEGER,
                        slow_rinse_2_time_min INTEGER,
                        fast_rinse_flowrate_gpm INTEGER,
                        fast_rinse_time_min INTEGER,
                        draining_down_min INTEGER,
                        air_mixing_min INTEGER,
                        final_rinse_flowrate_gpm INTEGER,
                        final_rinse_time_min INTEGER,
                        ph DECIMAL(5,2),
                        resistivity_mega_ohms DECIMAL(10,2),
                        amount_of_acid_chemical_used INTEGER,
                        amount_of_base_chemical_used INTEGER,
                        remarks TEXT
                    );
                    CREATE TABLE di_mixed_bed_01_regen (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        n2_level_mm_of_h2o_int INT,
                        inventory_gallons_int_decimal DECIMAL(10,2),
                        facilities_monitoring INT,
                        inventory_m3_int_decimal DECIMAL(10,2),
                        pressure_psi_int INT,
                        volume_percentage INT,
                        ppm_int_decimal DECIMAL(10,2),
                        vaporizer_use_no_1_no_2 VARCHAR(1), 
                        time TEXT,
                        remarks TEXT
                    );
                    CREATE TABLE di_mixed_bed_02 (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        flow_rate_gpm REAL,
                        resistivity_mega_ohms REAL,
                        ph REAL,
                        uv_hour_meter_hrs INTEGER,
                        micron_filter_no INTEGER,
                        pressure_psi INTEGER,
                        feedwater_tank_level TEXT,
                        di_pump_no INTEGER,
                        flowrate INTEGER,
                        totalizer_reading TEXT,
                        remarks TEXT
                    );
                    CREATE TABLE di_mixed_bed_02_regen (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        back_wash_flowrate_gpm REAL,
                        back_wash_time_min INTEGER,
                        settling_time_min INTEGER,
                        caustic_draw_flowrate_gpm REAL,
                        caustic_draw_time_min INTEGER,
                        slow_rinse1_flowrate_gpm REAL,
                        slow_rinse1_time_min INTEGER,
                        acid_draw_flowrate_gpm REAL,
                        acid_chem_draw_time_min INTEGER,
                        slow_rinse2_flowrate_gpm REAL,
                        slow_rinse2_time_min INTEGER,
                        fast_rinse_flowrate_gpm REAL,
                        fast_rinse_time_min INTEGER,
                        draining_down_min INTEGER,
                        air_mixing_min INTEGER,
                        final_rinse_flowrate_gpm REAL,
                        final_rinse_time_min INTEGER,
                        ph REAL,
                        resistivity_mega_ohms REAL,
                        amount_of_acid_chemical_used TEXT,
                        amount_of_base_chemical_used TEXT,
                        remarks TEXT
                    );
                    CREATE TABLE di_polishing_tank_replacement (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        polishing_tank_number TEXT,
                        rinsing_time_start TEXT,
                        rinsing_time_finish TEXT,
                        source_resistivity_before_mohms REAL,
                        source_resistivity_after_mohms REAL,
                        point_of_use_resistivity_before_mohms REAL,
                        point_of_use_resistivity_after_mohms REAL,
                        remarks TEXT
                    );
                    CREATE TABLE di_tank_bldg_1_point_of_use (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        tank_level TEXT,
                        di_pump_no INTEGER,
                        source_pressure_psi INTEGER,
                        polishing_tank_1_no TEXT,
                        polishing_tank_2_no TEXT,
                        uv_hour_meter_hrs INTEGER,
                        facilities_monitoring_14 INTEGER,
                        resistivity_mohms REAL,
                        remarks TEXT
                    );
                    CREATE TABLE di_water_analysis_class (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        saw_scribe_bacteria_count INTEGER,
                        saw_scribe_particulate_count INTEGER,
                        saw_scribe_total_chlorine_content INTEGER,
                        saw_scribe_total_solid_by_evaporation INTEGER,
                        fa_bacteria_count INTEGER,
                        fa_particulate_count INTEGER,
                        fa_total_chlorine_content INTEGER,
                        fa_total_solid_by_evaporation INTEGER,
                        remarks TEXT
                    );
                    CREATE TABLE di_water_analysis_class_c (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        tin_plating_total_chlorine_content INTEGER,
                        solder_dip_total_chlorine_content INTEGER,
                        can_wash_total_chlorine_content INTEGER,
                        remarks TEXT
                    );
                    CREATE TABLE uv_light_sterilizer (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        di_water_plant_total_running_hours INTEGER,
                        di_water_room_total_running_hours_bldg_1 INTEGER,
                        wafer_saw_total_running_hours_saw INTEGER,
                        remarks TEXT
                    );
                    CREATE TABLE water_consumption (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        drinking_fountain_cu_m REAL,
                        deflash_2_cu_m REAL,
                        di_plant_cu_m REAL,
                        fume_scrubbers_cu_m REAL,
                        cooling_tower_1_to_3_cu_m REAL,
                        cooling_tower_04_cu_m REAL,
                        wwtp_cu_m REAL,
                        facilities_monitoring_16 INTEGER,
                        go3_cu_m REAL,
                        time TEXT,
                        remarks TEXT
                    );
                    CREATE TABLE wwtp (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date DATE,
                        shift TEXT,
                        tech_no INTEGER,
                        date_time_encode DATETIME,
                        influent_meter_reading INTEGER,
                        effluent_meter_reading INTEGER,
                        ph_neutralization_tank INTEGER,
                        aluminum_sulfate_dosing INTEGER,
                        polymer_dosing INTEGER,
                        hydrochloric_acid_dosing INTEGER,
                        filtrate_pump INTEGER,
                        agitator_1 INTEGER,
                        agitator_2 INTEGER,
                        agitator_3 INTEGER,
                        clarifier_to_neutralization_tank INTEGER,
                        neutralization_tank_to_aeration_1 INTEGER,
                        neutralization_tank_to_agitator INTEGER,
                        aeration_1_to_aeration_2 INTEGER,
                        recycle_to_cooling_tower INTEGER,
                        clarifier_to_thickening_tank INTEGER,
                        filter_press INTEGER,
                        remarks TEXT
                    );
                ''')

            conn.commit()
            conn.close()


if __name__ == "__main__":
    creator = CreateDatabase()
    creator.create_database()
