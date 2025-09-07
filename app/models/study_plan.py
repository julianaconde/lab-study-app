from typing import Optional, Dict, Any
from pydantic import BaseModel

class StudyPlanRequest(BaseModel):
    area: str
    level: str
    weekly_hours: int
    duration_months: int
    specific_objectives: Optional[str] = None

class StudyPlanResponse(BaseModel):
    structured_plan: Optional[Dict[str, Any]] = None
    success: bool
    metadata: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
