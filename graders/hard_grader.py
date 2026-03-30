from models import Action, Observation, Reward
from typing import List

def grade_hard(actions: List[Action], obs: Observation) -> Reward:
    """
    Hard Grader: burn, high severity. Needs Burn Center (h1), request_resources (surgeon).
    Expectation: choose h1, request surgeon.
    """
    score = 0.0
    details = {}
    
    has_chosen = any(a.action_type == "choose_hospital" and a.target_hospital_id == "h1" for a in actions)
    has_requested = any(
        a.action_type == "request_resources" 
        and a.target_hospital_id == "h1" 
        and ("surgeon" in a.resources_requested or "icu_bed" in a.resources_requested) 
        for a in actions
    )
    chose_wrong_hospital = any(a.action_type == "choose_hospital" and a.target_hospital_id != "h1" for a in actions)
    
    if chose_wrong_hospital:
         score -= 0.5
         details["unsafe_action"] = -0.5
         
    if has_chosen:
        score += 0.5
        details["correct_hospital"] = 0.4
        details["efficient_decision"] = 0.1
        
    if has_requested:
        score += 0.5
        details["correct_resource_prep"] = 0.4
        details["efficient_decision"] = 0.1
        
    final_score = max(0.0, min(1.0, score))
    msg = "All resources correctly mapped." if final_score == 1.0 else "Requirements partially missing or inefficient."
    
    return Reward(score=final_score, details=details, message=msg)
