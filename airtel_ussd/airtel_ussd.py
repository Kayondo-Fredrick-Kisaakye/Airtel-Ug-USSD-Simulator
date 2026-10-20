import sys

print("=================================================")
print("\tWELCOME TO AIRTEL UGANDA USSD")
print("Subsscribe to our services | Pay bills and more")
print("=================================================")
print("\n\t\tDail *100# to start")

user_info = {
    "first_name": "Musinguzi",
    "second_name": "Vicent",
    "saved_pin": "1234",
    "airtel_money_acc": {
        "total_balance": 50000,
        "beerako_debt": 200,
    },
    "airtime_acc": {
        "total_balance": 3000,
    },
}

saved_pin = user_info["saved_pin"]
thank_part = "Thank you for subscribing to Airtel services"
invalid_input_msg = "Woops! Invalid Input"


start_code = input("Enter Code: ")

if start_code == "*100#":
    # MAIN MENU
    print(
        "Welcome Home\n"
        "0. MyPakalast/FreakyWknd\n"
        "1. Voice/SMS\n"
        "2. Data/Devices\n"
        "3. Combos(Voice+Data)\n"
        "4. Buy 4 Other\n"
        "5. Roaming/INTL Calls\n"
        "6. SmartPlan\n"
        "7. Broadband\n"
        "8. PostPaid\n"
        "9. AirtelMoney\n"
        "10. Self Help\n"
    )

if start_code != "*100#":
    print("Invalid Input (USE *100#)")
    sys.exit()

