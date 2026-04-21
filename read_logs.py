import json
import os
import hashlib
import time
from datetime import datetime

STATE_FILE = "state.txt"
LOG_FILE = "system.log"
EVIDENCE_FILE = "evidence_store.json"


# ----------------------------
# Hash function for integrity
# ----------------------------
def compute_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()


# ----------------------------
# Load last processed line
# ----------------------------
def load_state():
    if not os.path.exists(STATE_FILE):
        return 0

    with open(STATE_FILE, "r") as f:
        content = f.read().strip()
        return int(content) if content.isdigit() else 0


# ----------------------------
# Save state checkpoint
# ----------------------------
def save_state(value):
    with open(STATE_FILE, "w") as f:
        f.write(str(value))


# ----------------------------
# Load existing evidence
# ----------------------------
def load_existing_evidence():
    try:
        with open(EVIDENCE_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# ----------------------------
# Save evidence to JSON
# ----------------------------
def save_evidence(data):
    with open(EVIDENCE_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ----------------------------
# Evidence Collection Module
# ----------------------------
def collect_new_evidence():

    last_line = load_state()

    with open(LOG_FILE, "r") as file:
        lines = file.readlines()

    new_lines = lines[last_line:]

    existing_data = load_existing_evidence()

    evidence_counter = len(existing_data) + 1

    evidence_list = []

    for line in new_lines:

        parts = line.strip().split()

        if len(parts) < 3:
            continue

        timestamp = parts[0] + " " + parts[1]
        event = " ".join(parts[2:])
        event_lower = event.lower()

        if "login" in event_lower:
            evidence_type = "Authentication"
        elif "file" in event_lower:
            evidence_type = "File Activity"
        else:
            evidence_type = "Other"

        evidence_hash = compute_hash(timestamp + event + evidence_type)

        evidence = {
            "evidence_id": f"E{evidence_counter}",
            "timestamp": timestamp,
            "event": event,
            "evidence_type": evidence_type,
            "source": LOG_FILE,
            "collection_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hash_algorithm": "SHA-256",
            "evidence_hash": evidence_hash
        }

        evidence_list.append(evidence)

        evidence_counter += 1

    if evidence_list:

        existing_data.extend(evidence_list)

        save_evidence(existing_data)

        save_state(last_line + len(new_lines))

        print(f"\n{len(evidence_list)} new evidence entries collected.")

    return existing_data


# ----------------------------
# Timeline Reconstruction
# ----------------------------
def reconstruct_timeline(evidence_data):

    print("\n--- FORENSIC TIMELINE ---\n")

    sorted_data = sorted(
        evidence_data,
        key=lambda x: datetime.strptime(x["timestamp"], "%Y-%m-%d %H:%M:%S")
    )

    for e in sorted_data:
        print(f"{e['timestamp']} | {e['evidence_type']} | {e['event']}")

    return sorted_data


# ----------------------------
# Incident Summary Module
# ----------------------------
def generate_incident_summary(evidence_data):

    failed_logins = 0
    successful_logins = 0
    file_changes = 0
    logout_events = 0

    for e in evidence_data:

        event = e["event"].lower()

        if "failed login" in event:
            failed_logins += 1
        elif "logged in" in event:
            successful_logins += 1
        elif "file" in event and "modified" in event:
            file_changes += 1
        elif "logged out" in event:
            logout_events += 1

    print("\n--- INCIDENT SUMMARY ---\n")

    print("Total Failed Login Attempts:", failed_logins)
    print("Total Successful Logins:", successful_logins)
    print("Total File Modifications:", file_changes)
    print("Total Logout Events:", logout_events)

    if failed_logins > 0 and successful_logins > 0:
        print("\nPattern Detected: Failed login followed by successful access.")

    if file_changes > 0:
        print("Alert: File modification detected.")


# ----------------------------
# Main Monitoring Pipeline
# ----------------------------
def run_pipeline():

    evidence_data = collect_new_evidence()

    timeline = reconstruct_timeline(evidence_data)

    generate_incident_summary(timeline)


# ----------------------------
# Automated Monitoring System
# ----------------------------
if __name__ == "__main__":

    print("Starting Automated Forensic Monitoring Framework...\n")

    while True:

        try:

            run_pipeline()

        except Exception as e:

            print("Error occurred:", e)

        print("\nNext monitoring cycle in 60 seconds...\n")

        time.sleep(30)