from app.bot import BaseProcessor, BotProcessorFactory
from splitwise import Splitwise
from splitwise.expense import Expense
from splitwise.user import ExpenseUser
from splitwise.group import Group
from splitwise.debt import Debt
from datetime import datetime, timedelta
from botsplitwise import BotSplitwise
from botexception import BotException, LoginException
from constants import BotConstants, ErrorMessages
from flask import current_app as app
import random

class SplitwiseBotProcessorFactory(BotProcessorFactory):
    class ProcessorType(object):
        '''
        Processor Type
        '''
        HELP_PROCESSOR = "help"

    def __init__(self):
        super(SplitwiseBotProcessorFactory, self).__init__()

    def getProcessor(self, action):

        if action == SplitwiseBotProcessorFactory.ProcessorType.HELP_PROCESSOR:
            return HelpProcessor()

        else:
            return UnknownProcessor()


class HelpProcessor:
    help = "How much do i owe [John] \n" \
           "How much did i spend in last 7 days\n" \
    "List/show my bills for last 5 days\n" \
    "I paid John 10$ [in group Hangout]\n" \
    "I owe John 10$ [in group Hangout]"


    help_fix = "You can ask me following queries \n\n"


    @staticmethod
    def getHelp():
        return HelpProcessor.help_fix + HelpProcessor.help

    def __init__(self):
        pass


    def process(self, input):
        app.logger.debug("Processing help request")
        return HelpProcessor.getHelp()

class UnknownProcessor:
   
    default_text = "Sorry, i didn't understand."
    
    @staticmethod
    def getHelp():
        return UnknownProcessor.default_text 

    def __init__(self):
        pass


    def process(self, input):
        app.logger.debug("Processing help request")
        return HelpProcessor.getHelp()

class GreetingProcessor:
    greetings = [
        "Hey, How can i help you?",
        "Hello, may i help you in any way?",
        "Hi, do you need any help?"
    ]

    def __init__(self):
        pass

    def process(self, input):
        app.logger.debug("Processing Greeting Request")
        return random.choice(GreetingProcessor.greetings)