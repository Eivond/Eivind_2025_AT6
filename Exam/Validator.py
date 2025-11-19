list = []
while True:
    user_inp = input("Input a your number then exit to finish")
    if user_inp.isalpha():
        if user_inp == "exit":
            break
        if user_inp != "exit":
            print("Numbers only")
            continue
    if user_inp.isnumeric():
        list.append(user_inp)

class UserInputValidator:
    def __init__(self, list):
        self._list = list
        self.positive = []

    def validate_positive_integers(self):
        for n in list:
            if int(n) %2 == 0:
                self.positive.append(n)
        return self.positive

result = UserInputValidator(list).validate_positive_integers()
print(result)