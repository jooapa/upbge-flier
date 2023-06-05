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
    PAR0003 = nodes.ParameterObjectProperty()
    PAR0004 = nodes.ParameterArithmeticOp()
    CON0005 = nodes.ConditionMouseScrolled()
    ACT0006 = nodes.ActionSetGameObjectGameProperty()
    ACT0007 = nodes.ActionSetGameObjectGameProperty()
    ACT0008 = nodes.ActionSetCameraFov()
    CON0009 = nodes.ConditionMouseScrolled()
    ACT0010 = nodes.ActionSetCameraFov()
    CON0011 = nodes.ConditionKeyPressed()
    ACT0012 = nodes.ActionToggleGameObjectGameProperty()
    ACT0013 = nodes.ActionSetCameraFov()
    CON0014 = nodes.ConditionNot()
    ACT0015 = nodes.ActionMouseLook()
    CON0016 = nodes.ConditionKeyPressed()
    ACT0017 = nodes.ActionSetMouseCursorVisibility()
    ACT0018 = nodes.ActionToggleGameObjectGameProperty()
    CON0019 = nodes.ConditionAnd()
    CON0020 = nodes.ConditionMouseMoved()
    PAR0021 = nodes.ParameterObjectProperty()
    ACT0022 = nodes.SetEeveeBloom()
    ACT0023 = nodes.ActionSetMouseCursorVisibility()
    CON0024 = nodes.ConditionOnUpdate()
    PAR0025 = nodes.ParameterObjectProperty()
    PAR0026 = nodes.ParameterSwitchValue()
    ACT0027 = nodes.ActionSetGameObjectVisibility()
    CON0028 = nodes.GE_OnInit()
    ACT0029 = nodes.ActionSetGameObjectVisibility()
    CON0030 = nodes.ConditionKeyPressed()
    CON0031 = nodes.ConditionKeyPressed()
    CON0032 = nodes.ConditionKeyPressed()
    CON0033 = nodes.ConditionKeyPressed()
    CON0034 = nodes.ConditionKeyPressed()
    PAR0035 = nodes.ParameterArithmeticOp()
    ACT0036 = nodes.ActionApplyLocation()
    ACT0037 = nodes.ActionApplyLocation()
    ACT0038 = nodes.ActionApplyLocation()
    ACT0039 = nodes.ActionApplyLocation()
    ACT0040 = nodes.ActionApplyLocation()
    CON0041 = nodes.ConditionKeyPressed()
    PAR0042 = nodes.ParameterObjectProperty()
    PAR0043 = nodes.ParameterVector3Simple()
    PAR0044 = nodes.ParameterVector3Simple()
    PAR0045 = nodes.ParameterVector3Simple()
    PAR0046 = nodes.ParameterVector3Simple()
    PAR0047 = nodes.ParameterObjectProperty()
    PAR0048 = nodes.ParameterVector3Simple()
    PAR0049 = nodes.ParameterVector3Simple()
    ACT0050 = nodes.ActionApplyLocation()
    CON0051 = nodes.ConditionKeyPressed()
    ACT0052 = nodes.ActionSetGameObjectGameProperty()
    PAR0053 = nodes.ParameterObjectProperty()
    PAR0054 = nodes.ParameterArithmeticOp()
    CON0055 = nodes.ConditionKeyPressed()
    PAR0056 = nodes.ParameterObjectProperty()
    PAR0057 = nodes.ParameterArithmeticOp()
    CON0058 = nodes.ConditionKeyPressed()
    PAR0059 = nodes.ParameterObjectProperty()
    PAR0060 = nodes.ParameterArithmeticOp()
    ACT0061 = nodes.ActionSetGameObjectGameProperty()
    CON0062 = nodes.ConditionKeyPressed()
    PAR0063 = nodes.ParameterObjectProperty()
    ACT0064 = nodes.ActionSetGameObjectGameProperty()
    PAR0065 = nodes.ParameterArithmeticOp()
    ACT0066 = nodes.ActionSetGameObjectGameProperty()
    ACT0067 = nodes.SetLightColor()
    CON0068 = nodes.ConditionMousePressedOn()
    CON0069 = nodes.ConditionMousePressedOn()
    ACT0070 = nodes.SetLightColor()
    CON0071 = nodes.ConditionMousePressedOn()
    ACT0072 = nodes.SetLightColor()
    CON0000.mouse_button = bge.events.LEFTMOUSE
    CON0000.game_object = None
    CON0001.game_object = None
    PAR0002.game_object = "NLO:Pcontroller"
    PAR0002.property_name = "fov"
    PAR0003.game_object = "NLO:Pcontroller"
    PAR0003.property_name = "fov"
    PAR0004.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0004.operand_a = PAR0003
    PAR0004.operand_b = 4.0
    CON0005.wheel_direction = 2
    ACT0006.condition = ACT0010.OUT
    ACT0006.game_object = "NLO:Pcontroller"
    ACT0006.property_name = "fov"
    ACT0006.property_value = PAR0004
    ACT0007.condition = ACT0008.OUT
    ACT0007.game_object = "NLO:Pcontroller"
    ACT0007.property_name = "fov"
    ACT0007.property_value = PAR0035
    ACT0008.condition = CON0009
    ACT0008.camera = "NLO:Camera"
    ACT0008.fov = PAR0035
    CON0009.wheel_direction = 1
    ACT0010.condition = CON0005
    ACT0010.camera = "NLO:Camera"
    ACT0010.fov = PAR0004
    CON0011.key_code = bge.events.BKEY
    CON0011.pulse = False
    ACT0012.condition = CON0011
    ACT0012.game_object = "NLO:Pcontroller"
    ACT0012.property_name = "bloomTrue"
    ACT0013.condition = CON0028
    ACT0013.camera = "NLO:Camera"
    ACT0013.fov = PAR0003
    CON0014.condition = PAR0025
    ACT0015.axis = 1
    ACT0015.condition = CON0019
    ACT0015.game_object_x = "NLO:Pcontroller"
    ACT0015.game_object_y = None
    ACT0015.inverted = {'x': False, 'y': True}
    ACT0015.sensitivity = 0.46000003814697266
    ACT0015.use_cap_z = False
    ACT0015.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0015.use_cap_y = False
    ACT0015.cap_y = mathutils.Vector((0.0, 3.1241393089294434))
    ACT0015.smooth = 0.25833332538604736
    CON0016.key_code = bge.events.IKEY
    CON0016.pulse = False
    ACT0017.condition = None
    ACT0017.visibility_status = False
    ACT0018.condition = CON0016
    ACT0018.game_object = "NLO:Pcontroller"
    ACT0018.property_name = "uiTrue"
    CON0019.condition_a = CON0020
    CON0019.condition_b = CON0014
    CON0020.pulse = True
    PAR0021.game_object = "NLO:Pcontroller"
    PAR0021.property_name = "bloomTrue"
    ACT0022.condition = CON0024
    ACT0022.value = PAR0021
    ACT0023.condition = CON0024
    ACT0023.visibility_status = PAR0025
    PAR0025.game_object = "NLO:Pcontroller"
    PAR0025.property_name = "uiTrue"
    PAR0026.state = False
    ACT0027.condition = ACT0018.OUT
    ACT0027.game_object = "NLO:ui"
    ACT0027.visible = PAR0025
    ACT0027.recursive = True
    ACT0029.condition = CON0028
    ACT0029.game_object = "NLO:ui"
    ACT0029.visible = False
    ACT0029.recursive = True
    CON0030.key_code = bge.events.SKEY
    CON0030.pulse = True
    CON0031.key_code = bge.events.AKEY
    CON0031.pulse = True
    CON0032.key_code = bge.events.DKEY
    CON0032.pulse = True
    CON0033.key_code = bge.events.LEFTSHIFTKEY
    CON0033.pulse = True
    CON0034.key_code = bge.events.WKEY
    CON0034.pulse = True
    PAR0035.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0035.operand_a = PAR0003
    PAR0035.operand_b = 4.0
    ACT0036.local = True
    ACT0036.condition = CON0034
    ACT0036.game_object = "NLO:U_O"
    ACT0036.movement = PAR0043.OUTV
    ACT0037.local = True
    ACT0037.condition = CON0031
    ACT0037.game_object = "NLO:U_O"
    ACT0037.movement = PAR0044.OUTV
    ACT0038.local = True
    ACT0038.condition = CON0030
    ACT0038.game_object = "NLO:U_O"
    ACT0038.movement = PAR0049.OUTV
    ACT0039.local = True
    ACT0039.condition = CON0032
    ACT0039.game_object = "NLO:U_O"
    ACT0039.movement = PAR0048.OUTV
    ACT0040.local = True
    ACT0040.condition = CON0033
    ACT0040.game_object = "NLO:U_O"
    ACT0040.movement = PAR0045.OUTV
    CON0041.key_code = bge.events.SPACEKEY
    CON0041.pulse = True
    PAR0042.game_object = "NLO:Pcontroller"
    PAR0042.property_name = "walk-"
    PAR0043.input_x = 0.0
    PAR0043.input_y = 0.0
    PAR0043.input_z = PAR0042
    PAR0044.input_x = PAR0042
    PAR0044.input_y = 0.0
    PAR0044.input_z = 0.0
    PAR0045.input_x = 0.0
    PAR0045.input_y = PAR0042
    PAR0045.input_z = 0.0
    PAR0046.input_x = 0.0
    PAR0046.input_y = PAR0047
    PAR0046.input_z = 0.0
    PAR0047.game_object = "NLO:Pcontroller"
    PAR0047.property_name = "walk+"
    PAR0048.input_x = PAR0047
    PAR0048.input_y = 0.0
    PAR0048.input_z = 0.0
    PAR0049.input_x = 0.0
    PAR0049.input_y = 0.0
    PAR0049.input_z = PAR0047
    ACT0050.local = True
    ACT0050.condition = CON0041
    ACT0050.game_object = "NLO:U_O"
    ACT0050.movement = PAR0046.OUTV
    CON0051.key_code = bge.events.UPARROWKEY
    CON0051.pulse = True
    ACT0052.condition = CON0051
    ACT0052.game_object = "NLO:Pcontroller"
    ACT0052.property_name = "walk-"
    ACT0052.property_value = PAR0054
    PAR0053.game_object = "NLO:Pcontroller"
    PAR0053.property_name = "walk-"
    PAR0054.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0054.operand_a = PAR0053
    PAR0054.operand_b = -0.009999999776482582
    CON0055.key_code = bge.events.UPARROWKEY
    CON0055.pulse = True
    PAR0056.game_object = "NLO:Pcontroller"
    PAR0056.property_name = "walk+"
    PAR0057.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0057.operand_a = PAR0056
    PAR0057.operand_b = 0.009999999776482582
    CON0058.key_code = bge.events.DOWNARROWKEY
    CON0058.pulse = True
    PAR0059.game_object = "NLO:Pcontroller"
    PAR0059.property_name = "walk-"
    PAR0060.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0060.operand_a = PAR0059
    PAR0060.operand_b = 0.009999999776482582
    ACT0061.condition = CON0058
    ACT0061.game_object = "NLO:Pcontroller"
    ACT0061.property_name = "walk-"
    ACT0061.property_value = PAR0060
    CON0062.key_code = bge.events.DOWNARROWKEY
    CON0062.pulse = True
    PAR0063.game_object = "NLO:Pcontroller"
    PAR0063.property_name = "walk+"
    ACT0064.condition = CON0062
    ACT0064.game_object = "NLO:Pcontroller"
    ACT0064.property_name = "walk+"
    ACT0064.property_value = PAR0065
    PAR0065.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0065.operand_a = PAR0063
    PAR0065.operand_b = -0.009999999776482582
    ACT0066.condition = CON0055
    ACT0066.game_object = "NLO:Pcontroller"
    ACT0066.property_name = "walk+"
    ACT0066.property_value = PAR0057
    ACT0067.condition = CON0068
    ACT0067.lamp = "NLO:Area"
    ACT0067.color = mathutils.Vector((1.0, 0.006677865982055664, 0.0))
    CON0068.mouse_button = bge.events.LEFTMOUSE
    CON0068.game_object = "NLO:button"
    CON0069.mouse_button = bge.events.LEFTMOUSE
    CON0069.game_object = "NLO:button.001"
    ACT0070.condition = CON0069
    ACT0070.lamp = "NLO:Area"
    ACT0070.color = mathutils.Vector((0.20288240909576416, 1.0, 0.0))
    CON0071.mouse_button = bge.events.LEFTMOUSE
    CON0071.game_object = "NLO:button.002"
    ACT0072.condition = CON0071
    ACT0072.lamp = "NLO:Area"
    ACT0072.color = mathutils.Vector((1.0, 0.75, 0.0))
    network.add_cell(CON0000)
    network.add_cell(PAR0002)
    network.add_cell(CON0005)
    network.add_cell(CON0009)
    network.add_cell(CON0011)
    network.add_cell(CON0016)
    network.add_cell(ACT0018)
    network.add_cell(CON0020)
    network.add_cell(CON0024)
    network.add_cell(PAR0026)
    network.add_cell(CON0028)
    network.add_cell(CON0030)
    network.add_cell(CON0032)
    network.add_cell(CON0034)
    network.add_cell(CON0041)
    network.add_cell(PAR0047)
    network.add_cell(PAR0049)
    network.add_cell(CON0051)
    network.add_cell(PAR0053)
    network.add_cell(CON0055)
    network.add_cell(CON0058)
    network.add_cell(CON0062)
    network.add_cell(CON0068)
    network.add_cell(CON0071)
    network.add_cell(CON0001)
    network.add_cell(ACT0012)
    network.add_cell(ACT0017)
    network.add_cell(PAR0021)
    network.add_cell(PAR0025)
    network.add_cell(ACT0029)
    network.add_cell(CON0033)
    network.add_cell(ACT0038)
    network.add_cell(PAR0042)
    network.add_cell(PAR0044)
    network.add_cell(PAR0046)
    network.add_cell(ACT0050)
    network.add_cell(PAR0054)
    network.add_cell(PAR0059)
    network.add_cell(PAR0063)
    network.add_cell(PAR0065)
    network.add_cell(ACT0067)
    network.add_cell(ACT0072)
    network.add_cell(PAR0003)
    network.add_cell(ACT0013)
    network.add_cell(ACT0022)
    network.add_cell(ACT0027)
    network.add_cell(PAR0035)
    network.add_cell(PAR0043)
    network.add_cell(PAR0048)
    network.add_cell(PAR0056)
    network.add_cell(PAR0060)
    network.add_cell(ACT0064)
    network.add_cell(CON0069)
    network.add_cell(PAR0004)
    network.add_cell(ACT0008)
    network.add_cell(CON0014)
    network.add_cell(CON0019)
    network.add_cell(CON0031)
    network.add_cell(ACT0037)
    network.add_cell(PAR0045)
    network.add_cell(PAR0057)
    network.add_cell(ACT0066)
    network.add_cell(ACT0007)
    network.add_cell(ACT0015)
    network.add_cell(ACT0036)
    network.add_cell(ACT0040)
    network.add_cell(ACT0061)
    network.add_cell(ACT0010)
    network.add_cell(ACT0039)
    network.add_cell(ACT0070)
    network.add_cell(ACT0006)
    network.add_cell(ACT0052)
    network.add_cell(ACT0023)
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
