# Detection Workflow Diagram

```mermaid
graph TD
    A["Initialize Canary Honeyfile"] --> B["Compute Baseline SHA-256"]
    B --> C["Continuous File Inspection"]
    C --> D{"Checksum Changed?"}
    D -- "No" --> C
    D -- "Yes (or Deleted)" --> E["TRIP CANARY ALERT!"]
    E --> F["Automated Response:

Isolate Host / Kill Process"]