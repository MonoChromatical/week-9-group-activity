import asyncio

async def fetch_metadata(doc_id):
    print(f"Fetching doc {doc_id}....")
    await asyncio.sleep(1)
    return f"Metadata {doc_id}"

async def fetch_all():
    results = await asyncio.gather(
        fetch_metadata(1),
        fetch_metadata(2),
        fetch_metadata(3)
    )
    return results