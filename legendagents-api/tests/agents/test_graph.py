"""
Integration tests — require a valid GROQ_API_KEY in .env.
Run with:  pytest -m integration
LangSmith tracing is enabled automatically when LANGSMITH_API_KEY is set in .env.
"""

import pytest
from langchain_core.messages import AIMessage, HumanMessage

from legendagents.agents.graph import graph


@pytest.mark.integration
async def test_graph_compiles():
    assert graph is not None


@pytest.mark.integration
async def test_einstein_single_turn(legend_state):
    state = legend_state("einstein", messages=[
        HumanMessage(content="What is your theory of relativity in simple terms?")
    ])

    result = await graph.ainvoke(state)

    assert len(result["messages"]) >= 2
    assert isinstance(result["messages"][-1], AIMessage)
    assert len(result["messages"][-1].content) > 0


@pytest.mark.integration
async def test_gandhi_single_turn(legend_state):
    state = legend_state("gandhi", messages=[
        HumanMessage(content="How should we respond to injustice?")
    ])

    result = await graph.ainvoke(state)

    assert isinstance(result["messages"][-1], AIMessage)
    assert len(result["messages"][-1].content) > 0
