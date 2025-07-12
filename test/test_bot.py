import unittest
from app.security_checks import check_for_vulnerabilities

class TestSecurityChecks(unittest.TestCase):
    def test_hardcoded_password(self):
        code = 'password = "12345"'
        findings = check_for_vulnerabilities(code)
        self.assertIn("Possible hardcoded password detected.", findings)

    def test_sql_injection(self):
        code = 'query = "SELECT * FROM users WHERE name=" + username'
        findings = check_for_vulnerabilities(code)
        self.assertIn("Possible SQL Injection vulnerability (concatenation in SQL queries).", findings)

    def test_no_vulnerability(self):
        code = 'print("Hello, world!")'
        findings = check_for_vulnerabilities(code)
        self.assertEqual(len(findings), 0)

if __name__ == "__main__":
    unittest.main()
