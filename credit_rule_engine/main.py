from credit_rule_engine.models import Applicant
from credit_rule_engine.rules import MinCreditScoreRule, MinIncomeRule, MaxDebtToIncomeRatioRule
from credit_rule_engine.engine import CreditEngine

def main():
    # Initialize the engine
    engine = CreditEngine()

    # Add rules
    engine.add_rule(MinCreditScoreRule(min_score=650))
    engine.add_rule(MinIncomeRule(min_income=30000))
    engine.add_rule(MaxDebtToIncomeRatioRule(max_ratio=0.4))

    # Create applicants
    applicant1 = Applicant(
        id="A001",
        credit_score=700,
        annual_income=50000,
        total_debt=10000,
        employment_status="Employed"
    )

    applicant2 = Applicant(
        id="A002",
        credit_score=600,
        annual_income=25000,
        total_debt=5000,
        employment_status="Unemployed"
    )
    
    applicant3 = Applicant(
        id="A003",
        credit_score=720,
        annual_income=80000,
        total_debt=40000, # Ratio 0.5 > 0.4
        employment_status="Employed"
    )

    # Evaluate applicants
    applicants = [applicant1, applicant2, applicant3]
    
    print("Credit Application Results:")
    print("-" * 30)
    
    for app in applicants:
        result = engine.evaluate(app)
        print(f"Applicant ID: {app.id}")
        print(f"Status: {result['status']}")
        if result['status'] == "REJECTED":
            print("Reasons:")
            for reason in result['reasons']:
                print(f"  - {reason}")
        print("-" * 30)

if __name__ == "__main__":
    main()
