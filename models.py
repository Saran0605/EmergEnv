from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict

class Resource(BaseModel):
    id: str
    type: Literal["ambulance", "icu_bed", "blood_supply", "surgeon"]
    available: bool

class HospitalStatus(BaseModel):
    hospital_id: str
    name: str
    distance_km: float
    icu_available: bool
    beds_available: int
    specialties: List[str]
    resources: List[Resource] = Field(default_factory=list)

class PatientCondition(BaseModel):
    id: str
    type: Literal["accident", "heart_attack", "stroke", "burn", "none"]
    severity: Literal["low", "medium", "high"]
    notes: Optional[str] = None

class Observation(BaseModel):
    patient_condition: PatientCondition
    hospitals: List[HospitalStatus]
    current_time: str
    active_task: str

class Action(BaseModel):
    action_type: Literal["choose_hospital", "pre_notify", "request_resources"]
    target_hospital_id: str
    resources_requested: Optional[List[str]] = Field(default_factory=list)

class Reward(BaseModel):
    score: float
    details: Dict[str, float]
    message: str

class GameState(BaseModel):
    observation: Optional[Observation] = None
    history: List[Action] = Field(default_factory=list)
    done: bool = False
    score: float = 0.0
