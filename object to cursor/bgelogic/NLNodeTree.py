# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionMousePick()
    CON0001 = nodes.ConditionMousePressedOn()
    ACT0002 = nodes.SetLightColor()
    ACT0003 = nodes.ActionTranslate()
    PAR0004 = nodes.ParameterArithmeticOp()
    CON0005 = nodes.ConditionMousePressed()
    PAR0006 = nodes.ParameterMouseData()
    ACT0007 = nodes.ActionTranslate()
    ACT0008 = nodes.ActionMoveTo()
    ACT0009 = nodes.ActionApplyLocation()
    CON0010 = nodes.ConditionOnUpdate()
    PAR0011 = nodes.ParameterVector3Simple()
    ACT0000.condition = None
    ACT0000.camera = None
    ACT0000.property = ""
    ACT0000.xray = False
    ACT0000.distance = 100.0
    CON0001.mouse_button = bge.events.LEFTMOUSE
    CON0001.game_object = "NLO:U_O"
    ACT0002.condition = CON0001
    ACT0002.lamp = "NLO:Light"
    ACT0002.color = mathutils.Vector((1.0, 0.7402560710906982, 0.0))
    ACT0003.condition = None
    ACT0003.moving_object = "NLO:U_O"
    ACT0003.local = False
    ACT0003.vect = mathutils.Vector((0.5399999618530273, 0.0, 0.0))
    ACT0003.speed = 0.23999999463558197
    PAR0004.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0004.operand_a = 0.0
    PAR0004.operand_b = -1.0
    CON0005.mouse_button_code = bge.events.LEFTMOUSE
    CON0005.pulse = False
    ACT0007.condition = None
    ACT0007.moving_object = "NLO:U_O"
    ACT0007.local = True
    ACT0007.vect = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0007.speed = 100.0
    ACT0008.condition = None
    ACT0008.moving_object = "NLO:U_O"
    ACT0008.destination_point = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0008.dynamic = False
    ACT0008.speed = 1.0
    ACT0008.distance = 0.5
    ACT0009.local = True
    ACT0009.condition = CON0005
    ACT0009.game_object = "NLO:U_O"
    ACT0009.movement = PAR0011.OUTV
    PAR0011.input_x = PAR0006.MX
    PAR0011.input_y = 0.0
    PAR0011.input_z = 0.0
    network.add_cell(ACT0000)
    network.add_cell(ACT0003)
    network.add_cell(CON0005)
    network.add_cell(ACT0007)
    network.add_cell(CON0010)
    network.add_cell(CON0001)
    network.add_cell(PAR0004)
    network.add_cell(ACT0008)
    network.add_cell(ACT0002)
    network.add_cell(PAR0006)
    network.add_cell(PAR0011)
    network.add_cell(ACT0009)
    owner["IGNLTree_NodeTree"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__NodeTree')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_NodeTree")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
