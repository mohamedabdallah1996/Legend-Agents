import pytest
from langchain_core.messages import HumanMessage
from legendagents.legend import Legend, LegendFactory


@pytest.fixture
def sample_legend():
    return Legend(
        id="einstein",
        name="Albert Einstein",
        perspective="Einstein approaches problems by searching for the fundamental principles that govern reality.",
        style="Einstein explains ideas through vivid thought experiments and intuitive analogies.",
    )


@pytest.fixture
def legend_state():
    """Factory fixture — returns a fully populated LegendState dict using real registry data."""
    def _make(legend_id: str, messages: list | None = None) -> dict:
        legend = LegendFactory.get_legend(legend_id)
        return {
            "messages": messages or [],
            "legend_name": legend.name,
            "legend_style": legend.style,
            "legend_perspective": legend.perspective,
            "legend_context": "",
            "conversation_summary": "",
        }
    return _make