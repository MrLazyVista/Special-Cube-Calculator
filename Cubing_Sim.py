import random
import numpy as np
import matplotlib.pyplot as plt

                                             # input: array of up to length 3
# desired_stats = ['watt', 'boss', 'ied']    #  e.g. ['watt', 'boss', 'ied'], or 'str','dex','int','luk' or 'any'
# desired_scores = [21, 30, 0]               # input  integer value for stat %

desired_stats = ['str']
desired_scores = [20]
selected_cube = 'bonus'                      # input 'red', 'black', 'bonus', 'equality' or 'violet'
selected_equip = ['top']               # input 'hat','glove', 'top', 'bot', 'shoe', 'cape', 'belt', 'shoulder',
                                             # 'accessory' or 'heart_badge''weapon', 'secondary' or 'emblem', 
num_trials = 500

player_level = 290
item_level = 150
stat_ratio = [1,3.6,3.6*3.2]                # stat%, att, stat

# Hat - Top/Overall - Bottom - Gloves - Shoes - Cape/Belt/Shoulder

# Hat Legendary Cash Cube
hat_leg = {
    'str_12'        : 9.7561,
    'dex_12'        : 9.7561,
    'int_12'        : 9.7561,
    'luk_12'        : 9.7561,
    'hp_12'         : 9.7561,
    'mp_12'         : 9.7561,
    'allstat_9'     : 7.3171,
    'ignore_20'     : 7.3171,
    'ignore_40'     : 7.3171,
    'cdskip_1'      : 7.3171,
    'cdskip_2'      : 4.8780,
    'bless'         : 7.3171,
}

hat_unique = {
    'str_9'         : 8.6538,
    'dex_9'         : 8.6538,
    'int_9'         : 8.6538,
    'luk_9'         : 8.6538,
    'hp_9'          : 10.3846,     
    'mp_9'          : 10.3846,
    'allstat_6'     : 6.9231,
    'ignore_20'     : 6.9231,
    'ignore_40'     : 6.9231,
    'recov'         : 6.9231,
    'door'          : 6.9231,
}

# Top/Overall Legendary Top Cash Cube
top_leg = {
    'str_12'        : 10.2564,
    'dex_12'        : 10.2564,
    'int_12'        : 10.2564,
    'luk_12'        : 10.2564,
    'hp_12'         : 10.2564,
    'mp_12'         : 10.2564,
    'allstat_9'     : 7.6923,
    'ignore_20'     : 7.6923,
    'ignore_40'     : 7.6923,
    'invtime_3'     : 7.6923,
    'invchance_4'   : 7.6923,
}

top_unique = {
    'str_9'         : 7.2581,
    'dex_9'         : 7.2581,
    'int_9'         : 7.2581,
    'luk_9'         : 7.2581,
    'hp_9'          : 8.7097,
    'mp_9'          : 8.7097,
    'allstat_6'     : 5.8065,
    'ignore_20'     : 5.8065,
    'ignore_40'     : 5.8065,
    'invtime_2'     : 5.8065,
    'invchance_2'   : 5.8065,
    'reflect1'      : 5.8065,
    'reflect2'      : 5.8065,
    'recov'         : 5.8065,
}

# Bottom Legendary Cash Cube
bot_leg = {
    'str_12'        : 12.1212,
    'dex_12'        : 12.1212,
    'int_12'        : 12.1212,
    'luk_12'        : 12.1212,
    'hp_12'         : 12.1212,
    'mp_12'         : 12.1212,
    'allstat_9'     : 9.09091,
    'ignore_20'     : 9.09091,
    'ignore_40'     : 9.09091,
}   

bot_unique = {
    'str_9'         : 8.6538,
    'dex_9'         : 8.6538,
    'int_9'         : 8.6538,
    'luk_9'         : 8.6538,
    'hp_9'          : 10.3846,
    'mp_9'          : 10.3846,
    'allstat_6'     : 6.9231,
    'ignore_20'     : 6.9231,
    'ignore_40'     : 6.9231,
    'recov'         : 6.9231,
    'hyperbody'     : 6.9231,
}

# Gloves Legendary Cash Cube
glove_leg = {
    'str_12'        : 10,
    'dex_12'        : 10,
    'int_12'        : 10,
    'luk_12'        : 10,
    'hp_12'         : 10,
    'mp_12'         : 10,
    'critd_8'       : 10,
    'allstat_9'     : 7.500,
    'ignore_20'     : 7.500,
    'ignore_40'     : 7.500,
    'speedinf'      : 7.500,
}   

