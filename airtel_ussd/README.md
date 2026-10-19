# Airtel Uganda USSD Simulator - *100#

This beginner Python script simulates the Airtel Uganda *100# USSD Menus and process of accessing their services and more.
It's a learning project to practice nested if/elif logic, input validation, menu navigation.

## Does this...
Simulates the real Airtel Uganda flow:
- Main Menu(Pakalast, Voice/SMS, Data/Devices etc...)
- Sub Menus(PaymentMethod, PIN, SUCCESS Messages)

## Features
- Main Menu with 0 to 10 options
- Multi-level sub-menus using `sub_1`, `sub_2`, `sub_3`, `sub_4` etc.
- Payment options: AirtelMoney, Airtime(Onetime), Airtime(Autorenewal)
- PIN Validation:
    - Strictly 4 digits (just like in real life)
    - All must be numbers (checks with `len(pin)`, `isdigit()`)
    - Checks against saved PIN(`1234`)
    - Home Navigation (`*`Back, `#`Home)

## Why this way?
I'm in my beginner era (Mon Oct 19, 2026) haven't seen functions yet and i want to understand flow.

## How to run...
1. Clone/Download the file
2. Run in the Terminal: -> bash python airtel_ussd.py

## Concepts and Python Stuff it utilizes
## What i've learnt?