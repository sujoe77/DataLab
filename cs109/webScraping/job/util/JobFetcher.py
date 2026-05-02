from concurrent.futures import ThreadPoolExecutor, wait


def fetchJobs(fetchTasks):
    with ThreadPoolExecutor(max_workers=1) as executor:
        futures = [executor.submit(task.run) for task in fetchTasks]
        wait(futures)
