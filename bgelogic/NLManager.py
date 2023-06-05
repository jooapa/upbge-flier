# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    PAR0000 = nodes.ParameterArithmeticOp()
    CON0001 = nodes.ConditionMouseScrolled()
    ACT0002 = nodes.ActionSetGameObjectGameProperty()
    CON0003 = nodes.ConditionMouseScrolled()
    ACT0004 = nodes.ActionSetCameraFov()
    CON0005 = nodes.ConditionKeyPressed()
    ACT0006 = nodes.ActionToggleGameObjectGameProperty()
    ACT0007 = nodes.ActionSetCameraFov()
    CON0008 = nodes.ConditionNot()
    CON0009 = nodes.ConditionKeyPressed()
    CON0010 = nodes.ConditionAnd()
    CON0011 = nodes.ConditionMouseMoved()
    PAR0012 = nodes.ParameterObjectProperty()
    ACT0013 = nodes.ActionSetMouseCursorVisibility()
    CON0014 = nodes.GE_OnInit()
    CON0015 = nodes.ConditionKeyPressed()
    CON0016 = nodes.ConditionKeyPressed()
    CON0017 = nodes.ConditionKeyPressed()
    CON0018 = nodes.ConditionKeyPressed()
    ACT0019 = nodes.ActionApplyLocation()
    ACT0020 = nodes.ActionApplyLocation()
    ACT0021 = nodes.ActionApplyLocation()
    ACT0022 = nodes.ActionApplyLocation()
    ACT0023 = nodes.ActionApplyLocation()
    CON0024 = nodes.ConditionKeyPressed()
    PAR0025 = nodes.ParameterObjectProperty()
    PAR0026 = nodes.ParameterVector3Simple()
    PAR0027 = nodes.ParameterVector3Simple()
    PAR0028 = nodes.ParameterVector3Simple()
    PAR0029 = nodes.ParameterVector3Simple()
    PAR0030 = nodes.ParameterObjectProperty()
    PAR0031 = nodes.ParameterVector3Simple()
    PAR0032 = nodes.ParameterVector3Simple()
    ACT0033 = nodes.ActionApplyLocation()
    CON0034 = nodes.ConditionKeyPressed()
    ACT0035 = nodes.ActionSetGameObjectGameProperty()
    PAR0036 = nodes.ParameterObjectProperty()
    PAR0037 = nodes.ParameterArithmeticOp()
    CON0038 = nodes.ConditionKeyPressed()
    PAR0039 = nodes.ParameterObjectProperty()
    PAR0040 = nodes.ParameterArithmeticOp()
    CON0041 = nodes.ConditionKeyPressed()
    PAR0042 = nodes.ParameterObjectProperty()
    PAR0043 = nodes.ParameterArithmeticOp()
    ACT0044 = nodes.ActionSetGameObjectGameProperty()
    CON0045 = nodes.ConditionKeyPressed()
    PAR0046 = nodes.ParameterObjectProperty()
    ACT0047 = nodes.ActionSetGameObjectGameProperty()
    PAR0048 = nodes.ParameterArithmeticOp()
    ACT0049 = nodes.ActionSetGameObjectGameProperty()
    CON0050 = nodes.ConditionKeyPressed()
    ACT0051 = nodes.ActionSetGameObjectGameProperty()
    ACT0052 = nodes.ActionSetCameraFov()
    PAR0053 = nodes.ParameterObjectProperty()
    PAR0054 = nodes.ParameterArithmeticOp()
    ACT0055 = nodes.ActionMouseLook()
    PAR0056 = nodes.ParameterObjectProperty()
    CON0057 = nodes.ConditionKeyPressed()
    ACT0058 = nodes.ActionSetGameObjectGameProperty()
    CON0059 = nodes.ConditionKeyPressed()
    ACT0060 = nodes.ActionSetGameObjectGameProperty()
    PAR0061 = nodes.ParameterObjectProperty()
    PAR0062 = nodes.ParameterArithmeticOp()
    PAR0063 = nodes.ParameterArithmeticOp()
    PAR0064 = nodes.ParameterObjectProperty()
    CON0065 = nodes.ConditionOnUpdate()
    ACT0066 = nodes.SetEeveeBloom()
    ACT0067 = nodes.ActionToggleGameObjectGameProperty()
    ACT0068 = nodes.ActionSetGameObjectVisibility()
    PAR0069 = nodes.ParameterObjectProperty()
    ACT0070 = nodes.ActionSetGameObjectVisibility()
    CON0071 = nodes.ConditionMousePressedOn()
    ACT0072 = nodes.ParameterPythonModuleFunction()
    PAR0000.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0000.operand_a = PAR0053
    PAR0000.operand_b = 4.0
    CON0001.wheel_direction = 2
    ACT0002.condition = ACT0004.OUT
    ACT0002.game_object = "NLO:Pcontroller"
    ACT0002.property_name = "fov"
    ACT0002.property_value = PAR0000
    CON0003.wheel_direction = 1
    ACT0004.condition = CON0001
    ACT0004.camera = "NLO:Camera"
    ACT0004.fov = PAR0000
    CON0005.key_code = bge.events.BKEY
    CON0005.pulse = False
    ACT0006.condition = CON0005
    ACT0006.game_object = "NLO:Pcontroller"
    ACT0006.property_name = "bloomTrue"
    ACT0007.condition = CON0014
    ACT0007.camera = "NLO:Camera"
    ACT0007.fov = PAR0053
    CON0008.condition = PAR0069
    CON0009.key_code = bge.events.IKEY
    CON0009.pulse = False
    CON0010.condition_a = CON0011
    CON0010.condition_b = CON0008
    CON0011.pulse = True
    PAR0012.game_object = "NLO:Pcontroller"
    PAR0012.property_name = "bloomTrue"
    ACT0013.condition = CON0065
    ACT0013.visibility_status = PAR0069
    CON0015.key_code = bge.events.SKEY
    CON0015.pulse = True
    CON0016.key_code = bge.events.DKEY
    CON0016.pulse = True
    CON0017.key_code = bge.events.LEFTSHIFTKEY
    CON0017.pulse = True
    CON0018.key_code = bge.events.WKEY
    CON0018.pulse = True
    ACT0019.local = True
    ACT0019.condition = CON0018
    ACT0019.game_object = "NLO:U_O"
    ACT0019.movement = PAR0026.OUTV
    ACT0020.local = True
    ACT0020.condition = CON0050
    ACT0020.game_object = "NLO:U_O"
    ACT0020.movement = PAR0027.OUTV
    ACT0021.local = True
    ACT0021.condition = CON0015
    ACT0021.game_object = "NLO:U_O"
    ACT0021.movement = PAR0032.OUTV
    ACT0022.local = True
    ACT0022.condition = CON0016
    ACT0022.game_object = "NLO:U_O"
    ACT0022.movement = PAR0031.OUTV
    ACT0023.local = True
    ACT0023.condition = CON0017
    ACT0023.game_object = "NLO:U_O"
    ACT0023.movement = PAR0028.OUTV
    CON0024.key_code = bge.events.SPACEKEY
    CON0024.pulse = True
    PAR0025.game_object = "NLO:Pcontroller"
    PAR0025.property_name = "walk-"
    PAR0026.input_x = 0.0
    PAR0026.input_y = 0.0
    PAR0026.input_z = PAR0025
    PAR0027.input_x = PAR0025
    PAR0027.input_y = 0.0
    PAR0027.input_z = 0.0
    PAR0028.input_x = 0.0
    PAR0028.input_y = PAR0025
    PAR0028.input_z = 0.0
    PAR0029.input_x = 0.0
    PAR0029.input_y = PAR0030
    PAR0029.input_z = 0.0
    PAR0030.game_object = "NLO:Pcontroller"
    PAR0030.property_name = "walk+"
    PAR0031.input_x = PAR0030
    PAR0031.input_y = 0.0
    PAR0031.input_z = 0.0
    PAR0032.input_x = 0.0
    PAR0032.input_y = 0.0
    PAR0032.input_z = PAR0030
    ACT0033.local = True
    ACT0033.condition = CON0024
    ACT0033.game_object = "NLO:U_O"
    ACT0033.movement = PAR0029.OUTV
    CON0034.key_code = bge.events.UPARROWKEY
    CON0034.pulse = True
    ACT0035.condition = CON0034
    ACT0035.game_object = "NLO:Pcontroller"
    ACT0035.property_name = "walk-"
    ACT0035.property_value = PAR0037
    PAR0036.game_object = "NLO:Pcontroller"
    PAR0036.property_name = "walk-"
    PAR0037.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0037.operand_a = PAR0036
    PAR0037.operand_b = -0.009999999776482582
    CON0038.key_code = bge.events.UPARROWKEY
    CON0038.pulse = True
    PAR0039.game_object = "NLO:Pcontroller"
    PAR0039.property_name = "walk+"
    PAR0040.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0040.operand_a = PAR0039
    PAR0040.operand_b = 0.009999999776482582
    CON0041.key_code = bge.events.DOWNARROWKEY
    CON0041.pulse = True
    PAR0042.game_object = "NLO:Pcontroller"
    PAR0042.property_name = "walk-"
    PAR0043.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0043.operand_a = PAR0042
    PAR0043.operand_b = 0.009999999776482582
    ACT0044.condition = CON0041
    ACT0044.game_object = "NLO:Pcontroller"
    ACT0044.property_name = "walk-"
    ACT0044.property_value = PAR0043
    CON0045.key_code = bge.events.DOWNARROWKEY
    CON0045.pulse = True
    PAR0046.game_object = "NLO:Pcontroller"
    PAR0046.property_name = "walk+"
    ACT0047.condition = CON0045
    ACT0047.game_object = "NLO:Pcontroller"
    ACT0047.property_name = "walk+"
    ACT0047.property_value = PAR0048
    PAR0048.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0048.operand_a = PAR0046
    PAR0048.operand_b = -0.009999999776482582
    ACT0049.condition = CON0038
    ACT0049.game_object = "NLO:Pcontroller"
    ACT0049.property_name = "walk+"
    ACT0049.property_value = PAR0040
    CON0050.key_code = bge.events.AKEY
    CON0050.pulse = True
    ACT0051.condition = ACT0052.OUT
    ACT0051.game_object = "NLO:Pcontroller"
    ACT0051.property_name = "fov"
    ACT0051.property_value = PAR0054
    ACT0052.condition = CON0003
    ACT0052.camera = "NLO:Camera"
    ACT0052.fov = PAR0054
    PAR0053.game_object = "NLO:Pcontroller"
    PAR0053.property_name = "fov"
    PAR0054.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0054.operand_a = PAR0053
    PAR0054.operand_b = 4.0
    ACT0055.axis = 1
    ACT0055.condition = CON0010
    ACT0055.game_object_x = "NLO:Pcontroller"
    ACT0055.game_object_y = None
    ACT0055.inverted = {'x': False, 'y': True}
    ACT0055.sensitivity = PAR0056
    ACT0055.use_cap_z = False
    ACT0055.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0055.use_cap_y = False
    ACT0055.cap_y = mathutils.Vector((0.0, 3.1241393089294434))
    ACT0055.smooth = 0.25833332538604736
    PAR0056.game_object = "NLO:Pcontroller"
    PAR0056.property_name = "sensitivity"
    CON0057.key_code = bge.events.LEFTARROWKEY
    CON0057.pulse = True
    ACT0058.condition = CON0057
    ACT0058.game_object = "NLO:Pcontroller"
    ACT0058.property_name = "sensitivity"
    ACT0058.property_value = PAR0063
    CON0059.key_code = bge.events.RIGHTARROWKEY
    CON0059.pulse = True
    ACT0060.condition = CON0059
    ACT0060.game_object = "NLO:Pcontroller"
    ACT0060.property_name = "sensitivity"
    ACT0060.property_value = PAR0062
    PAR0061.game_object = "NLO:Pcontroller"
    PAR0061.property_name = "sensitivity"
    PAR0062.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0062.operand_a = PAR0061
    PAR0062.operand_b = 0.019999999552965164
    PAR0063.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0063.operand_a = PAR0064
    PAR0063.operand_b = -0.019999999552965164
    PAR0064.game_object = "NLO:Pcontroller"
    PAR0064.property_name = "sensitivity"
    ACT0066.condition = CON0065
    ACT0066.value = PAR0012
    ACT0067.condition = CON0009
    ACT0067.game_object = "NLO:Pcontroller"
    ACT0067.property_name = "uiTrue"
    ACT0068.condition = ACT0067.OUT
    ACT0068.game_object = "NLO:ui"
    ACT0068.visible = PAR0069
    ACT0068.recursive = True
    PAR0069.game_object = "NLO:Pcontroller"
    PAR0069.property_name = "uiTrue"
    ACT0070.condition = CON0014
    ACT0070.game_object = "NLO:ui"
    ACT0070.visible = True
    ACT0070.recursive = True
    CON0071.mouse_button = bge.events.LEFTMOUSE
    CON0071.game_object = "NLO:char1"
    ACT0072.condition = CON0071
    ACT0072.module_name = "hideCollection"
    ACT0072.module_func = ""
    ACT0072.arg = nodes.Invalid()
    network.add_cell(CON0001)
    network.add_cell(CON0003)
    network.add_cell(CON0005)
    network.add_cell(CON0009)
    network.add_cell(CON0011)
    network.add_cell(CON0014)
    network.add_cell(CON0016)
    network.add_cell(CON0018)
    network.add_cell(CON0024)
    network.add_cell(PAR0030)
    network.add_cell(PAR0032)
    network.add_cell(CON0034)
    network.add_cell(PAR0036)
    network.add_cell(CON0038)
    network.add_cell(CON0041)
    network.add_cell(CON0045)
    network.add_cell(CON0050)
    network.add_cell(PAR0053)
    network.add_cell(PAR0056)
    network.add_cell(CON0059)
    network.add_cell(PAR0061)
    network.add_cell(PAR0064)
    network.add_cell(ACT0067)
    network.add_cell(PAR0069)
    network.add_cell(CON0071)
    network.add_cell(PAR0000)
    network.add_cell(ACT0004)
    network.add_cell(ACT0007)
    network.add_cell(PAR0012)
    network.add_cell(CON0015)
    network.add_cell(ACT0021)
    network.add_cell(PAR0025)
    network.add_cell(PAR0027)
    network.add_cell(PAR0029)
    network.add_cell(ACT0033)
    network.add_cell(PAR0037)
    network.add_cell(PAR0042)
    network.add_cell(PAR0046)
    network.add_cell(PAR0048)
    network.add_cell(PAR0054)
    network.add_cell(CON0057)
    network.add_cell(PAR0062)
    network.add_cell(CON0065)
    network.add_cell(ACT0068)
    network.add_cell(ACT0072)
    network.add_cell(ACT0002)
    network.add_cell(CON0008)
    network.add_cell(ACT0013)
    network.add_cell(ACT0020)
    network.add_cell(PAR0026)
    network.add_cell(PAR0031)
    network.add_cell(PAR0039)
    network.add_cell(PAR0043)
    network.add_cell(ACT0047)
    network.add_cell(ACT0052)
    network.add_cell(ACT0060)
    network.add_cell(ACT0066)
    network.add_cell(ACT0006)
    network.add_cell(CON0017)
    network.add_cell(ACT0022)
    network.add_cell(PAR0028)
    network.add_cell(PAR0040)
    network.add_cell(ACT0049)
    network.add_cell(PAR0063)
    network.add_cell(CON0010)
    network.add_cell(ACT0023)
    network.add_cell(ACT0044)
    network.add_cell(ACT0055)
    network.add_cell(ACT0070)
    network.add_cell(ACT0019)
    network.add_cell(ACT0051)
    network.add_cell(ACT0035)
    network.add_cell(ACT0058)
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
