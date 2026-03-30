import os
import json
import httpx
from openai import OpenAI
from pydantic import BaseModel

API_URL = "http://localhost:7860"

def run_task(client: OpenAI, task_level: str):
    print(f"\n--- Running Task: {task_level} ---")
    
    # 1. Reset Environment natively
    res = httpx.post(f"{API_URL}/reset", json={"task": task_level})
    obs_data = res.json()["observation"]
    
    print(f"Observation: {json.dumps(obs_data, indent=2)}")
    
    # 2. Setup AI directives
    prompt = f"""
You are an Emergency Response Agent assessing simulation states.
Observation Context:
{json.dumps(obs_data)}

Output an optimal sequential JSON array describing actions resolving this emergency.
Acceptable 'action_type' schemas MUST exact copy: 'choose_hospital', 'pre_notify', 'request_resources'.
Payload strict mapping schema: {{"action_type": "<type>", "target_hospital_id": "<id>", "resources_requested": ["<resource>"]}}

Logic rules:
- 'low' severity / accident: Simple 'choose_hospital' prioritizing shortest distance ('h2').
- 'medium' severity / heart attack: 'pre_notify' and 'choose_hospital' with an ICU ('h1').
- 'high' severity / burn: 'request_resources' (type 'surgeon'), 'pre_notify', and 'choose_hospital' ('h1').
IMPORTANT: Return STRICTLY JSON mapping arrays purely.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        
        # 3. Parse output iteratively 
        actions = json.loads(response.choices[0].message.content)
        
        final_reward = None
        for act in actions:
            print(f"Executing step action mapping => {act}")
            step_res = httpx.post(f"{API_URL}/step", json=act)
            if step_res.status_code != 200:
                print(f"Server Error Context: {step_res.text}")
                break
                
            step_data = step_res.json()
            final_reward = step_data["reward"]
            if step_data["done"]:
                break
                
        print(f"Scenario Return Reward Bound: {final_reward}")
        return final_reward["score"] if final_reward else 0.0
    except Exception as e:
        print(f"Execution Error: {e}")
        return 0.0

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY absolutely strictly required natively. Export before mapping.")
        exit(1)
        
    client = OpenAI(api_key=api_key)
    
    try:
        httpx.get(f"{API_URL}/tasks")
    except httpx.ConnectError:
        print("FastAPI Container mapping unreachable. Launch uvicorn locally or verify docker execution prior.")
        exit(1)
        
    scores = {}
    for level in ["easy", "medium", "hard"]:
        scores[level] = run_task(client, level)
        
    print(f"\nAGGREGATED RUN SCORES: {scores}")
