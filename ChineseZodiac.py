import ask_sdk_core
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
sb = SkillBuilder()

class ErrorHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        speech_text = 'Sorry, your skill encountered an error';
        print(exception)
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)
    
    def handle(self, handler_input):
        speech_text = 'Welcome to my Alexa app';
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response

class ChineseZodiacHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("ChineseZodiac")(handler_input)

    def handle(self, handler_input):
        year = handler_input.request_envelope.request.intent.slots['year'].value


        speech_text = "This is my custom intent handler";
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response

    
sb.add_exception_handler(ErrorHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(ChineseZodiacHandler())
    
def handler(event, context):
    return sb.lambda_handler()(event, context)
    
