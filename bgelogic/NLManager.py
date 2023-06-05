# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionApplyLocation()
    CON0001 = nodes.ConditionKeyPressed()
    CON0002 = nodes.ConditionKeyPressed()
    CON0003 = nodes.ConditionKeyPressed()
    CON0004 = nodes.ConditionKeyPressed()
    CON0005 = nodes.ConditionKeyPressed()
    ACT0006 = nodes.ActionApplyLocation()
    ACT0007 = nodes.ActionApplyLocation()
    ACT0008 = nodes.ActionApplyLocation()
    CON0009 = nodes.ConditionKeyPressed()
    ACT0010 = nodes.ActionApplyLocation()
    ACT0011 = nodes.ActionApplyLocation()
    CON0012 = nodes.ConditionMousePressedOn()
    CON0013 = nodes.ConditionMouseTargeting()
    PAR0014 = nodes.ParameterObjectProperty()
    PAR0015 = nodes.ParameterObjectProperty()
    PAR0016 = nodes.ParameterArithmeticOp()
    PAR0017 = nodes.ParameterArithmeticOp()
    CON0018 = nodes.ConditionMouseScrolled()
    ACT0019 = nodes.ActionSetGameObjectGameProperty()
    ACT0020 = nodes.ActionSetGameObjectGameProperty()
    ACT0021 = nodes.ActionSetCameraFov()
    CON0022 = nodes.ConditionMouseScrolled()
    ACT0023 = nodes.ActionSetCameraFov()
    CON0024 = nodes.ConditionKeyPressed()
    ACT0025 = nodes.ActionToggleGameObjectGameProperty()
    ACT0026 = nodes.SetLightColor()
    CON0027 = nodes.ConditionMousePressedOn()
    ACT0028 = nodes.ActionSetCameraFov()
    CON0029 = nodes.ConditionNot()
    ACT0030 = nodes.ActionMouseLook()
    CON0031 = nodes.ConditionKeyPressed()
    ACT0032 = nodes.ActionSetMouseCursorVisibility()
    ACT0033 = nodes.ActionToggleGameObjectGameProperty()
    CON0034 = nodes.ConditionAnd()
    CON0035 = nodes.ConditionMouseMoved()
    PAR0036 = nodes.ParameterObjectProperty()
    ACT0037 = nodes.SetEeveeBloom()
    ACT0038 = nodes.ActionSetMouseCursorVisibility()
    CON0039 = nodes.ConditionOnUpdate()
    PAR0040 = nodes.ParameterObjectProperty()
    PAR0041 = nodes.ParameterSwitchValue()
    ACT0042 = nodes.ActionSetGameObjectVisibility()
    CON0043 = nodes.GE_OnInit()
    ACT0044 = nodes.ActionSetGameObjectVisibility()
    ACT0000.local = True
    ACT0000.condition = CON0001
    ACT0000.game_object = "NLO:U_O"
    ACT0000.movement = mathutils.Vector((0.0, 0.07999999821186066, 0.0))
    CON0001.key_code = bge.events.SPACEKEY
    CON0001.pulse = True
    CON0002.key_code = bge.events.WKEY
    CON0002.pulse = True
    CON0003.key_code = bge.events.SKEY
    CON0003.pulse = True
    CON0004.key_code = bge.events.AKEY
    CON0004.pulse = True
    CON0005.key_code = bge.events.DKEY
    CON0005.pulse = True
    ACT0006.local = True
    ACT0006.condition = CON0003
    ACT0006.game_object = "NLO:U_O"
    ACT0006.movement = mathutils.Vector((0.0, 0.0, 0.07999999821186066))
    ACT0007.local = True
    ACT0007.condition = CON0002
    ACT0007.game_object = "NLO:U_O"
    ACT0007.movement = mathutils.Vector((0.0, 0.0, -0.07999999821186066))
    ACT0008.local = True
    ACT0008.condition = CON0004
    ACT0008.game_object = "NLO:U_O"
    ACT0008.movement = mathutils.Vector((-0.07999999821186066, 0.0, 0.0))
    CON0009.key_code = bge.events.LEFTSHIFTKEY
    CON0009.pulse = True
    ACT0010.local = True
    ACT0010.condition = CON0005
    ACT0010.game_object = "NLO:U_O"
    ACT0010.movement = mathutils.Vector((0.07999999821186066, 0.0, 0.0))
    ACT0011.local = True
    ACT0011.condition = CON0009
    ACT0011.game_object = "NLO:U_O"
    ACT0011.movement = mathutils.Vector((0.0, -0.07999999821186066, 0.0))
    CON0012.mouse_button = bge.events.LEFTMOUSE
    CON0012.game_object = None
    CON0013.game_object = None
    PAR0014.game_object = "NLO:Pcontroller"
    PAR0014.property_name = "fov"
    PAR0015.game_object = "NLO:Pcontroller"
    PAR0015.property_name = "fov"
    PAR0016.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0016.operand_a = PAR0015
    PAR0016.operand_b = 4.0
    PAR0017.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0017.operand_a = PAR0015
    PAR0017.operand_b = 4.0
    CON0018.wheel_direction = 2
    ACT0019.condition = ACT0023.OUT
    ACT0019.game_object = "NLO:Pcontroller"
    ACT0019.property_name = "fov"
    ACT0019.property_value = PAR0016
    ACT0020.condition = ACT0021.OUT
    ACT0020.game_object = "NLO:Pcontroller"
    ACT0020.property_name = "fov"
    ACT0020.property_value = PAR0017
    ACT0021.condition = CON0022
    ACT0021.camera = "NLO:Camera"
    ACT0021.fov = PAR0017
    CON0022.wheel_direction = 1
    ACT0023.condition = CON0018
    ACT0023.camera = "NLO:Camera"
    ACT0023.fov = PAR0016
    CON0024.key_code = bge.events.BKEY
    CON0024.pulse = False
    ACT0025.condition = CON0024
    ACT0025.game_object = "NLO:Pcontroller"
    ACT0025.property_name = "bloomTrue"
    ACT0026.condition = CON0027
    ACT0026.lamp = "NLO:Area"
    ACT0026.color = mathutils.Vector((0.20499277114868164, 1.0, 0.0))
    CON0027.mouse_button = bge.events.LEFTMOUSE
    CON0027.game_object = "NLO:ui"
    ACT0028.condition = CON0043
    ACT0028.camera = "NLO:Camera"
    ACT0028.fov = PAR0015
    CON0029.condition = PAR0040
    ACT0030.axis = 1
    ACT0030.condition = CON0034
    ACT0030.game_object_x = "NLO:Pcontroller"
    ACT0030.game_object_y = None
    ACT0030.inverted = {'x': False, 'y': True}
    ACT0030.sensitivity = 0.46000003814697266
    ACT0030.use_cap_z = False
    ACT0030.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0030.use_cap_y = False
    ACT0030.cap_y = mathutils.Vector((0.0, 3.1241393089294434))
    ACT0030.smooth = 0.25833332538604736
    CON0031.key_code = bge.events.IKEY
    CON0031.pulse = False
    ACT0032.condition = None
    ACT0032.visibility_status = False
    ACT0033.condition = CON0031
    ACT0033.game_object = "NLO:Pcontroller"
    ACT0033.property_name = "uiTrue"
    CON0034.condition_a = CON0035
    CON0034.condition_b = CON0029
    CON0035.pulse = True
    PAR0036.game_object = "NLO:Pcontroller"
    PAR0036.property_name = "bloomTrue"
    ACT0037.condition = CON0039
    ACT0037.value = PAR0036
    ACT0038.condition = CON0039
    ACT0038.visibility_status = PAR0040
    PAR0040.game_object = "NLO:Pcontroller"
    PAR0040.property_name = "uiTrue"
    PAR0041.state = False
    ACT0042.condition = ACT0033.OUT
    ACT0042.game_object = "NLO:ui"
    ACT0042.visible = PAR0040
    ACT0042.recursive = True
    ACT0044.condition = CON0043
    ACT0044.game_object = "NLO:ui"
    ACT0044.visible = False
    ACT0044.recursive = True
    network.add_cell(CON0001)
    network.add_cell(CON0003)
    network.add_cell(CON0005)
    network.add_cell(CON0009)
    network.add_cell(ACT0011)
    network.add_cell(CON0013)
    network.add_cell(PAR0015)
    network.add_cell(PAR0017)
    network.add_cell(CON0022)
    network.add_cell(CON0024)
    network.add_cell(CON0027)
    network.add_cell(CON0031)
    network.add_cell(ACT0033)
    network.add_cell(CON0035)
    network.add_cell(CON0039)
    network.add_cell(PAR0041)
    network.add_cell(CON0043)
    network.add_cell(ACT0000)
    network.add_cell(CON0004)
    network.add_cell(ACT0008)
    network.add_cell(CON0012)
    network.add_cell(PAR0016)
    network.add_cell(ACT0021)
    network.add_cell(ACT0025)
    network.add_cell(ACT0028)
    network.add_cell(ACT0032)
    network.add_cell(PAR0036)
    network.add_cell(PAR0040)
    network.add_cell(ACT0044)
    network.add_cell(CON0002)
    network.add_cell(ACT0007)
    network.add_cell(PAR0014)
    network.add_cell(ACT0020)
    network.add_cell(ACT0026)
    network.add_cell(ACT0037)
    network.add_cell(ACT0042)
    network.add_cell(ACT0006)
    network.add_cell(CON0018)
    network.add_cell(ACT0023)
    network.add_cell(ACT0038)
    network.add_cell(ACT0010)
    network.add_cell(CON0029)
    network.add_cell(CON0034)
    network.add_cell(ACT0019)
    network.add_cell(ACT0030)
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
