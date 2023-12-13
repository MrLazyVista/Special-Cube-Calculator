import random
import numpy as np
import matplotlib.pyplot as plt
                                             # input: array of up to length 3
# desired_stats = ['watt', 'boss', 'ied']    #  e.g. ['watt', 'boss', 'ied'], or 'str','dex','int','luk' or 'any'
# desired_scores = [21, 30, 0]               # input  integer value for stat %

desired_stats = ['watt','boss']
desired_scores = [21,30]
selected_cube = 'violet'                      # input 'red', 'black', 'bonus', 'equality' or 'violet'
selected_equip = ['secondary']               # input 'hat','glove', 'top', 'bot', 'shoe', 'cape', 'belt', 'shoulder',
                                             # 'accessory' or 'heart_badge''weapon', 'secondary' or 'emblem', 
num_trials = 500
Percent_to_flat = 9
Att_to_flat = 3
Level = 270

# Hat - Top/Overall - Bottom - Gloves - Shoes - Cape/Belt/Shoulder

# Hat Legendary Cash Cube
hat_leg = {
    'str_12'        : 1/12.5,
    'dex_12'        : 1/12.5,
    'int_12'        : 1/12.5,
    'luk_12'        : 1/12.5,
    'allstat_9'     : 1/16.66,
    'cdskip_1'      : 1/16.66,
    'cdskip_2'      : 1/25,
    'hp'            : 1/12.5,
    'mp'            : 1/12.5,
#    'skill_2'       : 1/16.66,
#    'skill_3'       : 1/25,
    'ignore_20'     : 1/16.66,
    'ignore_40'     : 1/16.66,
    'recov'         : 0,
    'bless'         : 1/16.66,
}

hat_unique = {
    'str_9'         : 1/12.4,
    'dex_9'         : 1/12.4,
    'int_9'         : 1/12.4,
    'luk_9'         : 1/12.4,
    'allstat_6'     : 1/15.5,
    'hp'            : 1/10.33,     
    'mp'            : 1/10.33,
#    'skill_1'       : 1/15.5,
#    'skill_2'       : 1/31,
    'ignore_20'     : 1/15.5,
    'ignore_40'     : 1/15.5,
    'recov'         : 1/15.5,
    'door'          : 1/15.5,
}

# Top/Overall Legendary Top Cash Cube
top_leg = {
    'str_12'        : 1/11.25,
    'dex_12'        : 1/11.25,
    'int_12'        : 1/11.25,
    'luk_12'        : 1/11.25,
    'allstat_9'     : 1/15,
    'hp'            : 1/11.25,  
    'mp'            : 1/11.25,
#    'eleres'        : 1/22.5,
    'ignore_20'     : 1/15,
    'ignore_40'     : 1/15,
    'invtime_3'     : 1/15,
    'invchance_4'   : 1/15,
    'recov'         : 0,
}

top_unique = {
    'str_9'         : 1/13.2,
    'dex_9'         : 1/13.2,
    'int_9'         : 1/13.2,
    'luk_9'         : 1/13.2,
    'allstat_6'     : 1/16.5,
    'hp'            : 1/11, 
    'mp'            : 1/11,
#    'eleres'        : 0,
    'ignore_20'     : 1/16.5,
    'ignore_40'     : 1/16.5,
    'invtime_2'     : 1/16.5,
    'invchance_2'   : 1/16.5,
    'reflect1'      : 1/16.5,
    'reflect2'      : 1/33,
    'recov'         : 1/16.5,
}

# Bottom Legendary Cash Cube
bot_leg = {
    'str_12'        : 1/9.75,
    'dex_12'        : 1/9.75,
    'int_12'        : 1/9.75,
    'luk_12'        : 1/9.75,
    'allstat_9'     : 1/13,
    'hp'            : 1/9.75,  
    'mp'            : 1/9.75,
#    'status'        : 1/19.5,
    'ignore_20'     : 1/13,
    'ignore_40'     : 1/13, 
    'reflect1'      : 0,
    'reflect2'      : 0,
    'recov'         : 0,
}   