choice = input("Enter Choice: ")
##################################
# start of MY PAKALAST/FREAKYWKND
##################################
if choice == "0":
    print(
        "MY PAKALAST/FREAKYWKND\n"
        "1. Voice MyPakalast\n"
        "2. Data MyPakalast\n"
        "3. Freaky Weekend\n"
        "4. Mega 4 Dayz\n"
        "5. Night Bundles\n"
        "6. Masaza Bundles\n"
        "*. Back\n"
        "#. Home\n"
    )
    sub_1 = input("SELECT: ")
    ##################################
    # start of VOICE MYPAKALAST/FREAKYWKND
    ##################################
    if sub_1 == "1":
        print(
            "VOICE MY PAKALAST/FREAKYWKND\n"
            "1. 1,000/- 60Mins + 5Mbs + 5SMS\n"
            "2. 1,000/- 25Mins(All Networks)\n"
        )
        sub_2 = input("SELECT: \n")
        if sub_2 == "1":  # 1. 1,000/- 60Mins + 5Mbs + 5SMS
            print("PAYMENT METHOD\n1. AirtelMoney\n2. Airtime\n")
            sub_3 = input("SELECT: \n")
            if sub_3 == "1":  # 1. AIRTEL MONEY
                print("AIRTEL MONEY\n")
                pin = input("ENTER PIN: ")

                # 1. WE CHECK THE LENGTH OF PIN FIRST
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN! Must be 4 digits.")
                    sys.exit()

                # 2. CHECK THE SAVED PIN FROM DICT user_ifno
                elif pin != user_info["saved_pin"]:
                    print("Wrong PIN! Try again.")
                    sys.exit()

                # 3. CHECK THE BALANCE
                else:
                    price = 1000
                    balance = user_info["airtel_money_acc"]["total_balance"]

                    if balance < price:
                        print(
                            f"Dear {user_info['first_name']} {user_info['second_name']}, you have insufficient funds. Your balance is {balance}/-"
                        )
                    else:
                        # WE DEDUCT AND SHOW SUCCESS MESSAGE
                        user_info["airtel_money_acc"]["total_balace"] = balance - price
                        print(
                            f"SUCCESS! {thank_part}, {price}/- has been deducted and you've subscribed to 1,000/- 60Mins + 5Mbs + 5SMS"
                        )
                        print(
                            f"New Airtel Money Balance: {user_info['airtel_money_acc']['total_balance']}/-"
                        )

            elif sub_3 == "2":  # 2. AIRTIME
                price = 1000
                airtime_balance = user_info["airtime_acc"]["total_balance"]

                if airtime_balance < price:
                    print(f"Your airtime balance is {airtime_balance}/- and is low.")
                else:
                    user_info["airtime_acc"]["total_balance"] = airtime_balance - price
                    print(
                        f"SUCCESS! {thank_part} {price}/- has been deducted and you've subscribed to 1,000/- 60Mins + 5Mbs + 5SMS"
                    )
                    print(
                        f"New Airtime balance: {user_info['airtime_acc']['total_balance']}/-"
                    )

        elif sub_2 == "2":  # 2. 1,000/- 25Mins(All Networks
            print("PAYMENT METHOD\n1. AirtelMoney\n2. Airtime\n")
            sub_4 = input("SELECT: ")
            if sub_4 == "1":
                print("AIRTEL MONEY\n")
                pin = input("ENTER PIN: ")

                # WE CHECK THE LENGTH OF PIN FIRST
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN! Must be 4 digits.")
                    sys.exit()
                else:
                    print(f"SUCCESS! {thank_part}, You have subscribed!")

            elif sub_4 == "2":
                print(f"SUCCESS! {thank_part}, You have subscribed!")

        ##################################
        # start of DATA MYPAKALAST
        ##################################
    elif sub_1 == "2":
        print(
            "DATA MY PAKALAST\n"
            "1. 1,000/- 300Mb\n"
            "2. 2,000/- 1Gb(2 Days)\n"
            "3. 5,000/- 2.6Gb(3 Days)\n"
        )
        sub_1 = input("SELECT: ")
        if sub_1 == "1":
            print(
                "PAYMENT METHOD\n"
                "1. AirtelMoney\n"
                "2. Airtime-Onetime\n"
                "3. Airtime-Autorenewal\n"
            )
            sub_2 = input("SELECT: ")
            if sub_2 == "1":
                print("AIRTEL MONEY\n")
                pin = input("ENTER PIN: ")
                # WE CHECK THE LENTH OF THE PIN FIRST
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN! Must be 4 digits.")
                    sys.exit()
                else:
                    print(f"SUCCESS! {thank_part}, You have subscribed!")
            elif sub_2 == "2":
                print("AIRTIME-ONETIME\n")
                print(f"SUCCESS! {thank_part}, You have subscribed!")
            elif sub_2 == "3":
                print("AIRTIME-AUTORENEWAL\n")
                print(
                    f"SUCCESS, {thank_part}, You have subscribed and we shall autorenew once done or expired."
                )
        elif sub_1 == "2" or sub_1 == "3":
            print(
                "PAYMENT METHOD\n"
                "1. AirtelMoney\n"
                "2. Airtime-Onetime\n"
                "3. Airtime-Autorenewal\n"
            )
            sub_2 = input("SELECT: ")
            if sub_2 == "1":
                print("AIRTEL MONEY\n")
                pin = input("ENTER PIN: ")
                # WE CHECK THE LENTH OF PIN FIRST AGAIN
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN! Must be 4 digits.")
                    sys.exit()
                else:
                    print(f"SUCCESS! {thank_part}, You have subscribed!")
            elif sub_2 == "2":
                print("AIRTIME-ONETIME\n")
                print(f"SUCCESS! {thank_part}, You have subscribed.")
            elif sub_2 == "3":
                print("AIRTIME-AUTORENEWAL\n")
                print(
                    f"SUCCESS, {thank_part}, You have subscribed and we shall autorenew once done or expired."
                )
        elif sub_1 == "3":
            print(
                "PAYMENT METHOD\n"
                "1. AirtelMoney\n"
                "2. Airtime-Onetime\n"
                "3. Airtime-Autorenewal\n"
            )
            sub_2 = input("SELECT: ")
            if sub_2 == "1":
                print("AIRTEL MONEY\n")
                pin = input("ENTER PIN: ")
                # CHECK THE PIN LENTH
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN! Must be 4 digits.")
                    sys.exit()
                else:
                    print(f"SUCCESS! {thank_part}, You have subscribed.")
            elif sub_2 == "2":
                print("AIRTIME-ONETIME\n")
                print(f"SUCCESS! {thank_part}, You have subscribed!")
            elif sub_2 == "3":
                print("AIRTIME AUTO-RENEWAL\n")
                print(
                    f"SUCCESS, {thank_part}, You have subscribed and we shall autorenew once done or expired."
                )

        # #################################
        # start of FREAKY WEEKEND
        # ##################################
    elif sub_1 == "3":
        print("FREAKY WEEKEND")

        # #################################
        # start of MEGA 4 DAYZ
        # ##################################
    elif sub_1 == "4":
        print(
            "MEGA 4 DAYZ\n"
            "1. 7,000/- 5Gb + 20Mins(Thur 6AM)\n"
            "2. 10,000/- 8Gb + 20Mins(Thur 6AM\n)"
        )
        sub_1 = input("SELECT: ")
        if sub_1 == "1":
            print("CHOOSE PAYMENT METHOD\n1. Airtel Money\n2. Airtime\n")
            sub_2 = input("SELECT: ")
            if sub_2 == "1":
                print("AIRTEL MONEY\n")
                pin = input("ENTER PIN: ")
                # CHECK PIN LENGTH
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN! Must be 4 digits.")
                    sys.exit()
                else:
                    print(f"SUCCESS! {thank_part}, You have subscribed!")
            elif sub_2 == "2":
                print("AIRTIME\n")
                print(f"SUCCESS! {thank_part}, You have subscribed")
        elif sub_1 == "2":
            print("CHOOSE PAYMENT METHOD\n1. Airtel Money\n2. Airtime\n")
            sub_2 = input("SELECT: ")
            if sub_2 == "1":
                print("AIRTEL MONEY\n")
                pin = input("ENTER PIN:")
                # CHECK PIN LENGTH
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN! Must be 4 digits.")
                    sys.exit()
                else:
                    print(f"SUCCESS! {thank_part}, You have subscribed.")
            elif sub_2 == "2":
                print("AIRTIME\n")
                print(f"SUCCESS! {thank_part}, You have subscribed.")

        # #################################
        # start of NIGHT BUNDLES
        # ##################################
    elif sub_1 == "5":
        print("NIGHT BUNDELES")

        # ##################################
        # start of MASAZA BUNDLES
        # ##################################
    elif sub_1 == "6":
        print(
            "MASAZA BUNDLES\n"
            "1. 15k 3Gb + 150Mins(Airtel) 50Min(All) 50SMS\n"
            "2. 30k 10Gb + 400Mins(Airtel) 100Min(All) 100SMS\n"
            "3. 50k 20Gb + 800Mins(Airtel) 200Min(All 100SMS\n"
            "*. Back\n"
            "#. Home\n)"
        )  # rememer to add * and #
        sub_1 = input("SELECT: ")
        if sub_1 == "1":
            print(
                "CHOOSE PAYMENT METHOD\n"
                "1. Airtel Money\n"
                "2. Airtime\n"
                "3. Beerako\n"
                "*. Back\n"
                "#. Home\n"
            )  # rememer to add * and #
            sub_2 = input("SELECT: ")
            if sub_2 == "1":
                print("AIRTEL MONEY\n")
                pin = input("ENTER PIN: ")
                # pin lenth
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN! Must be 4 digits.")
                else:
                    print(f"SUCCESS! {thank_part}, You have subscribed.")
            elif sub_2 == "2":
                print("AIRTIME\n")
                print(f"SUCCESS, {thank_part}, You have subscribed.")
            elif sub_2 == "3":
                print("BEERAKO\nStandby as we check your account details...")
        elif sub_1 == "2":
            print(
                "CHOOSE PAYMENT METHOD\n"
                "1. Airtel Money\n"
                "2. Airtime\n"
                "3. Beerako\n"
                "*. Back\n"
                "#. Home\n"
            )  # rememer to add * and #
            sub_2 = input("SELECT: ")
            if sub_2 == "1":
                print("AIRTEL MONEY\n")
                pin = input("ENTER PIN: ")
                # pin length
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN! Must be 4 digits")
                else:
                    print(f"SUCCESS, {thank_part}, You have subscribed.")
            elif sub_2 == "2":
                print("AIRTIME\n")
                print(f"SUCCESS! {thank_part}, You have subscribed.")
            elif sub_2 == "3":
                print("BEERAKO\nStandby as we chech your account details...")
    # #################################
    #  start of VOICE/SMS
    # #################################