glove_unique = {
    'str_9'         : 8.03571,
    'dex_9'         : 8.03571,
    'int_9'         : 8.03571,
    'luk_9'         : 8.03571,
    'hp_9'          : 9.6429,     
    'mp_9'          : 9.6429,
    'allstat_6'     : 6.4286,
    'str_32'        : 1.6071,
    'dex_32'        : 1.6071,
    'int_32'        : 1.6071,
    'luk_32'        : 1.6071,
    'ignore_20'     : 6.4286,
    'ignore_40'     : 6.4286,
    'recov'         : 6.4286,    
    'sharpeyes'     : 6.4286,
}

# Shoes Legendary Cash Cube
shoe_leg = {
    'str_12'        : 11.1111,
    'dex_12'        : 11.1111,
    'int_12'        : 11.1111,
    'luk_12'        : 11.1111,
    'hp_12'         : 11.1111,
    'mp_12'         : 11.1111,
    'allstat_9'     : 8.3333,
    'ignore_20'     : 8.3333,
    'ignore_40'     : 8.3333, 
    'combatord'     : 8.3333, 
}

shoe_unique = {
    'str_9'         : 8.6538,
    'dex_9'         : 8.6538,
    'int_9'         : 8.6538,
    'luk_9'         : 8.6538,
    'hp_9'          : 10.3846,
    'mp_9'          : 10.3846,
    'allstat_6'     : 6.9231,
    'ignore_20'     : 6.9231,
    'ignore_40'     : 6.9231,
    'recov'         : 6.9231,
    'haste'         : 6.9231,
}

# Cape/Belt/Shoulder Legendary Cash Cube
cape_belt_shoulder_leg = {
    'str_12'        : 12.1212,
    'dex_12'        : 12.1212,
    'int_12'        : 12.1212,
    'luk_12'        : 12.1212,
    'hp_12'         : 12.1212,
    'mp_12'         : 12.1212,
    'allstat_9'     : 9.09091,
    'ignore_20'     : 9.09091,
    'ignore_40'     : 9.09091, 
}

cape_belt_shoulder_unique = {
    'str_9'         : 9.3750,
    'dex_9'         : 9.3750,
    'int_9'         : 9.3750,
    'luk_9'         : 9.3750,
    'hp_9'          : 11.250,
    'mp_9'          : 11.250,
    'allstat_6'     : 7.500,
    'ignore_20'     : 7.500,
    'ignore_40'     : 7.500,
    'recov'         : 7.500,
}

# Heart/Badge Legendary Cash Cube
heart_badge_leg = {
    'str_12'        : 14.8148,
    'dex_12'        : 14.8148,
    'int_12'        : 14.8148,
    'luk_12'        : 14.8148,
    'hp_12'         : 14.8148,
    'mp_12'         : 14.8148,
    'allstat_9'     : 11.1111,
}

heart_badge_unique = {
    'str_9'         : 11.2500,
    'dex_9'         : 11.2500,
    'int_9'         : 11.2500,
    'luk_9'         : 11.2500,
    'hp_9'          : 13.5000,
    'mp_9'          : 13.5000,
    'allstat_6'     : 9.00000,
    'recov'         : 9.00000,
}

# Accessory Legendary Cash Cube
accessory_leg = {
    'str_12'    : 10.2564,
    'dex_12'    : 10.2564,
    'int_12'    : 10.2564,
    'luk_12'    : 10.2564,
    'hp-12'     : 10.2564,
    'mp-12'     : 10.2564,
    'allstat_9' : 7.6923,
    'mpred1'    : 7.6923,
    'mpred2'    : 7.6923,
    'meso_20'   : 7.6923,
    'drop_20'   : 7.6923,
}

accessory_unique = {
    'str_9'     : 11.2500,
    'dex_9'     : 11.2500,
    'int_9'     : 11.2500,
    'luk_9'     : 11.2500,
    'hp_9'      : 13.5000,
    'mp_9'      : 13.5000,
    'allstat_6' : 9,
    'recov'     : 9,
}

# Weapon Legendary Cash Cube
weapon_leg = {
    'str_12'       : 9.7561,
    'dex_12'       : 9.7561,
    'int_12'       : 9.7561,
    'luk_12'       : 9.7561,
    'watt_12'      : 4.8780,
    'matt_12'      : 4.8780,
    'crit_rate'    : 4.8780,
    'damage_12'    : 4.8780,
    'allstat_9'    : 7.3171,
    'fwatt_32'     : 4.8780,   
    'fwatt_32'     : 4.8780,
    'ied_35'       : 4.8780,
    'ied_40'       : 4.8780,
    'boss_35'      : 9.7561,
    'boss_40'      : 4.8780,
}

weapon_unique = {
    'str_9'        : 10.4651,
    'dex_9'        : 10.4651,
    'int_9'        : 10.4651,
    'luk_9'        : 10.4651,
    'watt_9'       : 6.2791,
    'matt_9'       : 6.2791,
    'crit_rate'    : 8.3721,
    'damage_9'     : 6.2791,
    'allstat_6'    : 8.3721,
    'ied_30'       : 6.2791,
    'boss_30'      : 6.2791,
}

