from opentrons import protocol_api
from opentrons import types
metadata = {"robotType":"OT-2",'apiLevel': '2.13'}
import json
import math
import requests
import time
# ---------------------------------------------------------------------------- #
#                        Define a new transfer function                        #
# ---------------------------------------------------------------------------- #
def My_transfer(protocol,right_pipette,max_height,
                source_basic,dest_basic,
                source_mix_config,dest_mix_config,
                source_delay_config,dest_delay_config,
                source_touch_tip_config,dest_touch_tip_config,
                source_air_gap_config,dest_blow_out_config):
    right_pipette.move_to(source_basic["plate"][source_basic["well"]].bottom(max_height))
    if source_mix_config["mix_enable"] and source_mix_config["mix_volume"] is not None and source_mix_config["mix_times"] is not None and source_mix_config["mix_height"] is not None: 
        right_pipette.mix(source_mix_config["mix_times"],
                          volume   = source_mix_config["mix_volume"],
                          location = source_basic["plate"][source_basic["well"]].bottom(source_mix_config["mix_height"]),
                          rate     = source_mix_config["mix_rate"])
    right_pipette.aspirate(source_basic["volume"],source_basic["plate"][source_basic["well"]].bottom(source_basic["height"]),rate=source_basic["rate"])
    if source_delay_config["delay_enable"] and source_delay_config["delay_times"] is not None: 
        protocol.delay(seconds=source_delay_config["delay_times"])
    if source_touch_tip_config["touch_tip_enable"] and source_touch_tip_config["touch_tip_offset"] is not None: 
        right_pipette.touch_tip(source_basic["plate"][source_basic["well"]],speed=10,v_offset=source_touch_tip_config["touch_tip_offset"])
    if source_air_gap_config["air_gap_enable"] and source_air_gap_config["air_gap_volume"] is not None: 
        right_pipette.air_gap(source_air_gap_config["air_gap_volume"])
    right_pipette.move_to(dest_basic["plate"][dest_basic["well"]].bottom(max_height))
    right_pipette.dispense(dest_basic["volume"],dest_basic["plate"][dest_basic["well"]].bottom(dest_basic["height"]),rate=dest_basic["rate"])
    if dest_mix_config["mix_enable"] and dest_mix_config["mix_volume"] is not None and dest_mix_config["mix_times"]is not None and dest_mix_config["mix_height"]is not None: 
        right_pipette.mix(dest_mix_config["mix_times"],
                          volume   = dest_mix_config["mix_volume"],
                          location = dest_basic["plate"][dest_basic["well"]].bottom(dest_mix_config["mix_height"]),
                          rate     = dest_mix_config["mix_rate"])
    if dest_delay_config["delay_enable"] and dest_delay_config["delay_times"] is not None: 
        protocol.delay(seconds=dest_delay_config["delay_times"])
    if dest_blow_out_config["blow_out_enable"] and dest_blow_out_config["blow_out_height"]is not None: 
        right_pipette.blow_out(dest_basic["plate"][dest_basic["well"]].bottom(dest_blow_out_config["blow_out_height"]))
    if dest_touch_tip_config["touch_tip_enable"] and dest_touch_tip_config["touch_tip_offset"] is not None: 
        right_pipette.touch_tip(dest_basic["plate"][dest_basic["well"]],speed=10,v_offset=dest_touch_tip_config["touch_tip_offset"])
    right_pipette.move_to(dest_basic["plate"][dest_basic["well"]].bottom(max_height))
    #单通道P300移液器移液整合函数
def My_transfer_Multi(protocol,left_pipette,max_height,
                      
                source_basic,dest_basic,
                source_mix_config,dest_mix_config,
                source_delay_config,dest_delay_config,
                source_touch_tip_config,dest_touch_tip_config,
                source_air_gap_config,dest_blow_out_config):
    left_pipette.move_to(source_basic["plate"][source_basic["well"]].bottom(max_height))
    if source_mix_config["mix_enable"] and source_mix_config["mix_volume"] is not None and source_mix_config["mix_times"] is not None and source_mix_config["mix_height"] is not None: 
        left_pipette.mix(source_mix_config["mix_times"],
                         volume   = source_mix_config["mix_volume"],
                         location = source_basic["plate"][source_basic["well"]].bottom().move(types.Point(x=source_basic["x"],y=source_basic["y"],z=source_mix_config["mix_height"])),
                         rate     = source_mix_config["mix_rate"])
    left_pipette.aspirate(source_basic["volume"],source_basic["plate"][source_basic["well"]].bottom().move(types.Point(x=source_basic["x"],y=source_basic["y"],z=source_basic["height"])),
                          rate=source_basic["rate"])
    if source_delay_config["delay_enable"] and source_delay_config["delay_times"] is not None: 
        protocol.delay(seconds=source_delay_config["delay_times"])
    if source_touch_tip_config["touch_tip_enable"] and source_touch_tip_config["touch_tip_offset"] is not None: 
        left_pipette.touch_tip(source_basic["plate"][source_basic["well"]],speed=10,v_offset=source_touch_tip_config["touch_tip_offset"])
    if source_air_gap_config["air_gap_enable"] and source_air_gap_config["air_gap_volume"] is not None: 
        left_pipette.air_gap(source_air_gap_config["air_gap_volume"])
    left_pipette.move_to(dest_basic["plate"][dest_basic["well"]].bottom(max_height))
    left_pipette.dispense(dest_basic["volume"],dest_basic["plate"][dest_basic["well"]].bottom().move(types.Point(x=dest_basic["x"],y=dest_basic["y"],z=dest_basic["height"])),
                          rate=dest_basic["rate"])
    if dest_mix_config["mix_enable"] and dest_mix_config["mix_volume"] is not None and dest_mix_config["mix_times"]is not None and dest_mix_config["mix_height"]is not None: 
        left_pipette.mix(dest_mix_config["mix_times"],
                         volume   = dest_mix_config["mix_volume"],
                         location = dest_basic["plate"][dest_basic["well"]].bottom().move(types.Point(x=dest_basic["x"],y=dest_basic["y"],z=dest_mix_config["mix_height"])),
                         rate     = dest_mix_config["mix_rate"])
    if dest_delay_config["delay_enable"] and dest_delay_config["delay_times"] is not None: 
        protocol.delay(seconds=dest_delay_config["delay_times"])
    if dest_blow_out_config["blow_out_enable"] and dest_blow_out_config["blow_out_height"]is not None: 
        left_pipette.blow_out(dest_basic["plate"][dest_basic["well"]].bottom(dest_blow_out_config["blow_out_height"]))
    if dest_touch_tip_config["touch_tip_enable"] and dest_touch_tip_config["touch_tip_offset"] is not None: 
        left_pipette.touch_tip(dest_basic["plate"][dest_basic["well"]],
                               speed    = 10,
                               v_offset = dest_touch_tip_config["touch_tip_offset"])
    left_pipette.move_to(dest_basic["plate"][dest_basic["well"]].bottom(max_height))
    #多通道P300移液器移液函数


