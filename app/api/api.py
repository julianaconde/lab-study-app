"""
REST API of StudyPlan AI (simplified version)
"""
import os
import asyncio
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
from pathlib import Path

from app.models import StudyPlanRequest, StudyPlanResponse
from app.services.prompts import build_study_plan_prompt
"""
from app.services.github_client import GitHubModelsClient
"""
from app.models.study_plan import StudyPlanRequest, StudyPlanResponse

# Load .env from project root
project_root_env = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=project_root_env if project_root_env.exists() else None)

# Create a Flask blueprint instead of FastAPI
api_bp = Blueprint('api', __name__)

"""
# Initialize GitHub client
# github_client = GitHubModelsClient()
"""

@api_bp.route("/", methods=["GET"])
def root():
    return jsonify({"status": "ok", "message": "StudyPlan AI API"})

@api_bp.route("/generate-plan", methods=["POST"])
def generate_study_plan():
    data = request.json
    if not data:
        return jsonify({"success": False, "error": "Invalid data"}), 400
    # Create StudyPlanRequest object from JSON data
    req = StudyPlanRequest.from_dict(data)





    try:
        # Construir prompt usando os parâmetros do StudyPlanRequest
        prompt = build_study_plan_prompt(
            area=req.area,
            nivel=req.level,
            tempo=req.weekly_hours,
            duracao=req.duration_months,
            objetivos=req.specific_objectives
        )
        # Simulação de resposta
        generated_plan = f"Plano gerado para área: {req.area}, nível: {req.level}, tempo semanal: {req.weekly_hours}, duração: {req.duration_months}, objetivos: {req.specific_objectives}. (Simulado)"
        response = StudyPlanResponse(
            structured_plan=generated_plan,
            success=True,
            metadata={
                "area": req.area,
                "level": req.level,
                "weekly_hours": req.weekly_hours,
                "duration_months": req.duration_months,
            }
        )
        return jsonify(response.to_dict())

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Error generating study plan: {str(e)}"
        }), 500
