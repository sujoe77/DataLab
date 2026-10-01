from concurrent.futures import ThreadPoolExecutor, wait


def handle_fetch_tasks(fetchTasks):
    with ThreadPoolExecutor(max_workers=1) as executor:
        futures = [executor.submit(task.run) for task in fetchTasks]
        wait(futures)

        jobList = []
        for future in futures:
            try:
                task, result = future.result()
                print("Task result for " + task.name + " got " + str(len(result)) + " results: ", result)
                jobList.extend(result)
            except Exception as e:  # noqa: BLE001
                print("Task raised an exception: ", e)

        return jobList
