import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


HASHTAGS_TO_TRACK = [
    "shoes",
    "sneakers",
    "trendy",
]


async def scrape_hashtag(page, hashtag: str):
    url = f"https://www.instagram.com/explore/tags/{hashtag}/"
    print(f"Scraping: {url}")

    await page.goto(url, wait_until="networkidle")

    # HTML extraction
    html = await page.content()
    soup = BeautifulSoup(html, "html.parser")

    # Instagram loads posts inside <article>
    posts = soup.find_all("div", attrs={"role": "button"})

    results = []

    for post in posts[:12]:  # top posts only
        caption = post.get_text(separator=" ").strip()
        if caption:
            results.append(caption)

    return {
        "hashtag": hashtag,
        "top_posts": results,
    }


async def run_trend_agent():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        all_results = []

        for tag in HASHTAGS_TO_TRACK:
            try:
                result = await scrape_hashtag(page, tag)
                all_results.append(result)
            except Exception as e:
                print(f"Error scraping #{tag}: {e}")

        await browser.close()

        print("\n=== Trend Summary ===\n")
        for entry in all_results:
            print(f"### Trend: #{entry['hashtag']}")
            for i, post in enumerate(entry["top_posts"][:5], 1):
                print(f"{i}. {post[:200]}...")
            print("\n")

        return all_results


if __name__ == "__main__":
    asyncio.run(run_trend_agent())
