from opentrons import protocol_api

metadata = {'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):
    ################################
    ###Labware loading with location
    ################################
    ##reservoir => Is the source from which the transfer 
    ##              of liquid starts
    ##Labware    => agilent_1_reservoir_290ml
    ##Location   => slot 3
    reservoir = protocol.load_labware('agilent_1_reservoir_290ml', '3')

    ##plate      => Is the destination in which the liquids
    ##              need to be filled up
    ##Labware    => corning_96_wellplate_360ul_flat
    ##Location   => slot 2
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')

    ##tiprack    => Is the rack in which the tips for  
    ##              pipettes are arranged
    ##Labware    => opentrons_96_filtertiprack_200ul
    ##Location   => slot 6
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul','6');

    ###############################################
    ##Configuring and initiating the pipette action
    ###############################################
    pipette_multi = protocol.load_instrument('p300_multi', 'left', tip_racks=[tiprack])
    pipette_multi.pick_up_tip()
    for i in range(1,13):
        pipette_multi.transfer(100, reservoir['A1'], plate['A'+str(i)], touch_tip=True, blow_out=True, new_tip='never', air_gap=20)
    pipette_multi.drop_tip()