elif choice == "1":
    print(
        "VOICE/SMS\n"
        "1. Call Airtel\n"
        "2. Call All Networks\n"
        "3. SMS Bundles\n"
        "4. Buy Airtime\n"
        "5. Me2U(Share Airtime\n"
        "6. Check Balance\n"
        "7. Beerako\n"
        "*. Back\n"
        "#. Home\n"
    )  # rememer to add * and #
    sub_1 = input("SELECT:")
    if sub_1 == "1":
        # #################################
        # start of CALL AIRTEL
        # #################################
        print(
            "CALL AIRTEL\n"
            "1. Daily\n"
            "2. Weekly\n"
            "3. Monthly\n"
            "4. No Expiry\n"
            "5. Night Bundle\n"
            "*. Back\n"
            "#. Home\n"
        )  # dont forget to add * and #
        sub_2 = input("SELECT: ")
        if sub_2 == "1":
            # ###############################
            # start of DAILY 24HRS
            # ###############################
            print(
                "DAILY 24Hrs\n"
                "1. 2,0000/- 140Mins\n"
                "2. 1,000/- 70Mins + 5Mb + 5SMS\n"
                "3. 550/- 20Mins + 5Mb + 5SMS\n"
                "4. 2,000/- 70Mins(All Networks)\n"
                "5. 1,000/- 25Mins(All Networks)\n"
                "n. Next\n"
                "*. Back\n"
                "#. Home\n"
            )
            sub_3 = input("SELECT: ")
            if sub_3 in ("1", "2", "3", "4", "5"):
                print(
                    "CHOOSE PAYMENT METHOD\n"
                    "1. Airtel Money\n"
                    "2. Airtime\n"
                    "3. Beerako\n"
                    "*. Back\n"
                    "#. Home"
                )
                sub_4 = input("SELECT: ")
                if sub_4 == "1":
                    print("AIRTEL MONEY\n")
                    pin = input("ENTER PIN: ")
                    # PIN LENGTH
                    if len(pin) != 4 or pin.isdigit():
                        print("Invalid PIN! Must be 4 digits.")
                    else:
                        print(f"SUCCESS! {thank_part}, You have subscribed.")
                elif sub_4 == "2":
                    print("AIRTIME\n")
                    print(f"SUCCESS! {thank_part}, You have subscibed.")
                elif sub_4 == "3":
                    print("BEERAKO\n")
                    print("Standby as we check your account details...")

            # ###############
            # start of WEEKLY
            # ###############
        elif sub_2 == "2":
            print(
                "WEEKLY BUNDLES\n"
                "1. 2,000/- 80Mins\n"
                "2. 3,500/- 275Mins\n"
                "3. 5,000/- 450Mins\n"
                "4. 10,000/- 1000Mins\n"
                "5. 5,000/- 180Mins(All Networks)\n"
                "6. 2,500/- 40Mins(All Networks)\n"
                "n. Next"
                "*. Back"
            )
            sub_3 = input("SELECT: ")
            if sub_3 in ("1", "2", "3", "4", "5", "6"):
                print(
                    "CHOOSE PAYMENT METHOD\n"
                    "1. Airtel Money\n"
                    "2. Airtime\n"
                    "3. Beerako\n"
                    "*. Back\n"
                    "#. Home\n"
                )

            # ################
            # start of MONTHLY
            # ################
        elif sub_2 == "3":
            print(
                "MONTHLY\n"
                "1. 30,000/- 2000Mins\n"
                "2. 25,000/- 2500Mins\n"
                "3. 20,000/- 1300Mins\n"
                "4. 15,000/- 14000Mins\n"
                "5. 10,000/- 850Mins\n"
                "6. 5,000/- 125Mins\n"
                "n. Next\n"
                "*. Back\n"
            )
            sub_3 = input("SELECT: ")
            if sub_3 in ("1", "2", "3"):
                print(
                    "CHOOSE PAYMENT METHOD\n"
                    "1. Airtel Money\n"
                    "2. Airtime\n"
                    "3. Beerako\n"
                    "*. Back\n"
                    "#. Home\n"
                )
            elif sub_3 in ("4", "5", "6"):
                print(
                    "CHOOSE PAYMENT METHOD\n"
                    "1. Airtel Money\n"
                    "2. Airtime\n"
                    "3. Beerako\n"
                    "*. Back\n"
                    "#. Home\n"
                )
                print(
                    "CHOOSE PAYMENT METHOD\n"
                    "1. Airtel Money\n"
                    "2. Airtime\n"
                    "3. Beerako\n"
                    "*. Back\n"
                    "#. Home\n"
                )

            # ##################
            # start of NO EXPIRY
            # ##################
        elif sub_2 == "4":
            print(
                "NO EXPIRY(CHILLAX)\n"
                "1. 75,000/- 50000Mins\n"
                "2. 50,000/- 3000Mins\n"
                "3. 30,000/- 13000Mins(All Networks)\n"
                "4. 10,000/- 200Mins(All Networks)\n"
                "5. 5000/- 90Mins(All Networks)\n"
                "n. Next\n"
                "*. Back\n"
            )
            sub_3 = input("SELECT: ")
            if sub_3 in ("1", "2", "3", "4", "5"):
                print(
                    "CHOOSE PAYMENT METHOD\n"
                    "1. Airtel Money\n"
                    "2. Airtime\n"
                    "3. Beerako\n"
                    "*. Back\n"
                    "#. Home\n"
                )
                print(
                    "CHOOSE PAYMENT METHOD\n"
                    "1. Airtel Money\n"
                    "2. Airtime\n"
                    "3. Beerako\n"
                    "*. Back\n"
                    "#. Home\n"
                )
                print(
                    "CHOOSE PAYMENT METHOD\n"
                    "1. Airtel Money\n"
                    "2. Airtime\n"
                    "3. Beerako\n"
                    "*. Back\n"
                    "#. Home\n"
                )

            # #####################
            # start of NIGHT BUNDLE
            # #####################
        elif sub_2 == "5":
            print(
                "NIGHT BUNDLE Valid(11PM to 7AM)\n"
                "1. 30Mins @300(11PM to 7AM)\n"
                "*. Back\n"
                "#. Home\n"
            )
            sub_3 = input("SELECT: ")
            if sub_3 == "1":
                print("CHOOSE PAYMENT METHOD\n")

    elif sub_1 == "2":
        # #################################
        # start of CALL ALL NETWORKS/BOONA
        # #################################
        print(
            "CALL ALL NETWORKS (Call Boona)\n"
            "1. Daily\n"
            "2. Weekly\n"
            "3. Monthly\n"
            "No Expiry\n"
            "*. Back\n"
            "#. Home\n"
        )
    elif sub_1 == "3":
        # #################################
        # start of SMS BUNDLES
        # #################################
        print(
            "SMS BUNDLES\n"
            "0. Special Offers\n"
            "1. Airtel\n"
            "2. All Networks\n"
            "*. Back\n"
            "#. Home\n"
        )
    elif sub_1 == "4":
        # #################################
        # start of BUY AIRTIME
        # #################################
        print(
            "BUY AIRTIME\n"
            "1. For Myself\n"
            "2. For Another Airtel Number"
            "0. Back\n"
            "00. Main Menu\n"
        )
    elif sub_1 == "5":
        # #################################
        # start of ME2U(SHARE AIRTIME)
        # #################################
        print("ME2U(Share Airtime)\n*. Back\n#. Home\n")
        me2u_ammount = input("ENTER AMOUNT: ")
    elif sub_1 == "6":
        # #################################
        # start of BEERAKO
        # #################################
        print("BEERAKO\n")

    # #########################
    # start of DATA/DEVICES
    # #########################
