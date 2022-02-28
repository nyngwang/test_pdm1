import os
from lib import test


def main():
    print("Hello World! PDM 3")
    print("$FOO is", os.environ["FOO"])
    test.foo()


if __name__ == "__main__":
    main()
