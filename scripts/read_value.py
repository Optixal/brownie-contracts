from brownie import SimpleStorage, accounts, config


def read_contract():
    deployed = SimpleStorage[-1]
    print(deployed.retrieve())


def main():
    read_contract()
