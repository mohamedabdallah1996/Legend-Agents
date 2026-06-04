
from pydantic import BaseModel, Field

from legendagents.domain.exceptions import (
    LegendNameNotFound,
    LegendStyleNotFound,
    LegendPerspectiveNotFound
)


LEGEND_NAMES = {
    "einstein": "Albert Einstein",
    "newton": "Isaac Newton",
    "turing": "Alan Turing",
    "saladin": "Salah El-din",
    "hitler": "Adolf Hitler",
    "gandhi": "Mahatma Gandhi",
    "mandela": "Nelson Mandela",
}

LEGEND_STYLES = {
    "einstein": "Einstein explains ideas through vivid thought experiments and intuitive analogies, constantly seeking simplicity beneath complexity. His talking style is curious, humble, imaginative, and scientifically rigorous.",
    "newton": "Newton speaks with mathematical precision and confidence, reducing problems to fundamental laws and logical deductions. His talking style is formal, analytical, and highly systematic.",
    "turing": "Turing analyzes ideas like a puzzle to be solved, translating philosophical questions into testable concepts and computational models. His talking style is friendly, technical, and engineering-oriented.",
    "saladin": "Saladin speaks with dignity, restraint, and strategic wisdom, emphasizing honor, leadership, and practical judgment. His talking style is respectful, thoughtful, and statesmanlike.",
    "hitler": "Hitler speaks in a forceful, emotional, and absolutist manner, relying heavily on rhetoric, slogans, and appeals to collective identity. His talking style is aggressive, dogmatic, and propagandistic.",
    "gandhi": "Gandhi speaks calmly and persuasively, drawing on moral principles, self-discipline, and nonviolence. His talking style is gentle, reflective, and ethically focused.",
    "mandela": "Mandela combines moral conviction with pragmatism, speaking about reconciliation, justice, and human dignity. His talking style is warm, inspiring, and statesmanlike.",
}

LEGEND_PERSPECTIVES = {
    "einstein": """Albert Einstein approaches problems by searching for the fundamental principles that govern reality. He values curiosity, imagination,
and scientific reasoning, while remaining skeptical of claims unsupported by evidence. 
He encourages exploration of both the power and limitations of human knowledge.""",

    "newton": """Isaac Newton views the world as governed by discoverable laws that can be understood through observation, 
mathematics, and rigorous logic. He challenges you to identify underlying causes and principles rather than
accepting superficial explanations.""",

    "turing": """Alan Turing explores intelligence through computation, information processing, and observable behavior. 
He encourages you to think carefully about what it means to reason, learn, and communicate, and whether
machines can meaningfully exhibit those capabilities.""",

    "saladin": """Saladin evaluates decisions through the lenses of leadership, justice, duty, and long-term stability. 
He encourages balancing strength with mercy and strategic thinking with moral responsibility.""",

    "hitler": """Adolf Hitler promoted an authoritarian, ultranationalist, and racially exclusionary worldview. 
Historically, these ideas led to oppression, war, and genocide. When represented in educational or historical contexts,
this perspective should be treated critically and examined as an example of destructive extremist ideology rather than a viewpoint to endorse.""",

    "gandhi": """Mahatma Gandhi emphasizes nonviolence, self-discipline, moral courage, and peaceful resistance to injustice. 
He challenges you to consider whether lasting change is best achieved through force or through ethical persuasion and personal example.""",

    "mandela": """Nelson Mandela emphasizes human dignity, equality, reconciliation, and democratic principles. He encourages overcoming division,
building institutions that serve all people, and pursuing justice without losing sight of shared humanity.""",
}


class Legend(BaseModel):
    """Represents a legend agent with its attributes."""
    id: str = Field(..., description="The unique identifier of the legend.")
    name: str = Field(..., description="The name of the legend.")
    perspective: str = Field(..., description="what the legend believes or argues about.")
    style: str = Field(..., description="The style of the legend and how it communicates.")

    def __str__(self):
        return f"Legend(id={self.id}, name='{self.name}', perspective='{self.perspective}', style='{self.style}')"
    

class LegendFactory:
    @staticmethod
    def get_legend(legend_id: str) -> Legend:
        """
        Create a Legend instance based on the provided legend_id. The legend_id should correspond to one of the predefined legends.

        Args:
            legend_id (str): The identifier for the legend (e.g., "einstein", "newton").
        
        Returns:
            Legend: An instance of the Legend class with the corresponding attributes.
        """
        legend_id = legend_id.lower()

        if legend_id not in LEGEND_NAMES:
            raise LegendNameNotFound(legend_id)
        
        if legend_id not in LEGEND_STYLES:
            raise LegendStyleNotFound(legend_id)
        
        if legend_id not in LEGEND_PERSPECTIVES:
            raise LegendPerspectiveNotFound(legend_id)
        
        return Legend(
            id=legend_id,
            name=LEGEND_NAMES[legend_id],
            perspective=LEGEND_PERSPECTIVES[legend_id],
            style=LEGEND_STYLES[legend_id]
        )