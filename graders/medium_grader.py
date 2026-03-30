from models import Action, Observation, Reward
from typing import List

def grade_medium(actions: List[Action], obs: Observation) -> Reward:
    """
    Medium Grader: heart attack, high severity. Needs ICU (h1).
    Expectation: choose h1 AND pre_notify h1.
    """
    score = 0.0
    details = {}
    
    has_chosen = any(a.action_type == "choose_hospital" and a.target_hospital_id == "h1" for a in actions)
    has_notified = any(a.action_type == "pre_notify" and a.target_hospital_id == "h1" for a in actions)
    chose_wrong_hospital = any(a.action_type == "choose_hospital" and a.target_hospital_id != "h1" for a in actions)
    
    if chose_wrong_hospital:
         score -= 0.5
         details["unsafe_action"] = -0.5

    if has_chosen:
        score += 0.5
        details["correct_hospital"] = 0.4
        details["efficient_decision"] = 0.1
        
    if has_notified:
        score += 0.5
        details["correct_resource_prep"] = 0.4
        details["efficient_decision"] = 0.1
        
    final_score = max(0.0, min(1.0, score))
    msg = "Perfect coordination." if final_score == 1.0 else "Partial or incorrect coordination."
    
    return Reward(score=final_score, details=details, message=msg)
