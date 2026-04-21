# Proactive Digital Forensic Readiness Framework

## Overview
This project presents a **Proactive Digital Forensic Readiness Framework** that continuously collects system logs, converts them into structured forensic evidence, preserves integrity using cryptographic hashing, and reconstructs event timelines for investigation.

---

## Problem Statement
Traditional digital forensic investigations are reactive, where evidence collection starts only after a cyber incident occurs. By that time, logs may be overwritten, deleted, or unavailable. Additionally, raw logs are unstructured, making it difficult to reconstruct events.

This project addresses this issue by implementing a proactive system that prepares evidence in advance.

---

## Key Features
- Automated log monitoring
- Structured forensic evidence generation (JSON format)
- SHA-256 hashing for evidence integrity
- Timeline reconstruction
- Incident summary generation

---

## System Architecture

Logs → Evidence Extraction → Hashing → JSON Storage → Timeline → Summary

---

## How It Works

1. Reads system logs from a log file  
2. Extracts relevant events and timestamps  
3. Converts them into structured forensic evidence  
4. Applies SHA-256 hashing for integrity  
5. Stores evidence in JSON format  
6. Reconstructs timeline of events  
7. Generates incident summary  

---

## Sample Evidence Record

```json
{
  "evidence_id": "E1",
  "timestamp": "2025-01-01 10:15:23",
  "event": "User admin failed login",
  "evidence_type": "Authentication",
  "source": "system.log",
  "collection_time": "2026-04-22 10:00:00",
  "hash_algorithm": "SHA-256",
  "evidence_hash": "abc123..."
}
```

---

## Sample Output

*Timeline*

2025-01-01 10:15:23 | Authentication | User admin failed login
2025-01-01 10:16:01 | Other | User admin logged in

*Incident Summary*

Failed Logins: 1
Successful Logins: 1
File Modifications: 1
Logouts: 1

---

## Technologies Used

1. Python
2. JSON
3. Hashlib

---

## Project Structure

├── read_logs.py
├── system.log
├── evidence_store.json
├── state.txt
├── screenshots/
└── README.md

---

## How to Run

### Prerequisites
- Python 3 installed

### Steps

1. Clone the repository:
git clone https://github.com/your-username/proactive-digital-forensic-readiness-framework.git

2. Navigate to project folder:
cd proactive-digital-forensic-readiness-framework

3. Run the script:
python read_logs.py

---

## Future Work

- Integration with multiple log sources such as network logs, application logs, and cloud audit logs to enhance evidence coverage.

- Support for mobile and cloud environments by incorporating log sources like Android logcat and cloud monitoring systems.

- Implementation of intelligent anomaly detection techniques to identify suspicious patterns and potential security incidents.

- Development of a real-time dashboard for visualization of forensic timelines and incident summaries.

- Enhancement of evidence integrity mechanisms through continuous verification and tamper detection.

---

## Research Background

This project is inspired by existing research in digital forensic readiness and log-based forensic investigation frameworks.

Foundational works emphasize the importance of preparing systems for forensic investigations in advance, while standard guidelines such as NIST SP 800-86 define best practices for evidence collection and preservation.

However, many existing approaches are either conceptual or focused on detection rather than structured evidence preparation.

This project aims to bridge that gap by providing a practical prototype implementation of a proactive forensic readiness framework that automates evidence collection, ensures integrity, and supports investigation through timeline reconstruction.

---

## Author

**Aditya Agrawal**  
M.Tech (Cyber Security)  
Department of Computer Engineering
NIT Kurukshetra

*Project developed as part of academic research in digital forensics.*
