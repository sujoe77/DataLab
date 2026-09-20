from datetime import datetime
from zoneinfo import ZoneInfo

from constants import EXECLUDE_COMPANY, EXECLUDE_TITLE, KEYWORD_DIC_ALL, OUTPUT_FOLDER
from FetchTask import FetchTask
from LinkedIn import LinkedInJob
from util.JobFetcher import handle_fetch_tasks


def main():
    jobList = fetch_jobs()
    save_jobs_to_file(jobList)


if __name__ == "__main__":
    main()


def fetch_jobs():
    job_sites = [LinkedInJob(EXECLUDE_TITLE, EXECLUDE_COMPANY)]

    jl = []
    for jobSite in job_sites:
        tasks = [
            FetchTask(jobSite, [keyWord], size, "task_" + keyWord, 5)
            for keyWord, size in KEYWORD_DIC_ALL.items()
        ]
        jl.extend(handle_fetch_tasks(tasks))

    return jl


def save_jobs_to_file(jobList):
    output_file = get_output_file_name()
    print("write to output file: " + output_file)
    with open(output_file, "w") as file:
        file.writelines(f"{item}\n" for item in jobList)


def get_output_file_name():
    now = datetime.now(ZoneInfo("Europe/Copenhagen"))
    format = now.strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_FOLDER + "jobs_" + format + ".txt"
    return output_file