bot_unique = {
    'str_9'         : 1/11.2,
    'dex_9'         : 1/11.2,
    'int_9'         : 1/11.2,
    'luk_9'         : 1/11.2,
    'allstat_6'     : 1/14,
    'hp'            : 1/9.33,     
    'mp'            : 1/9.33,
    'ignore_20'     : 1/14,
    'ignore_40'     : 1/14,
    'recov'         : 1/14,
    'hyperbody'     : 1/14,
}

# Gloves Legendary Cash Cube
glove_leg = {
    'str_12'        : 1/11,
    'dex_12'        : 1/11,
    'int_12'        : 1/11,
    'luk_12'        : 1/11,
    'allstat_9'     : 1/14.66,
    'critd_8'       : 1/11,
    'hp'            : 1/11,  
    'mp'            : 1/11,
    'ignore_20'     : 1/14.66,
    'ignore_40'     : 1/14.66, 
    'recov'         : 0,
    'steal3'        : 0,
    'steal5'        : 0,
    'steal7'        : 0,
    'speedinf'      : 1/14.66, 
}   

glove_unique = {
    'str_9'         : 1/12,
    'dex_9'         : 1/12,
    'int_9'         : 1/12,
    'luk_9'         : 1/12,
    'allstat_6'     : 1/15,
    'hp'            : 1/10,     
    'mp'            : 1/10,
    'str_3'         : 1/60,  # str +1 per 10 character levels
    'dex_3'         : 1/60,
    'int_3'         : 1/60,
    'luk_3'         : 1/60,
    'ignore_20'     : 1/15,
    'ignore_40'     : 1/15,
    'recov'         : 1/15,    
    'steal1'        : 0,
    'steal2'        : 0,
    'sharpeyes'     : 1/15,
}

# Shoes Legendary Cash Cube
shoe_leg = {
    'str_12'        : 1/10,
    'dex_12'        : 1/10,
    'int_12'        : 1/10,
    'luk_12'        : 1/10,
    'allstat_9'     : 1/13.33,
    'hp'            : 1/10,  
    'mp'            : 1/10,
    'ignore_20'     : 1/13.33,
    'ignore_40'     : 1/13.33, 
    'recov'         : 0,
    'combatord'     : 1/13.33, 
}

shoe_unique = {
    'str_9'         : 1/11.2,
    'dex_9'         : 1/11.2,
    'int_9'         : 1/11.2,
    'luk_9'         : 1/11.2,
    'allstat_6'     : 1/14,
    'hp'            : 1/9.33,  
    'mp'            : 1/9.33,
    'ignore_20'     : 1/14,
    'ignore_40'     : 1/14, 
    'recov'         : 1/14,
    'haste'         : 1/14, 
}

# Cape/Belt/Shoulder Legendary Cash Cube
cape_belt_shoulder_leg = {
    'str_12'    : 1/9.25,
    'dex_12'    : 1/9.25,
    'int_12'    : 1/9.25,
    'luk_12'    : 1/9.25,
    'allstat_9' : 1/12.33,
    'hp'        : 1/9.25,
    'mp'        : 1/9.25,
    'ignore_20' : 1/12.33,
    'ignore_40' : 1/12.33, 
    'recov'     : 0,
}

cape_belt_shoulder_unique = {
    'str_9'     : 1/10.4,
    'dex_9'     : 1/10.4,
    'int_9'     : 1/10.4,
    'luk_9'     : 1/10.4,
    'allstat_6' : 1/13,
    'hp'        : 1/8.66,
    'mp'        : 1/8.66,
    'ignore_20' : 1/13,
    'ignore_40' : 1/13, 
    'recov'     : 1/13,
}