elif choice == "2":  # DATA/DEVICES
    print(
        "DATA/DEVICES\n"
        "1. Daily\n"
        "2. Weekly\n"
        "3. Monthly\n"
        "4. No Expiry(Chillax\n"
        "5. Check Data Volume\n"
        "6. Share Data\n"
        "7. Beerako\n"
        "8. Device Offers\n"
        "9. TV/Music\n"
        "10. Learn From Home\n"
        "*. Back\n"
        "#. Home\n"
    )  # rememer to add * and # logicVC

elif choice == "3":
    print(
        "COMBOS(VOICE + DATA)\n"
        "1. 7,500/- 2Gb + 75Mins(Airtel) + 75SMS - 7Days\n"
        "2. 10,000/- 3Gb + 100Mins(Airtel) + 100SMS - 7Days\n"
        "3. 15,000/- 3Gb + 150Mins(Airtel) + 50Mins(All Networks) (30Days)\n"
        "n. Next\n"
        "*. Back\n"
        "#. Home\n"
    )

elif choice == "4":
    print(
        "BUY 4 OTHER\n"
        "1. Voice & SMS\n"
        "2. Data Bundles\n"
        "3. Combos\n"
        "4. Roaming/INTL Calls\n"
        "5. SmartPlan\n"
        "6. Freaky Weekend\n"
        "7. Mega 4 Dayz\n"
        "8. Save your number\n"
        "9. Night Bundles\n"
        "*. Back\n"
        "#. Home\n"
    )

