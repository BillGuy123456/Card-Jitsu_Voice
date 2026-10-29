from py_mp import CommandServer
from py_mp import ServerSideServerCommand
from py_mp.commands import NerworkFlags

import ask_sdk_core.utils as ask_utils
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

Server = CommandServer("172.21.8.7", 5050)

class Card():
    def random():
        return str(range(1, 15)) + random.choice(" fire", " water", " snow") + " card in the color" + random.choice("red", "orange", "yellow", "green", "blue", "purple")
    
    def isAvailable(color, element, value, inv: Inventory):
        for index, card in inv.cards:
            if card.color == color and card.value == value and card.element == element:
                return True
                
        return False
