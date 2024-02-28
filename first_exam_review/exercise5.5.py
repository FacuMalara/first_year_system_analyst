"""
Exercise 5.5
Create a function that should:

Ask the user for a number of segments of a trip
Ask the user for the duration in minutes of each segment (use lists)
Calculate the total travel time (show in hours)
All possible errors should not appear and should be taken into account
"""


def journey():
    list = []
    time = 0
    try:
        while True:
            segments = input("Enter amount of segments: ")
            if segments.isnumeric():
                segments = int(segments)
                break
            else:
                print("Invalid character")

        for i in range(segments):
            while True:
                segment_duration = (
                    input(f"Enter segment duration {i+1}: "))
                if segment_duration.isnumeric():
                    segment_duration = int(segment_duration)
                    list.append(segment_duration)
                    time = segment_duration + time
                    break
                else:
                    print("Wrong income")

        print(f"Journey has a total duration of {time} hours")
    except ValueError as e:
        print(f"Error {e}")


journey()