# Heart/Badge Legendary Cash Cube
heart_badge_leg = {
    'str_12'    : 1/7.75,
    'dex_12'    : 1/7.75,
    'int_12'    : 1/7.75,
    'luk_12'    : 1/7.75,
    'allstat_9' : 1/10.33,
    'hp'        : 1/7.75,
    'mp'        : 1/7.75,
    'recov'     : 0,
}

heart_badge_unique = {
    'str_9'     : 1/8.8,
    'dex_9'     : 1/8.8,
    'int_9'     : 1/8.8,
    'luk_9'     : 1/8.8,
    'allstat_6' : 1/11,
    'hp'        : 1/7.33,
    'mp'        : 1/7.33,
    'recov'     : 1/11,
}

# Accessory Legendary Cash Cube
accessory_leg = {
    'str_12'    : 1/10.75,
    'dex_12'    : 1/10.75,
    'int_12'    : 1/10.75,
    'luk_12'    : 1/10.75,
    'allstat_9' : 1/14.33,
    'hp'        : 1/10.75,
    'mp'        : 1/10.75,
    'mpred1'    : 1/14.33,
    'mpred2'    : 1/14.33,
    'recov'     : 0,
    'meso_20'   : 1/14.33,
    'drop_20'   : 1/14.33,
}

accessory_unique = {
    'str_9'     : 1/8.8,
    'dex_9'     : 1/8.8,
    'int_9'     : 1/8.8,
    'luk_9'     : 1/8.8,
    'allstat_6' : 1/11,
    'hp'        : 1/7.33,
    'mp'        : 1/7.33,
    'recov'     : 1/11,
}

# Weapon Legendary Cash Cube
weapon_leg = {
    'str_12'       : 1/10.25,
    'dex_12'       : 1/10.25,
    'int_12'       : 1/10.25,
    'luk_12'       : 1/10.25,
    'watt_12'      : 1/20.5,
    'matt_12'      : 1/20.5,
    'crit_rate'    : 1/20.5,
    'damage'       : 1/20.5,
    'allstat_9'    : 1/13.66,
    'wattplvl_0'   : 1/20.5,    
    'mattplvl_0'   : 1/20.5,
    'ied_35'       : 1/20.5,
    'ied_40'       : 1/20.5,
    'boss_35'      : 1/20.5,
    'boss_40'      : 1/20.5,
}

weapon_unique = {
    'str_9'        : 1/9,
    'dex_9'        : 1/9,
    'int_9'        : 1/9,
    'luk_9'        : 1/9,
    'watt_9'       : 1/15,
    'matt_9'       : 1/15,
    'crit_rate'    : 1/11.25,
    'damage'       : 1/15,
    'allstat_6'    : 1/11.25,
    'ied_30'       : 1/15,
    'boss_30'      : 1/9,
}

# Secondary Legendary Cash Cube
secondary_leg = {
    'str_12'       : 1/11.75,
    'dex_12'       : 1/11.75,
    'int_12'       : 1/11.75,
    'luk_12'       : 1/11.75,
    'watt_12'      : 1/23.5,
    'matt_12'      : 1/23.5,
    'crit_rate'    : 1/23.5,
    'damage'       : 1/23.5,
    'allstat_9'    : 1/15.66,
    'wattplvl_0'   : 1/23.5,    
    'mattplvl_0'   : 1/23.5,
    'ied_35'       : 1/23.5,
    'ied_40'       : 1/23.5,
    'ignore_20'    : 1/15.66,
    'ignore_40'    : 1/15.66,
    'boss_35'      : 1/23.5,
    'boss_40'      : 1/23.5,
}

secondary_unique = {
    'str_9'        : 1/10.6,
    'dex_9'        : 1/10.6,
    'int_9'        : 1/10.6,
    'luk_9'        : 1/10.6,
    'watt_9'       : 1/17.66,
    'matt_9'       : 1/17.66,
    'crit_rate'    : 1/13.25,
    'damage'       : 1/17.66,
    'allstat_6'    : 1/13.25,
    'ied_30'       : 1/17.66,
    'ignore_20'    : 1/13.25,
    'ignore_40'    : 1/13.25,
    'boss_30'      : 1/10.6,
}

