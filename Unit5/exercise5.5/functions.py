"""Functions file"""


def ask():
    try:
        list = []
        segments = int(input("\nEnter amount of segments: "))
        total_time = 0
        for segment in range(segments):
            time_per_segment = float(
                input(f"Enter segment length(hours) {segment+1}: "))
            total_time += time_per_segment
            list.append(time_per_segment)
            print(list)
        print(f"Journey´s total length {total_time}\n")
    except ValueError as e:
        print(f"Error {e}")
