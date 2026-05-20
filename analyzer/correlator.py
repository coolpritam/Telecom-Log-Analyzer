import re


def correlate_transactions(log_data, seed_transaction_ids):

    packets = log_data.split("Frame ")

    discovered_ids = set(seed_transaction_ids)

    correlated_packets = []

    changed = True

    while changed:

        changed = False

        for packet in packets:

            # Check if packet contains known transaction ID
            if any(
                transaction_id in packet
                for transaction_id in discovered_ids
            ):

                correlated_packets.append(packet)

                # Discover new transaction IDs
                new_matches = re.findall(
                    r"Transaction Id:\s*([A-Fa-f0-9]+)",
                    packet
                )

                for transaction_id in new_matches:

                    if transaction_id not in discovered_ids:
                        discovered_ids.add(transaction_id)
                        changed = True

    return "\n".join(set(correlated_packets))