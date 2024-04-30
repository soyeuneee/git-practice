#############################
# 앱 시작 페이지
#############################
import names


def run():
    for name in names.__dict__:
        print(name.hi)


if __name__ == "__main__":
    run()
