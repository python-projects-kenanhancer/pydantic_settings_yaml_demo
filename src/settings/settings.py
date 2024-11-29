from pydantic_settings import SettingsConfigDict
from pydantic_settings_yaml import YamlBaseSettings

from settings import (
    AirflowCoreSettings,
    AirflowInitSettings,
    BackendDBSettings,
    CdtToNexumSettings,
    Environment,
    FeatureFlagsSettings,
    MetaDatabaseSettings,
)


class Settings(YamlBaseSettings):
    project_env: Environment

    feature_flags: FeatureFlagsSettings
    meta_database: MetaDatabaseSettings
    backend_db: BackendDBSettings
    airflow_init: AirflowInitSettings
    airflow_core: AirflowCoreSettings
    cdt_to_nexum: CdtToNexumSettings

    @classmethod
    def with_environment(cls, environment: Environment = None):
        yaml_file = "env.yaml"  # Default file
        if environment:
            yaml_file = f"env.{environment.value}.yaml"

        # Dynamically create a subclass with the updated model_config
        class DynamicSettingsV3(cls):
            model_config = SettingsConfigDict(yaml_file=yaml_file, case_sensitive=False, extra="ignore")

        return DynamicSettingsV3()
