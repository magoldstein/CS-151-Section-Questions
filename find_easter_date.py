
def find_easter_date(year):
    a = year%19
    b = year%4
    c = year%7
    d = (19*a+24)%30
    e = (2*b + 4*c + 6*d + 5)%7
    if d+e < 10:
        date = 22+d+e
        month = "March "
    else:
        date = d+e-9
        month = "April "
    datestring = str(date)
    easter = month + datestring
    return(easter)

if __name__ == '__main__':
    assert find_easter_date(2020) == "April 12"
    assert find_easter_date(2021) == "April 4"
    assert find_easter_date(2022) == "April 17"
    assert find_easter_date(2023) == "April 9"
    assert find_easter_date(2024) == "March 31"
    assert find_easter_date(2025) == "April 20"