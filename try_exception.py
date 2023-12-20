# width = 0
# length = 40
# print(length / width)
#
# try:
#     # width=0
#     length=40
#     print(length / width)
# # except Exception:
# # except ZeroDivisionError:
# except NameError:
#     print("Division by zero invalid kindly change ur input")





try:
    width=0
    length=0
    length / width

# except Exception:
#     print("A new issue has occured")
except NameError:
    print("Varibale hass been used before definding it")
except ZeroDivisionError:
    print("Division by zero is invalid")
except Exception:
    print("A new issue has occured")

finally:
    print("I will run atleast once")
