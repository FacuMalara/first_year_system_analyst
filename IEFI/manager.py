""" A EventManager class must be created that has the following functions for a menu:

1.  Create instances of an event and save them in an event list. 

    1.1) It must be verified what type of event instance to create and the parameters. 
            IMPORTANT!: Child classes verify and request parameters
             - event_name: must be unique. Help: verify that no object in the list has that name
             - Date: format (dd/mm/yyyy) -> only verify that the length of the string is 10. 
                Help!: len() method
             - Time: format (hh:mm) -> no verification necessary
             - Location: no specific format -> no verification necessary

    1.2) When creating an event, it is necessary to log it (Write on a new line: 
                event_name-Date-Time-Location-Event_type(class type)) 
             in a file named event_list.txt (Create function in the same manager). 
             IMPORTANT!: verify permissions

    1.3) In case the event instance is a PersonalEvent.
             - For the organizer, the user must choose through a key (shown by the program) 
                from a dictionary of organizers.
             - In case the desired organizer does not exist, it should be "incognito" 
             (HELP: get function of dictionaries)

     2.   List available events, reading the event_list.txt file. IMPORTANT!: Read the file, not the list. 


"""


from classes import *
import os


class EventManager:
    def __init__(self):
        self.event_list: list[Event] = []

    def create_event(self):

        organizer = {
            "FA": "family",
            "FD": "friends",
            "PS": "personal"
        }

        event_name = input("Nombre del evento: ")
        verify_name = self.verify_name(event_name)
        if verify_name:
            date = input("(dd/mm/yyyy): ")
            verify_date = self.verify_date(date)
            if verify_date == True:
                hour = input("Event hour (hh:mm): ")
                place = input("Event place: ")
                type = input(
                    "Insert event type 'Event' 'PersonalEvent' 'LaboralEvent': ").lower()
                if type == 'PersonalEvent':
                    print(organizer)
                    organizer = input("Organizer: ")
                    ver_organizer = self.verify_organizer(
                        organizer)
                    print(ver_organizer)
                    event = PersonalEvent(
                        event_name, date, hour, place, organizer)
                    event_txt = f"{event_name} - {date} - {hour} - {place} - {organizer}"
                elif type == 'laboral event':
                    mandatory = True
                    event = LaboralEvent(
                        event_name, date, hour, place, mandatory)
                    event_txt = f"{event_name} - {date} - {hour} - {place} - {mandatory}"
                elif type == 'event':
                    event = Event(event_name, date, hour, place)
                    event_txt = f"{event_name} - {date} - {hour} - {place}"
                else:
                    print("Incorrect income")
                    return
            else:
                print("Incorrect date")
        else:
            print("Event name already exists")
            return
        self.event_list.append(event)
        self.log_event(event_txt)

    def verify_organizer(self, organizer):
        organizers = {
            "FA": "family",
            "FD": "Friends",
            "PS": "Personal"
        }
        return organizers.get(organizer, "unknown")

    def log_event(self, event_txt):
        try:
            file = open(
                f"{os.path.abspath(os.path.dirname(__file__))}//event.txt", "+a")
            file.write(event_txt + "\n")
            file.close()
        except:
            print("File is not found")

    def verify_name(self, event_name):
        flag = True
        while flag:
            for event in self.event_list:
                if event.event_name == event_name:
                    flag = False
                    return flag
            return True

    def verify_date(self, date):
        if len(date) == 10:
            return True
        else:
            return False

    def read_event_list(self):
        try:
            file = open(
                f"{os.path.abspath(os.path.dirname(__file__))}//event.txt", "r")
            print(file.read())
            file.close()
        except:
            print("Unknown file")
