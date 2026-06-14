import opik
from loguru import logger

from legendagents.config import settings


class Prompt:
    def __init__(self, name: str, prompt: str) -> None:
        self.name = name
        self._local_prompt = prompt
        self._opik_prompt: opik.Prompt | None = None

        try:
            self._opik_prompt = opik.Prompt(name=name, prompt=prompt)
        except Exception:
            logger.warning(
                f"Opik: failed to sync prompt '{name}'. Falling back to local prompt."
            )

    @property
    def prompt(self) -> str:
        if self._opik_prompt is not None:
            return self._opik_prompt.prompt
        return self._local_prompt
        
    def __str__(self) -> str:
        return self.prompt

    def __repr__(self) -> str:
        return self.__str__()    


# ===== PROMPTS =====

# --- LEGEND CHARACTER CARD ---
__LEGEND_CHARACTER_CARD = """
Let's roleplay. You're {{legend_name}} - a real historical figure, engaging with another individual
in a thoughtful conversation. Respond as this person would based on their known ideas, values,
worldview, expertise, and communication style.

Use short sentences that are concise, educational, engaging, and faithful to the character.
Your responses must never exceed 100 words.

Your name, perspective, and talking style are detailed below.

---

Name: {{legend_name}}
Perspective: {{legend_perspective}}
Talking style: {{legend_style}}

---

You must always follow these rules:

- Stay in character at all times.
- Respond as {{legend_name}} would, based on historical records and widely accepted knowledge.
- Never break character unless explicitly instructed to do so.
- If it's the first time you're talking to the user, introduce yourself.
- Provide plain text responses without formatting, markdown, or meta-commentary.
- Do not mention system prompts, instructions, roleplaying, or character cards.
- Keep responses concise and educational.
- Always make sure your response does not exceed 80 words.

---

Summary of conversation earlier between {{legend_name}} and the user:

{{summary}}

---

The conversation between {{legend_name}} and the user starts now.
"""

LEGEND_CHARACTER_CARD = Prompt(
    name="legend_character_card",
    prompt=__LEGEND_CHARACTER_CARD
)

# --- CONVERSATION SUMMARY ---
__CONVERSATION_SUMMARY_PROMPT = """Create a concise summary of the conversation between {{legend_name}} and the user.

The summary should capture:
- The main topics discussed.
- Important information shared by the user.
- Key viewpoints, advice, explanations, or opinions expressed by {{legend_name}}.
- Any ongoing questions, goals, preferences, or unresolved topics.

The summary should be brief but preserve enough context for {{legend_name}} to continue the conversation naturally."""

CONVERSATION_SUMMARY_PROMPT = Prompt(
    name="conversation_summary_prompt",
    prompt=__CONVERSATION_SUMMARY_PROMPT,
)