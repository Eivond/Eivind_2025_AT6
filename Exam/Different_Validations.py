list = []
list2 = []
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

while True:
    user_inp2 = input("Input a your number then exit to finish")
    if user_inp2.isalpha():
        if user_inp2 == "exit":
            break
        if user_inp2 != "exit":
            print("Numbers only")
            continue
    if user_inp2.isnumeric():
        list2.append(user_inp2)

class UserInputValidator:
    def __init__(self, list):
        self._list = list
        self.positive = []

    def validate_positive_integers(self):
        for n in list:
            if int(n) %2 == 0:
                self.positive.append(n)
        return self.positive
    
    def message(self, result):
        if result:
            return "Validated"
        else:
            raise ValueError("Invalid")
result = UserInputValidator(list).validate_positive_integers()
message = UserInputValidator(list).message(result)
result2 = UserInputValidator(list2).validate_positive_integers()
message2 = UserInputValidator(list2).message(result)
print(message)
print(message2)