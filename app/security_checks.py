def check_for_vulnerabilities(code: str) -> list:
    findings = []
    # Example: Simple check for hardcoded passwords
    if "password" in code and "=" in code:
        findings.append("Possible hardcoded password detected.")
    # Example: Simple check for SQL Injection
    if ("SELECT" in code or "INSERT" in code) and ("+" in code):
        findings.append("Possible SQL Injection vulnerability (concatenation in SQL queries).")
    # Add more checks as needed
    return findings
