"""
###Exercise 3.20
The program should:

Ask the user for a number of segments of a trip
ask the user for the duration in minutes of each segment
calculate the total travel time
should not generate errors"""
while True:
    try:
        segments = int(input("Enter amount of segments: "))
        break
    except ValueError as e:
        print(e)

total_duration = 0
for i in range(segments):
    while True:
        try:
            total_duration += float(
                input(f'Enter segment duration {i+1}: '))
            break
        except ValueError as e:
            print('Value must be a number!!!')
print(f"Journey´s total amount of time: {total_duration}")
