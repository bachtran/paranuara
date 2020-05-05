from flask import jsonify, current_app
from app.api import api_blueprint
from app.services import company as company_service

"""Routes for Company"""


@api_blueprint.route('/company/<int:company_id>/employees')
def company_employees(company_id):
    """Return list of employees give a company's index"""
    try:
        company = company_service.get_company(company_id)
        if not company:
            return not_found_response()

        if not company.employees:
            return jsonify({'message': 'This company does not have any employees'})

        return jsonify([employee.to_dict() for employee in company.employees])
    except Exception as e:
        current_app.logger.error(e)
        return exception_response()


@api_blueprint.route('/company/<int:company_id>')
def get_company(company_id):
    """Return details given a company's index"""
    try:
        company = company_service.get_company(company_id)
        if not company:
            return not_found_response()
        return jsonify(company.to_dict())
    except Exception as e:
        current_app.logger.error(e)
        return exception_response()


def not_found_response():
    """Return not found response"""
    message = {
        'message': 'Company not found',
    }
    return jsonify(message), 404


def exception_response():
    """Return exception response"""
    message = {
        'message': 'We encountered an issue',
    }
    return jsonify(message), 500
