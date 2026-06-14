from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from opik.integrations.langchain import OpikTracer
from contextlib import asynccontextmanager

from legendagents.legend import LegendFactory
from legendagents.services.chat_service import get_response
from legendagents.infrastructure.opik_utils import configure

configure()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles startup and shutdown events for the API."""
    # Startup code (if any) goes here
    yield
    # Shutdown code goes here
    opik_tracer = OpikTracer()
    opik_tracer.flush()

app = FastAPI(lifespan=lifespan)


class ChatMessage(BaseModel):
    message: str = Field(..., description="The message content to send to the Legend agent.")
    legend_id: str = Field(..., description="The identifier of the Legend agent to chat with.")

@app.post("/chat")
async def chat(chat_message: ChatMessage):
    try:
        legend = LegendFactory.get_legend(chat_message.legend_id)

        response = await get_response(
            messages=chat_message.message,
            legend_id=chat_message.legend_id,
            legend_name=legend.name,
            legend_style=legend.style,
            legend_perspective=legend.perspective,
            legend_context=""
        )

        return {"response": response}

    except Exception as e:
        opik_tracer = OpikTracer()
        opik_tracer.flush()

        raise HTTPException(status_code=500, detail=str(e))
