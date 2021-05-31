#!/usr/bin/env python3

# Created by Brian Musembi
# Created on May 2021
# This program formats a user inputted address to mailing address specs


def mailing(name, srt_num, srt_name, city, province, post_code,
            apt_num=None):
    # This function formats a mailing address

    # process
    mail_address = name
    if apt_num is not None:
        mail_address = (mail_address + "\n" + apt_num + "-" + srt_num + " " +
                        srt_name + "\n" + city + " " + province + "  " +
                        post_code)
    else:
        mail_address = (mail_address + "\n" + srt_num + " " + srt_name +
                        "\n" + city + " " + province + "  " + post_code)

    return mail_address


def main():
    # this function receives input
    print("This program formats your address to a mailing address.")

    # apartment check
    apt_num = None

    # input
    name = input("Please enter your full name: ")
    question = input("Do you live in an apartment? (Y/N): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_num = input("Please enter your apartment number: ")
    srt_num = input("Please enter your street number: ")
    srt_name = input("Please enter your street name: ")
    city = input("Please enter your city: ")
    province = input("Please enter your province (as an abbreviation, eg:"
                     " ON, BC etc...): ")
    post_code = input("Please enter your postal code (eg: A1B C2D): ")
    print("")

    # call functions
    if apt_num is not None:
        address = mailing(name.upper(), srt_num.upper(),
                          srt_name.upper(), city.upper(),
                          province.upper(), post_code.upper(),
                          apt_num.upper())
    else:
        address = mailing(name.upper(), srt_num.upper(),
                          srt_name.upper(), city.upper(),
                          province.upper(), post_code.upper())

    # output
    print(address)


if __name__ == "__main__":
    main()
