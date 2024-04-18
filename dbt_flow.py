from prefect import flow
from prefect_dbt.cli.commands import DbtCoreOperation

@flow
def trigger_dbt_flow() -> str:
    result = DbtCoreOperation(
        commands=["pwd", "dbt debug", "dbt run"],
        project_dir="/Users/matt.brown/Documents/matt-dbt",
        profiles_path="/Users/matt.brown/.dbt/profiles.yml"
    ).run()
    return result

trigger_dbt_flow()
