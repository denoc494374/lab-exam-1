def check_network(mobile_number):
    key_digits = mobile_number[2:4]

    networks = {
        'SMART': ['13', '14', '20', '21', '28', '29', '30'],
        'TNT': ['09', '10', '11', '12', '18', '19'],
        'SUN': ['22', '23', '32', '33'],
        'GLOBE': ['15', '16', '17', '25', '26', '27', '56'],
        'RED': ['01', '02', '24'],
        'DITO': ['91', '92', '93', '94', '95', '96', '97', '98']
    }

    for network, prefixes in networks.items():
        if key_digits in prefixes:
            return network

    return "Unknown Network"


def main():
    mobile_number = input("Enter a mobile number: ").strip()

    if len(mobile_number) == 11 and mobile_number[0:2] == "09":
        network = check_network(mobile_number)
        print(f"The network of the mobile number is {network}")
    else:
        print("INVALID!!! Please enter a valid number. and please put space between 4th and 5th number and in between 7th and 8th number.")


main()
