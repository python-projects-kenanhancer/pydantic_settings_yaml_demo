from settings import Environment, Settings


def test_settings(environment: Environment = None):
    settings = Settings.with_environment(environment=environment)

    print(f"project_env: {settings.project_env.value}")

    print(f"meta_database: {settings.meta_database.model_dump_json()}")

    print(f"airflow_core: {settings.airflow_core.model_dump_json()}")

    print(f"airflow_init: {settings.airflow_init.model_dump_json()}")

    print(f"backend_db: {settings.backend_db.model_dump_json()}")

    print(f"settings: {settings.model_dump_json()}")


def main():
    test_settings()


if __name__ == "__main__":
    main()
