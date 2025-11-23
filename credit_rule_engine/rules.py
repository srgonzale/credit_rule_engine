from abc import ABC, abstractmethod
from .models import Applicant

class CreditRule(ABC):
    """
    Abstract base class for credit rules.
    """
    
    @abstractmethod
    def evaluate(self, applicant: Applicant) -> bool:
        """
        Evaluates the rule against the applicant.
        Returns True if the rule is passed, False otherwise.
        """
        pass

    @property
    @abstractmethod
    def reason(self) -> str:
        """
        Returns the reason for rejection if the rule fails.
        """
        pass

class MinCreditScoreRule(CreditRule):
    def __init__(self, min_score: int):
        self.min_score = min_score

    def evaluate(self, applicant: Applicant) -> bool:
        return applicant.credit_score >= self.min_score

    @property
    def reason(self) -> str:
        return f"Credit score is below the minimum requirement of {self.min_score}."

class MinIncomeRule(CreditRule):
    def __init__(self, min_income: float):
        self.min_income = min_income

    def evaluate(self, applicant: Applicant) -> bool:
        return applicant.annual_income >= self.min_income

    @property
    def reason(self) -> str:
        return f"Annual income is below the minimum requirement of {self.min_income}."

class MaxDebtToIncomeRatioRule(CreditRule):
    def __init__(self, max_ratio: float):
        self.max_ratio = max_ratio

    def evaluate(self, applicant: Applicant) -> bool:
        if applicant.annual_income == 0:
            return False
        ratio = applicant.total_debt / applicant.annual_income
        return ratio <= self.max_ratio

    @property
    def reason(self) -> str:
        return f"Debt-to-income ratio exceeds the maximum allowed of {self.max_ratio}."
