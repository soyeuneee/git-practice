#############################
# 앱 시작 페이지
#############################
import names


def run():
    for _name in filter(lambda x: '_' not in x, dir(names)):
        name = names.__getattribute__(_name)
        print(name.hi)


if __name__ == "__main__":
    run()
