import unittest
from credit_rule_engine.models import Applicant
from credit_rule_engine.rules import MinCreditScoreRule, MinIncomeRule, MaxDebtToIncomeRatioRule

class TestRules(unittest.TestCase):
    def setUp(self):
        self.applicant = Applicant(
            id="test",
            credit_score=700,
            annual_income=50000,
            total_debt=10000,
            employment_status="Employed"
        )

    def test_min_credit_score_rule(self):
        rule = MinCreditScoreRule(650)
        self.assertTrue(rule.evaluate(self.applicant))
        
        rule = MinCreditScoreRule(750)
        self.assertFalse(rule.evaluate(self.applicant))
        self.assertIn("Credit score is below", rule.reason)

    def test_min_income_rule(self):
        rule = MinIncomeRule(40000)
        self.assertTrue(rule.evaluate(self.applicant))

        rule = MinIncomeRule(60000)
        self.assertFalse(rule.evaluate(self.applicant))
        self.assertIn("Annual income is below", rule.reason)

    def test_max_debt_to_income_ratio_rule(self):
        # Ratio is 0.2
        rule = MaxDebtToIncomeRatioRule(0.3)
        self.assertTrue(rule.evaluate(self.applicant))

        rule = MaxDebtToIncomeRatioRule(0.1)
        self.assertFalse(rule.evaluate(self.applicant))
        self.assertIn("Debt-to-income ratio exceeds", rule.reason)

    def test_zero_income(self):
        self.applicant.annual_income = 0
        rule = MaxDebtToIncomeRatioRule(0.5)
        self.assertFalse(rule.evaluate(self.applicant))

if __name__ == '__main__':
    unittest.main()
