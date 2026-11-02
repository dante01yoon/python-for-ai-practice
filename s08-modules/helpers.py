def tip(bill, percent=20):
    return round(bill * percent / 100, 2)

if __name__ == "__main__":
    print(tip(40))
