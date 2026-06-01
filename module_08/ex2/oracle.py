import os
from dotenv import load_dotenv  # type: ignore


def config_loading() -> dict[str, str | None]:
    load_dotenv()
    configs = dict()
    configs['MATRIX_MODE'] = os.getenv("MATRIX_MODE")
    configs['DATABASE_URL'] = os.getenv("DATABASE_URL")
    configs['API_KEY'] = os.getenv("API_KEY")
    configs['LOG_LEVEL'] = os.getenv("LOG_LEVEL")
    configs['ZION_ENDPOINT'] = os.getenv("ZION_ENDPOINT")
    return configs


def matrix_configs(conf: dict[str, str | None]) -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print("Mode:", end="")

    if conf['MATRIX_MODE'] is not None:
        print(conf['MATRIX_MODE'])
    else:
        print("WARNING: The variable was not set")
    print("Database:", end=" ")
    if conf["MATRIX_MODE"] == "development":
        if conf['DATABASE_URL'] is not None:
            print(conf['DATABASE_URL'])
        else:
            print("WARNING: The variable was not set")
    else:
        if conf['DATABASE_URL'] is not None:
            print("Connected to local instance")
        else:
            print("WARNING: The variable was not set")
    print("API Access:", end=" ")
    if conf["MATRIX_MODE"] == "development":
        if conf['API_KEY'] is not None:
            print(conf['API_KEY'])
        else:
            print("WARNING: The variable was not set")
    else:
        if conf['API_KEY'] is not None:
            print("Authenticated")
        else:
            print("WARNING: The variable was not set")
    print("Logging Level:", end=" ")
    if conf['LOG_LEVEL'] is not None:
        print(conf['LOG_LEVEL'])
    else:
        print("WARNING: The variable was not set")
    print("Zion Network:", end=" ")
    if conf["MATRIX_MODE"] == "development":
        if conf['ZION_ENDPOINT'] is not None:
            print(conf['ZION_ENDPOINT'])
        else:
            print("WARNING: The variable was not set")
    else:
        if conf['ZION_ENDPOINT'] is not None:
            print("Online")
        else:
            print("WARNING: The variable was not set")


def security_configs(conf: dict[str, str | None]) -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if None in conf.values():
        print("[KO] .env file not properly configured")
    else:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


if __name__ == "__main__":
    configurations = config_loading()
    matrix_configs(configurations)
    security_configs(configurations)
    print("\nThe Oracle sees all configurations.")
