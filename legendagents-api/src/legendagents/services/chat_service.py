
from legendagents.agents.graph import graph

from typing import Any, Union
from langchain_core.messages import AIMessage, AIMessageChunk, HumanMessage


async def get_response(
    messages: str | list[str] | list[dict[str, Any]],    
    legend_id: str,
    legend_name: str,
    legend_style: str,
    legend_perspective: str,
    legend_context: str = "",
) -> str:
    """
    Generate a response from the Legend agent based on the provided messages and legend attributes.

    Args:
        messages (str | list[str] | list[dict[str, Any]]): The conversation history or input messages.
        legend_id (str): The identifier for the legend (e.g., "einstein", "newton").
        legend_name (str): The name of the legend.
        legend_style (str): The communication style of the legend.
        legend_perspective (str): The perspective or beliefs of the legend.
        legend_context (str, optional): Additional context to inform the response generation. Defaults to "".

    Returns:
        str: The generated response from the Legend agent.
    """
    try:
        output_state = await graph.ainvoke(
            input={
                "messages": __format_messages(messages),
                "legend_id": legend_id,
                "legend_name": legend_name,
                "legend_style": legend_style,
                "legend_perspective": legend_perspective,
                "legend_context": legend_context
            }
        )

        last_message = output_state["messages"][-1]
        return last_message.content
    
    except Exception as e:
        raise RuntimeError(f"Error generating response from Legend agent: {str(e)}") from e
    

def __format_messages(
    messages: Union[str, list[dict[str, Any]]],
) -> list[Union[HumanMessage, AIMessage]]:
    """Convert various message formats to a list of LangChain message objects.

    Args:
        messages: Can be one of:
            - A single string message
            - A list of string messages
            - A list of dictionaries with 'role' and 'content' keys

    Returns:
        List[Union[HumanMessage, AIMessage]]: A list of LangChain message objects
    """
    if isinstance(messages, str):
        return [HumanMessage(content=messages)]

    if isinstance(messages, list):
        if not messages:
            return []

        if (
            isinstance(messages[0], dict)
            and "role" in messages[0]
            and "content" in messages[0]
        ):
            result = []
            for msg in messages:
                if msg["role"] == "user":
                    result.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    result.append(AIMessage(content=msg["content"]))
            return result

        return [HumanMessage(content=message) for message in messages]

    return []
