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
from app.services.github_client import GitHubModelsClient

# Load .env from project root
project_root_env = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=project_root_env if project_root_env.exists() else None)

# Create a Flask blueprint instead of FastAPI
api_bp = Blueprint('api', __name__)

# Initialize GitHub client
github_client = GitHubModelsClient()

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
    
    # Simplified version: Return an example plan instead of calling the API
    example_plan = f"""
# PERSONALIZED STUDY PLAN

## 1. PROFILE ANALYSIS

**Area of interest:** {req.area.title()}
**Current level:** {req.level.title()}
**Available time:** {req.weekly_hours} hours per week
**Desired duration:** {req.duration_months} months
**Specific objectives:** {req.specific_objectives or "General development"}

## 2. WEEKLY SCHEDULE

- **Monday:** 1 hour of theory, 1 hour of practice
- **Wednesday:** 1 hour of documentation study
- **Friday:** 1 hour of practical project
- **Weekend:** 2 hours of practice on personal project

## 3. MONTHLY ROADMAP

### Month 1: Fundamentals
- Week 1-2: Basic concepts
- Week 3-4: Essential tools

### Month 2: Intermediate
- Week 1-2: Patterns and best practices
- Week 3-4: Intermediate practical project

### Month 3: Advanced
- Week 1-2: Advanced topics
- Week 3-4: Final project

## 4. RECOMMENDED RESOURCES

- Official documentation
- Free online courses
- Developer communities
- Open source projects

## 5. PRACTICAL PROJECTS

- **Project 1:** Basic application of concepts
- **Project 2:** Implementation of intermediate features
- **Project 3:** Complete portfolio project

## 6. SUCCESS TIPS

- Practice regularly
- Participate in communities
- Contribute to open source projects
- Keep a record of your progress
"""
    
    response = StudyPlanResponse(
        structured_plan=example_plan,
        success=True,
        metadata={
            "area": req.area,
            "level": req.level,
            "weekly_hours": req.weekly_hours,
            "duration_months": req.duration_months,
        }
    )
    
    return jsonify(response.to_dict())
