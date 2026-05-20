import re
from collections import Counter


def detect_issues(log_data):

    issues = {}

    # Detect MAP operations
    map_operations = re.findall(
        r"sendRoutingInfoForSM|mt-forwardSM",
        log_data
    )

    issues["map_operations"] = len(map_operations)

    # Detect TCAP aborts
    tcap_aborts = re.findall(
        r"\bP_ABORT\b|\bABORT\b",
        log_data
    )

    issues["tcap_aborts"] = len(tcap_aborts)

    # Detect timeout events
    timeouts = re.findall(
        r"timeout",
        log_data,
        re.IGNORECASE
    )

    issues["timeouts"] = len(timeouts)

    # Detect resource limitation errors
    resource_limitations = re.findall(
        r"resource limitation|RESOURCE_LIMITATION",
        log_data,
        re.IGNORECASE
    )

    issues["resource_limitations"] = len(resource_limitations)

    # Extract telecom error names
    telecom_errors = re.findall(
        r"localValue:\s*([A-Za-z0-9_-]+)",
        log_data
    )

    # Exclude MAP operation names
    excluded_operations = {
        "sendRoutingInfoForSM",
        "mt-forwardSM"
    }

    filtered_errors = [
        error for error in telecom_errors
        if error not in excluded_operations
    ]

    issues["telecom_errors"] = dict(
        Counter(filtered_errors)
    )

    # Extract transaction IDs
    transaction_ids = re.findall(
        r"Transaction Id:\s*([A-Fa-f0-9]+)",
        log_data
    )

    issues["transaction_count"] = len(
        set(transaction_ids)
    )

    # Extract IMSI values
    imsis = re.findall(
        r"IMSI:\s*(\d+)",
        log_data
    )

    issues["unique_imsis"] = list(
        set(imsis)
    )

    return issues