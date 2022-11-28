"""
    This a way for check input and output type variables.
"""


def myfunction(myparamter: int):
    print(myparamter)


def myfunction2(myparamter: int) -> str:
    return f"{myparamter + 10}"


# def dosth(param: list[int]):
#     return


myfunction(10)
print(myfunction2(10))
# myfunction('Hello World!') -> mypy error
