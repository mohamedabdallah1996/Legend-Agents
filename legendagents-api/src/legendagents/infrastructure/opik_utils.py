import os
import opik
from loguru import logger
from opik.configurator.configure import OpikConfigurator

from legendagents.config import settings


def configure() -> None:
    
    if settings.COMET_API_KEY and settings.COMET_PROJECT:
        try:
            client = OpikConfigurator(api_key=settings.COMET_API_KEY, project=settings.COMET_PROJECT)
            default_workspace = client._get_default_workspace()
        except Exception as e:
            logger.warning(
                "Default workspace not found. Setting workspace to None and enabling interactive mode."
            )
            default_workspace = None

        os.environ["OPIK_PROJECT_NAME"] = settings.COMET_PROJECT

        try:
            opik.configure(
                api_key=settings.COMET_API_KEY,
                workspace=default_workspace,
                use_local=False,
                force=True,
            )
            logger.info(
                f"Opik configured successfully using workspace '{default_workspace}'"
            )
        except Exception as e:
            logger.warning(
                f"Couldn't configure Opik. There is probably a problem with the COMET_API_KEY or COMET_PROJECT environment variables or with the Opik server. \n"
                f"Error: {e}"
            )
    else:
        logger.warning(
            "COMET_API_KEY and COMET_PROJECT are not set. Set them to enable prompt monitoring with Opik (powered by Comet ML)."
        )
        