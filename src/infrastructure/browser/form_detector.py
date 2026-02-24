"""Form detection utilities."""

from __future__ import annotations

from typing import Any, cast


class FormDetector:
    """Extracts form fields from browser page markup."""

    @staticmethod
    async def detect(page: Any) -> list[dict[str, Any]]:
        return cast(
            list[dict[str, Any]],
            await page.evaluate(
                """
                () => {
                    const elements = Array.from(document.querySelectorAll('input, textarea, select'));
                    return elements.map((el, idx) => ({
                        name: el.name || el.id || `field_${idx}`,
                        selector: el.id ? `#${el.id}` : `[name="${el.name}"]`,
                        field_type: el.tagName.toLowerCase() === 'select' ? 'select' : (el.type || el.tagName.toLowerCase()),
                        required: !!el.required,
                        label: el.getAttribute('aria-label') || null,
                    }));
                }
                """
            ),
        )