# Secondary Legendary Cash Cube
secondary_leg = {
    'str_12'       : 8.5106,
    'dex_12'       : 8.5106,
    'int_12'       : 8.5106,
    'luk_12'       : 8.5106,
    'watt_12'      : 4.2553,
    'matt_12'      : 4.2553,
    'crit_rate'    : 4.2553,
    'damage_12'    : 4.2553,
    'allstat_9'    : 6.3830,
    'fwatt_32'     : 4.2553, 
    'fwatt_32'     : 4.2553,
    'ied_35'       : 4.2553,
    'ied_40'       : 4.2553,
    'ignore_20'    : 6.3830,
    'ignore_40'    : 6.3830,
    'boss_35'      : 8.5106,
    'boss_40'      : 4.2553,
}

secondary_unique = {
    'str_9'        : 8.8235,
    'dex_9'        : 8.8235,
    'int_9'        : 8.8235,
    'luk_9'        : 8.8235,
    'watt_9'       : 5.2941,
    'matt_9'       : 5.2941,
    'crit_rate'    : 7.05882,
    'damage_9'     : 5.2941,
    'allstat_6'    : 7.05882,
    'ied_30'       : 5.2941,
    'ignore_20'    : 7.05882,
    'ignore_40'    : 7.05882,
    'boss_30'      : 5.2941,
}

# Emblem Legendary Cash Cube
emblem_leg = {
    'str_12'       : 11.4286,
    'dex_12'       : 11.4286,
    'int_12'       : 11.4286,
    'luk_12'       : 11.4286,
    'watt_12'      : 5.7143,
    'matt_12'      : 5.7143,
    'crit_rate'    : 5.7143,
    'damage_12'    : 5.7143,
    'allstat_9'    : 8.5714,
    'fwatt_32'     : 5.7143,   
    'fmatt_32'     : 5.7143,
    'ied_35'       : 5.7143,
    'ied_40'       : 5.7143,
}

emblem_unique = {
    'str_9'        : 11.2500,
    'dex_9'        : 11.2500,
    'int_9'        : 11.2500,
    'luk_9'        : 11.2500,
    'watt_9'       : 6.7500,
    'matt_9'       : 6.7500,
    'crit_rate'    : 9,
    'damage_9'     : 6.75,
    'allstat_6'    : 9,
    'ied_30'       : 6.75,
}
###############################################################################
###############################################################################
# Bonus Potentials
# Hat Legendary Bonus Cash Cube
hat_b_leg = {
    'fstr_20'       : 5,
    'fdex_20'       : 5,
    'fint_20'       : 5,
    'fluk_20'       : 5,   
    'hp'            : 5,
    'mp'            : 5,
    'fwatt_16'      : 3.333,
    'fmatt_16'      : 3.333,
    'str_8'         : 3.333,
    'dex_8'         : 3.333,
    'int_8'         : 3.333,
    'luk_8'         : 3.333,
    'hp_11'         : 5,
    'mp_11'         : 5, 
    'critd_1'       : 3.333,
    "allstat_6"     : 3.333,
    "strplvl_2"     : 3.333,
    "dexplvl_2"     : 3.333,
    "intplvl_2"     : 3.333,
    "lukplvl_2"     : 3.333,
    'cdskip_1'      : 5,
    'meso'          : 5,
    'drop'          : 5,
    'recov'         : 5,
}

hat_b_unique = {
    'fstr_18'       : 6.09199,
    'fdex_18'       : 6.09199,
    'fint_18'       : 6.09199,
    'fluk_18'       : 6.09199,    
    'hp'            : 6.09199,
    'mp'            : 6.09199,
    'fwatt_14'      : 4.06133,
    'fmatt_14'      : 4.06133,
    'str_6'         : 4.06133,
    'dex_6'         : 4.06133,
    'int_6'         : 4.06133,
    'luk_6'         : 4.06133,
    'hp_8'          : 6.09199,
    'mp_8'          : 6.09199,
    "allstat_5"     : 4.06133,
    "strplvl_1"     : 4.06133,
    "dexplvl_1"     : 4.06133,
    "intplvl_1"     : 4.06133,
    "lukplvl_1"     : 4.06133,
    'recov'         : 6.09199,
}

