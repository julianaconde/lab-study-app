"""
AI prompts for generating study plans
"""
from typing import List, Dict, Optional

def build_study_plan_prompt(area: str, nivel: str, tempo: int, duracao: int, objetivos: Optional[str] = None) -> List[Dict]:
    area_mapping = {
        "backend": "Backend Development",
        "frontend": "Frontend Development",
        "fullstack": "Full-Stack Development",
        "data_science": "Data Science",
        "ai_ml": "Artificial Intelligence and Machine Learning",
    }

    level_mapping = {
        "iniciante": "Beginner (little or no experience)",
        "intermediario": "Intermediate (has been programming for some time)",
        "avancado": "Advanced (significant professional experience)",
    }

    system_prompt = """
    You are an education specialist with over 10 years of experience.
    Your mission is to create practical, structured, and realistic study plans.
    Always respond in the user's preferred language.
    Include progressive hands-on projects and specific resources (courses, books, tools).
    Requirements:
    1. Provide a detailed weekly schedule for the entire duration.
    2. Recommend specific resources (courses, books, tools, communities) for each phase.
    3. Include progressive practical projects for each month.
    4. Define monthly evaluation milestones.
    5. Make the plan structured, realistic, and actionable.

    Format:
    - Weekly schedule
    - Monthly roadmap with projects and milestones
    - List of resources (with links if possible)
    - Practical projects description
    - Evaluation milestones
    - Success tips

    Be specific, motivational, and always respond in the user's preferred language!
"""

    user_prompt = f"""
    Create a detailed and personalized study plan for:

    📊 STUDENT PROFILE:
    - Area: {area_mapping.get(area, area)}
    - Level: {level_mapping.get(nivel, nivel)}
    - Available time per week: {tempo} hours
    - Total duration: {duracao} months
    - Objectives: {objetivos or "Not specified"}

    Requirements:
    1. Provide a detailed weekly schedule for the entire duration.
    2. Recommend specific resources (courses, books, tools, communities) for each phase.
    3. Include progressive practical projects for each month.
    4. Define monthly evaluation milestones.
    5. Make the plan structured, realistic, and actionable.

    Format:
    - Weekly schedule
    - Monthly roadmap with projects and milestones
    - List of resources (with links if possible)
    - Practical projects description
    - Evaluation milestones
    - Success tips

    Be specific, motivational, and always respond in the user's preferred language!
"""

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
