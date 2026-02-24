"""OpenAI-compatible LLM client."""

from __future__ import annotations

import asyncio
import json
from typing import Any, cast

from openai import AsyncOpenAI

from src.domain.interfaces.llm import ILLMClient


class OpenAIClient(ILLMClient):
    """Thin async wrapper for OpenAI-compatible chat APIs."""

    def __init__(self, api_key: str, model_name: str, base_url: str = "https://api.openai.com/v1") -> None:
        self.model_name = model_name
        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)
        self.max_retries = 3

    async def chat_completion(
        self,
        messages: list[dict[str, str]],
        model: str | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
        tools: list[dict[str, Any]] | None = None,
        tool_choice: str | None = None,
    ) -> dict[str, Any]:
        request: dict[str, Any] = {
            "model": model or self.model_name,
            "messages": messages,
        }
        if temperature is not None:
            request["temperature"] = temperature
        if max_tokens is not None:
            request["max_tokens"] = max_tokens
        if tools is not None:
            request["tools"] = tools
        if tool_choice is not None:
            request["tool_choice"] = tool_choice
        for attempt in range(self.max_retries):
            try:
                response = await self.client.chat.completions.create(**request)
                return cast(dict[str, Any], response.model_dump())
            except Exception:
                if attempt == self.max_retries - 1:
                    raise
                await asyncio.sleep(0.2 * (attempt + 1))
        return {"choices": [{"message": {"content": ""}}]}

    async def extract_structured_data(
        self,
        text: str,
        schema: dict[str, Any],
        model: str | None = None,
    ) -> dict[str, Any]:
        prompt = (
            "Extract structured JSON from this text.\n"
            f"Schema: {json.dumps(schema)}\n"
            f"Text:\n{text}"
        )
        result = await self.chat_completion(
            messages=[
                {"role": "system", "content": "You output strict JSON only."},
                {"role": "user", "content": prompt},
            ],
            model=model,
            temperature=0.0,
        )
        content = result["choices"][0]["message"]["content"]
        return json.loads(content) if content else {}

    async def generate_text(
        self,
        prompt: str,
        model: str | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
    ) -> str:
        result = await self.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return result["choices"][0]["message"]["content"] or ""
