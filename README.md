# Financial Modeling Framework

This Python package provides a framework for financial modeling and
analysis, designed to facilitate the management and analysis of
financial data for businesses. It includes classes for representing
financial statements, expenses, revenues, reporting periods, boards,
committees, people, and relationships within a company.

## Usage
### Basic Usage

```python
from fundy import *

# Create a company instance
company = company()

# Access financial statements
income_statement = company.statements().income_statement()
balance_sheet = company.statements().balance_sheet()
cash_flow_statement = company.statements().cash_flow_statement()

# Compute financial metrics
net_income = income_statement.netincome()
gross_profit = income_statement.grossprofit()
operating_profit = income_statement.operatingprofit()

# Access board information
board_of_directors = company.boardofdirectors()
audit_committee = company.auditcommittee()
compensation_committee = company.compensationcommittee()
```

## Features

    * Representation of financial statements: income statement, balance sheet, and cash flow statement.
    * Calculation of various financial metrics and ratios.
    * Representation of boards, committees, people, and relationships within a company.
    * Framework for financial modeling and analysis.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for
improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE- see the
[LICENSE](LICENSE) file for details.