# Emblem Legendary Cash Cube
emblem_leg = {
    'str_12'       : 1/8.75,
    'dex_12'       : 1/8.75,
    'int_12'       : 1/8.75,
    'luk_12'       : 1/8.75,
    'watt_12'      : 1/17.5,
    'matt_12'      : 1/17.5,
    'crit_rate'    : 1/17.5,
    'damage'       : 1/17.5,
    'allstat_9'    : 1/11.66,
    'wattplvl_0'   : 1/17.5,    
    'mattplvl_0'   : 1/17.5,
    'ied_35'       : 1/17.5,
    'ied_40'       : 1/17.5,
}

emblem_unique = {
    'str_9'        : 1/8,
    'dex_9'        : 1/8,
    'int_9'        : 1/8,
    'luk_9'        : 1/8,
    'watt_9'       : 1/13.33,
    'matt_9'       : 1/13.33,
    'crit_rate'    : 1/10,
    'damage'       : 1/13.33,
    'allstat_6'    : 1/10,
    'ied_30'       : 1/13.33,
}
###############################################################################
###############################################################################
# Bonus Potentials
# Hat Legendary Bonus Cash Cube
hat_b_leg = {
    'fstr_18'       : 1/22.66,
    'fdex_18'       : 1/22.66,
    'fint_18'       : 1/22.66,
    'fluk_18'       : 1/22.66,    
    'fwatt_14'       : 1/34,
    'fmatt_14'       : 1/34,
    'hp'            : 1/22.66,
    'mp'            : 1/22.66,
    'str_7'         : 1/34,
    'dex_7'         : 1/34,
    'int_7'         : 1/34,
    'luk_7'         : 1/34,
    'hp_10'         : 1/22.66,
    'mp_10'         : 1/22.66,
    'def_10'        : 1/22.66,
    'critd_1'       : 1/34,
    'allstat_5'     : 1/34,
    'dexplvl_2'     : 1/34,
    'intplvl_2'     : 1/34,
    'strplvl_2'     : 1/34,
    'lukplvl_2'     : 1/34,
    'cdskip_1'      : 1/22.66,
    'meso'          : 1/22.66,
    'drop'          : 1/22.66,
    'recov'         : 1/22.66,
}

hat_b_unique = {
    'fstr_16'       : 1/18.66,
    'fdex_16'       : 1/18.66,
    'fint_16'       : 1/18.66,
    'fluk_16'       : 1/18.66,    
    'fwatt_12'       : 1/28,
    'fmatt_12'       : 1/28,
    'hp'            : 1/18.66,
    'mp'            : 1/18.66,
    'str_5'         : 1/28,
    'dex_5'         : 1/28,
    'int_5'         : 1/28,
    'luk_5'         : 1/28,
    'hp_7'          : 1/18.66,
    'mp_7'          : 1/18.66,
    'def_7'         : 1/18.66,
    'allstat_4'     : 1/28,
#    'eleres'        : 1/56,
    'recov'         : 1/18.66,
    'strplvl_1'     : 1/28,
    'dexplvl_1'     : 1/28,
    'intplvl_1'     : 1/28,
    'lukplvl_1'     : 1/28,
}

