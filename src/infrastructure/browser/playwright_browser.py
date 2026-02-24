"""Playwright browser implementation."""

from __future__ import annotations

from typing import Any

from playwright.async_api import Browser, Page, async_playwright

from src.domain.interfaces.browser import IBrowserAutomation
from src.infrastructure.browser.form_detector import FormDetector


class PlaywrightBrowser(IBrowserAutomation):
    """Concrete browser adapter using Playwright."""

    def __init__(self, headless: bool = True) -> None:
        self.headless = headless
        self._playwright: Any = None
        self._browser: Browser | None = None
        self._page: Page | None = None

    async def _ensure_page(self) -> Page:
        if self._page is None:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(headless=self.headless)
            self._page = await self._browser.new_page()
        return self._page

    async def navigate(self, url: str) -> None:
        page = await self._ensure_page()
        await page.goto(url)

    async def get_current_url(self) -> str:
        page = await self._ensure_page()
        return page.url

    async def get_page_title(self) -> str:
        page = await self._ensure_page()
        return await page.title()

    async def find_element(self, selector: str, timeout: float | None = None) -> Any | None:
        page = await self._ensure_page()
        return await page.query_selector(selector)

    async def find_elements(self, selector: str, timeout: float | None = None) -> list[Any]:
        page = await self._ensure_page()
        return await page.query_selector_all(selector)

    async def click(self, selector: str, timeout: float | None = None) -> None:
        page = await self._ensure_page()
        await page.click(selector, timeout=timeout * 1000 if timeout else None)

    async def fill(self, selector: str, value: str, timeout: float | None = None) -> None:
        page = await self._ensure_page()
        await page.fill(selector, value, timeout=timeout * 1000 if timeout else None)

    async def select_option(self, selector: str, value: str, timeout: float | None = None) -> None:
        page = await self._ensure_page()
        await page.select_option(selector, value, timeout=timeout * 1000 if timeout else None)

    async def upload_file(self, selector: str, file_path: str, timeout: float | None = None) -> None:
        page = await self._ensure_page()
        await page.set_input_files(selector, file_path, timeout=timeout * 1000 if timeout else None)

    async def wait_for_element(self, selector: str, timeout: float | None = None) -> None:
        page = await self._ensure_page()
        await page.wait_for_selector(selector, timeout=timeout * 1000 if timeout else None)

    async def wait_for_navigation(self, timeout: float | None = None) -> None:
        page = await self._ensure_page()
        await page.wait_for_load_state(timeout=timeout * 1000 if timeout else None)

    async def get_text(self, selector: str, timeout: float | None = None) -> str:
        page = await self._ensure_page()
        element = await page.wait_for_selector(selector, timeout=timeout * 1000 if timeout else None)
        if element is None:
            raise RuntimeError(f"Element not found for selector: {selector}")
        return await element.inner_text()

    async def get_attribute(self, selector: str, attribute: str, timeout: float | None = None) -> str | None:
        page = await self._ensure_page()
        element = await page.wait_for_selector(selector, timeout=timeout * 1000 if timeout else None)
        if element is None:
            return None
        return await element.get_attribute(attribute)

    async def screenshot(self, path: str | None = None) -> bytes:
        page = await self._ensure_page()
        return await page.screenshot(path=path)

    async def execute_script(self, script: str) -> Any:
        page = await self._ensure_page()
        return await page.evaluate(script)

    async def detect_forms(self) -> list[dict[str, Any]]:
        page = await self._ensure_page()
        return await FormDetector.detect(page)

    async def close(self) -> None:
        if self._browser is not None:
            await self._browser.close()
        if self._playwright is not None:
            await self._playwright.stop()
