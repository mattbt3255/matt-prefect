from prefect import flow
from prefect_dbt.cli.commands import DbtCoreOperation

@flow
def trigger_dbt_flow() -> str:
    result = DbtCoreOperation(
        commands=["dbt run --models +marts.core"],
        project_dir="/Users/matt.brown/Documents/matt-dbt",
        profiles_path="/Users/matt.brown/.dbt/profiles.yml"
    ).run()
    return result

if __name__ == "__main__":
    trigger_dbt_flow.serve(
        name="dbt-deployment",
        cron="0 0 * * *",
        tags=["testing", "tutorial"],
        description="Runs the training dbt project.",
    )
