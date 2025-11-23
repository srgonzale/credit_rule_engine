from typing import List, Dict, Any
from .models import Applicant
from .rules import CreditRule

class CreditEngine:
    """
    Engine to evaluate credit applicants based on a set of rules.
    """
    def __init__(self):
        self.rules: List[CreditRule] = []

    def add_rule(self, rule: CreditRule):
        """
        Adds a rule to the engine.
        """
        self.rules.append(rule)

    def evaluate(self, applicant: Applicant) -> Dict[str, Any]:
        """
        Evaluates the applicant against all rules.
        Returns a dictionary with the status and reasons for rejection (if any).
        """
        failed_reasons = []
        for rule in self.rules:
            if not rule.evaluate(applicant):
                failed_reasons.append(rule.reason)

        if failed_reasons:
            return {
                "status": "REJECTED",
                "reasons": failed_reasons
            }
        else:
            return {
                "status": "APPROVED",
                "reasons": []
            }
