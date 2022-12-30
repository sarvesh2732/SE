class mobileNumberValidater:

    def validateMobileNumber(self,number):

        if len(str(number))==12:
            number = str(number)[2:]
            return int(number)

        elif len(str(number))==11:
            number = str(number)[1:]
            return int(number)

        elif len(str(number))==10:
            return number

        else:
            print("Entered number is invalid")
            return 0






