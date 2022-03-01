from lib import test_env, test_lib, test_requests


def main():
    test_env.from_toml()
    test_lib.test_emulated_switch(10)
    print("test **dict: %s" % test_lib.emulated_switch(**{"comp": 3}))
    print("test *dict: %s" % test_lib.emulated_switch(*{"comp": 3}))
    print(test_requests.get_url().status_code)


if __name__ == "__main__":
    main()

