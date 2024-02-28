"""
Introduction:
    The following program consists of software that simulates a personal agenda.
    The program should allow adding and removing Events from the system, as well 
    as managing event data (Date, Time, Location).

Requirements:
The program must:
*   Have an Event Class with attributes (event_name (unique), date, time, location)
*   Have two Child Classes that use the constructor of the parent class but have one 
    more attribute:
        - PersonalEvent (Attribute: organizer (name of the group organizing))
        - WorkEvent (Attribute: mandatory "True or False" (default = True))
        
*   Four methods must be created for the parent Event class (which will inherit the 
    child classes):
        1. Show information: Which indicates the event_name, date, and location of 
            the event 
        2. Get event type (type of inherited or parent classes)
        3. Set date and time (Set the Date and Time in a single function)
        4. Set location (Set the location)
"""


class Event:
    def __init__(self, name_event, date, hour, place):
        self.name_event = name_event
        self.date = date
        self.hour = hour
        self.place = place

    def show_info(self):
        print(
            f"Name_event: {self.name_event} - date: {self.date} - hour: {self.hour} - place: {self.place}")

    def get_type(self):
        print(f"I´m an event of type: {type(self).__name__}")
        return type(self).__name__

    def set_date_hour(self, date, hour):
        self.date = date
        self.hour = hour

    def set_place(self, place):
        self.place = place


class PersonalEvent(Event):
    def __init__(self, name_event, date, hour, place, organizer):
        super().__init__(name_event, date, hour, place)
        self.organizer = organizer


class LaboralEvent(Event):
    def __init__(self, name_event, date, hour, place, mandatory=True):
        super().__init__(name_event, date, hour, place)
        self.mandatory = mandatory
