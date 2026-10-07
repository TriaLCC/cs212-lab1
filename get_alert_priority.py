from enum import Enum

class AlertPriority(Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    CLEAR = "CLEAR"

class HealthCode(Enum):
    Critical = 1
    Warning = 2
    Optimal = 3

def get_server_alert_priority (health_code: HealthCode, since_last_check: float) -> AlertPriority:

    if not validate_health_code(health_code) or not validate_since_last_check(since_last_check):
        raise ValueError(
            f"Invalid input:\n"
            f"Health Code: '{health_code}'\n"
            f"Since last check: '{since_last_check}'"
        )

    if health_code == HealthCode.Critical:
        return AlertPriority.HIGH

    elif health_code == HealthCode.Warning:
        return AlertPriority.HIGH if since_last_check > 4 else AlertPriority.MEDIUM

    elif health_code == HealthCode.Optimal:
        return AlertPriority.LOW if since_last_check > 10 else AlertPriority.CLEAR

def validate_health_code(health_code) -> bool:
    return isinstance(health_code, HealthCode)

def validate_since_last_check(since_last_check) -> bool:
    return isinstance(since_last_check, (int, float)) and since_last_check >= 0

def print_status_message(health_code: HealthCode, hours_since_last_check: float):
    print(f"Health Code: {health_code}\nHours since last check: {hours_since_last_check}\nAlert Priority: {get_server_alert_priority(health_code, hours_since_last_check)}\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example 1: Critical, 2 hours since last check
    print_status_message(HealthCode.Critical, 2 )

    # Example 2: Warning, 2 hours since last check
    print_status_message(HealthCode.Warning, 2)

    # Example 3: Warning, 6 hours since last check
    print_status_message(HealthCode.Warning, 6)

    # Example 4: Optimal, 6 hours since last check
    print_status_message(HealthCode.Optimal, 6)

    # Example 5:  Optimal, 12 hours since last check
    print_status_message(HealthCode.Optimal, 12)