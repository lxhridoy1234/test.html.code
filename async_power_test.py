import asyncio
import aiohttp
import time

# ===================== ইউজারের ইনপুট =====================
url = input("Enter target URL: ")
num_requests = int(input("Enter number of requests: "))
concurrency = int(input("Enter concurrency limit (একসাথে কতগুলো): "))
delay = float(input("Enter delay between requests (seconds): "))

# ===================== Custom headers =====================
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PowerTestBot/1.0"
}

# ===================== Global counters =====================
success_count = 0
fail_count = 0

# ===================== Concurrency control =====================
sem = asyncio.Semaphore(concurrency)

# ===================== Fetch function =====================
async def fetch(session, i):
    global success_count, fail_count
    async with sem:
        try:
            async with session.get(url, headers=headers) as response:
                status = response.status
                if 200 <= status < 400:
                    success_count += 1
                else:
                    fail_count += 1
                print(f"[{i}] Status: {status}")
        except Exception as e:
            fail_count += 1
            print(f"[{i}] Error: {e}")
        await asyncio.sleep(delay)

# ===================== Main runner =====================
async def run():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(num_requests):
            task = asyncio.create_task(fetch(session, i))
            tasks.append(task)
        await asyncio.gather(*tasks)

# ===================== Script execution =====================
if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(run())
    end_time = time.time()
    print("\n✅ Test Finished")
    print(f"Total requests: {num_requests}")
    print(f"Successful: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
