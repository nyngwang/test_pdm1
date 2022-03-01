from lib import test_env
from lib import test_lib


def main():
    test_env.from_toml()
    for i in range(1, 10):
        print(test_lib.emulated_switch(i))


if __name__ == "__main__":
    main()
