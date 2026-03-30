from models import PatientCondition, HospitalStatus, Observation

def get_medium_task() -> Observation:
    """
    MEDIUM TASK: Choose hospital + pre-notify resources for high severity heart attack.
    """
    patient = PatientCondition(id="p2", type="heart_attack", severity="high")
    hospitals = [
        HospitalStatus(
            hospital_id="h1", name="City General", distance_km=15.0,
            icu_available=True, beds_available=2, specialties=["cardiology"]
        ),
        HospitalStatus(
            hospital_id="h2", name="Local Hospital", distance_km=3.0,
            icu_available=False, beds_available=10, specialties=[]
        )
    ]
    return Observation(
        patient_condition=patient, 
        hospitals=hospitals, 
        current_time="11:30 AM", 
        active_task="medium"
    )