# Top/Overall/Bottom/Shoes/Cape/Belt/Shoulder Legendary Top Cash Cube
top_b_leg = {
    'fstr_20'       : 5.2632,
    'fdex_20'       : 5.2632,
    'fint_20'       : 5.2632,
    'fluk_20'       : 5.2632,
    'hp'            : 5.2632,
    'mp'            : 5.2632,
    'fwatt_16'      : 3.5088,
    'fmatt_16'      : 3.5088,
    'str_8'         : 3.5088,
    'dex_8'         : 3.5088,
    'int_8'         : 3.5088,
    'luk_8'         : 3.5088,
    'hp_11'         : 5.2632,
    'mp_11'         : 5.2632,
    'critd_1'       : 3.5088,
    "allstat_6"     : 3.5088,
    "strplvl_2"     : 3.5088,
    "dexplvl_2"     : 3.5088,
    "intplvl_2"     : 3.5088,
    "lukplvl_2"     : 3.5088,
    'meso'          : 5.2632,
    'drop'          : 5.2632,
    'recov'         : 5.2632,
}

top_b_unique = {
    'fstr_18'       : 6.09199,
    'fdex_18'       : 6.09199,
    'fint_18'       : 6.09199,
    'fluk_18'       : 6.09199,    
    'hp'            : 6.09199,
    'mp'            : 6.09199,
    'fwatt_14'      : 4.06133,
    'fmatt_14'      : 4.06133,
    'str_6'         : 4.06133,
    'dex_6'         : 4.06133,
    'int_6'         : 4.06133,
    'luk_6'         : 4.06133,
    'hp_8'          : 6.09199,
    'mp_8'          : 6.09199,
    "allstat_5"     : 4.06133,
    "strplvl_1"     : 4.06133,
    "dexplvl_1"     : 4.06133,
    "intplvl_1"     : 4.06133,
    "lukplvl_1"     : 4.06133,
    'recov'         : 6.09199
    }



# Gloves Legendary Bonus Cash Cube
glove_b_leg = {
    'fstr_20'       : 5.08475,
    'fdex_20'       : 5.08475,
    'fint_20'       : 5.08475,
    'fluk_20'       : 5.08475,
    'hp'            : 5.08475,
    'mp'            : 5.08475,
    'fwatt_16'      : 3.3898,
    'fmatt_16'      : 3.3898,
    'str_8'         : 3.3898,
    'dex_8'         : 3.3898,
    'int_8'         : 3.3898,
    'luk_8'         : 3.3898,
    'hp_11'         : 5.08475,
    'mp_11'         : 5.08475,
    'critd_3'       : 3.3898,
    'critd_1'       : 3.3898,
    "allstat_6"     : 3.3898,
    "strplvl_2"     : 3.3898,
    "dexplvl_2"     : 3.3898,
    "intplvl_2"     : 3.3898,
    "lukplvl_2"     : 3.3898,
    'meso'          : 5.08475,
    'drop'          : 5.08475,
    'recov'         : 5.08475,
}   

glove_b_unique = {
    'fstr_18'       : 6.09199,
    'fdex_18'       : 6.09199,
    'fint_18'       : 6.09199,
    'fluk_18'       : 6.09199,    
    'hp'            : 6.09199,
    'mp'            : 6.09199,
    'fwatt_14'      : 4.06133,
    'fmatt_14'      : 4.06133,
    'str_6'         : 4.06133,
    'dex_6'         : 4.06133,
    'int_6'         : 4.06133,
    'luk_6'         : 4.06133,
    'hp_8'          : 6.09199,
    'mp_8'          : 6.09199,
    "allstat_5"     : 4.06133,
    "strplvl_1"     : 4.06133,
    "dexplvl_1"     : 4.06133,
    "intplvl_1"     : 4.06133,
    "lukplvl_1"     : 4.06133,
    'recov'         : 6.09199,
    }

# Heart/Badge Legendary Bonus Cash Cube
heart_badge_b_leg = {
    'fstr_20'       : 5.4545,
    'fdex_20'       : 5.4545,
    'fint_20'       : 5.4545,
    'fluk_20'       : 5.4545,
    'hp'            : 5.4545,
    'mp'            : 5.4545,
    'fwatt_16'      : 3.6364,
    'fmatt_16'      : 3.6364,
    'str_8'         : 3.6364,
    'dex_8'         : 3.6364,
    'int_8'         : 3.6364,
    'luk_8'         : 3.6364,
    'hp_11'         : 5.4545,
    'mp_11'         : 5.4545,
    "allstat_6"     : 3.6364,
    "strplvl_2"     : 3.6364,
    "dexplvl_2"     : 3.6364,
    "intplvl_2"     : 3.6364,
    "lukplvl_2"     : 3.6364,
    'meso'          : 5.4545,
    'drop'          : 5.4545,
    'recov'         : 5.4545,
}

