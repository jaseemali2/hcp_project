# Install Declarative Automation Bundles package locally
# pip install databricks-bundles==0.275.0
#
# copy contents into resources/test_job.py
from databricks.bundles.jobs import Job


test_job = Job.from_dict(
    {
        "name": "test_job",
        "tasks": [
            {
                "task_key": "tsk1",
                "notebook_task": {
                    "notebook_path": "performance/pg.ipynb",
                },
            },
        ],
        "queue": {
            "enabled": True,
        },
        # "run_as": {
        #     "service_principal_name": "da1a3e69-c15b-4e1d-9aa6-cf15b3958825",
        # },
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)
