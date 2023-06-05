# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionAndNot()
    CON0001 = nodes.ConditionAndNot()
    CON0002 = nodes.ConditionMouseReleased()
    CON0003 = nodes.ConditionNotNone()
    CON0004 = nodes.ConditionMousePressed()
    CON0005 = nodes.ConditionMousePressedOn()
    CON0006 = nodes.ConditionNot()
    CON0007 = nodes.ConditionAnd()
    ACT0008 = nodes.ActionApplyLocation()
    ACT0009 = nodes.ActionApplyLocation()
    CON0000.condition_a = None
    CON0000.condition_b = None
    CON0001.condition_a = None
    CON0001.condition_b = None
    CON0002.mouse_button_code = bge.events.LEFTMOUSE
    CON0002.pulse = True
    CON0003.checked_value = None
    CON0004.mouse_button_code = bge.events.LEFTMOUSE
    CON0004.pulse = False
    CON0005.mouse_button = bge.events.RIGHTMOUSE
    CON0005.game_object = "NLO:U_O"
    CON0006.condition = CON0002
    CON0007.condition_a = CON0005
    CON0007.condition_b = CON0006
    ACT0008.local = True
    ACT0008.condition = CON0007
    ACT0008.game_object = "NLO:U_O"
    ACT0008.movement = mathutils.Vector((0.0, 0.0, 0.17999997735023499))
    ACT0009.local = True
    ACT0009.condition = CON0005
    ACT0009.game_object = "NLO:U_O"
    ACT0009.movement = mathutils.Vector((0.0899999737739563, 0.0, 0.0))
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(CON0004)
    network.add_cell(CON0006)
    network.add_cell(CON0001)
    network.add_cell(CON0005)
    network.add_cell(ACT0009)
    network.add_cell(CON0003)
    network.add_cell(CON0007)
    network.add_cell(ACT0008)
    owner["IGNLTree_toucher"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__toucher')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_toucher")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
