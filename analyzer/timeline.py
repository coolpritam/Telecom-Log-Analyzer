import re


def build_timeline(log_data):

    timeline_events = []

    packets = log_data.split("Frame ")

    for packet in packets:

        packet_events = []

        # Extract frame number
        frame_match = re.search(
            r"^(\d+)",
            packet
        )

        frame_number = None

        if frame_match:
            frame_number = frame_match.group(1)

        # Extract transaction ID
        transaction_match = re.search(
            r"Transaction Id:\s*([A-Fa-f0-9]+)",
            packet
        )

        transaction_id = None

        if transaction_match:
            transaction_id = transaction_match.group(1)

        # Extract IMSI
        imsi_match = re.search(
            r"IMSI:\s*(\d+)",
            packet
        )

        imsi = None

        if imsi_match:
            imsi = imsi_match.group(1)

        # Detect ALL telecom events inside packet

        if "sendRoutingInfoForSM" in packet:

            packet_events.append(
                "SRI-SM Request"
            )

        if "mt-forwardSM" in packet:

            packet_events.append(
                "MT-FSM Forward SM"
            )

        if "alertServiceCentre" in packet:

            packet_events.append(
                "Alert Service Centre"
            )

        if "absentSubscriberSM" in packet:

            packet_events.append(
                "Absent Subscriber"
            )

        if "facilityNotSupported" in packet:

            packet_events.append(
                "Facility Not Supported"
            )

        # Build timeline entries
        for telecom_event in packet_events:

            event = {
                "event": telecom_event
            }

            if frame_number:
                event["frame"] = frame_number

            if transaction_id:
                event["transaction_id"] = transaction_id

            if imsi:
                event["imsi"] = imsi

            timeline_events.append(event)

    return timeline_events