# EmergEnv
AI-powered OpenEnv simulation for emergency response coordination, enabling agents to make real-time hospital selection and resource allocation decisions.

# 🚑 EmergEnv: Emergency Response Coordination Environment

## 🧠 Overview

EmergEnv is a real-world OpenEnv simulation environment designed to train and evaluate AI agents in handling time-critical emergency scenarios. The environment models the decision-making process involved in ambulance-to-hospital coordination, including hospital selection, ICU availability, and pre-arrival resource preparation.

This project was built as part of a hackathon focused on developing AI training environments using standardized APIs.

---

## 🎯 Problem Statement

In real-world emergency situations, delays in hospital coordination can lead to critical outcomes. Ambulances often reach hospitals without prior preparation, leading to inefficiencies in treatment.

EmergEnv simulates this challenge and enables AI agents to:

* Select the most appropriate hospital
* Pre-notify required resources (ICU, operation theatre)
* Optimize decisions under time constraints

---

## ⚙️ Environment Design

The environment follows the OpenEnv standard interface:

* `reset()` → Initializes a new emergency scenario
* `step(action)` → Processes agent action and returns observation, reward, done, info
* `state()` → Returns current environment state

---

## 📥 Observation Space

Each episode provides structured input:

```json
{
  "patient_condition": "heart_attack",
  "severity": "high",
  "distance": 8,
  "available_hospitals": [
    {"name": "A", "icu": 1, "beds": 2},
    {"name": "B", "icu": 0, "beds": 1}
  ]
}
```

---

## ⚡ Action Space

Agents can perform:

```json
{
  "action_type": "choose_hospital | pre_notify | request_resources",
  "target": "Hospital A"
}
```

---

## 🎯 Tasks

### 🟢 Easy

* Select the correct hospital based on availability

### 🟡 Medium

* Select hospital + prepare necessary resources

### 🔴 Hard

* Full coordination: hospital selection, ICU allocation, and emergency preparation

---

## 🏆 Reward Function

* Correct hospital selection → +0.4
* Correct resource preparation → +0.4
* Efficient decisions → +0.2
* Wrong decision → -0.3
* Invalid/unsafe action → -0.5

---

## 🧪 Grader

Each task includes a deterministic grader that evaluates:

* Decision correctness
* Resource allocation
* Efficiency

Returns a score between **0.0 and 1.0**

---

## 🌐 API Endpoints

* `POST /reset`
* `POST /step`
* `GET /state`
* `GET /tasks`
* `GET /grader`
* `GET /baseline`

---

## 🤖 Baseline Agent

A baseline inference script is included using the OpenAI API. It runs across all tasks and produces reproducible scores.

---

## 🐳 Deployment

The environment is containerized using Docker and deployed on Hugging Face Spaces.

👉 Live Demo: (add your HF link here)

---

## 🧱 Project Structure

```
project/
 ├── env.py
 ├── models.py
 ├── tasks/
 ├── graders/
 ├── app.py
 ├── baseline.py
 ├── openenv.yaml
 ├── Dockerfile
 └── README.md
```

---

## 🚀 Setup Instructions

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app:app --reload
```

---

## 🧠 Key Highlights

* Real-world emergency simulation
* OpenEnv-compliant environment
* Multi-step decision making
* Deterministic evaluation system
* Fully deployable with Docker

---

## 🏁 Conclusion

EmergEnv provides a structured and realistic environment for evaluating AI agents in critical decision-making scenarios, bridging the gap between theoretical AI models and real-world applications.

---
