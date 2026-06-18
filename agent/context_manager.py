"""Sliding window context management for LLM token limits."""
from typing import List, Dict

class ContextManager:
    def __init__(self, max_tokens: int = 4096):
        self.max_tokens = max_tokens
        self.history: List[Dict[str, str]] = []

    def add_message(self, role: str, content: str):
        self.history.append({"role": role, "content": content})
        self._prune()

    def _prune(self):
        # Heuristic: 1 token ~ 4 characters
        while sum(len(m["content"]) // 4 for m in self.history) > self.max_tokens and len(self.history) > 1:
            self.history.pop(0)
