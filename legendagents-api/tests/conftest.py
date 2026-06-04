import pytest
from legendagents.legend import Legend


@pytest.fixture
def sample_legend():
    return Legend(
        id="einstein",
        name="Albert Einstein",
        perspective="Einstein approaches problems by searching for the fundamental principles that govern reality.",
        style="Einstein explains ideas through vivid thought experiments and intuitive analogies.",
    )