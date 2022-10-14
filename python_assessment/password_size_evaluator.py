# In the function below create a control flow (if statement) that will evaluate a string for its size and output the
# below messages: < 5 in length must return the string "Your password is too short."> 20 in length, the method must
# return "Your password is too long and may be forgotten."in between 5-20 the method must return "Your password is an
# acceptable length."

def eval_pass_len(password):
    if len(password) > 20:
        return "Your password is too long and may be forgotten."
    elif len(password) < 5:
        return "Your password is too short."
    else:
        return "Your password is of an acceptable length"


print(eval_pass_len("TestingPassword"))
