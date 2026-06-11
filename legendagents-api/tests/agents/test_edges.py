from langgraph.graph import END
from langchain_core.messages import HumanMessage

from legendagents.agents.edges import should_summarize_conversation
from legendagents.config import settings


def test_below_threshold_routes_to_end(legend_state):
    state = legend_state("einstein", messages=[
        HumanMessage(content=f"msg {i}")
        for i in range(settings.TOTAL_MESSAGES_SUMMARY_TRIGGER - 1)
    ])
    assert should_summarize_conversation(state) == END


def test_at_threshold_routes_to_summarize(legend_state):
    state = legend_state("einstein", messages=[
        HumanMessage(content=f"msg {i}")
        for i in range(settings.TOTAL_MESSAGES_SUMMARY_TRIGGER)
    ])
    assert should_summarize_conversation(state) == "summarize_conversation_node"


def test_empty_messages_routes_to_end(legend_state):
    state = legend_state("einstein")
    assert should_summarize_conversation(state) == END
