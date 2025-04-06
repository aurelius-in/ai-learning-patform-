import time
import random

def simulate_api_load(n_requests):
    success_count = 0
    for _ in range(n_requests):
        # Simulate success/failure response times
        response_time = random.uniform(0.01, 0.2)
        time.sleep(response_time / 100)  # scale for test
        if response_time < 0.15:
            success_count += 1
    return success_count / n_requests

def test_api_scalability():
    start = time.time()
    success_rate = simulate_api_load(500)
    duration = time.time() - start
    print(f"Success Rate: {success_rate:.2%}")
    print(f"Completed in: {duration:.2f} seconds")

if __name__ == "__main__":
    test_api_scalability()
