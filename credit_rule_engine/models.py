from dataclasses import dataclass

@dataclass
class Applicant:
    """
    Represents a credit applicant.
    """
    id: str
    credit_score: int
    annual_income: float
    total_debt: float
    employment_status: str
