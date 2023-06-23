# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionMousePressedOn()
    CON0001 = nodes.ConditionMousePressed()
    CON0002 = nodes.ConditionMouseTargeting()
    CON0003 = nodes.ConditionOnUpdate()
    CON0004 = nodes.ConditionKeyPressed()
    CON0005 = nodes.ConditionAndList()
    CON0006 = nodes.ConditionOrList()
    CON0007 = nodes.GE_OnInit()
    ACT0008 = nodes.ActionPlayAction()
    ACT0009 = nodes.ActionPlayAction()
    CON0010 = nodes.ConditionKeyPressed()
    ACT0011 = nodes.ActionPlayAction()
    CON0000.mouse_button = bge.events.LEFTMOUSE
    CON0000.game_object = "NLO:U_O"
    CON0001.mouse_button_code = bge.events.LEFTMOUSE
    CON0001.pulse = True
    CON0002.game_object = "NLO:U_O"
    CON0004.key_code = bge.events.AKEY
    CON0004.pulse = False
    CON0005.ca = True
    CON0005.cb = True
    CON0005.cc = True
    CON0005.cd = True
    CON0005.ce = True
    CON0005.cf = True
    CON0006.ca = None
    CON0006.cb = None
    CON0006.cc = None
    CON0006.cd = None
    CON0006.ce = None
    CON0006.cf = None
    ACT0008.condition = CON0004
    ACT0008.game_object = "NLO:U_O"
    ACT0008.action_name = "left"
    ACT0008.start_frame = 0.0
    ACT0008.end_frame = 9.0
    ACT0008.layer = 0
    ACT0008.priority = 1
    ACT0008.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0008.stop = False
    ACT0008.layer_weight = 1.0
    ACT0008.speed = 1.0
    ACT0008.blendin = 0.0
    ACT0008.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0009.condition = ACT0011.FINISHED
    ACT0009.game_object = "NLO:U_O"
    ACT0009.action_name = "idle"
    ACT0009.start_frame = 0.0
    ACT0009.end_frame = 15.0
    ACT0009.layer = 0
    ACT0009.priority = 0
    ACT0009.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0009.stop = False
    ACT0009.layer_weight = 1.0
    ACT0009.speed = 1.0
    ACT0009.blendin = 0.0
    ACT0009.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    CON0010.key_code = bge.events.DKEY
    CON0010.pulse = False
    ACT0011.condition = CON0010
    ACT0011.game_object = "NLO:U_O"
    ACT0011.action_name = "right"
    ACT0011.start_frame = 0.0
    ACT0011.end_frame = 9.0
    ACT0011.layer = 0
    ACT0011.priority = 1
    ACT0011.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0011.stop = False
    ACT0011.layer_weight = 1.0
    ACT0011.speed = 1.0
    ACT0011.blendin = 0.0
    ACT0011.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(CON0004)
    network.add_cell(CON0006)
    network.add_cell(ACT0008)
    network.add_cell(CON0010)
    network.add_cell(CON0001)
    network.add_cell(CON0005)
    network.add_cell(ACT0011)
    network.add_cell(CON0003)
    network.add_cell(ACT0009)
    network.add_cell(CON0007)
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