# Top/Overall/Bottom/Shoes/Cape/Belt/Shoulder Legendary Top Cash Cube
top_b_leg = {
    'fstr_18'       : 1/21.33,
    'fdex_18'       : 1/21.33,
    'fint_18'       : 1/21.33,
    'fluk_18'       : 1/21.33,    
    'fwatt_14'       : 1/32,
    'fmatt_14'       : 1/32,
    'hp'            : 1/21.33,
    'mp'            : 1/21.33,
    'str_7'         : 1/32,
    'dex_7'         : 1/32,
    'int_7'         : 1/32,
    'luk_7'         : 1/32,
    'hp_10'         : 1/21.33,
    'mp_10'         : 1/21.33,
    'def_10'        : 1/21.33,
    'critd_1'       : 1/32,
    'allstat_5'     : 1/32,
#    'eleres'        : 1/64,
    'strplvl_2'     : 1/32,
    'dexplvl_2'     : 1/32,
    'intplvl_2'     : 1/32,
    'lukplvl_2'     : 1/32,
    'meso'          : 1/21.33,
    'drop'          : 1/21.33,
    'recov'         : 1/21.33,
}

top_b_unique = {
    'fstr_16'       : 1/18.66,
    'fdex_16'       : 1/18.66,
    'fint_16'       : 1/18.66,
    'fluk_16'       : 1/18.66,    
    'fwatt_12'       : 1/28,
    'fmatt_12'       : 1/28,
    'hp'            : 1/18.66,
    'mp'            : 1/18.66,
    'str_5'         : 1/28,
    'dex_5'         : 1/28,
    'int_5'         : 1/28,
    'luk_5'         : 1/28,
    'hp_7'          : 1/18.66,
    'mp_7'          : 1/18.66,
    'def_7'         : 1/18.66,
    'allstat_4'     : 1/28,
#    'eleres'        : 1/56,
    'recov'         : 1/18.66,
    'strplvl_1'     : 1/28,
    'dexplvl_1'     : 1/28,
    'intplvl_1'     : 1/28,
    'lukplvl_1'     : 1/28,
}



# Gloves Legendary Bonus Cash Cube
glove_b_leg = {
    'fstr_18'       : 1/22,
    'fdex_18'       : 1/22,
    'fint_18'       : 1/22,
    'fluk_18'       : 1/22,
    'fwatt_14'       : 1/33,
    'fmatt_14'       : 1/33,
    'hp'            : 1/22,
    'mp'            : 1/22,
    'str_7'         : 1/33,
    'dex_7'         : 1/33,
    'int_7'         : 1/33,
    'luk_7'         : 1/33,
    'hp_10'         : 1/22,
    'mp_10'         : 1/22,
    'def_10'        : 1/22,
    'critd_3'       : 1/33,
    'critd_1'       : 1/33,
    'allstat_5'     : 1/32,
#    'eleres'        : 1/66,
    'strplvl_2'     : 1/33,
    'dexplvl_2'     : 1/33,
    'intplvl_2'     : 1/33,
    'lukplvl_2'     : 1/33,
    'meso'          : 1/22,
    'drop'          : 1/22,
    'recov'         : 1/22,
}   

glove_b_unique = {
    'fstr_16'       : 1/18.66,
    'fdex_16'       : 1/18.66,
    'fint_16'       : 1/18.66,
    'fluk_16'       : 1/18.66,    
    'fwatt_12'       : 1/28,
    'fmatt_12'       : 1/28,
    'hp'            : 1/18.66,
    'mp'            : 1/18.66,
    'str_5'         : 1/28,
    'dex_5'         : 1/28,
    'int_5'         : 1/28,
    'luk_5'         : 1/28,
    'hp_7'          : 1/18.66,
    'mp_7'          : 1/18.66,
    'def_7'         : 1/18.66,
    'allstat_4'     : 1/28,
#    'eleres'        : 1/56,
    'recov'         : 1/18.66,
    'strplvl_1'     : 1/28,
    'dexplvl_1'     : 1/28,
    'intplvl_1'     : 1/28,
    'lukplvl_1'     : 1/28,
}

