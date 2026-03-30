from models import PatientCondition, HospitalStatus, Observation, Resource

def get_hard_task() -> Observation:
    """
    HARD TASK: Full coordination. Burn victim needing specific hospital, ICU pre-notification and surgeon availability.
    """
    patient = PatientCondition(
        id="p3", type="burn", severity="high", 
        notes="Requires immediate localized surgery and ICU."
    )
    hospitals = [
        HospitalStatus(
            hospital_id="h1", name="Burn Center", distance_km=25.0,
            icu_available=True, beds_available=1, specialties=["burns", "trauma"],
            resources=[Resource(id="r1", type="surgeon", available=True)]
        ),
        HospitalStatus(
            hospital_id="h2", name="City General", distance_km=10.0,
            icu_available=False, beds_available=0, specialties=["cardiology"]
        )
    ]
    return Observation(
        patient_condition=patient, 
        hospitals=hospitals, 
        current_time="14:00 PM", 
        active_task="hard"
    )
