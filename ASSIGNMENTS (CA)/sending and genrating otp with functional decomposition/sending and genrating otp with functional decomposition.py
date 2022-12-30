# after code review all library are arranged in alphabetical order.
#after code review we use camel case and verb as the function name.
#after code review program is divided into multiple methods.
#after code review we try to replace the file with dictionary.

import json
import pywhatkit as pwt
import random
import re
import traceback



def genrateOtp():
        random_number = random.randrange(1,1000)
        OTP = 1000 + random_number
        return OTP

def validateMobileNo(number):

    if re.finditer("\d{10}", str(number)):
        return 1
    else:
        return 0

if __name__ == "__main__":
    fd = None
    try:
        fd = open("Customer.csv","a")
    except Exception as ex:
        print(traceback.format_exc())
    finally:
        print("enter the number")
        number = int(input())
        if validateMobileNo(number):
            list_l = []
            OTP = genrateOtp()
            pwt.sendwhatmsg("+91"+str(number),str(OTP),19,53)
            list_l.append([number,OTP])
            list_l = json.dumps(list_l)
            fd.write(list_l)

            print("enter the otp u got")
            n = int(input())
            try:
                fd = open("customer.csv")
                data = fd.read()
            except Exception as ex:
                print(traceback.format_exc())
            finally:
                data = json.loads(data)
                print(data)
                for i in data:
                    if i[0] == number:
                        if i[1] == n:
                            print("U LOGED IN SUCSSESFULLY")
                            break
                        else:
                            print("U ENTERED WRONG OTP")