# Heart/Badge Legendary Bonus Cash Cube
heart_badge_b_leg = {
    'fstr_18'       : 1/20.66,
    'fdex_18'       : 1/20.66,
    'fint_18'       : 1/20.66,
    'fluk_18'       : 1/20.66,    
    'fwatt_14'       : 1/31,
    'fmatt_14'       : 1/31,
    'hp'            : 1/20.66,
    'mp'            : 1/20.66,
    'str_7'         : 1/31,
    'dex_7'         : 1/31,
    'int_7'         : 1/31,
    'luk_7'         : 1/31,
    'hp_10'         : 1/20.66,
    'mp_10'         : 1/20.66,
    'def_10'        : 1/20.66,
    'allstat_5'     : 1/31,
#    'eleres'        : 1/62,
    'strplvl_2'     : 1/31,
    'dexplvl_2'     : 1/31,
    'intplvl_2'     : 1/31,
    'lukplvl_2'     : 1/31,
    'meso'          : 1/20.66,
    'drop'          : 1/20.66,
    'recov'         : 1/20.66,
}

heart_badge_b_unique = {
    'fstr_16'       : 1/18.66,
    'fdex_16'       : 1/18.66,
    'fint_16'       : 1/18.66,
    'fluk_16'       : 1/18.66,    
    'fwatt_12'       : 1/28,
    'fmatt_12'       : 1/28,
    'hp'            : 1/18.66,
    'mp'            : 1/18.66,
    'str_5'         : 1/28,
    'dex_5'         : 1/28,
    'int_5'         : 1/28,
    'luk_5'         : 1/28,
    'hp_7'          : 1/18.66,
    'mp_7'          : 1/18.66,
    'def_7'         : 1/18.66,
    'allstat_4'     : 1/28,
#    'eleres'        : 1/56,
    'recov'         : 1/18.66,
    'strplvl_1'     : 1/28,
    'dexplvl_1'     : 1/28,
    'intplvl_1'     : 1/28,
    'lukplvl_1'     : 1/28,
}

# Accessory Legendary Bonus Cash Cube
accessory_b_leg = {
    'fstr_18'       : 1/21.66,
    'fdex_18'       : 1/21.66,
    'fint_18'       : 1/21.66,
    'fluk_18'       : 1/21.66,    
    'fwatt_14'       : 1/32.5,
    'fmatt_14'       : 1/32.5,
    'hp'            : 1/21.66,
    'mp'            : 1/21.66,
    'str_7'         : 1/32.5,
    'dex_7'         : 1/32.5,
    'int_7'         : 1/32.5,
    'luk_7'         : 1/32.5,
    'hp_10'         : 1/21.66,
    'mp_10'         : 1/21.66,
    'def_10'        : 1/21.66,
    'allstat_5'     : 1/32.5,
#    'eleres'        : 1/65,
    'mpred'         : 1/21.66,
    'strplvl_2'     : 1/32.5,
    'dexplvl_2'     : 1/32.5,
    'intplvl_2'     : 1/32.5,
    'lukplvl_2'     : 1/32.5,
    'meso'          : 1/21.66,
    'drop'          : 1/21.66,
    'recov'         : 1/21.66,
}
accessory_b_unique = {
    'fstr_16'       : 1/18.66,
    'fdex_16'       : 1/18.66,
    'fint_16'       : 1/18.66,
    'fluk_16'       : 1/18.66,    
    'fwatt_12'       : 1/28,
    'fmatt_12'       : 1/28,
    'hp'            : 1/18.66,
    'mp'            : 1/18.66,
    'str_5'         : 1/28,
    'dex_5'         : 1/28,
    'int_5'         : 1/28,
    'luk_5'         : 1/28,
    'hp_7'          : 1/18.66,
    'mp_7'          : 1/18.66,
    'def_7'         : 1/18.66,
    'allstat_4'     : 1/28,
#    'eleres'        : 1/56,
    'recov'         : 1/18.66,
    'strplvl_1'     : 1/28,
    'dexplvl_1'     : 1/28,
    'intplvl_1'     : 1/28,
    'lukplvl_1'     : 1/28,
}

