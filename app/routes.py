from flask import Blueprint
from controllers.analysis_controller import analyze
from controllers.home_controller import home

bp_analysis = Blueprint("analysis", __name__)
bp_analysis.route("/analyze", methods=["POST"])(analyze)
bp_analysis.route("/", methods=["GET"])(home)
