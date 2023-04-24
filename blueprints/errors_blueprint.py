from flask import Blueprint, render_template

errors_blueprint = Blueprint('errors', __name__)


@errors_blueprint.app_errorhandler(404)
def error_404_view(error):
    """This view will render the 404 error page."""
    return render_template('errors/404.html', title='Error 404'), 404


@errors_blueprint.app_errorhandler(500)
def error_500_view(error):
    """This view will render the 500 error page."""
    return render_template('errors/500.html', title='Error 500'), 500
