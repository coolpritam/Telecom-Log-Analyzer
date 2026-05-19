Telecom Log Analyzer

A Python-based telecom log analyzer for parsing and analyzing SS7, SIGTRAN, MAP, and TCAP transaction logs.

Features

* Parse SS7 / SIGTRAN / MAP logs
* Detect TCAP aborts and transaction failures
* Identify timeout and delayed response patterns
* Generate summary reports
* Detect possible stale TCAP context issues
* Root Cause Analysis suggestions

Supported Protocols

* SS7
* SIGTRAN
* MAP
* TCAP
* SCCP
* M3UA
* SCTP

Example Detection

The analyzer can identify:

* sendRoutingInfoForSM
* returnResultLast
* P_ABORT_RESOURCE_LIMITATION
* Timeout scenarios
* Delayed MAP responses

Tech Stack

* Python
* Regex
* Pandas
* CLI-based processing
