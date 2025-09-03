"""
Models for StudyPlan AI application (simplified version)
"""
from typing import Optional, Dict, Any

class StudyPlanRequest:
    """Simple class to represent a study plan request"""
    def __init__(
        self, 
        area: str, 
        level: str, 
        weekly_hours: int,
        duration_months: int,
        specific_objectives: Optional[str] = None
    ):
        self.area = area
        self.level = level
        self.weekly_hours = weekly_hours
        self.duration_months = duration_months
        self.specific_objectives = specific_objectives

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            area=data.get('area'),
            level=data.get('nivel'),
            weekly_hours=data.get('tempo_semanal'),
            duration_months=data.get('duracao_meses'),
            specific_objectives=data.get('objetivos_especificos')
        )

class StudyPlanResponse:
    """Simple class to represent a study plan response"""
    def __init__(
        self,
        structured_plan: str = "",
        success: bool = True,
        metadata: Dict[str, Any] = None,
        error: Optional[str] = None
    ):
        self.structured_plan = structured_plan
        self.success = success
        self.metadata = metadata or {}
        self.error = error
    
    def to_dict(self):
        return {
            "plano_estruturado": self.structured_plan,
            "sucesso": self.success,
            "metadata": self.metadata,
            "erro": self.error
        }
