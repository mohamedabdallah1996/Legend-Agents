from unittest.mock import AsyncMock, patch

import pytest
from langchain_core.messages import AIMessage, HumanMessage, RemoveMessage

from legendagents.agents.nodes import conversation_node, summarize_conversation_node
from legendagents.config import settings


async def test_conversation_node_returns_ai_message(legend_state):
    """
    Test does conversation_node() return the AI message from the chain?
    """
    state = legend_state("einstein", messages=[HumanMessage(content="What is gravity?")])
    fake_reply = AIMessage(content="Gravity is a curvature of spacetime.")
    mock_chain = AsyncMock(ainvoke=AsyncMock(return_value=fake_reply))

    with patch("legendagents.agents.nodes.get_conversation_chain", return_value=mock_chain):
        result = await conversation_node(state, {})

    assert result["messages"] == fake_reply


async def test_conversation_node_passes_correct_summary_key(legend_state):
    """
    Test does conversation_node() send the correct input data into the chain?
    """
    state = legend_state("einstein", messages=[HumanMessage(content="Tell me more.")])
    state["conversation_summary"] = "We discussed time dilation."
    mock_chain = AsyncMock(ainvoke=AsyncMock(return_value=AIMessage(content="...")))

    with patch("legendagents.agents.nodes.get_conversation_chain", return_value=mock_chain):
        await conversation_node(state, {})

    invoked_with = mock_chain.ainvoke.call_args[0][0]
    assert invoked_with["summary"] == "We discussed time dilation."
    assert invoked_with["legend_name"] == state["legend_name"]


async def test_summarize_node_stores_summary(legend_state):
    messages = [HumanMessage(content=f"msg {i}", id=f"id-{i}") for i in range(10)]
    state = legend_state("einstein", messages=messages)
    mock_chain = AsyncMock(ainvoke=AsyncMock(return_value="Summary of the conversation."))

    with patch("legendagents.agents.nodes.get_summary_chain", return_value=mock_chain):
        result = await summarize_conversation_node(state)

    assert result["conversation_summary"] == "Summary of the conversation."


async def test_summarize_node_removes_old_messages(legend_state):
    n = settings.TOTAL_MESSAGES_AFTER_SUMMARY + 5
    messages = [HumanMessage(content=f"msg {i}", id=f"id-{i}") for i in range(n)]
    state = legend_state("einstein", messages=messages)
    mock_chain = AsyncMock(ainvoke=AsyncMock(return_value="Summary."))

    with patch("legendagents.agents.nodes.get_summary_chain", return_value=mock_chain):
        result = await summarize_conversation_node(state)

    removed_ids = {m.id for m in result["messages"]}
    kept_ids = {m.id for m in messages[-settings.TOTAL_MESSAGES_AFTER_SUMMARY:]}
    removed_expected = {m.id for m in messages[:-settings.TOTAL_MESSAGES_AFTER_SUMMARY]}

    assert removed_ids == removed_expected
    assert removed_ids.isdisjoint(kept_ids)
