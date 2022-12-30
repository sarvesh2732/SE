import datetime
import GenrateOTP
import pywhatkit
import ValidateMobileNo
import validateotp


class otpSender:
    def __init__(self):
        self.dic = {}

    def sendOtp(self):
        obj1 = GenrateOTP.numericOtpGenrater()
        obj2 = ValidateMobileNo.mobileNumberValidater()
        obj3 = validateotp.otpvalidetor()

        number = obj2.validateMobileNumber(int(input()))
        otp = obj1.genrateFourDigitNumericOtp()

        mydate = datetime.datetime.now()


        if number:
            pywhatkit.sendwhatmsg("+91" + str(number),str(otp),mydate.hour,mydate.minute+1)

            dic = self.addTodictionary("+91" + str(number),str(otp))

            print("enter the otp u got ")
            enterdOtp = int(input())
            if obj3.validateotp(dic,"+91" + str(number),enterdOtp):
                return 1
            else:
                return 0
        else:
            self.sendOtp()


    def addTodictionary(self,number,otp):
        self.dic[number]=otp
        print(self.dic)
        return self.dic





