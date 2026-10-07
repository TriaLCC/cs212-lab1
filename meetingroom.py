def recommend_room(attendees: int, projector_needed: bool):
    print("--- Meeting Room Reservation ---")
    print(f"Request: Attendees={attendees}, Projector Needed={projector_needed}")

    if validate_num_attendees(attendees):
        room = get_room_selection(attendees, projector_needed)
        print_room_selection( room)
    else:
        print_room_selection("Error: Invalid number of attendees.")

def print_room_selection(room_str: str):
    print(f"Recommended Room: {room_str}")
    print("---------------------------------")

def get_room_selection(attendees: int, projector_needed: bool) -> str:
    ROOM_ALPHA = "Room Alpha (Small, No Projector)"
    ROOM_BETA = "Room Beta (Medium, Has Projector)"
    ROOM_GAMMA = "Room Gamma (Medium, No Projector)"
    NO_ROOMS_MSG = "Reservation Denied (No large rooms available)"

    if attendees >= 16:
        return NO_ROOMS_MSG
    elif attendees >= 6:
        return ROOM_BETA if projector_needed else ROOM_GAMMA
    else:
        return ROOM_ALPHA


def validate_num_attendees(num_attendees) -> bool:
    return isinstance(num_attendees, int) and not isinstance(num_attendees, bool) and num_attendees > 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example 1: Small group, projector not needed
    recommend_room(4, False)

    # Example 2: Medium group, projector needed
    recommend_room(12, True)

    # Example 3: Medium group, projector not needed
    recommend_room(10, False)

    # Example 4: Large group, projector not needed
    recommend_room(18, False)

    # Example 5: Invalid group, projector not needed
    recommend_room(0, False)