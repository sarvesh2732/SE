import random
import traceback
import re
import pywhatkit as pwt
import json


def otp_genrator():
        random_number = random.randrange(1,1000)
        OTP = 1000 + random_number
        return OTP

if __name__ == "__main__":
    fd = None
    try:
        fd = open("Customer.csv","a")
    except Exception as ex:
        print(traceback.format_exc())
    finally:
        print("enter the number")
        number = int(input())
        if re.finditer("\d{10}",str(number)):
            list_l = []
            OTP = otp_genrator()
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





