import sys
import argparse
import math

args = sys.argv
n = len(args)
# Calculates annuity and differential payment using if elif and else
if len(args) != 5:
    print("Incorrect parameters.")
else:
    parser = argparse.ArgumentParser()  # parsing arguments
    parser.add_argument("--type", action="store",
                        type=str, help="Enter a string")
    parser.add_argument("--payment", action="store", type=float,
                        help="Enter a positive value", default=0, nargs='?')
    parser.add_argument("--principal", action="store", type=float,
                        help="Enter a positive value", default=0, nargs='?')
    parser.add_argument("--periods", action="store",
                        type=int, help="Enter a positive value", default=0, nargs='?')
    parser.add_argument("--interest", action="store",
                        type=float, help="Enter a positive value", default=0, nargs='?')
    args = parser.parse_args()
    if args.type == "annuity" and args.payment > 0 and args.periods > 0 and args.interest > 0:
        annuity = args.payment
        total_periods = args.periods
        credit_interest = args.interest
        interest_rate = (credit_interest / 12) / 100
        quoitent = interest_rate * math.pow(1 + interest_rate, total_periods)
        remainder = math.pow(1 + interest_rate, total_periods) - 1
        credit_principal = math.floor(annuity / (quoitent / remainder))
        overpayment = round(annuity * total_periods - credit_principal)
        print(f'Your credit principal = {credit_principal}!')
        print(f'Overpayment = {overpayment}')
    elif args.type == "annuity" and args.principal > 0 and args.periods > 0 and args.interest > 0:
        credit_principal = args.principal
        total_periods = args.periods
        credit_interest = args.interest
        interest_rate = (credit_interest / 12) / 100
        quoitent = interest_rate * math.pow(1 + interest_rate, total_periods)
        remainder = math.pow(1 + interest_rate, total_periods) - 1
        annuity = math.ceil(credit_principal * (quoitent / remainder))
        overpayment = round(annuity * total_periods - credit_principal)
        print(f'Your annuity payment = {annuity}!')
        print(f'Overpayment = {overpayment}')
    elif args.type == "annuity" and args.principal > 0 and args.payment > 0 and args.interest > 0:
        credit_principal = args.principal
        monthly_payment = args.payment
        credit_interest = args.interest
        interest_rate = credit_interest / (12 * 100)
        n_periods = math.ceil(math.log((monthly_payment / (monthly_payment - interest_rate * credit_principal)),
                                       1 + interest_rate))
        total_years = round(n_periods // 12)
        total_months = n_periods % 12
        overpayment = round(monthly_payment * (total_years * 12 + total_months) - credit_principal)
        if total_years == 0 and total_months == 1:
            print(f'You need {total_months} month to repay this credit!')
            print(overpayment)
        elif total_years == 0 and total_months < 12:
            print(f'You need {total_months} months to repay this credit!')
            print(overpayment)
        elif total_years == 1 and total_months == 0:
            print(f'You need {total_years} year to repay this credit!')
            print(overpayment)
        elif total_years > 1 and total_months == 0:
            print(f'You need {total_years} years to repay this credit!')
            print(overpayment)
        elif total_years == 1 and total_months == 1:
            print(f'You need {total_years} year and {total_months} month to repay this credit!')
            print(overpayment)
        else:
            print(f'You need {total_years} years and {total_months} months to repay this credit!')
            print(overpayment)
    elif args.type == "diff" and args.principal > 0 and args.periods > 0 and args.interest > 0:
        principal = args.principal
        n = args.periods
        interest = args.interest
        i = interest / (12 * 100)
        overpayment = 0
        for x in range(1, n+1):
            differential = math.ceil((principal / n) + i * (principal - (principal * (x - 1)) / n))
            print(f'Month {x}: paid out {differential}')
            overpayment += differential
        print()
        overpayment = round(overpayment - principal)
        print(f'Overpayment = {overpayment}')
    else:
        print("Incorrect parameters.")