# Weapon Legendary Bonus Cash Cube
weapon_b_leg = {
    'str_12'        : 1/13.33,
    'dex_12'        : 1/13.33,
    'int_12'        : 1/13.33,
    'luk_12'        : 1/13.33,
    'watt_12'       : 1/20,
    'matt_12'       : 1/20,
    'damage'        : 1/40,
    'crit_rate'     : 1/20,
    'hp'            : 1/13.33,
    'mp'            : 1/13.33,
    'allstat_9'     : 1/20,
    'boss_18'       : 1/40,
    'ied_5'         : 1/40,
    'strplvl_2'     : 1/20,
    'dexplvl_2'     : 1/20,
    'intplvl_2'     : 1/20,
    'lukplvl_2'     : 1/20,
    'wattplvl_2'    : 1/40,
    'mattplvl_2'    : 1/40,
}

weapon_b_unique = {
    'str_9'        : 1/14.33,
    'dex_9'        : 1/14.33,
    'int_9'        : 1/14.33,
    'luk_9'        : 1/14.33,
    'watt_9'       : 1/21.5,
    'matt_9'       : 1/21.5,
    'damage'        : 1/43,
    'crit_rate'     : 1/21.5,
    'hp'            : 1/14.33,
    'mp'            : 1/14.33,
    'allstat_6'     : 1/21.5,
    'boss_12'       : 1/43,
    'ied_4'         : 1/43,
    'hprecov'       : 1/14.33,
    'mprecov'       : 1/14.33,
    'strplvl_1'     : 1/21.5,
    'dexplvl_1'     : 1/21.5,
    'intplvl_1'     : 1/21.5,
    'lukplvl_1'     : 1/21.5,
}

# Emblem Legendary Bonus Cash Cube
emblem_b_leg = {
    'str_12'        : 1/13,
    'dex_12'        : 1/13,
    'int_12'        : 1/13,
    'luk_12'        : 1/13,
    'watt_12'       : 1/19.5,
    'matt_12'       : 1/19.5,
    'damage'        : 1/39,
    'crit_rate'     : 1/19.5,
    'hp'            : 1/13,
    'mp'            : 1/13,
    'allstat_9'     : 1/19.5,
    'ied_5'         : 1/39,
    'strplvl_2'     : 1/19.5,
    'dexplvl_2'     : 1/19.5,
    'intplvl_2'     : 1/19.5,
    'lukplvl_2'     : 1/19.5,
    'wattplvl_2'    : 1/39,
    'mattplvl_2'    : 1/39,
}

emblem_b_unique = {
    'str_9'        : 1/14,
    'dex_9'        : 1/14,
    'int_9'        : 1/14,
    'luk_9'        : 1/14,
    'watt_9'       : 1/21,
    'matt_9'       : 1/21,
    'damage'        : 1/42,
    'crit_rate'     : 1/21,
    'hp'            : 1/14,
    'mp'            : 1/14,
    'allstat_6'     : 1/21,
    'ied_4'         : 1/21,
    'hprecov'       : 1/14,
    'mprecov'       : 1/14,
    'strplvl_1'     : 1/21,
    'dexplvl_1'     : 1/21,
    'intplvl_1'     : 1/21,
    'lukplvl_1'     : 1/21,
}

# Secondary Legendary Bonus Cash Cube
secondary_b_leg = {
    'str_12'        : 1/14,
    'dex_12'        : 1/14,
    'int_12'        : 1/14,
    'luk_12'        : 1/14,
    'watt_12'       : 1/21,
    'matt_12'       : 1/21,
    'damage'        : 1/42,
    'crit_rate'     : 1/21,
    'hp'            : 1/14,
    'mp'            : 1/14,
    'allstat_9'     : 1/21,
    'critd_1'       : 1/21,
    'boss_18'       : 1/42,
    'ied_5'         : 1/42,
    'strplvl_2'     : 1/21,
    'dexplvl_2'     : 1/21,
    'intplvl_2'     : 1/21,
    'lukplvl_2'     : 1/21,
    'wattplvl_2'    : 1/42,
    'mattplvl_2'    : 1/42,
}

