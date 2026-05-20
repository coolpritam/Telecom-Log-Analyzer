from analyzer.parser import read_log_file
from analyzer.detector import detect_issues
from analyzer.report import generate_report
from analyzer.timeline import build_timeline


def main():

    print("\n========== Telecom Log Analyzer ==========\n")

    log_path = "logs/sample_log.txt"

    target_msisdn = input(
        "Enter MSISDN to analyze: "
    )

    log_data = read_log_file(
        log_path,
        msisdn=target_msisdn
    )

    if not log_data:
        print("[ERROR] No correlated log data found.")
        return

    detected_issues = detect_issues(log_data)

    generate_report(detected_issues)

    # Build subscriber timeline
    timeline = build_timeline(log_data)

    print("\n========== Subscriber Timeline ==========\n")

    for index, event in enumerate(timeline, start=1):

        print(f"[{index}] {event['event']}")

        if "transaction_id" in event:
            print(f"    Transaction ID : {event['transaction_id']}")

        if "imsi" in event:
            print(f"    IMSI           : {event['imsi']}")

        print()

    print("========== Timeline Completed ==========\n")


if __name__ == "__main__":
    main()