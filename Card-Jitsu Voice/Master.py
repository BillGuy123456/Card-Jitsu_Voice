import ask_sdk_core.utils as ask_utils
from py_mp import CommandClient
from py_mp import ClientCommand
from py_mp.commands import NetworkFlag
import Multiplayer


from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

players: [Player]

class Player():
    data: PlayerData
    inventory: Inventory

class PlayerData():
    DoB: str

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.speak("Sorry, this skill is a work in progress.").response
        self.close()

class PlayCardIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("PlayCard")(handler_input)

    def handle(self, handler_input):
        if card.isAVailable(handler_input.get_slot_value("Color"), handler_input.get_slot_value("Value"), handler_input.get_slot_value("Element"), self.player.inventory):
            return h

SB = SkillBuilder()
SB.addRquestHandler(LaunchRequestHaandler())