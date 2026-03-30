from models import Observation, Action, Reward, GameState
from tasks.easy import get_easy_task
from tasks.medium import get_medium_task
from tasks.hard import get_hard_task
from graders.easy_grader import grade_easy
from graders.medium_grader import grade_medium
from graders.hard_grader import grade_hard
from typing import Tuple

class ERCEEnvironment:
    def __init__(self):
        self.game_state = GameState()
        self.max_steps = 3
        
    def reset(self, task_difficulty: str = "easy") -> Observation:
        """
        Resets environment and fetches starting data payload.
        """
        self.game_state.history = []
        self.game_state.done = False
        self.game_state.score = 0.0
        
        if task_difficulty == "easy":
            self.game_state.observation = get_easy_task()
        elif task_difficulty == "medium":
            self.game_state.observation = get_medium_task()
        elif task_difficulty == "hard":
            self.game_state.observation = get_hard_task()
        else:
            raise ValueError("Invalid task difficulty")
            
        return self.game_state.observation

    def step(self, action: Action) -> Tuple[Observation, Reward, bool, dict]:
        """
        Calculates impact of agent's step on the system constraints.
        """
        if self.game_state.done:
            raise RuntimeError("Environment is already done. Please request /reset.")
            
        self.game_state.history.append(action)
        
        # We declare a terminal phase if standard mapping finishes
        if action.action_type == "choose_hospital" or len(self.game_state.history) >= self.max_steps:
            self.game_state.done = True
            
            task_type = self.game_state.observation.active_task
            if task_type == "easy":
                reward = grade_easy(self.game_state.history, self.game_state.observation)
            elif task_type == "medium":
                reward = grade_medium(self.game_state.history, self.game_state.observation)
            elif task_type == "hard":
                reward = grade_hard(self.game_state.history, self.game_state.observation)
            else:
                 reward = Reward(score=0.0, details={}, message="Unknown task grader.")
            
            self.game_state.score = reward.score
        else:
            # Intermediate step mapping
            reward = Reward(score=0.0, details={}, message="Action noted continuously. Resolving phase open.")
            
        return self.game_state.observation, reward, self.game_state.done, {}

    def state(self) -> GameState:
         """Returns entire internal snapshot history and metrics."""
         return self.game_state
