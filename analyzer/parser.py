import re

from analyzer.correlator import correlate_transactions


def read_log_file(file_path, msisdn=None):

    try:

        with open(file_path, "r") as file:
            raw_data = file.read()

        # Normalize whitespace
        cleaned_data = re.sub(
            r"\n\s*\n",
            "\n",
            raw_data
        )

        cleaned_data = re.sub(
            r"[ \t]+",
            " ",
            cleaned_data
        )

        # Return full logs if no MSISDN filter
        if not msisdn:
            return cleaned_data

        packets = cleaned_data.split("Frame ")

        seed_transaction_ids = set()

        # STEP 1:
        # Find packets containing MSISDN
        for packet in packets:

            if msisdn in packet:

                matches = re.findall(
                    r"Transaction Id:\s*([A-Fa-f0-9]+)",
                    packet
                )

                seed_transaction_ids.update(matches)

        # STEP 2:
        # Correlate all related transactions
        correlated_data = correlate_transactions(
            cleaned_data,
            seed_transaction_ids
        )

        return correlated_data

    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None

    except Exception as error:
        print(f"[ERROR] {error}")
        return None