elif choice == "5":
    print(
        "ROAMING/INTL CALLS\n"
        "1. Roaming Outside Uganda\n"
        "2. Call International from Uganda\n"
        "*. Back\n"
        "#. Home\n"
    )

elif choice == "6":
    print(
        "SMERT PLAN\n"
        "1. Activate/Buy Plan\n"
        "2. Check Balance\n"
        "3. Deactivate\n"
        "4. Buy For Other\n"
    )

elif choice == "7":
    print(
        "BROADBAND\n"
        "1. SmartConnect WIFI (5G Unlimited Internet\n"
        "2. MIFI/Router Bundles\n"
        "3. Fiber\n"
        "4. Get Connected\n"
        "5. Check Volume\n"
        "6. Check Validity\n"
        "*. Back\n"
        "#. Home\n"
    )

elif choice == "8":
    print(
        "POSTPAID\n"
        "1. Combo (Data + Mins + SMS)\n"
        "2. Voice/SMS\n"
        "3. Data\n"
        "4. ROAMING/INTL Calls\n"
    )

elif choice == "9":
    print(
        "AIRTELMONEY\n"
        "1. Send Money\n"
        "2. Airtime/Bundles\n"
        "3. Withdraw Cash\n"
        "4. Pay Bill\n"
        "5. Payments\n"
        "6. School Fees\n"
        "7. Financial Services\n"
        "8. Loans\n"
        "9. Pay Merchant\n"
        "10. Self Help\n"
    )