heart_badge_b_unique = {
    'fstr_18'       : 6.09199,
    'fdex_18'       : 6.09199,
    'fint_18'       : 6.09199,
    'fluk_18'       : 6.09199,    
    'hp'            : 6.09199,
    'mp'            : 6.09199,
    'fwatt_14'      : 4.06133,
    'fmatt_14'      : 4.06133,
    'str_6'         : 4.06133,
    'dex_6'         : 4.06133,
    'int_6'         : 4.06133,
    'luk_6'         : 4.06133,
    'hp_8'          : 6.09199,
    'mp_8'          : 6.09199,
    "allstat_5"     : 4.06133,
    "strplvl_1"     : 4.06133,
    "dexplvl_1"     : 4.06133,
    "intplvl_1"     : 4.06133,
    "lukplvl_1"     : 4.06133,
    'recov'         : 6.09199,
}

# Accessory Legendary Bonus Cash Cube
accessory_b_leg = {
    'fstr_20'       : 5.1724,
    'fdex_20'       : 5.1724,
    'fint_20'       : 5.1724,
    'fluk_20'       : 5.1724,
    'hp'            : 5.1724,
    'mp'            : 5.1724,
    'fwatt_16'      : 3.4483,
    'fmatt_16'      : 3.4483,
    'str_8'         : 3.4483,
    'dex_8'         : 3.4483,
    'int_8'         : 3.4483,
    'luk_8'         : 3.4483,
    'hp_11'         : 5.1724,
    'mp_11'         : 5.1724,
    "allstat_6"     : 3.4483,
    "strplvl_2"     : 3.4483,
    "dexplvl_2"     : 3.4483,
    "intplvl_2"     : 3.4483,
    "lukplvl_2"     : 3.4483,
    'meso'          : 5.1724,
    'drop'          : 5.1724,
    'recov'         : 5.1724,
}
accessory_b_unique = {
    'fstr_18'       : 6.09199,
    'fdex_18'       : 6.09199,
    'fint_18'       : 6.09199,
    'fluk_18'       : 6.09199,    
    'hp'            : 6.09199,
    'mp'            : 6.09199,
    'fwatt_14'      : 4.06133,
    'fmatt_14'      : 4.06133,
    'str_6'         : 4.06133,
    'dex_6'         : 4.06133,
    'int_6'         : 4.06133,
    'luk_6'         : 4.06133,
    'hp_8'          : 6.09199,
    'mp_8'          : 6.09199,
    "allstat_5"     : 4.06133,
    "strplvl_1"     : 4.06133,
    "dexplvl_1"     : 4.06133,
    "intplvl_1"     : 4.06133,
    "lukplvl_1"     : 4.06133,
    'recov'         : 6.09199,
}

# Weapon Legendary Bonus Cash Cube
weapon_b_leg = {
    'hp'            : 7.6923,
    'mp'            : 7.6923,
    'watt_12'       : 5.1282,
    'matt_12'       : 5.1282,
    'crit_rate'     : 5.1282,
    'str_12'        : 7.6923,
    'dex_12'        : 7.6923,
    'int_12'        : 7.6923,
    'luk_12'        : 7.6923,
    'damage_12'     : 2.5641,
    'allstat_9'     : 5.1282,
    'strplvl_2'     : 5.1282,
    'dexplvl_2'     : 5.1282,
    'intplvl_2'     : 5.1282,
    'lukplvl_2'     : 5.1282,
    'fwatt_32'      : 2.5641,
    'fwatt_32'      : 2.5641,
    'ied_5'         : 2.5641,
    'boss_18'       : 2.5641,
}

weapon_b_unique = {
    'hp'            : 6.9420,
    'mp'            : 6.9420,
    'watt_9'        : 4.6248,
    'matt_9'        : 4.6248,
    'crit_rate'     : 4.6248,
    'str_9'         : 6.9420,
    'dex_9'         : 6.9420,
    'int_9'         : 6.9420,
    'luk_9'         : 6.9420,
    'damage_9'      : 2.3140,
    'allstat_6'     : 4.6248,
    'strplvl_1'     : 4.6248,
    'dexplvl_1'     : 4.6248,
    'intplvl_1'     : 4.6248,
    'lukplvl_1'     : 4.6248,
    'hprecov'       : 6.9420,
    'mprecov'       : 6.9420,
    'ied_4'         : 2.3140,
    'boss_12'       : 2.3140,
}

# Emblem Legendary Bonus Cash Cube
emblem_b_leg = {
    'hp'            : 7.8947,
    'mp'            : 7.8947,
    'watt_12'       : 5.2632,
    'matt_12'       : 5.2632,
    'crit_rate'     : 5.2632,
    'str_12'        : 7.8947,
    'dex_12'        : 7.8947,
    'int_12'        : 7.8947,
    'luk_12'        : 7.8947,
    'damage_12'     : 2.6316,
    'allstat_9'     : 5.2632,
    'strplvl_2'     : 5.2632,
    'dexplvl_2'     : 5.2632,
    'intplvl_2'     : 5.2632,
    'lukplvl_2'     : 5.2632,
    'fwatt_32'      : 2.6316,
    'fwatt_32'      : 2.6316,
    'ied_5'         : 2.6316,
}

