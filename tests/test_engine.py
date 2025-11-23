import unittest
from credit_rule_engine.models import Applicant
from credit_rule_engine.rules import MinCreditScoreRule
from credit_rule_engine.engine import CreditEngine

class TestCreditEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CreditEngine()
        self.engine.add_rule(MinCreditScoreRule(650))
        
        self.applicant = Applicant(
            id="test",
            credit_score=700,
            annual_income=50000,
            total_debt=10000,
            employment_status="Employed"
        )

    def test_approve(self):
        result = self.engine.evaluate(self.applicant)
        self.assertEqual(result['status'], "APPROVED")
        self.assertEqual(len(result['reasons']), 0)

    def test_reject(self):
        self.applicant.credit_score = 600
        result = self.engine.evaluate(self.applicant)
        self.assertEqual(result['status'], "REJECTED")
        self.assertEqual(len(result['reasons']), 1)
        self.assertIn("Credit score is below", result['reasons'][0])

if __name__ == '__main__':
    unittest.main()
