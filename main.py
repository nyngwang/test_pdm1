import os
from lib import test
from lib import test_lib


def testing_toml():
    print("Hello World! PDM 3")
    print("$FOO is", os.environ["FOO"])


def main():
    testing_toml()
    test.foo()
    for i in range(1, 10):
        print(test_lib.emulated_switch(i))


if __name__ == "__main__":
    main()