def move(protocol,url,data):
    Done=False
    Error=0
    if not protocol.is_simulating():
        while not Done:
            if not protocol.is_simulating():
                data1 = f'{data}'
                response = requests.post(url,data1)
                if response.text=='END':
                    Done=True
                    protocol.set_rail_lights(False)
                time.sleep(1)
                Error+=1
                if Error==10:
                    protocol.pause(f'Connect Error:{str(data1)}')
                    Error=0
    protocol.set_rail_lights(True)
    Done=False
    

def DropTip(protocol,url,tip_number,tiprack1,leftpipette):
    leftpipette.drop_tip()
    tip_number=tip_number+1 
    if tip_number%12==0:
        if (8+2*int(tip_number/12))!=20:
            move(protocol,url,8+2*int(tip_number/12))
            move(protocol,url,9+2*int(tip_number/12))
        else:
            move(protocol,url,8+2*int(tip_number/12))
            tip_number=0
    return tip_number
   
def SpeedSet(protocol):
    protocol.max_speeds['x'] = 80
    protocol.max_speeds['y'] = 80
    protocol.max_speeds['a'] = 20
   
def run(protocol:protocol_api.ProtocolContext): 
    # ------------------------------------------------------------------------------------------------ #
    #                                       Protocol Basic Config                                      #
    # ------------------------------------------------------------------------------------------------ #
    time_config={
    "time_nurture" : 1,
    "time_magnetic": 1,
    "time_crack"   : 1,
    "time_lysc"    : 1,
    "time_trypsin" : 1,
    "time_TFA"     : 1
    }
    
    speed_config={
         "Nurture":1200,
         "Lysis":1200,
         "Lysc":1200,
         "Trypsin":1200,
         "TFA":1000
    }
    
    url = 'http://169.254.83.118:80/MoveMode'  
    url_mail='http://169.254.83.118:80/Mail'
    
    liquid_config={
        "Sample":,
        "PBS":,
        "TFA":,
        "Lysis-EV":,
        "Lysis-Pro":,
        "TEAB":,

        "Beads_EV":,
        "Beads_Pro":,
        "Trypsin":,
        "Trypsin_Pro":,
        "Lysc":,
        "Water":
    }
    Sample_Select=[1]
    Initial_Volume={
        "PBS":liquid_config['PBS']*2*len(Sample_Select)*1.5,
        "Lysis-EV":liquid_config['Lysis-EV']*1.5*len(Sample_Select),
        "Lysis-Pro":liquid_config["Lysis-Pro"]*1.5*len(Sample_Select),
        "TEAB":liquid_config['TEAB']*1.5*len(Sample_Select)*2,
        "TFA":liquid_config['TFA']*1.5*len(Sample_Select)*2,
        "Water":liquid_config['Water']*1.5,
        "Water":liquid_config['Water']*1.5,
        "Water":liquid_config['Water']*1.5,
        "Water":liquid_config['Water']*1.5,


        "Beads_EV":liquid_config['Beads_EV']*1.5,     
        "Beads_Pro":liquid_config['Beads_Pro']*1.5,
        "Lysc":liquid_config['Lysc']*1.5,
        "Trypsin":liquid_config['Trypsin']*1.5,
        "Trypsin_Pro":liquid_config['Trypsin_Pro']*1.5,    
    }
    
    #SpeedSet(protocol=protocol)
    protocol.set_rail_lights(on=True)
    # ------------------------------------------------------------------------------------------------ #
    #                                           Load Labware                                           #
    # ------------------------------------------------------------------------------------------------ #
    #ProteinPlate    = protocol.load_labware('nest_96_wellplate_2ml_deep', '4')
    temp_mod        = protocol.load_module(module_name='temperature module gen2',location='1')
    tiprack1        = protocol.load_labware("opentrons_96_tiprack_300ul",'7')
    tiprack1.set_offset(x=-1.40, y=0.00, z=19.50)
    WastePlate      = protocol.load_labware('nest_96_wellplate_2ml_deep',  '2')
    CollectionPlate_EV = protocol.load_labware('nest_96_wellplate_2ml_deep','4')
    CollectionPlate_Pro = protocol.load_labware('nest_96_wellplate_2ml_deep',  '8')
    MagnicPlate     = protocol.load_labware('nest_96_wellplate_2ml_deep',  '10')
    WaterWall       = protocol.load_labware("nest_96_wellplate_2ml_deep",'11')
    EnzymePlate     = temp_mod.load_labware("opentrons_96_aluminumblock_nest_wellplate_100ul")
    tip_number=0
    

    normal_plate_config={
        "air_gap":20,
        "delay_time":3,
        "touch_tip_offset":-8,
        "blow_out_height":30,
    }

    EnzymePlate_config={
        "air_gap":20,
        "delay_time":3,
        "touch_tip_offset":-8,
    }

    Magnic_plate_config={
        "air_gap":20,
        "delay_time":3,
        "touch_tip_offset":12,
        "blow_out_height":50,
    }

    collection_plate_config={
        "air_gap":20,
        "delay_time":3,
        "touch_tip_offset":-8,
        "blow_out_height":30,
    }
 
    
    hs_mod        = protocol.load_module(module_name="heaterShakerModuleV1",location="6")
    right_pipette = protocol.load_instrument(
        instrument_name = 'p300_single_gen2',
        mount           = 'right',
        tip_racks       = [tiprack1])
    left_pipette = protocol.load_instrument(
        instrument_name = 'p300_multi_gen2',
        mount           = 'left',
        tip_racks       = [tiprack1])
    # ------------------------------------------------------------------------------------------------ #
    #                                    Config Liquid Transfer Para                                   #
    # ------------------------------------------------------------------------------------------------ #
    source_mix_config = {"mix_enable":False,"mix_volume":100, "mix_times":3,"mix_height":30,"mix_rate":0.4}
    dest_mix_config   = {"mix_enable":False,"mix_volume":100,"mix_times":3,"mix_height":30,"mix_rate":0.4}
    
    source_delay_config = {"delay_enable":False,"delay_times":3}
    dest_delay_config   = {"delay_enable":False,"delay_times":3}

    source_touch_tip_config = {"touch_tip_enable":False,"touch_tip_offset":12}
    dest_touch_tip_config   = {"touch_tip_enable":False,"touch_tip_offset":12}
    
    source_air_gap_config = {"air_gap_enable":False,"air_gap_volume":50}
    dest_blow_out_config  = {"blow_out_enable":False,"blow_out_height":50}

    ProteinPlate_Heat = hs_mod.load_labware('nest_96_wellplate_2ml_deep')
    
    hs_mod.open_labware_latch()
    protocol.pause('Place ProteinPlate,Load EV beads')
    
    hs_mod.close_labware_latch()

    # ------------------------------------------------------------------------------------------------ #
    #                                           Add EV-Beads                                           #
    # ------------------------------------------------------------------------------------------------ #
    
    for i in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        source_basic            = {"plate":EnzymePlate,"well":f'A{1+i}',"x":0,"y":0,"height":0.1,"volume":liquid_config["Beads_EV"],"rate":0.2}
        dest_basic              = {"plate":ProteinPlate_Heat,"well":f'A{Sample_Select[i]}',"x":0,"y":0,"height":10,"volume":liquid_config["Beads_EV"]+40,"rate":0.2}
        source_air_gap_config   = {"air_gap_enable":False,"air_gap_volume":EnzymePlate_config["air_gap"]}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":EnzymePlate_config["touch_tip_offset"]}
        source_delay_config     = {"delay_enable":True,"delay_times":EnzymePlate_config["delay_time"]}
        source_mix_config = {"mix_enable":True,"mix_volume":20, "mix_times":8,"mix_height":1,"mix_rate":3}
        
        dest_mix_config   = {"mix_enable":True,"mix_volume":100,"mix_times":3,"mix_height":5,"mix_rate":2.5}
        dest_touch_tip_config   = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        dest_blow_out_config    = {"blow_out_enable":True,"blow_out_height":normal_plate_config["blow_out_height"]}
        dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}
        
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=50,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    # ------------------------------------------------------------------------------------------------ #
    #                                          Nature EV-Beads                                         #
    # ------------------------------------------------------------------------------------------------ #
    move(protocol,url,2)#add lid

    hs_mod.set_and_wait_for_temperature(43)
    hs_mod.set_and_wait_for_shake_speed(speed_config["Nurture"])
    protocol.delay(minutes=time_config["time_nurture"])
    protocol.comment('Nuture:1400')
    
    hs_mod.deactivate_shaker()
    hs_mod.deactivate_heater()
    
    protocol.comment('End Nurture')
    move(protocol,url,3)#remove lid
    
    hs_mod.open_labware_latch()
    move(protocol,url,4)#move plate
    # ------------------------------------------------------------------------------------------------ #
    #                                          Magnetic Beads                                          #
    # ------------------------------------------------------------------------------------------------ #
    
    protocol.delay(minutes=time_config["time_magnetic"])
    hs_mod.close_labware_latch()
    protocol.comment("End Magnetic Separate")
    protocol.home()

    # ------------------------------------------------------------------------------------------------ #
    #                                          Separate Beads                                          #
    # ------------------------------------------------------------------------------------------------ #
    protocol.max_speeds['a']=20
    for j in range(0,len(Sample_Select)): 
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        for i in range(0,((liquid_config["Sample"]+liquid_config["Beads_EV"])//200)+2): 
                source_basic = {"plate":MagnicPlate,"well":f'A{Sample_Select[j]}',
                                "x": (int(Sample_Select[j]%2==0)*2-1)*1.5,#There need to test
                                "y": 0,                                    "height": 19.5, "volume": 200, "rate": 0.1}#
                dest_basic   = {"plate":MagnicPlate,"well":f'A{Sample_Select[j]+1}',
                                "x": 0,
                                "y": 0, "height": 25, "volume": 240, "rate": 1}
                
                source_air_gap_config   = {"air_gap_enable":False, "air_gap_volume":Magnic_plate_config["air_gap"]}
                source_delay_config     = {"delay_enable":True,    "delay_times":Magnic_plate_config['delay_time']}
                source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
                source_mix_config       = {"mix_enable":False,"mix_volume":20, "mix_times":5,"mix_height":0.1,"mix_rate":1.5}

                dest_mix_config       = {"mix_enable":True,"mix_volume":200, "mix_times":2,"mix_height":19.5,"mix_rate":1}
                dest_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
                dest_delay_config     = {"delay_enable":True,"delay_times":Magnic_plate_config["delay_time"]}
                dest_blow_out_config  = {"blow_out_enable":True,"blow_out_height":Magnic_plate_config["blow_out_height"]}
                My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                        source_basic            = source_basic,            dest_basic            = dest_basic,
                        source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                        source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                        source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                        source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    
    
    # ------------------------------------------------------------------------------------------------ #
    #                                          PBS Wash Beads                                          #
    # ------------------------------------------------------------------------------------------------ #
    for i in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        source_basic            = {"plate":WaterWall,"well":f'A{1}',
                                   "x":0,
                                   "y":0,
                                   "height":Surface(Initial_Volume["PBS"]-i*liquid_config['PBS'],liquid_config['PBS']),"volume":liquid_config["PBS"],"rate":1}
        dest_basic              = {"plate":MagnicPlate,"well":f'A{Sample_Select[i]}',"x":(int(Sample_Select[i]%2==0)*2-1)*1.5,"y":0,"height":19.5,"volume":liquid_config["PBS"]+20,"rate":0.1}#there need to test
        source_air_gap_config   = {"air_gap_enable":False,"air_gap_volume":normal_plate_config["air_gap"]}
        source_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}
        source_mix_config       = {"mix_enable":False,"mix_volume":200, "mix_times":3,"mix_height":1,"mix_rate":0.1}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}

        dest_mix_config       = {"mix_enable":True,"mix_volume":liquid_config['PBS'], "mix_times":6,"mix_height":19.5,"mix_rate":0.1}
        dest_touch_tip_config = {"touch_tip_enable":False,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
        dest_delay_config     = {"delay_enable":False,"delay_times":Magnic_plate_config["delay_time"]}
        dest_blow_out_config  = {"blow_out_enable":False,"blow_out_height":Magnic_plate_config["blow_out_height"]}
        
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        
        source_basic            = {"plate":MagnicPlate,"well":f'A{Sample_Select[i]}',
                                   "x":(int(Sample_Select[i]%2==0)*2-1)*1.5,
                                   "y":0,"height":19.5,
                                   "volume":liquid_config["PBS"]+50,"rate":0.1}#there need to test                                         
        dest_basic              = {"plate":MagnicPlate,"well":f'A{Sample_Select[i]+1}',"x":0,"y":0,"height":25,"volume":liquid_config["PBS"]+80,"rate":1}
        source_air_gap_config   = {"air_gap_enable":False,"air_gap_volume":Magnic_plate_config["air_gap"]}
        source_delay_config     = {"delay_enable":True,"delay_times":Magnic_plate_config["delay_time"]}
        source_mix_config       = {"mix_enable":False,"mix_volume":200, "mix_times":3,"mix_height":1,"mix_rate":0.2}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}

        dest_mix_config       = {"mix_enable":False,"mix_volume":liquid_config['PBS'], "mix_times":2,"mix_height":19.5,"mix_rate":1}
        dest_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
        dest_delay_config     = {"delay_enable":True,"delay_times":Magnic_plate_config["delay_time"]}                             
        dest_blow_out_config  = {"blow_out_enable":True,"blow_out_height":Magnic_plate_config["blow_out_height"]}
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    del protocol.max_speeds['a']
    hs_mod.open_labware_latch()
    
    move(protocol,url,1)#move to hs_mod
    hs_mod.close_labware_latch()
    
    # ------------------------------------------------------------------------------------------------ #
    #                                           Add Protein-Beads                                      #
    # ------------------------------------------------------------------------------------------------ #
 
    for i in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        source_basic            = {"plate":EnzymePlate,"well":f'A{3+i}',"x":0,"y":0,"height":0.1,"volume":liquid_config['Beads_Pro'],"rate":0.2}
        dest_basic              = {"plate":ProteinPlate_Heat,"well":f'A{Sample_Select[i]+1}',"x":0,"y":0,"height":10,"volume":liquid_config['Beads_Pro']+40,"rate":0.2}
        source_air_gap_config   = {"air_gap_enable":False,"air_gap_volume":EnzymePlate_config["air_gap"]}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":EnzymePlate_config["touch_tip_offset"]}
        source_delay_config     = {"delay_enable":True,"delay_times":EnzymePlate_config["delay_time"]}
        source_mix_config       = {"mix_enable":True,"mix_volume":20, "mix_times":8,"mix_height":1,"mix_rate":3}
        
        dest_mix_config       = {"mix_enable":True,"mix_volume":100,"mix_times":3,"mix_height":10,"mix_rate":2.5}
        dest_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        dest_blow_out_config  = {"blow_out_enable":True,"blow_out_height":normal_plate_config["blow_out_height"]}
        dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}
        
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=50,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)


    # ------------------------------------------------------------------------------------------------ #
    #                                             Add Lysis-EV                                            #
    # ------------------------------------------------------------------------------------------------ #
    for i in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        source_basic            = {"plate":WaterWall,"well":f'A{2}',"x":0,"y":0,"height":Surface(Initial_Volume['Lysis-EV']-i*liquid_config['Lysis-EV'],liquid_config["Lysis-EV"]),"volume":liquid_config['Lysis-EV'],"rate":1}
        dest_basic              = {"plate":ProteinPlate_Heat,"well":f'A{Sample_Select[i]}',"x":0,"y":0,"height":3,"volume":liquid_config['Lysis-EV']+40,"rate":1}
        source_air_gap_config   = {"air_gap_enable":False,"air_gap_volume":normal_plate_config["air_gap"]}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        source_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}

        source_mix_config = {"mix_enable":False,"mix_volume":100, "mix_times":2,"mix_height":3,"mix_rate":1}
        dest_mix_config   = {"mix_enable":False,"mix_volume":100,"mix_times":3,"mix_height":3,"mix_rate":2.5}
        dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}


        dest_touch_tip_config   = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        dest_blow_out_config    = {"blow_out_enable":True,"blow_out_height":normal_plate_config['blow_out_height']}
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)


    move(protocol,url,2)
    hs_mod.set_and_wait_for_temperature(42)
    hs_mod.set_and_wait_for_shake_speed(speed_config["Nurture"])
    protocol.delay(minutes=time_config["time_nurture"])

    hs_mod.deactivate_heater()
    hs_mod.deactivate_shaker()

    protocol.comment('End Nurture')
    move(protocol,url,3)#remove lid
    
    hs_mod.open_labware_latch()
    move(protocol,url,4)#move plate
    # ------------------------------------------------------------------------------------------------ #

    protocol.delay(minutes=time_config["time_magnetic"])
    hs_mod.close_labware_latch()
    protocol.comment("End Magnetic Separate")
    protocol.home()

    # ------------------------------------------------------------------------------------------------ #
    #                                          Separate Beads                                          #
    # ------------------------------------------------------------------------------------------------ #
    protocol.max_speeds['a']=20
    for j in range(0,len(Sample_Select)): 
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        for i in range(0,((liquid_config["Sample"]+liquid_config["Beads_EV"]+liquid_config['PBS'])//200)+2): 
                source_basic = {"plate":MagnicPlate,"well":f'A{Sample_Select[j]+1}',
                                "x": (int((Sample_Select[j]+1)%2==0)*2-1)*1.5,
                                "y": 0,"height": 19.5, "volume": 200, "rate": 0.1}
                

                dest_basic   = {"plate":WastePlate,"well":f'A{Sample_Select[j]}',
                                "x": 0,
                                "y": 0, "height": 25, "volume": 240, "rate": 1}
                
                source_air_gap_config   = {"air_gap_enable":False, "air_gap_volume":Magnic_plate_config["air_gap"]}
                source_delay_config     = {"delay_enable":True,    "delay_times":Magnic_plate_config['delay_time']}
                source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
                source_mix_config       = {"mix_enable":False,"mix_volume":20, "mix_times":5,"mix_height":0.1,"mix_rate":1.5}

                dest_mix_config       = {"mix_enable":False,"mix_volume":200, "mix_times":2,"mix_height":19.5,"mix_rate":1}
                dest_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
                dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}
                dest_blow_out_config  = {"blow_out_enable":True,"blow_out_height":normal_plate_config["blow_out_height"]}
                My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                        source_basic            = source_basic,            dest_basic            = dest_basic,
                        source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                        source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                        source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                        source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    
    # ------------------------------------------------------------------------------------------------ #
    #                                          PBS Wash Beads                                          #
    # ------------------------------------------------------------------------------------------------ #
    
    for i in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        source_basic            = {"plate":WaterWall,"well":f'A{1}',
                                   "x":0,
                                   "y":0,
                                   "height":Surface(Initial_Volume["PBS"]-(len(Sample_Select)+i)*liquid_config["PBS"],liquid_config['PBS']),"volume":liquid_config["PBS"],"rate":1}
        dest_basic              = {"plate":MagnicPlate,"well":f'A{Sample_Select[i]+1}',"x":(int((Sample_Select[j]+1)%2==0)*2-1)*1.5,"y":0,"height":19.4,"volume":liquid_config["PBS"]+20,"rate":0.1}#there need to test
        source_air_gap_config   = {"air_gap_enable":False,"air_gap_volume":normal_plate_config["air_gap"]}
        source_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}
        source_mix_config       = {"mix_enable":False,"mix_volume":200, "mix_times":3,"mix_height":1,"mix_rate":0.1}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}

        dest_mix_config       = {"mix_enable":True,"mix_volume":liquid_config['PBS'], "mix_times":6,"mix_height":19.5,"mix_rate":0.1}
        dest_touch_tip_config = {"touch_tip_enable":False,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
        dest_delay_config     = {"delay_enable":False,"delay_times":Magnic_plate_config["delay_time"]}
        dest_blow_out_config  = {"blow_out_enable":False,"blow_out_height":Magnic_plate_config["blow_out_height"]}
        
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        
        source_basic            = {"plate":MagnicPlate,"well":f'A{Sample_Select[i]+1}',
                                   "x":(int((Sample_Select[j]+1)%2==0)*2-1)*1.5,
                                   "y":0,"height":19.4,
                                   "volume":liquid_config["PBS"]+30,"rate":0.1}#there need to test                                         
        dest_basic              = {"plate":WastePlate,"well":f'A{Sample_Select[i]+1}',"x":0,"y":0,"height":25,"volume":liquid_config["PBS"]+50,"rate":1}
        source_air_gap_config   = {"air_gap_enable":False,"air_gap_volume":Magnic_plate_config["air_gap"]}
        source_delay_config     = {"delay_enable":True,"delay_times":Magnic_plate_config["delay_time"]}
        source_mix_config       = {"mix_enable":False,"mix_volume":200, "mix_times":3,"mix_height":1,"mix_rate":0.2}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}

        dest_mix_config       = {"mix_enable":False,"mix_volume":liquid_config['PBS'], "mix_times":2,"mix_height":19.4,"mix_rate":1}
        dest_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}                             
        dest_blow_out_config  = {"blow_out_enable":True,"blow_out_height":normal_plate_config["blow_out_height"]}
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    del protocol.max_speeds['a']
 
    
    # ------------------------------------------------------------------------------------------------ #
    #                                             Add Lysis-Pro                                        #
    # ------------------------------------------------------------------------------------------------ #
    for i in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        source_basic            = {"plate":WaterWall,"well":f'A{3}',"x":0,"y":0,"height":Surface(Initial_Volume["Lysis-Pro"]-i*liquid_config["Lysis-Pro"],liquid_config['Lysis-Pro']),"volume":liquid_config['Lysis-Pro'],"rate":1}
        dest_basic              = {"plate":MagnicPlate,"well":f'A{Sample_Select[i]+1}',"x":0,"y":0,"height":20,"volume":liquid_config['Lysis-Pro']+40,"rate":1}
        source_air_gap_config   = {"air_gap_enable":False,"air_gap_volume":normal_plate_config["air_gap"]}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        source_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}

        source_mix_config = {"mix_enable":False,"mix_volume":100, "mix_times":2,"mix_height":3,"mix_rate":1}
        dest_mix_config   = {"mix_enable":False,"mix_volume":100,"mix_times":3,"mix_height":3,"mix_rate":2.5}
        dest_delay_config     = {"delay_enable":True,"delay_times":Magnic_plate_config["delay_time"]}


        dest_touch_tip_config   = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
        dest_blow_out_config    = {"blow_out_enable":True,"blow_out_height":Magnic_plate_config['blow_out_height']}
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)


    hs_mod.open_labware_latch()
    hs_mod.set_and_wait_for_temperature(95)
    move(protocol,url,1)
    hs_mod.close_labware_latch()
    move(protocol,url,2)#add lid
    hs_mod.set_and_wait_for_shake_speed(speed_config["Lysis"])
    protocol.delay(minutes=time_config["time_crack"])

    hs_mod.deactivate_heater()
    hs_mod.deactivate_shaker()
    move(protocol,url,3)#remove lid
    hs_mod.open_labware_latch()
    move(protocol,url,4)#move to magnic 
    
    hs_mod.set_target_temperature(40)
    temp_mod.set_temperature(4)
    hs_mod.wait_for_temperature()
    protocol.home()
    
      # ------------------------------------------------------------------------------------------------ #
    #                                             Add TEAB                                             #
    # ------------------------------------------------------------------------------------------------ #
    for i in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        source_basic            = {"plate":WaterWall,"well":f'A{4}',"x":0,"y":0,"height":Surface(Initial_Volume['TEAB']-i*liquid_config['TEAB'],liquid_config["TEAB"]),"volume":liquid_config['TEAB'],"rate":1}
        dest_basic              = {"plate":MagnicPlate,"well":f'A{Sample_Select[i]}',"x":(int(Sample_Select[i]%2==0)*2-1)*1.5,"y":0,"height":20,"volume":liquid_config['TEAB']+40,"rate":1}
        source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":normal_plate_config["air_gap"]}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        source_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}

        source_mix_config = {"mix_enable":False,"mix_volume":100, "mix_times":2,"mix_height":1,"mix_rate":0.1}
        dest_mix_config   = {"mix_enable":False,"mix_volume":60,"mix_times":3,"mix_height":19.5,"mix_rate":0.1}
        dest_delay_config     = {"delay_enable":True,"delay_times":Magnic_plate_config["delay_time"]}


        dest_touch_tip_config   = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
        dest_blow_out_config    = {"blow_out_enable":True,"blow_out_height":Magnic_plate_config['blow_out_height']}
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    for i in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        source_basic            = {"plate":WaterWall,"well":f'A{4}',"x":0,"y":0,"height":Surface(Initial_Volume['TEAB']-(len(Sample_Select)+i)*liquid_config['TEAB'],liquid_config["TEAB"]),"volume":liquid_config['TEAB'],"rate":1}
        dest_basic              = {"plate":MagnicPlate,"well":f'A{Sample_Select[i]+1}',"x":0,"y":0,"height":20,"volume":liquid_config['TEAB']+40,"rate":1}
        source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":normal_plate_config["air_gap"]}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        source_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}

        source_mix_config = {"mix_enable":False,"mix_volume":100, "mix_times":2,"mix_height":3,"mix_rate":1}
        dest_mix_config   = {"mix_enable":False,"mix_volume":100,"mix_times":3,"mix_height":3,"mix_rate":2.5}
        dest_delay_config     = {"delay_enable":True,"delay_times":Magnic_plate_config["delay_time"]}


        dest_touch_tip_config   = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
        dest_blow_out_config    = {"blow_out_enable":True,"blow_out_height":Magnic_plate_config['blow_out_height']}
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    
    move(protocol,url,1)#move to hs_mod
    hs_mod.set_target_temperature(40)
   

    hs_mod.close_labware_latch()
    move(protocol,url,5)
    #ProteinPlate_Heat = hs_mod.load_labware('nest_96_wellplate_2ml_deep')

    # ------------------------------------------------------------------------------------------------ #
    #                                             Add Lysc                                             #
    # ------------------------------------------------------------------------------------------------ #
    for i in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        source_basic            = {"plate":EnzymePlate,"well":f'A{5+i}',"x":0,"y":0,"height":0.1,"volume":liquid_config['Lysc'],"rate":0.2}
        dest_basic              = {"plate":ProteinPlate_Heat,"well":f'A{Sample_Select[i]}',"x":0,"y":0,"height":5,"volume":liquid_config["Lysc"]+20,"rate":1}
        source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":EnzymePlate_config["air_gap"]}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":EnzymePlate_config["touch_tip_offset"]}
        source_delay_config     = {"delay_enable":True,"delay_times":EnzymePlate_config["delay_time"]}

        source_mix_config = {"mix_enable":True,"mix_volume":20, "mix_times":3,"mix_height":1,"mix_rate":0.2}
        dest_mix_config   = {"mix_enable":False,"mix_volume":20,"mix_times":3,"mix_height":1,"mix_rate":1}
        dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}


        dest_touch_tip_config   = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        dest_blow_out_config    = {"blow_out_enable":True,"blow_out_height":normal_plate_config['blow_out_height']}
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=50,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

   
    
    # ------------------------------------------------------------------------------------------------ #
    #                                            Add Trypsin                                           #
    # ------------------------------------------------------------------------------------------------ #
    for i in range(0,len(Sample_Select)):
            left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
            source_basic            = {"plate":EnzymePlate,"well":f'A{7+i}',"x":0,"y":0,"height":0.1,"volume":liquid_config["Trypsin"],"rate":0.2}
            dest_basic              = {"plate":ProteinPlate_Heat,"well":f'A{Sample_Select[i]}',"x":0,"y":0,"height":5,"volume":liquid_config['Trypsin']+20,"rate":1}
            source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":EnzymePlate_config["air_gap"]}
            source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":EnzymePlate_config["touch_tip_offset"]}
            source_delay_config     = {"delay_enable":True,"delay_times":EnzymePlate_config["delay_time"]}

            source_mix_config = {"mix_enable":True,"mix_volume":20, "mix_times":3,"mix_height":1,"mix_rate":0.2}
            dest_mix_config   = {"mix_enable":False,"mix_volume":20,"mix_times":3,"mix_height":1,"mix_rate":1}
            dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}


            dest_touch_tip_config   = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
            dest_blow_out_config    = {"blow_out_enable":True,"blow_out_height":normal_plate_config['blow_out_height']}
            My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=50,
                    source_basic            = source_basic,            dest_basic            = dest_basic,
                    source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                    source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                    source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                    source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
            tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    
    for i in range(0,len(Sample_Select)):
            left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
            source_basic            = {"plate":EnzymePlate,"well":f'A{9+i}',"x":0,"y":0,"height":0.1,"volume":liquid_config['Trypsin_Pro'],"rate":0.2}
            dest_basic              = {"plate":ProteinPlate_Heat,"well":f'A{Sample_Select[i]+1}',"x":0,"y":0,"height":5,"volume":liquid_config['Trypsin_Pro']+20,"rate":1}
            source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":EnzymePlate_config["air_gap"]}
            source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":EnzymePlate_config["touch_tip_offset"]}
            source_delay_config     = {"delay_enable":True,"delay_times":EnzymePlate_config["delay_time"]}

            source_mix_config = {"mix_enable":True,"mix_volume":20, "mix_times":3,"mix_height":1,"mix_rate":0.2}
            dest_mix_config   = {"mix_enable":False,"mix_volume":20,"mix_times":3,"mix_height":1,"mix_rate":1}
            dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}


            dest_touch_tip_config   = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
            dest_blow_out_config    = {"blow_out_enable":True,"blow_out_height":normal_plate_config['blow_out_height']}
            My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=50,
                    source_basic            = source_basic,            dest_basic            = dest_basic,
                    source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                    source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                    source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                    source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
            tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    temp_mod.deactivate()
    move(protocol,url,2)#add lid
    hs_mod.set_and_wait_for_shake_speed(speed_config["Trypsin"])
    protocol.delay(minutes=time_config["time_trypsin"])
    protocol.pause('END')

    hs_mod.deactivate_shaker()
    move(protocol,url,3)#remove lid
    move(protocol,url,6)
    protocol.home()
    # ------------------------------------------------------------------------------------------------ #
    #                                              Add TFA                                             #
    # ------------------------------------------------------------------------------------------------ #
    for i in range(0,len(Sample_Select)):
                left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
                source_basic            = {"plate":WaterWall,"well":f'A{5}',"x":0,"y":0,"height":Surface(Initial_Volume["TFA"]-i*liquid_config["TFA"],liquid_config["TFA"]),"volume":liquid_config['TFA'],"rate":1}
                dest_basic              = {"plate":ProteinPlate_Heat,"well":f'A{Sample_Select[i]}',"x":0,"y":0,"height":5,"volume":liquid_config['TFA']+40,"rate":1}
                source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":normal_plate_config["air_gap"]}
                source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
                source_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}

                source_mix_config = {"mix_enable":False,"mix_volume":50, "mix_times":3,"mix_height":1,"mix_rate":0.2}
                dest_mix_config   = {"mix_enable":False,"mix_volume":50,"mix_times":3,"mix_height":1,"mix_rate":1}
                dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}


                dest_touch_tip_config   = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
                dest_blow_out_config    = {"blow_out_enable":True,"blow_out_height":normal_plate_config['blow_out_height']}
                My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                        source_basic            = source_basic,            dest_basic            = dest_basic,
                        source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                        source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                        source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                        source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
                tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    for i in range(0,len(Sample_Select)):
                left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
                source_basic            = {"plate":WaterWall,"well":f'A{5}',"x":0,"y":0,"height":Surface(Initial_Volume["TFA"]-(len(Sample_Select)+i)*liquid_config["TFA"],liquid_config["TFA"]),"volume":liquid_config['TFA'],"rate":1}
                dest_basic              = {"plate":ProteinPlate_Heat,"well":f'A{Sample_Select[i]+1}',"x":0,"y":0,"height":5,"volume":liquid_config['TFA']+40,"rate":1}
                source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":normal_plate_config["air_gap"]}
                source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
                source_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}

                source_mix_config = {"mix_enable":False,"mix_volume":50, "mix_times":3,"mix_height":1,"mix_rate":0.2}
                dest_mix_config   = {"mix_enable":False,"mix_volume":50,"mix_times":3,"mix_height":1,"mix_rate":1}
                dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}


                dest_touch_tip_config   = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
                dest_blow_out_config    = {"blow_out_enable":True,"blow_out_height":normal_plate_config['blow_out_height']}
                My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                        source_basic            = source_basic,            dest_basic            = dest_basic,
                        source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                        source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,                                                      
                        source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                        source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
                tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    move(protocol,url,2)#add lid
    hs_mod.set_and_wait_for_shake_speed(speed_config["TFA"])
    protocol.delay(minutes=time_config["time_TFA"])
    

    hs_mod.deactivate_shaker()
    hs_mod.deactivate_heater()
    move(protocol,url,3)#remove lid
    hs_mod.open_labware_latch()
    move(protocol,url,4)#move to magnicplate
    hs_mod.close_labware_latch()
    
    protocol.delay(minutes=5)
    
    protocol.max_speeds['a']=20

    # ------------------------------------------------------------------------------------------------ #
    #                                        Collect EVPs                                      #
    # ------------------------------------------------------------------------------------------------ #
    for j in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        for i in range(0,((liquid_config["Beads_EV"]+liquid_config['Lysis-EV']+liquid_config['TEAB']+liquid_config['Lysc']+liquid_config['TFA']+liquid_config['Trypsin'])//200)+2):
                source_basic            = {"plate":MagnicPlate,"well":f'A{Sample_Select[j]}',"x":(int(Sample_Select[j]%2==0)*2-1)*1.5,"y":0,"height":19.5,"volume":200,"rate":0.1}#
                dest_basic              = {"plate":CollectionPlate_EV,"well":f'A{Sample_Select[j]}',"x":0,"y":0,"height":13,"volume":220,"rate":1}
                source_air_gap_config   = {"air_gap_enable":True, "air_gap_volume":Magnic_plate_config["air_gap"]}
                source_delay_config     = {"delay_enable":True,    "delay_times":Magnic_plate_config['delay_time']}
                source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
                source_mix_config       = {"mix_enable":False,"mix_volume":20, "mix_times":5,"mix_height":0.1,"mix_rate":1.5}

                dest_mix_config       = {"mix_enable":True,"mix_volume":200, "mix_times":3,"mix_height":13,"mix_rate":1}
                dest_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":collection_plate_config["touch_tip_offset"]}
                dest_delay_config     = {"delay_enable":True,"delay_times":collection_plate_config["delay_time"]}
                dest_blow_out_config  = {"blow_out_enable":True,"blow_out_height":collection_plate_config["blow_out_height"]} 
                My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                        source_basic            = source_basic,            dest_basic            = dest_basic,
                        source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                        source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                        source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                        source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        
        source_basic            = {"plate":WaterWall,"well":f'A{6+j}',"x":0,"y":0,"height":0.1,"volume":liquid_config["Water"],"rate":1}
        dest_basic              = {"plate":MagnicPlate,"well":f'A{Sample_Select[j]}',"x":(int(Sample_Select[j]%2==0)*2-1)*1.5,"y":0,"height":19.5,"volume":liquid_config["Water"]+20,"rate":0.1}
        source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":normal_plate_config["air_gap"]}
        source_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}
        source_mix_config       = {"mix_enable":False,"mix_volume":200, "mix_times":3,"mix_height":1,"mix_rate":0.1}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}

        dest_mix_config       = {"mix_enable":True,"mix_volume":liquid_config['Water'], "mix_times":5,"mix_height":19.4,"mix_rate":0.1}
        dest_touch_tip_config = {"touch_tip_enable":False,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
        dest_delay_config     = {"delay_enable":False,"delay_times":Magnic_plate_config["delay_time"]}
        dest_blow_out_config  = {"blow_out_enable":False,"blow_out_height":Magnic_plate_config["blow_out_height"]}
        
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        
        source_basic            = {"plate":MagnicPlate,"well":f'A{Sample_Select[j]}',"x":(int(Sample_Select[j]%2==0)*2-1)*1.5,"y":0,"height":19.5,"volume":liquid_config['Water']+20,"rate":0.1}#
        dest_basic              = {"plate":CollectionPlate_EV,"well":f'A{Sample_Select[j]}',"x":0,"y":0,"height":13,"volume":liquid_config['Water']+40,"rate":1}
        source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":Magnic_plate_config["air_gap"]}
        source_delay_config     = {"delay_enable":True,"delay_times":Magnic_plate_config["delay_time"]}
        source_mix_config       = {"mix_enable":False,"mix_volume":200, "mix_times":3,"mix_height":1,"mix_rate":0.2}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}

        dest_mix_config       = {"mix_enable":True,"mix_volume":liquid_config['Water'], "mix_times":3,"mix_height":13,"mix_rate":1}
        dest_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}
        dest_blow_out_config  = {"blow_out_enable":True,"blow_out_height":normal_plate_config["blow_out_height"]}
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)
    # ------------------------------------------------------------------------------------------------ #
    #                                        Collect SPs                                        #
    # ------------------------------------------------------------------------------------------------ #
    for j in range(0,len(Sample_Select)):
        left_pipette.pick_up_tip(tiprack1[f'A{tip_number%12+1}'])
        for i in range(0,((liquid_config["Beads_EV"]+liquid_config['Lysis-Pro']
                           +liquid_config['TEAB']+liquid_config['TFA']+liquid_config['Trypsin'])//200)+2):
                source_basic            = {"plate":MagnicPlate,"well":f'A{Sample_Select[j]+1}',"x":(int((Sample_Select[j]+1)%2==0)*2-1)*1.5,"y":0,"height":19.5,"volume":200,"rate":0.1}#
                dest_basic              = {"plate":CollectionPlate_Pro,"well":f'A{Sample_Select[j]+1}',"x":0,"y":0,"height":13,"volume":220,"rate":1}
                source_air_gap_config   = {"air_gap_enable":True, "air_gap_volume":Magnic_plate_config["air_gap"]}
                source_delay_config     = {"delay_enable":True,    "delay_times":Magnic_plate_config['delay_time']}
                source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
                source_mix_config       = {"mix_enable":False,"mix_volume":20, "mix_times":5,"mix_height":0.1,"mix_rate":1.5}

                dest_mix_config       = {"mix_enable":True,"mix_volume":200, "mix_times":3,"mix_height":13,"mix_rate":1}
                dest_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":collection_plate_config["touch_tip_offset"]}
                dest_delay_config     = {"delay_enable":True,"delay_times":collection_plate_config["delay_time"]}
                dest_blow_out_config  = {"blow_out_enable":True,"blow_out_height":collection_plate_config["blow_out_height"]} 
                My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                        source_basic            = source_basic,            dest_basic            = dest_basic,
                        source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                        source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                        source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                        source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
                protocol.comment(source_basic["x"])
        source_basic            = {"plate":WaterWall,"well":f'A{8+j}',"x":0,"y":0,"height":0.1,"volume":liquid_config["Water"],"rate":1}
        dest_basic              = {"plate":MagnicPlate,"well":f'A{Sample_Select[j]+1}',"x":(int((Sample_Select[j]+1)%2==0)*2-1)*1.5,"y":0,"height":19.5,"volume":liquid_config["Water"]+20,"rate":0.1}
        source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":normal_plate_config["air_gap"]}
        source_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}
        source_mix_config       = {"mix_enable":False,"mix_volume":200, "mix_times":3,"mix_height":1,"mix_rate":0.1}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}

        dest_mix_config       = {"mix_enable":True,"mix_volume":liquid_config['Water'], "mix_times":5,"mix_height":19.4,"mix_rate":0.1}
        dest_touch_tip_config = {"touch_tip_enable":False,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}
        dest_delay_config     = {"delay_enable":False,"delay_times":Magnic_plate_config["delay_time"]}
        dest_blow_out_config  = {"blow_out_enable":False,"blow_out_height":Magnic_plate_config["blow_out_height"]}
        
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        
        source_basic            = {"plate":MagnicPlate,"well":f'A{Sample_Select[j]+1}',"x":(int((Sample_Select[j]+1)%2==0)*2-1)*1.5,"y":0,"height":19.5,"volume":liquid_config['Water']+20,"rate":0.1}#
        dest_basic              = {"plate":CollectionPlate_Pro,"well":f'A{Sample_Select[j]+1}',"x":0,"y":0,"height":13,"volume":liquid_config['Water']+40,"rate":1}
        source_air_gap_config   = {"air_gap_enable":True,"air_gap_volume":Magnic_plate_config["air_gap"]}
        source_delay_config     = {"delay_enable":True,"delay_times":Magnic_plate_config["delay_time"]}
        source_mix_config       = {"mix_enable":False,"mix_volume":200, "mix_times":3,"mix_height":1,"mix_rate":0.2}
        source_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":Magnic_plate_config["touch_tip_offset"]}

        dest_mix_config       = {"mix_enable":True,"mix_volume":liquid_config['Water'], "mix_times":3,"mix_height":13,"mix_rate":1}
        dest_touch_tip_config = {"touch_tip_enable":True,"touch_tip_offset":normal_plate_config["touch_tip_offset"]}
        dest_delay_config     = {"delay_enable":True,"delay_times":normal_plate_config["delay_time"]}
        dest_blow_out_config  = {"blow_out_enable":True,"blow_out_height":normal_plate_config["blow_out_height"]}
        My_transfer_Multi(protocol=protocol,left_pipette=left_pipette,max_height=64,
                source_basic            = source_basic,            dest_basic            = dest_basic,
                source_mix_config       = source_mix_config,       dest_mix_config       = dest_mix_config,
                source_delay_config     = source_delay_config,     dest_delay_config     = dest_delay_config,
                source_touch_tip_config = source_touch_tip_config, dest_touch_tip_config = dest_touch_tip_config,
                source_air_gap_config   = source_air_gap_config,   dest_blow_out_config  = dest_blow_out_config)
        tip_number=DropTip(protocol,url,tip_number,tiprack1,left_pipette)

    
