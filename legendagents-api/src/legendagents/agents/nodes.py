from legendagents.config import settings
from legendagents.agents.state import LegendState
from legendagents.agents.chains import get_conversation_chain, get_summary_chain

from langchain_core.runnables import RunnableConfig
from langchain_core.messages import RemoveMessage


async def conversation_node(state: LegendState, config: RunnableConfig):
    """
    Conversation node that processes the conversation messages and generates a response using the conversation chain.
    """
    conversation_summary = state.get("conversation_summary", "")
    conversation_chain = get_conversation_chain()

    response = await conversation_chain.ainvoke(
        {
            "messages": state["messages"],
            "legend_name": state["legend_name"],
            "legend_perspective": state["legend_perspective"],
            "legend_style": state["legend_style"],
            "summary": conversation_summary
        },
        config
    )

    return {"messages": response}


async def summarize_conversation_node(state: LegendState):
    """
    Summarize conversation node that takes the conversation messages and generates a summary to be used as context for the conversation chain.
    """
    summary_chain = get_summary_chain()

    summary = await summary_chain.ainvoke(
        {
            "messages": state["messages"],
            "legend_name": state["legend_name"]
        }
    )

    updated_messages = [
        RemoveMessage(id=m.id)
        for m in state["messages"][:-settings.TOTAL_MESSAGES_AFTER_SUMMARY]
    ]

    return {"conversation_summary": summary, "messages": updated_messages}