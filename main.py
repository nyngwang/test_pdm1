from lib import test_env
from lib import test_lib


def main():
    test_env.from_toml()
    test_lib.test_emulated_switch(10)


if __name__ == "__main__":
    main()
