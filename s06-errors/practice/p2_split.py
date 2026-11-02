def split_bill(total, people):
    try:
        share = total / people
    except ZeroDivisionError:
        print("Nobody to split with!")
        return None
    else:
        return round(share, 2)
    finally:
        print("Done splitting.")


print(split_bill(90, 4))
print(split_bill(90, 0))
