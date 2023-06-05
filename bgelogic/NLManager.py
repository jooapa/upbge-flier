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
    CON0013 = nodes.ConditionAnd()
    CON0014 = nodes.ConditionMouseMoved()
    PAR0015 = nodes.ParameterObjectProperty()
    ACT0016 = nodes.ActionSetMouseCursorVisibility()
    CON0017 = nodes.GE_OnInit()
    CON0018 = nodes.ConditionKeyPressed()
    CON0019 = nodes.ConditionKeyPressed()
    CON0020 = nodes.ConditionKeyPressed()
    CON0021 = nodes.ConditionKeyPressed()
    ACT0022 = nodes.ActionApplyLocation()
    ACT0023 = nodes.ActionApplyLocation()
    ACT0024 = nodes.ActionApplyLocation()
    ACT0025 = nodes.ActionApplyLocation()
    ACT0026 = nodes.ActionApplyLocation()
    CON0027 = nodes.ConditionKeyPressed()
    PAR0028 = nodes.ParameterObjectProperty()
    PAR0029 = nodes.ParameterVector3Simple()
    PAR0030 = nodes.ParameterVector3Simple()
    PAR0031 = nodes.ParameterVector3Simple()
    PAR0032 = nodes.ParameterVector3Simple()
    PAR0033 = nodes.ParameterObjectProperty()
    PAR0034 = nodes.ParameterVector3Simple()
    PAR0035 = nodes.ParameterVector3Simple()
    ACT0036 = nodes.ActionApplyLocation()
    CON0037 = nodes.ConditionKeyPressed()
    ACT0038 = nodes.ActionSetGameObjectGameProperty()
    PAR0039 = nodes.ParameterObjectProperty()
    PAR0040 = nodes.ParameterArithmeticOp()
    CON0041 = nodes.ConditionKeyPressed()
    PAR0042 = nodes.ParameterObjectProperty()
    PAR0043 = nodes.ParameterArithmeticOp()
    CON0044 = nodes.ConditionKeyPressed()
    PAR0045 = nodes.ParameterObjectProperty()
    PAR0046 = nodes.ParameterArithmeticOp()
    ACT0047 = nodes.ActionSetGameObjectGameProperty()
    CON0048 = nodes.ConditionKeyPressed()
    PAR0049 = nodes.ParameterObjectProperty()
    ACT0050 = nodes.ActionSetGameObjectGameProperty()
    PAR0051 = nodes.ParameterArithmeticOp()
    ACT0052 = nodes.ActionSetGameObjectGameProperty()
    CON0053 = nodes.ConditionKeyPressed()
    ACT0054 = nodes.ActionSetGameObjectGameProperty()
    ACT0055 = nodes.ActionSetCameraFov()
    PAR0056 = nodes.ParameterObjectProperty()
    PAR0057 = nodes.ParameterArithmeticOp()
    ACT0058 = nodes.ActionMouseLook()
    PAR0059 = nodes.ParameterObjectProperty()
    CON0060 = nodes.ConditionKeyPressed()
    ACT0061 = nodes.ActionSetGameObjectGameProperty()
    CON0062 = nodes.ConditionKeyPressed()
    ACT0063 = nodes.ActionSetGameObjectGameProperty()
    PAR0064 = nodes.ParameterObjectProperty()
    PAR0065 = nodes.ParameterArithmeticOp()
    PAR0066 = nodes.ParameterArithmeticOp()
    PAR0067 = nodes.ParameterObjectProperty()
    CON0068 = nodes.ConditionOnUpdate()
    ACT0069 = nodes.SetEeveeBloom()
    ACT0070 = nodes.ActionToggleGameObjectGameProperty()
    ACT0071 = nodes.ActionSetGameObjectVisibility()
    PAR0072 = nodes.ParameterObjectProperty()
    ACT0073 = nodes.ActionSetGameObjectVisibility()
    CON0000.mouse_button = bge.events.LEFTMOUSE
    CON0000.game_object = None
    CON0001.game_object = None
    PAR0002.game_object = "NLO:Pcontroller"
    PAR0002.property_name = "fov"
    PAR0003.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0003.operand_a = PAR0056
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
    ACT0010.condition = CON0017
    ACT0010.camera = "NLO:Camera"
    ACT0010.fov = PAR0056
    CON0011.condition = PAR0072
    CON0012.key_code = bge.events.IKEY
    CON0012.pulse = False
    CON0013.condition_a = CON0014
    CON0013.condition_b = CON0011
    CON0014.pulse = True
    PAR0015.game_object = "NLO:Pcontroller"
    PAR0015.property_name = "bloomTrue"
    ACT0016.condition = CON0068
    ACT0016.visibility_status = PAR0072
    CON0018.key_code = bge.events.SKEY
    CON0018.pulse = True
    CON0019.key_code = bge.events.DKEY
    CON0019.pulse = True
    CON0020.key_code = bge.events.LEFTSHIFTKEY
    CON0020.pulse = True
    CON0021.key_code = bge.events.WKEY
    CON0021.pulse = True
    ACT0022.local = True
    ACT0022.condition = CON0021
    ACT0022.game_object = "NLO:U_O"
    ACT0022.movement = PAR0029.OUTV
    ACT0023.local = True
    ACT0023.condition = CON0053
    ACT0023.game_object = "NLO:U_O"
    ACT0023.movement = PAR0030.OUTV
    ACT0024.local = True
    ACT0024.condition = CON0018
    ACT0024.game_object = "NLO:U_O"
    ACT0024.movement = PAR0035.OUTV
    ACT0025.local = True
    ACT0025.condition = CON0019
    ACT0025.game_object = "NLO:U_O"
    ACT0025.movement = PAR0034.OUTV
    ACT0026.local = True
    ACT0026.condition = CON0020
    ACT0026.game_object = "NLO:U_O"
    ACT0026.movement = PAR0031.OUTV
    CON0027.key_code = bge.events.SPACEKEY
    CON0027.pulse = True
    PAR0028.game_object = "NLO:Pcontroller"
    PAR0028.property_name = "walk-"
    PAR0029.input_x = 0.0
    PAR0029.input_y = 0.0
    PAR0029.input_z = PAR0028
    PAR0030.input_x = PAR0028
    PAR0030.input_y = 0.0
    PAR0030.input_z = 0.0
    PAR0031.input_x = 0.0
    PAR0031.input_y = PAR0028
    PAR0031.input_z = 0.0
    PAR0032.input_x = 0.0
    PAR0032.input_y = PAR0033
    PAR0032.input_z = 0.0
    PAR0033.game_object = "NLO:Pcontroller"
    PAR0033.property_name = "walk+"
    PAR0034.input_x = PAR0033
    PAR0034.input_y = 0.0
    PAR0034.input_z = 0.0
    PAR0035.input_x = 0.0
    PAR0035.input_y = 0.0
    PAR0035.input_z = PAR0033
    ACT0036.local = True
    ACT0036.condition = CON0027
    ACT0036.game_object = "NLO:U_O"
    ACT0036.movement = PAR0032.OUTV
    CON0037.key_code = bge.events.UPARROWKEY
    CON0037.pulse = True
    ACT0038.condition = CON0037
    ACT0038.game_object = "NLO:Pcontroller"
    ACT0038.property_name = "walk-"
    ACT0038.property_value = PAR0040
    PAR0039.game_object = "NLO:Pcontroller"
    PAR0039.property_name = "walk-"
    PAR0040.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0040.operand_a = PAR0039
    PAR0040.operand_b = -0.009999999776482582
    CON0041.key_code = bge.events.UPARROWKEY
    CON0041.pulse = True
    PAR0042.game_object = "NLO:Pcontroller"
    PAR0042.property_name = "walk+"
    PAR0043.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0043.operand_a = PAR0042
    PAR0043.operand_b = 0.009999999776482582
    CON0044.key_code = bge.events.DOWNARROWKEY
    CON0044.pulse = True
    PAR0045.game_object = "NLO:Pcontroller"
    PAR0045.property_name = "walk-"
    PAR0046.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0046.operand_a = PAR0045
    PAR0046.operand_b = 0.009999999776482582
    ACT0047.condition = CON0044
    ACT0047.game_object = "NLO:Pcontroller"
    ACT0047.property_name = "walk-"
    ACT0047.property_value = PAR0046
    CON0048.key_code = bge.events.DOWNARROWKEY
    CON0048.pulse = True
    PAR0049.game_object = "NLO:Pcontroller"
    PAR0049.property_name = "walk+"
    ACT0050.condition = CON0048
    ACT0050.game_object = "NLO:Pcontroller"
    ACT0050.property_name = "walk+"
    ACT0050.property_value = PAR0051
    PAR0051.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0051.operand_a = PAR0049
    PAR0051.operand_b = -0.009999999776482582
    ACT0052.condition = CON0041
    ACT0052.game_object = "NLO:Pcontroller"
    ACT0052.property_name = "walk+"
    ACT0052.property_value = PAR0043
    CON0053.key_code = bge.events.AKEY
    CON0053.pulse = True
    ACT0054.condition = ACT0055.OUT
    ACT0054.game_object = "NLO:Pcontroller"
    ACT0054.property_name = "fov"
    ACT0054.property_value = PAR0057
    ACT0055.condition = CON0006
    ACT0055.camera = "NLO:Camera"
    ACT0055.fov = PAR0057
    PAR0056.game_object = "NLO:Pcontroller"
    PAR0056.property_name = "fov"
    PAR0057.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0057.operand_a = PAR0056
    PAR0057.operand_b = 4.0
    ACT0058.axis = 1
    ACT0058.condition = CON0013
    ACT0058.game_object_x = "NLO:Pcontroller"
    ACT0058.game_object_y = None
    ACT0058.inverted = {'x': False, 'y': True}
    ACT0058.sensitivity = PAR0059
    ACT0058.use_cap_z = False
    ACT0058.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0058.use_cap_y = False
    ACT0058.cap_y = mathutils.Vector((0.0, 3.1241393089294434))
    ACT0058.smooth = 0.25833332538604736
    PAR0059.game_object = "NLO:Pcontroller"
    PAR0059.property_name = "sensitivity"
    CON0060.key_code = bge.events.LEFTARROWKEY
    CON0060.pulse = True
    ACT0061.condition = CON0060
    ACT0061.game_object = "NLO:Pcontroller"
    ACT0061.property_name = "sensitivity"
    ACT0061.property_value = PAR0066
    CON0062.key_code = bge.events.RIGHTARROWKEY
    CON0062.pulse = True
    ACT0063.condition = CON0062
    ACT0063.game_object = "NLO:Pcontroller"
    ACT0063.property_name = "sensitivity"
    ACT0063.property_value = PAR0065
    PAR0064.game_object = "NLO:Pcontroller"
    PAR0064.property_name = "sensitivity"
    PAR0065.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0065.operand_a = PAR0064
    PAR0065.operand_b = 0.019999999552965164
    PAR0066.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0066.operand_a = PAR0067
    PAR0066.operand_b = -0.019999999552965164
    PAR0067.game_object = "NLO:Pcontroller"
    PAR0067.property_name = "sensitivity"
    ACT0069.condition = CON0068
    ACT0069.value = PAR0015
    ACT0070.condition = CON0012
    ACT0070.game_object = "NLO:Pcontroller"
    ACT0070.property_name = "uiTrue"
    ACT0071.condition = ACT0070.OUT
    ACT0071.game_object = "NLO:ui"
    ACT0071.visible = PAR0072
    ACT0071.recursive = True
    PAR0072.game_object = "NLO:Pcontroller"
    PAR0072.property_name = "uiTrue"
    ACT0073.condition = CON0017
    ACT0073.game_object = "NLO:ui"
    ACT0073.visible = True
    ACT0073.recursive = True
    network.add_cell(CON0000)
    network.add_cell(PAR0002)
    network.add_cell(CON0004)
    network.add_cell(CON0006)
    network.add_cell(CON0008)
    network.add_cell(CON0012)
    network.add_cell(CON0014)
    network.add_cell(CON0017)
    network.add_cell(CON0019)
    network.add_cell(CON0021)
    network.add_cell(CON0027)
    network.add_cell(PAR0033)
    network.add_cell(PAR0035)
    network.add_cell(CON0037)
    network.add_cell(PAR0039)
    network.add_cell(CON0041)
    network.add_cell(CON0044)
    network.add_cell(CON0048)
    network.add_cell(CON0053)
    network.add_cell(PAR0056)
    network.add_cell(PAR0059)
    network.add_cell(CON0062)
    network.add_cell(PAR0064)
    network.add_cell(PAR0067)
    network.add_cell(ACT0070)
    network.add_cell(PAR0072)
    network.add_cell(CON0001)
    network.add_cell(ACT0009)
    network.add_cell(CON0011)
    network.add_cell(PAR0015)
    network.add_cell(CON0018)
    network.add_cell(ACT0024)
    network.add_cell(PAR0028)
    network.add_cell(PAR0030)
    network.add_cell(PAR0032)
    network.add_cell(ACT0036)
    network.add_cell(PAR0040)
    network.add_cell(PAR0045)
    network.add_cell(PAR0049)
    network.add_cell(PAR0051)
    network.add_cell(PAR0057)
    network.add_cell(CON0060)
    network.add_cell(PAR0065)
    network.add_cell(CON0068)
    network.add_cell(ACT0071)
    network.add_cell(PAR0003)
    network.add_cell(ACT0007)
    network.add_cell(CON0013)
    network.add_cell(CON0020)
    network.add_cell(ACT0023)
    network.add_cell(PAR0029)
    network.add_cell(PAR0034)
    network.add_cell(PAR0042)
    network.add_cell(PAR0046)
    network.add_cell(ACT0050)
    network.add_cell(ACT0055)
    network.add_cell(ACT0063)
    network.add_cell(ACT0069)
    network.add_cell(ACT0005)
    network.add_cell(ACT0016)
    network.add_cell(ACT0025)
    network.add_cell(PAR0031)
    network.add_cell(PAR0043)
    network.add_cell(ACT0052)
    network.add_cell(ACT0058)
    network.add_cell(PAR0066)
    network.add_cell(ACT0010)
    network.add_cell(ACT0026)
    network.add_cell(ACT0047)
    network.add_cell(ACT0061)
    network.add_cell(ACT0022)
    network.add_cell(ACT0054)
    network.add_cell(ACT0038)
    network.add_cell(ACT0073)
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