emblem_b_unique = {
    'hp'            : 7.1073,
    'mp'            : 7.1073,
    'watt_9'        : 4.7382,
    'matt_9'        : 4.7382,
    'crit_rate'     : 4.7382,
    'str_9'         : 7.1073,
    'dex_9'         : 7.1073,
    'int_9'         : 7.1073,
    'luk_9'         : 7.1073,
    'damage_9'      : 2.3691,
    'allstat_6'     : 4.7382,
    'strplvl_1'     : 4.7382,
    'dexplvl_1'     : 4.7382,
    'intplvl_1'     : 4.7382,
    'lukplvl_1'     : 4.7382,
    'hprecov'       : 7.1073,
    'mprecov'       : 7.1073,
    'ied_4'         : 2.3691,
}

# Secondary Legendary Bonus Cash Cube
secondary_b_leg = {
    'hp'            : 7.3171,
    'mp'            : 7.3171,
    'watt_12'       : 4.8780,
    'matt_12'       : 4.8780,
    'crit_rate'     : 4.8780,
    'str_12'        : 7.3171,
    'dex_12'        : 7.3171,
    'int_12'        : 7.3171,
    'luk_12'        : 7.3171,
    'damage_12'     : 2.4390,
    'allstat_9'     : 4.8780,
    'strplvl_2'     : 4.8780,
    'dexplvl_2'     : 4.8780,
    'intplvl_2'     : 4.8780,
    'lukplvl_2'     : 4.8780,
    'fwatt_32'      : 2.4390,
    'fwatt_32'      : 2.4390,
    'ied_5'         : 2.4390,
    'boss_18'       : 2.4390,
}

secondary_b_unique = {
    'hp'            : 6.9420,
    'mp'            : 6.9420,
    'watt_9'        : 4.6248,
    'matt_9'        : 4.6248,
    'crit_rate'     : 4.6248,
    'str_9'         : 6.9420,
    'dex_9'         : 6.9420,
    'int_9'         : 6.9420,
    'luk_9'         : 6.9420,
    'damage_9'      : 2.3140,
    'allstat_6'     : 4.6248,
    'strplvl_1'     : 4.6248,
    'dexplvl_1'     : 4.6248,
    'intplvl_1'     : 4.6248,
    'lukplvl_1'     : 4.6248,
    'hprecov'       : 6.9420,
    'mprecov'       : 6.9420,
    'ied_4'         : 2.3140,
    'boss_12'       : 2.3140,
}
###############################################################################
###############################################################################

def populate_dictionary(lines_and_weights, array):
    for item, leg, unique in array:
        leg_lines = []
        leg_weights = []
        for k,v in leg.items():
            leg_lines += [k]
            leg_weights += [v]

        unique_lines = []
        unique_weights = []
        for k,v in unique.items():
            unique_lines += [k]
            unique_weights += [v]
            
        s = sum(leg_weights)
        for i in range(len(leg_weights)):
            leg_weights[i] /= s

        s = sum(unique_weights)
        for i in range(len(unique_weights)):
            unique_weights[i] /= s
        # print(f"{item}, {sum(leg_weights)}, {sum(unique_weights)}")

        lines_and_weights[item] = [leg_lines, leg_weights, unique_lines, unique_weights]


lines_and_weights = {}
populate_dictionary(lines_and_weights, [
        ['hat', hat_leg, hat_unique],
        ['top', top_leg, top_unique],
        ['bot', bot_leg, bot_unique],
        ['glove', glove_leg, glove_unique],
        ['shoe', shoe_leg, shoe_unique],
        ['cape',     cape_belt_shoulder_leg, cape_belt_shoulder_unique],
        ['belt',     cape_belt_shoulder_leg, cape_belt_shoulder_unique],
        ['shoulder', cape_belt_shoulder_leg, cape_belt_shoulder_unique],
        ['heart_badge', heart_badge_leg, heart_badge_unique],
        ['accessory', accessory_leg, accessory_unique],
        ['weapon', weapon_leg, weapon_unique],
        ['secondary', secondary_leg, secondary_unique],
        ['emblem', emblem_leg, emblem_unique],
    ])

lines_and_weights_bonus = {}
populate_dictionary(lines_and_weights_bonus, [
        ['hat', hat_b_leg, hat_b_unique],
        ['top',      top_b_leg, top_b_unique],
        ['bot',      top_b_leg, top_b_unique],
        ['shoe',     top_b_leg, top_b_unique],
        ['cape',     top_b_leg, top_b_unique],
        ['belt',     top_b_leg, top_b_unique],
        ['shoulder', top_b_leg, top_b_unique],
        ['glove', glove_b_leg, glove_b_unique],
        ['heart_badge', heart_badge_b_leg, heart_badge_b_unique],
        ['accessory', accessory_b_leg, accessory_b_unique],
        ['weapon', weapon_b_leg, weapon_b_unique],
        ['secondary', secondary_b_leg, secondary_b_unique],
        ['emblem', emblem_b_leg, emblem_b_unique],
    ])

    



