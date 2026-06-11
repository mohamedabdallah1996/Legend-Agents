
from langgraph.graph import MessagesState


class LegendState(MessagesState):
    """
    State class for the LangGraph workflow. It keeps track of the information necessary to maintain a coherent
    conversation between the Legend and the user.

    Attributes: 
        legend_name (str): The name of the legend being represented.
        legend_style (str): The communication style of the legend.
        legend_perspective (str): The perspective or worldview of the legend.
        legend_context (str): Additional context about the legend that may be relevant to the conversation.
        conversation_summary (str): A summary of the conversation so far, which can be used to 
    """
    legend_name: str 
    legend_style: str
    legend_perspective: str
    legend_context: str
    conversation_summary: str
    

