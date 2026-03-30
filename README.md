---
title: Emergency Response Coordination Env
emoji: 🚑
colorFrom: red
colorTo: blue
sdk: docker
pinned: false
---

# Emergency Response Coordination Environment (ERCE)

## Overview & Real-World Motivation
ERCE presents an OpenEnv-compatible orchestration layer simulating high-impact real-world triage mapping. Managing ambulances, intensive care logistics, and localized distance-time mapping provides a complex baseline testing how securely AI reasoning isolates the perfect safe pathways across competing variable demands securely.

## Environment Architecture

**Observation Schema:**
- `patient_condition` (Accident, heart attack logic alongside bounds like low/medium/high severities and textual context).
- `hospitals` (Available localized zones with granular flags covering ICU availability, active bed pools, exact distance logic mapped, and resource sub-arrays).
- `active_task` (The runtime scenario bounds map).

**Action Schema:**
- `action_type`: Strictly (`choose_hospital`, `pre_notify`, `request_resources`)
- `target_hospital_id`: String
- `resources_requested`: Array

## Tasks Execution Flow
1. **Easy Task**: Patient mapped suffering minor accident. The AI strictly should parse minimum distance requirements over ICU variables seamlessly terminating the sequence quickly natively choosing `h2`.
2. **Medium Task**: Patient suffers a massive heart attack requiring specialized ICU resources. The AI will learn it requires both alerting the specific location containing the ICU alongside executing the terminal hospital choice sequentially.
3. **Hard Task**: Advanced burn context demanding specific trauma specializations logic bounds mapped. Agent needs to alert location, reserve extremely specific resources locally (`surgeon`), and then finish mapping routing securely validating 1.0 logic bounds exactly.

## Reward Engine Determinism
Grading runs fully natively per episode:
- Perfect hospital matches map out `+0.4`
- Exact resource execution loops `+0.4`
- Correct priority execution distances map `+0.2`
- Unsafe allocations / mismatched hospital criteria dynamically restrict variables bound downwards securely via `-0.5` bounds tracking securely.

## Local Test Build Operations

**Using Docker Container (Recommended)**:
```bash
docker build -t erce-env .
docker run -p 7860:7860 erce-env
```

**Executing Local Source Validation (Standard Desktop)**:
Ensure python > 3.9 boundaries logic.
```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 7860
```

## Running the OpenAI AI Baseline

Once the FastAPI mapping is serving correctly internally over port 7860 securely simply map OpenAI's valid execution boundary logic to see baseline output mappings run securely via API parameters dynamically mapping endpoints:
```bash
export OPENAI_API_KEY="sk-..."
python baseline.py
```
