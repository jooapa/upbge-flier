# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionMousePressedOn()
    CON0001 = nodes.ConditionMouseTargeting()
    PAR0002 = nodes.ParameterObjectProperty()
    PAR0003 = nodes.ParameterArithmeticOp()
    CON0004 = nodes.ConditionMouseScrolled()
    ACT0005 = nodes.ActionSetGameObjectGameProperty()
    CON0006 = nodes.ConditionMouseScrolled()
    ACT0007 = nodes.ActionSetCameraFov()
    CON0008 = nodes.ConditionKeyPressed()
    ACT0009 = nodes.ActionToggleGameObjectGameProperty()
    ACT0010 = nodes.ActionSetCameraFov()
    CON0011 = nodes.ConditionNot()
    CON0012 = nodes.ConditionKeyPressed()
    ACT0013 = nodes.ActionToggleGameObjectGameProperty()
    CON0014 = nodes.ConditionAnd()
    CON0015 = nodes.ConditionMouseMoved()
    PAR0016 = nodes.ParameterObjectProperty()
    ACT0017 = nodes.SetEeveeBloom()
    ACT0018 = nodes.ActionSetMouseCursorVisibility()
    PAR0019 = nodes.ParameterObjectProperty()
    ACT0020 = nodes.ActionSetGameObjectVisibility()
    CON0021 = nodes.GE_OnInit()
    ACT0022 = nodes.ActionSetGameObjectVisibility()
    CON0023 = nodes.ConditionKeyPressed()
    CON0024 = nodes.ConditionKeyPressed()
    CON0025 = nodes.ConditionKeyPressed()
    CON0026 = nodes.ConditionKeyPressed()
    ACT0027 = nodes.ActionApplyLocation()
    ACT0028 = nodes.ActionApplyLocation()
    ACT0029 = nodes.ActionApplyLocation()
    ACT0030 = nodes.ActionApplyLocation()
    ACT0031 = nodes.ActionApplyLocation()
    CON0032 = nodes.ConditionKeyPressed()
    PAR0033 = nodes.ParameterObjectProperty()
    PAR0034 = nodes.ParameterVector3Simple()
    PAR0035 = nodes.ParameterVector3Simple()
    PAR0036 = nodes.ParameterVector3Simple()
    PAR0037 = nodes.ParameterVector3Simple()
    PAR0038 = nodes.ParameterObjectProperty()
    PAR0039 = nodes.ParameterVector3Simple()
    PAR0040 = nodes.ParameterVector3Simple()
    ACT0041 = nodes.ActionApplyLocation()
    CON0042 = nodes.ConditionKeyPressed()
    ACT0043 = nodes.ActionSetGameObjectGameProperty()
    PAR0044 = nodes.ParameterObjectProperty()
    PAR0045 = nodes.ParameterArithmeticOp()
    CON0046 = nodes.ConditionKeyPressed()
    PAR0047 = nodes.ParameterObjectProperty()
    PAR0048 = nodes.ParameterArithmeticOp()
    CON0049 = nodes.ConditionKeyPressed()
    PAR0050 = nodes.ParameterObjectProperty()
    PAR0051 = nodes.ParameterArithmeticOp()
    ACT0052 = nodes.ActionSetGameObjectGameProperty()
    CON0053 = nodes.ConditionKeyPressed()
    PAR0054 = nodes.ParameterObjectProperty()
    ACT0055 = nodes.ActionSetGameObjectGameProperty()
    PAR0056 = nodes.ParameterArithmeticOp()
    ACT0057 = nodes.ActionSetGameObjectGameProperty()
    CON0058 = nodes.ConditionKeyPressed()
    ACT0059 = nodes.ActionSetGameObjectGameProperty()
    ACT0060 = nodes.ActionSetCameraFov()
    PAR0061 = nodes.ParameterObjectProperty()
    PAR0062 = nodes.ParameterArithmeticOp()
    ACT0063 = nodes.ActionMouseLook()
    PAR0064 = nodes.ParameterObjectProperty()
    CON0065 = nodes.ConditionKeyPressed()
    ACT0066 = nodes.ActionSetGameObjectGameProperty()
    CON0067 = nodes.ConditionKeyPressed()
    ACT0068 = nodes.ActionSetGameObjectGameProperty()
    PAR0069 = nodes.ParameterObjectProperty()
    PAR0070 = nodes.ParameterArithmeticOp()
    PAR0071 = nodes.ParameterArithmeticOp()
    PAR0072 = nodes.ParameterObjectProperty()
    CON0073 = nodes.ConditionOnUpdate()
    ACT0074 = nodes.SetMaterial()
    CON0075 = nodes.ConditionMousePressedOn()
    CON0076 = nodes.ConditionMousePressedOn()
    ACT0077 = nodes.SetMaterial()
    ACT0078 = nodes.ActionSetGameObjectGameProperty()
    ACT0079 = nodes.ActionSetGameObjectGameProperty()
    ACT0080 = nodes.ActionSetGameObjectGameProperty()
    CON0081 = nodes.ConditionMousePressedOn()
    ACT0082 = nodes.SetMaterial()
    CON0000.mouse_button = bge.events.LEFTMOUSE
    CON0000.game_object = None
    CON0001.game_object = None
    PAR0002.game_object = "NLO:Pcontroller"
    PAR0002.property_name = "fov"
    PAR0003.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0003.operand_a = PAR0061
    PAR0003.operand_b = 4.0
    CON0004.wheel_direction = 2
    ACT0005.condition = ACT0007.OUT
    ACT0005.game_object = "NLO:Pcontroller"
    ACT0005.property_name = "fov"
    ACT0005.property_value = PAR0003
    CON0006.wheel_direction = 1
    ACT0007.condition = CON0004
    ACT0007.camera = "NLO:Camera"
    ACT0007.fov = PAR0003
    CON0008.key_code = bge.events.BKEY
    CON0008.pulse = False
    ACT0009.condition = CON0008
    ACT0009.game_object = "NLO:Pcontroller"
    ACT0009.property_name = "bloomTrue"
    ACT0010.condition = CON0021
    ACT0010.camera = "NLO:Camera"
    ACT0010.fov = PAR0061
    CON0011.condition = PAR0019
    CON0012.key_code = bge.events.IKEY
    CON0012.pulse = False
    ACT0013.condition = CON0012
    ACT0013.game_object = "NLO:Pcontroller"
    ACT0013.property_name = "uiTrue"
    CON0014.condition_a = CON0015
    CON0014.condition_b = CON0011
    CON0015.pulse = True
    PAR0016.game_object = "NLO:Pcontroller"
    PAR0016.property_name = "bloomTrue"
    ACT0017.condition = CON0073
    ACT0017.value = PAR0016
    ACT0018.condition = CON0073
    ACT0018.visibility_status = PAR0019
    PAR0019.game_object = "NLO:Pcontroller"
    PAR0019.property_name = "uiTrue"
    ACT0020.condition = ACT0013.OUT
    ACT0020.game_object = "NLO:ui"
    ACT0020.visible = PAR0019
    ACT0020.recursive = True
    ACT0022.condition = CON0021
    ACT0022.game_object = "NLO:ui"
    ACT0022.visible = False
    ACT0022.recursive = True
    CON0023.key_code = bge.events.SKEY
    CON0023.pulse = True
    CON0024.key_code = bge.events.DKEY
    CON0024.pulse = True
    CON0025.key_code = bge.events.LEFTSHIFTKEY
    CON0025.pulse = True
    CON0026.key_code = bge.events.WKEY
    CON0026.pulse = True
    ACT0027.local = True
    ACT0027.condition = CON0026
    ACT0027.game_object = "NLO:U_O"
    ACT0027.movement = PAR0034.OUTV
    ACT0028.local = True
    ACT0028.condition = CON0058
    ACT0028.game_object = "NLO:U_O"
    ACT0028.movement = PAR0035.OUTV
    ACT0029.local = True
    ACT0029.condition = CON0023
    ACT0029.game_object = "NLO:U_O"
    ACT0029.movement = PAR0040.OUTV
    ACT0030.local = True
    ACT0030.condition = CON0024
    ACT0030.game_object = "NLO:U_O"
    ACT0030.movement = PAR0039.OUTV
    ACT0031.local = True
    ACT0031.condition = CON0025
    ACT0031.game_object = "NLO:U_O"
    ACT0031.movement = PAR0036.OUTV
    CON0032.key_code = bge.events.SPACEKEY
    CON0032.pulse = True
    PAR0033.game_object = "NLO:Pcontroller"
    PAR0033.property_name = "walk-"
    PAR0034.input_x = 0.0
    PAR0034.input_y = 0.0
    PAR0034.input_z = PAR0033
    PAR0035.input_x = PAR0033
    PAR0035.input_y = 0.0
    PAR0035.input_z = 0.0
    PAR0036.input_x = 0.0
    PAR0036.input_y = PAR0033
    PAR0036.input_z = 0.0
    PAR0037.input_x = 0.0
    PAR0037.input_y = PAR0038
    PAR0037.input_z = 0.0
    PAR0038.game_object = "NLO:Pcontroller"
    PAR0038.property_name = "walk+"
    PAR0039.input_x = PAR0038
    PAR0039.input_y = 0.0
    PAR0039.input_z = 0.0
    PAR0040.input_x = 0.0
    PAR0040.input_y = 0.0
    PAR0040.input_z = PAR0038
    ACT0041.local = True
    ACT0041.condition = CON0032
    ACT0041.game_object = "NLO:U_O"
    ACT0041.movement = PAR0037.OUTV
    CON0042.key_code = bge.events.UPARROWKEY
    CON0042.pulse = True
    ACT0043.condition = CON0042
    ACT0043.game_object = "NLO:Pcontroller"
    ACT0043.property_name = "walk-"
    ACT0043.property_value = PAR0045
    PAR0044.game_object = "NLO:Pcontroller"
    PAR0044.property_name = "walk-"
    PAR0045.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0045.operand_a = PAR0044
    PAR0045.operand_b = -0.009999999776482582
    CON0046.key_code = bge.events.UPARROWKEY
    CON0046.pulse = True
    PAR0047.game_object = "NLO:Pcontroller"
    PAR0047.property_name = "walk+"
    PAR0048.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0048.operand_a = PAR0047
    PAR0048.operand_b = 0.009999999776482582
    CON0049.key_code = bge.events.DOWNARROWKEY
    CON0049.pulse = True
    PAR0050.game_object = "NLO:Pcontroller"
    PAR0050.property_name = "walk-"
    PAR0051.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0051.operand_a = PAR0050
    PAR0051.operand_b = 0.009999999776482582
    ACT0052.condition = CON0049
    ACT0052.game_object = "NLO:Pcontroller"
    ACT0052.property_name = "walk-"
    ACT0052.property_value = PAR0051
    CON0053.key_code = bge.events.DOWNARROWKEY
    CON0053.pulse = True
    PAR0054.game_object = "NLO:Pcontroller"
    PAR0054.property_name = "walk+"
    ACT0055.condition = CON0053
    ACT0055.game_object = "NLO:Pcontroller"
    ACT0055.property_name = "walk+"
    ACT0055.property_value = PAR0056
    PAR0056.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0056.operand_a = PAR0054
    PAR0056.operand_b = -0.009999999776482582
    ACT0057.condition = CON0046
    ACT0057.game_object = "NLO:Pcontroller"
    ACT0057.property_name = "walk+"
    ACT0057.property_value = PAR0048
    CON0058.key_code = bge.events.AKEY
    CON0058.pulse = True
    ACT0059.condition = ACT0060.OUT
    ACT0059.game_object = "NLO:Pcontroller"
    ACT0059.property_name = "fov"
    ACT0059.property_value = PAR0062
    ACT0060.condition = CON0006
    ACT0060.camera = "NLO:Camera"
    ACT0060.fov = PAR0062
    PAR0061.game_object = "NLO:Pcontroller"
    PAR0061.property_name = "fov"
    PAR0062.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0062.operand_a = PAR0061
    PAR0062.operand_b = 4.0
    ACT0063.axis = 1
    ACT0063.condition = CON0014
    ACT0063.game_object_x = "NLO:Pcontroller"
    ACT0063.game_object_y = None
    ACT0063.inverted = {'x': False, 'y': True}
    ACT0063.sensitivity = PAR0064
    ACT0063.use_cap_z = False
    ACT0063.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0063.use_cap_y = False
    ACT0063.cap_y = mathutils.Vector((0.0, 3.1241393089294434))
    ACT0063.smooth = 0.25833332538604736
    PAR0064.game_object = "NLO:Pcontroller"
    PAR0064.property_name = "sensitivity"
    CON0065.key_code = bge.events.LEFTARROWKEY
    CON0065.pulse = True
    ACT0066.condition = CON0065
    ACT0066.game_object = "NLO:Pcontroller"
    ACT0066.property_name = "sensitivity"
    ACT0066.property_value = PAR0071
    CON0067.key_code = bge.events.RIGHTARROWKEY
    CON0067.pulse = True
    ACT0068.condition = CON0067
    ACT0068.game_object = "NLO:Pcontroller"
    ACT0068.property_name = "sensitivity"
    ACT0068.property_value = PAR0070
    PAR0069.game_object = "NLO:Pcontroller"
    PAR0069.property_name = "sensitivity"
    PAR0070.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0070.operand_a = PAR0069
    PAR0070.operand_b = 0.019999999552965164
    PAR0071.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0071.operand_a = PAR0072
    PAR0071.operand_b = -0.019999999552965164
    PAR0072.game_object = "NLO:Pcontroller"
    PAR0072.property_name = "sensitivity"
    ACT0074.condition = CON0075
    ACT0074.game_object = "NLO:char2"
    ACT0074.slot = 1
    ACT0074.mat_name = "emis"
    CON0075.mouse_button = bge.events.LEFTMOUSE
    CON0075.game_object = "NLO:char2"
    CON0076.mouse_button = bge.events.LEFTMOUSE
    CON0076.game_object = "NLO:char3"
    ACT0077.condition = CON0076
    ACT0077.game_object = "NLO:char3"
    ACT0077.slot = 1
    ACT0077.mat_name = "emis"
    ACT0078.condition = ACT0074.OUT
    ACT0078.game_object = "NLO:Pcontroller"
    ACT0078.property_name = "char"
    ACT0078.property_value = 2
    ACT0079.condition = ACT0077.OUT
    ACT0079.game_object = "NLO:Pcontroller"
    ACT0079.property_name = "char"
    ACT0079.property_value = 3
    ACT0080.condition = ACT0082.OUT
    ACT0080.game_object = "NLO:Pcontroller"
    ACT0080.property_name = "char"
    ACT0080.property_value = 1
    CON0081.mouse_button = bge.events.LEFTMOUSE
    CON0081.game_object = "NLO:char1"
    ACT0082.condition = CON0081
    ACT0082.game_object = "NLO:char1"
    ACT0082.slot = 1
    ACT0082.mat_name = "emis"
    network.add_cell(CON0000)
    network.add_cell(PAR0002)
    network.add_cell(CON0004)
    network.add_cell(CON0006)
    network.add_cell(CON0008)
    network.add_cell(CON0012)
    network.add_cell(CON0015)
    network.add_cell(PAR0019)
    network.add_cell(CON0021)
    network.add_cell(CON0023)
    network.add_cell(CON0025)
    network.add_cell(CON0032)
    network.add_cell(PAR0038)
    network.add_cell(PAR0040)
    network.add_cell(CON0042)
    network.add_cell(PAR0044)
    network.add_cell(CON0046)
    network.add_cell(CON0049)
    network.add_cell(CON0053)
    network.add_cell(CON0058)
    network.add_cell(PAR0061)
    network.add_cell(PAR0064)
    network.add_cell(CON0067)
    network.add_cell(PAR0069)
    network.add_cell(PAR0072)
    network.add_cell(CON0075)
    network.add_cell(CON0081)
    network.add_cell(CON0001)
    network.add_cell(ACT0009)
    network.add_cell(CON0011)
    network.add_cell(CON0014)
    network.add_cell(ACT0022)
    network.add_cell(CON0026)
    network.add_cell(ACT0029)
    network.add_cell(PAR0033)
    network.add_cell(PAR0035)
    network.add_cell(PAR0037)
    network.add_cell(ACT0041)
    network.add_cell(PAR0045)
    network.add_cell(PAR0050)
    network.add_cell(PAR0054)
    network.add_cell(PAR0056)
    network.add_cell(PAR0062)
    network.add_cell(CON0065)
    network.add_cell(PAR0070)
    network.add_cell(CON0073)
    network.add_cell(CON0076)
    network.add_cell(ACT0082)
    network.add_cell(PAR0003)
    network.add_cell(ACT0007)
    network.add_cell(ACT0013)
    network.add_cell(ACT0018)
    network.add_cell(CON0024)
    network.add_cell(ACT0028)
    network.add_cell(PAR0034)
    network.add_cell(PAR0039)
    network.add_cell(PAR0047)
    network.add_cell(PAR0051)
    network.add_cell(ACT0055)
    network.add_cell(ACT0060)
    network.add_cell(ACT0068)
    network.add_cell(ACT0074)
    network.add_cell(ACT0078)
    network.add_cell(ACT0080)
    network.add_cell(ACT0005)
    network.add_cell(PAR0016)
    network.add_cell(ACT0020)
    network.add_cell(ACT0030)
    network.add_cell(PAR0036)
    network.add_cell(PAR0048)
    network.add_cell(ACT0057)
    network.add_cell(ACT0063)
    network.add_cell(PAR0071)
    network.add_cell(ACT0010)
    network.add_cell(ACT0027)
    network.add_cell(ACT0043)
    network.add_cell(ACT0059)
    network.add_cell(ACT0077)
    network.add_cell(ACT0017)
    network.add_cell(ACT0052)
    network.add_cell(ACT0079)
    network.add_cell(ACT0031)
    network.add_cell(ACT0066)
    owner["IGNLTree_Manager"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__Manager')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_Manager")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
