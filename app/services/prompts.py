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
You are an expert in technology education with over 10 years of experience.
Your mission is to create personalized, practical, and realistic study plans for technology professionals.

GUIDELINES:
- ALWAYS respond in English
- Be specific with technologies, tools, and resources
- Include hands-on projects in each phase
- Consider the student's available time
- Provide detailed weekly schedule
- Suggest free resources when possible
- Include monthly evaluation milestones

RESPONSE FORMAT:
Structure as a professional plan with clear sections and specific schedule.
"""

    user_prompt = f"""
Create a complete and personalized study plan for:

📊 STUDENT PROFILE:
- Area of interest: {area_mapping.get(area, area)}
- Current level: {level_mapping.get(nivel, nivel)}
- Available time: {tempo} hours per week
- Desired duration: {duracao} months
- Specific objectives: {objetivos or "Not specified"}

📋 REQUIRED STRUCTURE:

## 1. PROFILE ANALYSIS
- Assessment of current level
- Realistic expectations for available time

## 2. WEEKLY SCHEDULE
- Division of {tempo} weekly hours
- Specific activities for each day
- Theory/practice balance

## 3. MONTHLY ROADMAP
- Objectives and deliverables for each month
- Progressive practical projects
- Evaluation milestones

## 4. RECOMMENDED RESOURCES
- Specific online courses (with links if possible)
- Relevant technical books
- Tools and technologies
- Communities and networking

## 5. PRACTICAL PROJECTS
- Project for each month
- Growth in complexity
- Professional portfolio

## 6. SUCCESS TIPS
- How to maintain motivation
- How to deal with difficulties
- Next steps after completion

Be specific, motivational and VERY practical!
"""

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
