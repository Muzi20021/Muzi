import time

def process_job(job_id):

    time.sleep(30)
    print(f"Job {job_id} completed.")

def read_jobs_from_file():
    with open('jobs.txt', 'r') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines]

def update_job_status(job_id, new_status):
    with open('jobs.txt', 'r') as file:
        lines = file.readlines()
    with open('jobs.txt', 'w') as file:
        for line in lines:
            job, status = line.strip().split(',')
            if job == job_id:
                file.write(f"{job},{new_status}\n")
            else:
                file.write(line)

def main():
    while True:
        jobs = read_jobs_from_file()
        for job in jobs:
            job_id, status = job
            if status == 'pending':
                print(f"Job {job_id} in progress.")
                process_job(job_id)
                update_job_status(job_id, 'done')
        time.sleep(5)  # Sprawdzanie pracy co 5 sekund

if __name__ == "__main__":
    main()
