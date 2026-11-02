import logging

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

logging.info("App started")
for amount in [20, -5, 40]:
    if amount < 0:
        logging.warning("Negative amount: %s", amount)
    else:
        logging.info("Deposit: %s", amount)
print("Done. Check app.log")
