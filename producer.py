import time

def save_job_to_file(job_id, status):
    with open('jobs.txt', 'a') as file:
        file.write(f"{job_id},{status}\n")

def main():
    job_id = 1
    while True:
        save_job_to_file(job_id, 'pending')
        print(f"Job {job_id} added to the queue.")
        job_id += 1
        time.sleep(10)

if __name__ == "__main__":
    main()
