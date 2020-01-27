# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

#from typing import Any, Text, Dict, List

#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher


#class ActionResSearch(Action):

#      def name(self) -> Text:
 #       return "action_hello_world"
  #    def run(self, dispatcher: CollectingDispatcher,
   #       tracker: Tracker,
    #      domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
     #     dispatcher.utter_message(text="Hello World!")
      #    return []

#from typing import Any, Text, Dict, List

#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher


#class ActionResSearch(Action):

#    def name(self) -> Text:
#         return "action_res_search"

#    def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

       

         
#         myname=tracker.get_slot("name")
#         details=("your country is {} :".format(myname))
#         dispatcher.utter_message(details)
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.core.events import SlotSet
import pandas
from sqlalchemy import create_engine


class ActionResSearch(Action):

    def name(self) -> Text:
        return "action_res_search"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        res=pandas.read_csv("world.csv")
        engine=create_engine("sqlite://",echo=False)
        res.to_sql("ressql",con=engine)

        
        name=tracker.get_slot("name")
        
        
        print(name)
        
# here res=name,city=city,dish=dish

        
        results=engine.execute("SELECT * FROM ressql WHERE country='%s' "%(name))
        for row in results:
            record=row[0]
            a=row[1]
            b=row[2]
            c=row[3]
            d=row[4]
            e=row[5]
           
            # displaying the result
            details=("Your country is {}, its country code is {} and its capital is {}. Here currency is {} and currency code is {} : " .format(a,b,c,d,e))
            dispatcher.utter_message(details)

        
        return []









