secondary_b_unique = {
    'str_9'        : 1/14.33,
    'dex_9'        : 1/14.33,
    'int_9'        : 1/14.33,
    'luk_9'        : 1/14.33,
    'watt_9'       : 1/21.5,
    'matt_9'       : 1/21.5,
    'damage'        : 1/43,
    'crit_rate'     : 1/21.5,
    'hp'            : 1/14.33,
    'mp'            : 1/14.33,
    'allstat_6'     : 1/21.5,   
    'boss_12'       : 1/43,
    'ied_4'         : 1/43,
    'hprecov'       : 1/14.33,
    'mprecov'       : 1/14.33,
    'strplvl_1'     : 1/21.5,
    'dexplvl_1'     : 1/21.5,
    'intplvl_1'     : 1/21.5,
    'lukplvl_1'     : 1/21.5,
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
        'boss', 'ied', 'drop', 'ignore', 'invchance',
    ]
    one_appearance_max = ['skill', 'invtime', 'sharpeyes',
                          'bless', 'haste', 'hyperbody']

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


if   selected_cube == 'red':       roll_function = red_cube_roll
elif selected_cube == 'black':     roll_function = black_cube_roll
elif selected_cube == 'bonus':     roll_function = bonus_cube_roll
elif selected_cube == 'equality':  roll_function = equality_cube_roll
elif selected_cube == 'violet':    roll_function = violet_cube_roll
else:                              roll_function = red_cube_roll

def count_this_stat(roll, stat):
    good_lines = []
#########################################
    if selected_cube == 'bonus':
        if stat in ['str','dex','int','luk']:
            for line in roll:
                if line.startswith(stat+'_') or line.startswith('all'):
                    good_lines += [float(line.split('_')[-1])]
                elif line.startswith('f'+stat):
                    good_lines += [float(line.split('_')[-1])/Percent_to_flat]
                elif line.startswith(stat+'plvl'):
                    good_lines += [float(line.split('_')[-1])*Level/Percent_to_flat/9]
                elif stat != 'int' and line.startswith('fwatt'):
                    good_lines += [float(line.split('_')[-1])/Att_to_flat]
                elif stat == 'int' and line.startswith('fmatt'):
                    good_lines += [float(line.split('_')[-1])/Att_to_flat]
                elif stat != 'int' and line.startswith('wattplvl'):
                    good_lines += [float(line.split('_')[-1])*Level*Att_to_flat/9/Percent_to_flat]
                elif stat == 'int' and line.startswith('mattplvl'):
                    good_lines += [float(line.split('_')[-1])*Level*Att_to_flat/9/Percent_to_flat]
        else:
            for line in roll:
                if line.startswith(stat+'_'):
                    good_lines += [float(line.split('_')[-1])]
#########################################
    else:
        if stat in ['str','dex','int','luk']:  # because allstat is a wildcard
            for line in roll:
                if line.startswith(stat) or line.startswith('all'):
                    good_lines += [float(line.split('_')[-1])]

        else:
            for line in roll:
                if line.startswith(stat):
                    good_lines += [float(line.split('_')[-1])]
#########################################
    good_lines.sort()
    return sum(good_lines[-3:])  # pick highest 3 for violet cubes



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
    print(f'Number of Trials    : {num_trials}')
    print('---------------------------------------------------------')
    print(f'Average Cube Amount : {sum(counts)/num_trials}')
    print(f'50 percentile       : {counts[round(num_trials/(100/50))]}')
    print(f'75 percentile       : {counts[round(num_trials/(100/75))]}')
    print(f'90 percentile       : {counts[round(num_trials/(100/90))]}')
    print(f'95 percentile       : {counts[round(num_trials/(100/99))]}')
    print('---------------------------------------------------------')

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
