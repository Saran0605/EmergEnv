from models import Action, Observation, Reward
from typing import List

def grade_easy(actions: List[Action], obs: Observation) -> Reward:
    """
    Easy Grader: Choose correct hospital. 
    Ideal: Suburban Clinic (h2) is closer (2.0km) and has beds. No ICU needed for 'low' severity.
    """
    if not actions:
         return Reward(score=0.0, details={"wrong_decision": -0.3}, message="No actions taken.")
         
    action = actions[0] # Easy expects just one direct action generally
    
    if action.action_type != "choose_hospital":
        return Reward(score=0.0, details={"unsafe_action": -0.5}, message="Must directly choose a hospital.")
    
    if action.target_hospital_id == "h2":
        return Reward(score=1.0, details={"correct_hospital": 0.4, "efficient_decision": 0.6}, message="Perfect choice.")
    elif action.target_hospital_id == "h1":
        # Safe but further away
        return Reward(score=0.4, details={"correct_hospital": 0.4}, message="Valid hospital, but inefficient distance.")
    
    return Reward(score=0.0, details={"wrong_decision": -0.3}, message="Invalid hospital selection.")
