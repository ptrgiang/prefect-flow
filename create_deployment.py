from prefect import flow

# Source for the code to deploy (here, a GitHub repo)
SOURCE_REPO="https://github.com/ptrgiang/prefect-flow.git"

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="my_workflow.py:main", # Specific flow to run
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-work-pool",
        cron="0 * * * *",  # Run every hour
    )