elif choice == "10":
    print(
        "SELF HELP\n"
        "1. My Balance\n"
        "2. PUK\n"
        "3. My Number\n"
        "4. Beerako\n"
        "5. Block Stolen Sim/Number\n"
        "6. Me2U(Share Airtime)\n"
        "7. Enable DND\n"
        "8. Call Me back\n"
        "9. Auto-Renewal\n"
        "10. Agriculture\n"
        "n. Next\n"
        "*. Back\n"
        "#. Home\n"
    )
    sub_1 = input("SELECT: ")
    if sub_1 == "1":
        print("YOUR BALANCE\n")
        print(
            f"Your account Balance is UGX {user_info['airtime_acc']}, Dail *100# to buy a bundle."
        )
    elif sub_1 == "2":
        print("PUK")
    elif sub_1 == "3":
        print("YOUR NUMBER")
    elif sub_1 == "4":
        print("BEERAKO")
    elif sub_1 == "5":
        print("BLOCK STOLEN")
    elif sub_1 == "6":
        print("ME2U(AIRTIME)")
    elif sub_1 == "7":
        print("ENABLE DND")
    elif sub_1 == "8":
        print("CALL ME BACK")
    elif sub_1 == "9":
        print("AUTO-RENEWAL")
    elif sub_1 == "10":
        print("AGRICULTURE")
