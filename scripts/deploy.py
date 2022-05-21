from brownie import accounts, config, SimpleStorage, network


def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        # return accounts.load("ethereum-dev")
        # return accounts.add(str(os.getenv("WEB3_PRIVATE_KEY")))
        return accounts.add(config["wallets"]["from_key"])


def deploy_simple_storage():
    account = get_account()
    print(account)

    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)  # number of blocks
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
