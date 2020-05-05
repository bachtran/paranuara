from app.models import Company

"""Business logic for Company endpoint"""


def get_company(company_id):
    """Get a company object given an index"""
    try:
        company = Company.query.filter_by(index=company_id).first()
        return company
    except Exception as e:
        raise e
