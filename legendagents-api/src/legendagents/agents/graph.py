
from langgraph.graph import StateGraph, START, END
from legendagents.agents.nodes import conversation_node, summarize_conversation_node
from legendagents.agents.edges import should_summarize_conversation
from legendagents.agents.state import LegendState
from functools import lru_cache


@lru_cache(maxsize=1)
def create_workflow_graph():
    graph_builder = StateGraph(LegendState)

    # add all nodes
    graph_builder.add_node("conversation_node", conversation_node)
    graph_builder.add_node("summarize_conversation_node", summarize_conversation_node)

    # add edges
    graph_builder.add_edge(START, "conversation_node")
    graph_builder.add_conditional_edges("conversation_node", should_summarize_conversation)
    graph_builder.add_edge("summarize_conversation_node", END)

    return graph_builder 

graph = create_workflow_graph().compile()