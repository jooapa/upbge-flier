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
    PAR0004 = nodes.ParameterVector3Simple()
    CON0005 = nodes.ConditionMousePressed()
    ACT0006 = nodes.ActionApplyForce()
    ACT0007 = nodes.ActionMoveTo()
    PAR0008 = nodes.ParameterMouseData()
    PAR0009 = nodes.ParameterArithmeticOp()
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
    PAR0004.input_x = PAR0008.MX
    PAR0004.input_y = PAR0009
    PAR0004.input_z = 0.0
    CON0005.mouse_button_code = bge.events.LEFTMOUSE
    CON0005.pulse = False
    ACT0006.local = True
    ACT0006.condition = ACT0007
    ACT0006.game_object = "NLO:U_O"
    ACT0006.force = mathutils.Vector((0.0, 0.0, 0.0))
    ACT0007.condition = CON0005
    ACT0007.moving_object = "NLO:U_O"
    ACT0007.destination_point = PAR0004.OUTV
    ACT0007.dynamic = False
    ACT0007.speed = 100.0
    ACT0007.distance = 0.0
    PAR0009.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0009.operand_a = PAR0008.MY
    PAR0009.operand_b = -1.0
    network.add_cell(ACT0000)
    network.add_cell(ACT0003)
    network.add_cell(CON0005)
    network.add_cell(PAR0008)
    network.add_cell(CON0001)
    network.add_cell(PAR0009)
    network.add_cell(ACT0002)
    network.add_cell(PAR0004)
    network.add_cell(ACT0007)
    network.add_cell(ACT0006)
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
