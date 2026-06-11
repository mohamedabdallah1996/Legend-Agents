
from legendagents.config import settings
from legendagents.agents.state import LegendState

from langgraph.graph import END
from typing_extensions import Literal

def should_summarize_conversation(
        state: LegendState
) -> Literal["summarize_conversation_node", "__end__"]:
    messages = state["messages"]
    if len(messages) >= settings.TOTAL_MESSAGES_SUMMARY_TRIGGER:
        return "summarize_conversation_node"
    
    return END