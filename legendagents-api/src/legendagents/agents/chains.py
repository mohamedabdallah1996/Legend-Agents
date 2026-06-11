
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


from legendagents.config import settings
from legendagents.domain.prompts import LEGEND_CHARACTER_CARD, CONVERSATION_SUMMARY_PROMPT


def get_chat_model(temperature: float = 0.7, model_name: str = settings.GROQ_LLM_MODEL) -> ChatGroq:
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model_name=model_name,
        temperature=temperature,
    )


def get_conversation_chain():
    """
    Gets the conversation chain for the Legend agent. This chain will be responsible for managing the conversation flow,
    including generating responses from the Legend based on the character card and the conversation history.
    """
    model = get_chat_model()
    system_message = LEGEND_CHARACTER_CARD

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message.prompt),
            MessagesPlaceholder(variable_name="messages"),
        ],
        template_format="jinja2"
    )

    return prompt | model


def get_summary_chain():
    """
    Gets the summary chain for the Legend agent. This chain will be responsible for summarizing the conversation history
    to provide context for the Legend's responses.
    """
    model = get_chat_model(model_name=settings.GROQ_LLM_MODEL_CONTEXT_SUMMARY)
    summary_message = CONVERSATION_SUMMARY_PROMPT

    prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder(variable_name="messages"),
            ("human", summary_message.prompt),
        ],
        template_format="jinja2"
    )

    return prompt | model


    