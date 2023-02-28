from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreetUser(Action):

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Check if the greeting has already been displayed in the conversation
        if tracker.get_slot("greeting_displayed"):
            return []

        # Set the slot to indicate that the greeting has been displayed
        tracker.slots["greeting_displayed"] = True

        # Display the greeting message
        dispatcher.utter_message(template="utter_greeting")

        return []

class ActionAddNumbers(Action):

    def name(self) -> Text:
        return "action_add_numbers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        num1 = tracker.get_slot("num1")
        num2 = tracker.get_slot("num2")
        result = num1 + num2
        
        dispatcher.utter_message(template="utter_result", operation="sum", num1=num1, num2=num2, result=result)
        
        return []

class ActionSubtractNumbers(Action):

    def name(self) -> Text:
        return "action_subtract_numbers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        num1 = tracker.get_slot("num1")
        num2 = tracker.get_slot("num2")
        result = num1 - num2
        
        dispatcher.utter_message(template="utter_result", operation="difference", num1=num1, num2=num2, result=result)
        
        return []

class ActionMultiplyNumbers(Action):

    def name(self) -> Text:
        return "action_multiply_numbers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        num1 = tracker.get_slot("num1")
        num2 = tracker.get_slot("num2")
        result = num1 * num2
        
        dispatcher.utter_message(template="utter_result", operation="product", num1=num1, num2=num2, result=result)
        
        return []
   
class ActionDivideNumbers(Action):

    def name(self) -> Text:
        return "action_divide_numbers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        num1 = tracker.get_slot("num1")
        num2 = tracker.get_slot("num2")
        result = num1 / num2
        
        dispatcher.utter_message(template="utter_result", operation="quotient", num1=num1, num2=num2, result=result)
        
        return []

