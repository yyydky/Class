# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:12:53 2018

@author: Carol Zhu
"""

# importing enum for enumerations
import enum

"""
class excavation_monitoring_frequency(Enum):
    #contents
    
class gas_contents(Enum):
    #contents
    
class excavation_monitoring_frequency(Enum):
    #contents
    
    joint_field_applied_coating: enum
    line_backfill_type: enum
    line_burial_location: enum
    line_locate_system_effectiveness: enum
    line_locate_system_type: enum
    line_prot_measures_excavation: enum
    line_prot_measures_fire_explosion: enum
    line_prot_measures_other_outside_damage: enum
    line_prot_measusres_rain_flood: enumb
    line_prot_measures_vandalism: enum
    line_prot_measures_vehicles: enum
"""
    
class pipe:
    above_below_ground = True
    ac_induced_corrosion_potential = True
    adjacent_services_measure = 0
    age = 0
    arcing_potential_of_line = True
    cp_history = 0.00
    cust_spec_earth_movement_index = 0.00
    cust_spec_electric_arcing_index = 0.00
    cust_spec_excessive_temperature_index = 0.00
    cust_spec_external_corrosion_index = 0.00
    cust_spec_failure_mode_index = 0.00
    cust_spec_fire_explosion_damage_index = 0.00
    cust_spec_first_party_damage_index = 0.00
    cust_spec_frost_heave_index = 0.00
    cust_spec_incorrect_operations_index = 0.00
    cust_spec_internal_corrosion_index = 0.00
    cust_spec_lightning_index = 0.00
    cust_spec_other_failures_index = 0.00
    cust_spec_other_outside_forces_index = 0.00
    cust_spec_rain_flood_damage_index = 0.00
    cust_spec_stress_corrosion_cracking_index = 0.00
    cust_spec_third_party_damage_index = 0.00
    cust_spec_vandalism_index = 0.00
    cust_spec_vehicle_damage_index = 0.00
    cust_spec_wind_damage_index = 0.00
    depth_of_cover = 0.00
    earth_movement_potential = 0.00
    #excavation_monitoring_frequency
    excavation_practice_effectiveness = 0.00
    fire_explosion_potential = 0.00
    flood_potential = 0.00
    frost_heave_potential = 0.00
    #gas_contents
    haz_external_corrosion_leak_history = 0.00
    haz_internal_corrosion_leak_history = 0.00
    haz_plastic_material_failure_leak_history = 0.00
    haz_stress_corrosion_cracking_leak_history = 0.00
    high_temperature_potential = 0.00
    joint_failures_potential = 0.00
    #joint_field_applied_coating
    lightning_strikes_intensity = 0.00
    """
    line_backfill_type
    line_burial_location: enum
    line_locate_system_effectiveness: enum
    line_locate_system_type: enum
    line_prot_measures_excavation: enum
    line_prot_measures_fire_explosion: enum
    line_prot_measures_other_outside_damage: enum
    line_prot_measusres_rain_flood: enumb
    line_prot_measures_vandalism: enum
    line_prot_measures_vehicles: enum
    """
    #line_prot_measures_wind: enum
    low_temperature_potential = 0.00
    maintenance_history = 0.00
    #material_type: enum
    non_haz_external_corrosion_leak_history = 0.00
    non_haz_internal_corrosion_leak_history = 0.00
    non_haz_plastic_material_failure_leak_history = 0.00
    non_haz_stress_corrosion_cracking_leak_history = 0.00
    number_of_fittings = 0
    number_of_services = 0
    one_call_density = 0.00
    one_call_effectiveness = 0.00
    #operating_area_type: enum
    operating_pressure = 0
    operating_temperature = 0
    operations_activity_density = 0.00
    operator_contractor_activity = 0.00
    operator_contractor_excavation_program_effectiveness = 0.00
    oq_effectiveness = 0.00
    other_failures_potential = 0.00
    other_materials_failure_potential = 0.00
    other_outside_forces_potential = 0.00
    """
    pipe_coating_type: enum
    pipe_diameter: enum
    pipe_joining_method: enum
    pipe_wall_thickness: enum
    """
    rain_potential = 0.00
    seismic_intensity = 0.00
    #soil_type: enum
    tee_cap_failures_potential = 0.00
    training_program_effectiveness = 0.00
    vandalism_mitigation_program_effectiveness = 0.00
    vandalism_potential = 0.00
    vehicle_damage_potential = 0.00
    wind_potential = 0.00



    