def is_valid_roll(roll):
    two_appeareances_max = [
        'ied', 'drop', 'ignore', 'invchance',
    ]
    one_appearance_max = ['skill', 'invtime']

    for key in two_appeareances_max:
        if sum(line.startswith(key) for line in roll) > 2:
            return False
    
    for key in one_appearance_max:
        if sum(line.startswith(key) for line in roll) > 1:
            return False
    
    return True



def red_cube_roll(leg_lines, leg_weights, unique_lines, unique_weights):
    
    line2_prime = 0.10
    line3_prime = 0.01

    prime_line = [
        True,
        random.uniform(0,1) < line2_prime,
        random.uniform(0,1) < line3_prime
    ]
    result = []

    for is_prime in prime_line:
        if is_prime:
            result += [np.random.choice(leg_lines, p=leg_weights)]
        else:
            result += [np.random.choice(unique_lines, p=unique_weights)]
        
    return result

def black_cube_roll(leg_lines, leg_weights, unique_lines, unique_weights):
    
    line2_prime = 0.20
    line3_prime = 0.05

    prime_line = [
        True,
        random.uniform(0,1) < line2_prime,
        random.uniform(0,1) < line3_prime
    ]
    result = []

    for is_prime in prime_line:
        if is_prime:
            result += [np.random.choice(leg_lines, p=leg_weights)]
        else:
            result += [np.random.choice(unique_lines, p=unique_weights)]
        
    return result

def equality_cube_roll(leg_lines, leg_weights, unique_lines, unique_weights):
    
    line2_prime = 1
    line3_prime = 1

    prime_line = [
        True,
        random.uniform(0,1) < line2_prime,
        random.uniform(0,1) < line3_prime
    ]
    result = []

    for is_prime in prime_line:
        if is_prime:
            result += [np.random.choice(leg_lines, p=leg_weights)]
        else:
            result += [np.random.choice(unique_lines, p=unique_weights)]
        
    return result

def violet_cube_roll(leg_lines, leg_weights, unique_lines, unique_weights):
    
    line2_prime = 0.10
    line3_prime = 0.01
    line4_prime = 0.01
    line5_prime = 0.10
    line6_prime = 0.01

    prime_line = [
        True,
        random.uniform(0,1) < line2_prime,
        random.uniform(0,1) < line3_prime,
        random.uniform(0,1) < line4_prime,
        random.uniform(0,1) < line5_prime,
        random.uniform(0,1) < line6_prime,

    ]
    result = []

    for is_prime in prime_line:
        if is_prime:
            result += [np.random.choice(leg_lines, p=leg_weights)]
        else:
            result += [np.random.choice(unique_lines, p=unique_weights)]
        
    return result

def bonus_cube_roll(leg_lines, leg_weights, unique_lines, unique_weights):
    
    line2_prime = 1 / 201
    line3_prime = 1 / 201

    prime_line = [
        True,
        random.uniform(0,1) < line2_prime,
        random.uniform(0,1) < line3_prime
    ]
    result = []

    for is_prime in prime_line:
        if is_prime:
            result += [np.random.choice(leg_lines, p=leg_weights)]
        else:
            result += [np.random.choice(unique_lines, p=unique_weights)]
        
    return result




def count_this_stat(roll, stat):
    good_lines = []
