import sys


class Money:
    """
    this class should make an object
    with attributes equity, debt, gold
    :param equity, debt, gold:
    """
    # class attributes (pay_rate)
    all = []

    def __init__(self, equity: int, debt: int, gold: int):
        # Run validations to the received args
        assert debt >= 0, f"debt {equity} is not greater than or equal to zero!"
        assert gold >= 0, f"gold {debt} is not greater than or equal to zero!"
        assert gold >= 0, f"gold {gold} is not greater than or equal to zero!"

        # Assign to self object
        self.equity = equity
        self.debt = debt
        self.gold = gold
        # initial rates

        Money.all.append(self)

    def sip(self, sip_equity: float, sip_debt: float, sip_gold: float):
        """
        :param sip_gold:
        :param sip_debt:
        :param sip_equity:
        this function will add some amounts to the money
        from the second month
        """
        self.equity += sip_equity
        self.debt += sip_debt
        self.gold += sip_gold


def test(file):
    """
    this class instantiates an object
    of class Money
    :param file:
    """
    pass


def main():
    """
    the function that starts our program
    our command line will take 1 argument
    :param
    """
    input_file = sys.argv[1]
    test(input_file)


if __name__ == "__main__":
    main()