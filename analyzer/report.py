def generate_report(issues):

    total_events = (
        issues["map_operations"]
        + issues["tcap_aborts"]
        + issues["timeouts"]
        + issues["resource_limitations"]
    )

    print("\n========== SignalScope Analysis Report ==========\n")

    print(f"Total Events             : {total_events}")
    print(f"Transaction Count        : {issues['transaction_count']}")
    print(f"MAP Operations Detected  : {issues['map_operations']}")
    print(f"TCAP Aborts Detected     : {issues['tcap_aborts']}")
    print(f"Timeout Events           : {issues['timeouts']}")
    print(f"Resource Limitations     : {issues['resource_limitations']}")

    print("\n========== Telecom Error Summary ==========\n")

    if issues["telecom_errors"]:

        for error_name, count in issues["telecom_errors"].items():
            print(f"{error_name} : {count}")

    else:
        print("No telecom errors detected.")

    print("\n========== IMSI Summary ==========\n")

    if issues["unique_imsis"]:

        for imsi in issues["unique_imsis"]:
            print(imsi)

    else:
        print("No IMSI values detected.")

    print("\n========== RCA Suggestion ==========\n")

    if issues["tcap_aborts"] > 0:
        print("- Possible stale TCAP transaction context")

    if issues["timeouts"] > 0:
        print("- Investigate timeout thresholds and delayed responses")

    if issues["resource_limitations"] > 0:
        print("- Check SMSC/IPSTG utilization and memory usage")

    if total_events == 0:
        print("- No major telecom issues detected")

    print("\n========== Analysis Completed ==========\n")