# Install Declarative Automation Bundles package locally
# pip install databricks-bundles==0.275.0
#
# copy contents into resources/test_job.py
from databricks.bundles.jobs import Job
from globals.global_variables import env 


test_job = Job.from_dict(
    {
        "name": "test_job",
        "tasks": [
            {
                "task_key": "tsk1",
                "notebook_task": {
                    "notebook_path": "performance/pg.ipynb",
                    "base_parameters": {
                        "env": env,
                    },
                },
                "job_cluster_key": "Job_cluster",
            },
        ],
        "job_clusters": [
            {
                "job_cluster_key": "Job_cluster",
                "new_cluster": {
                    "spark_version": "17.3.x-scala2.13",
                    "node_type_id": "Standard_DS3_v2",
                    "kind": "CLASSIC_PREVIEW"
                    "data_security_mode": "DATA_SECURITY_MODE_DEDICATED",
                    "runtime_engine": "STANDARD",
                    "is_single_node": True,
                },
            },
        ],
        "queue": {
            "enabled": True,
        },
    }
)
