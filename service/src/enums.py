from enum import Enum
import os


class ServiceEnum(Enum):
    model = os.getenv("LLM_MODEL_NAME", "")
    base_url=os.getenv("LLM_BASE_URL", "")