#########################################
    adjust = 0
    if item_level >= 160 and stat in ['str','dex','int','luk']:
        adjust = 1;
    if selected_cube == 'bonus':
        if stat in ['str','dex','int','luk']:
            for line in roll:
                if line.startswith(stat+'_') or line.startswith('all'):
                    good_lines += [float(line.split('_')[-1])+ adjust] 
                elif line.startswith('f'+stat):
                    good_lines += [float(line.split('_')[-1])/stat_ratio[2] + adjust]
                elif line.startswith(stat+'plvl'):
                    good_lines += [float(line.split('_')[-1])*(player_level//9)/stat_ratio[2]]
                elif stat != 'int' and line.startswith('fwatt'):
                    good_lines += [float(line.split('_')[-1])/stat_ratio[1] + adjust]
                elif stat == 'int' and line.startswith('fmatt'):
                    good_lines += [float(line.split('_')[-1])/stat_ratio[1] + adjust]
                elif stat != 'int' and line.startswith('wattplvl'):
                    good_lines += [float(line.split('_')[-1])*(player_level//9)/stat_ratio[2]]
                elif stat == 'int' and line.startswith('mattplvl'):
                    good_lines += [float(line.split('_')[-1])*(player_level//9)/stat_ratio[2]]
                elif line.startswith('critd'):
                    good_lines += [float(line.split('_')[-1])*4]
        else:
            for line in roll:
                if line.startswith(stat+'_'):
                    good_lines += [float(line.split('_')[-1]) + adjust]
#########################################
    else:
        if stat in ['str','dex','int','luk']:  # because allstat is a wildcard
            for line in roll:
                if line.startswith(stat) or line.startswith('all'):
                    good_lines += [float(line.split('_')[-1]) + adjust]

        else:
            for line in roll:
                if line.startswith(stat):
                    good_lines += [float(line.split('_')[-1]) + adjust]
#########################################
    good_lines.sort()
    return sum(good_lines[-3:])  # pick highest 3 for violet cubes

if   selected_cube == 'red':       roll_function = red_cube_roll
elif selected_cube == 'black':     roll_function = black_cube_roll
elif selected_cube == 'bonus':     roll_function = bonus_cube_roll
elif selected_cube == 'equality':  roll_function = equality_cube_roll
elif selected_cube == 'violet':    roll_function = violet_cube_roll
else:                              roll_function = red_cube_roll

for equip in selected_equip:
    counts = [0]*num_trials
    for i in range(num_trials):

        count = 0
        while True:
            count += 1
            
            valid = False
            while not valid:
                if selected_cube == 'bonus':
                    a = roll_function(*lines_and_weights_bonus[equip])
                else:
                    a = roll_function(*lines_and_weights[equip])
                valid = is_valid_roll(a)
            
            scores = []
            for stat in desired_stats:
                if stat == 'any':
                    scores += [max(count_this_stat(a, s) for s in ['str','dex','int','luk'])]
                else:
                    scores += [count_this_stat(a, stat)]
            
            if all(x >= y for x,y in zip(scores, desired_scores)):
                # print(f'Trial: {i: 3}  {a}')
                break
        
        counts[i] = count

    counts.sort()

    print('---------------------------------------------------------')
    print(f'Desired stat        : {desired_stats}')
    print(f'Desired %stat       : {desired_scores}')
    print(f'Selected Cube       : {selected_cube}')
    print(f'Selected Equip      : {equip}')
    print(f'Item Level          : {item_level}')
    print('---------------------------------------------------------')
    print(f'Average Cube Amount : {sum(counts)/num_trials}')
    print(f'50 percentile       : {counts[round(num_trials/(100/50))]}')
    print(f'75 percentile       : {counts[round(num_trials/(100/75))]}')
    print(f'90 percentile       : {counts[round(num_trials/(100/90))]}')
    print(f'95 percentile       : {counts[round(num_trials/(100/95))]}')
    print('---------------------------------------------------------')



# counts = [0]*num_trials
# for i in range(num_trials):

#     count = 0
#     while True:
#         count += 1
        
#         valid = False
#         while not valid:
#             if selected_cube == 'bonus':
#                 a = roll_function(*lines_and_weights_bonus[selected_equip])
#             else:
#                 a = roll_function(*lines_and_weights[selected_equip])
#             valid = is_valid_roll(a)
        
#         scores = []
#         for stat in desired_stats:
#             if stat == 'any':
#                 scores += [max(count_this_stat(a, s) for s in ['str','dex','int','luk'])]
#             else:
#                 scores += [count_this_stat(a, stat)]
        
#         if all(x >= y for x,y in zip(scores, desired_scores)):
#             print(f'Trial: {i: 3}  {a}')
#             break
    
#     counts[i] = count

# counts.sort()

# print('---------------------------------------------------------')
# print(f'Desired stat        : {desired_stats}')
# print(f'Desired %stat       : {desired_scores}')
# print(f'Selected Cube       : {selected_cube}')
# print(f'Selected Equip      : {selected_equip}')
# print('---------------------------------------------------------')
# print(f'Average Cube Amount : {sum(counts)/num_trials}')
# print(f'50 percentile       : {counts[round(num_trials/(100/50))]}')
# print(f'75 percentile       : {counts[round(num_trials/(100/75))]}')
# print(f'90 percentile       : {counts[round(num_trials/(100/90))]}')
# print(f'95 percentile       : {counts[round(num_trials/(100/95))]}')
# print('---------------------------------------------------------')




# HISTOGRAM 
# 
# a = np.random.choice(top_leg_lines, size=10000, p=top_leg_weights)
# # bins = range(len(top_leg_lines))
# c = {x:0 for x in top_leg_lines}
# for x in a:
#     c[x] += 1
# # print(h)
# b = [c[x] for x in top_leg_lines]

# plt.bar(range(len(b)), b, tick_label=top_leg_lines)
# plt.show()
