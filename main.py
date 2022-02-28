import os
from lib import test
from lib import test2


def main():
    print("Hello World! PDM 3")
    print("$FOO is", os.environ["FOO"])
    test.foo()
    test2.foo_enhanced()


if __name__ == "__main__":
    main()
