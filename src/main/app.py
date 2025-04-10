#############################
# 앱 시작 페이지
#############################
import names


def run():
    for index, _name in enumerate(filter(lambda x: '_' not in x, dir(names))):
        name = names.__getattribute__(_name)
        print(index, "|", _name, ":", name.hi)


if __name__ == "__main__":
    run()
