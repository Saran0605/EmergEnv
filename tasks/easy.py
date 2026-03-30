from models import PatientCondition, HospitalStatus, Observation

def get_easy_task() -> Observation:
    """
    EASY TASK: Choose correct hospital for low severity accident.
    """
    patient = PatientCondition(id="p1", type="accident", severity="low")
    hospitals = [
        HospitalStatus(
            hospital_id="h1", name="City General", distance_km=5.0,
            icu_available=True, beds_available=10, specialties=["trauma"]
        ),
        HospitalStatus(
            hospital_id="h2", name="Suburban Clinic", distance_km=2.0,
            icu_available=False, beds_available=5, specialties=[]
        )
    ]
    return Observation(
        patient_condition=patient, 
        hospitals=hospitals, 
        current_time="10:00 AM", 
        active_task="easy"
    )
