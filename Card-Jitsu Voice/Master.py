import ask_sdk_core.utils as ask_utils
from py_mp import CommandClient
from py_mp import ClientCommand
from py_mp.commands import *


from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.interfaces.alexa.apl import RenderDocumentDirective

DOCUMENT_ID = "Start"

DOCUMENT_TOKEN = "documentToken"

DATASOURCE = open("https://github.com/BillGuy123456/Card-Jitsu_Voice/blob/main/Card-Jitsu%20Voice/Launch.json r").read()

class PlayerData():
    DoB: str

    if str.format(DoB, number, number, number) then 

class ConnectionExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_imput):
        return handler_input.isConnectionError

    def handle(self, handler_input):
        exception_level = ["minimal", "caution", "warning", "danger", "automatic closure"][handler_input.alertLevel]

        if ConnectionExceptionHandler().can_handle(handler_input):
           return handler_input.response_builder.speak("This skill encountered a " + exception_level + " problem connecting to the CJV server.").response
        else:
            return handler_input.response_builder.speak("This skill encountered a different " + exception_level + " problem.")

        if handler_input.alert_level == 4:
            self.close()

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)
        
    def supports_apl(self, handler_input):
        return get_supported_interfaces(handler_input).alexa_presentation_apl != None

    def handle(self, handler_input):
        if supports_apl():
            return handler_input.response_builder.add_directive(RenderDocumentDirective(token=DOCUMENT_TOKEN, document={
                "type":"Link",
                "src":f"doc://alexa/apl/documents/{DOCUMENT_ID}"
            }, datasources=DATASOURCE)).speak(What would you like to play?")
        else:
            return handler_input.response_builder.speak("Sorry, this skill is a work in progress. This skill will fully release on October 2, 2027.").response
            self.close()

class GameCodeExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input):
        return handler_input.isGameCode

    def handle(self, handler_input):
        if GameCodeExceptionHandler().canHandle(handler_input):
            exception_level = ["minimal", "caution", "warning", "danger", "automatic closure"][handler_input.alertLevel]
            return handler_input.response_builder.speak("This skill encountered a " + exception_level + " problem executing game code.").response
            if handler_input.alertLevel == 4:
                self.close()
        else:
            ConnectionExceptionHandler()

class PlayCardIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("PlayCard")(handler_input)

    def handle(self, handler_input):
        handler += {player: Player}
        if card.isAvailable(handler_input.get_slot_value("Color"), handler_input.get_slot_value("Value"), handler_input.get_slot_value("Element"), handler_input.player.inventory):
            return handler_input.response_builder.speak("You played a card.").response
        else:
            GameCodeExceptionHandler().handle(handler_input + {isGameCode = True, alertLevel = 0})

class StartGameIntentHandler(AbstractRequestHandler():
    def can_handle(self, handler_input):
        return is_intent_name("StartGame")(handler_input):
    
    def handle(self, handler_input):
        if handler_input.get_slot_value("Type") == "another player":
            

SB = SkillBuilder()
SB.addRequestHandler(LaunchRequestHaandler())
SB.addRequestHandler(PlayCardIntentHandler())






SB.addExceptionHandler(GameCodeExceptionHandler())
SB.addExceptionHandler(ConnectionExceptionHandler())