************************************************************
 SUBJECT: Algorithms and Data Structures 1
 EXAM: IEFI
 LAST NAME AND FIRST NAME: Malara Carnet Facundo Esteban
 ID: 40751854
 CAREER: Systems Analyst
 YEAR: 2023
 Uploaded to classroom in a compressed folder [Last Name, First Name Rec_2_exam]
 ************************************************************
 Items to evaluate:
 1. Subject contents
 2. Requirements and understanding of instructions
 3. Structure (modularization), readability, and code comments.

Any questions about the statement, consult the teacher!
************************************************************
STATEMENT: "Agenda Program"

Introduction:
    The following program consists of software that simulates a personal agenda.
    The program should allow adding and removing Events from the system, as well as managing event data (Date, Time, Location).

Requirements:
The program must:
*   Have an Event Class with attributes (event_name (unique), date, time, location)
*   Have two Child Classes that use the constructor of the parent class but have one more attribute:
        - PersonalEvent (Attribute: organizer (name of the group organizing))
        - WorkEvent (Attribute: mandatory "True or False" (default = True))
        
*   Four methods must be created for the parent Event class (which will inherit the child classes):
        1. Show information: Which indicates the event_name, date, and location of the event 
        2. Get event type (type of inherited or parent classes)
        3. Set date and time (Set the Date and Time in a single function)
        4. Set location (Set the location)

*   A EventManager class must be created that has the following functions for a menu:

    1.  Create instances of an event and save them in an event list. 
        1.1) It must be verified what type of event instance to create and the parameters. IMPORTANT!: Child classes verify and request parameters
             - event_name: must be unique. Help: verify that no object in the list has that name
             - Date: format (dd/mm/yyyy) -> only verify that the length of the string is 10. Help!: len() method
             - Time: format (hh:mm) -> no verification necessary
             - Location: no specific format -> no verification necessary
        1.2) When creating an event, it is necessary to log it (Write on a new line: event_name-Date-Time-Location-Event_type(class type)) 
             in a file named event_list.txt (Create function in the same manager). IMPORTANT!: verify permissions
        1.3) In case the event instance is a PersonalEvent.
             - For the organizer, the user must choose through a key (shown by the program) 
                from a dictionary of organizers.
             - In case the desired organizer does not exist, it should be "incognito" (HELP: get function of dictionaries)
    2.   List available events, reading the event_list.txt file. IMPORTANT!: Read the file, not the list. 
    
*   The corresponding methods for the menu functions must be created in the corresponding classes
*   Handle possible errors
*   Structure the program according to your own criteria