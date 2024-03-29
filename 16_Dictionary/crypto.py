data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

keys = list(data.keys())
values = list(data.values())
data['ETH']['total_diff'] = 100
# print(keys)
# print(values)
# data['tokens'][0]['fst_token_info']['name'] = 'dog'
# print(data)

data['ETH']['totalOut'] += data['tokens'][0]['total_out']
data['ETH']['totalOut'] += data['tokens'][1]['total_out']

del data['tokens'][0]['total_out']
del data['tokens'][1]['total_out']
# print(data['ETH']['totalOut'])

del data['tokens'][1]['price']
data['tokens'][1]['total_price'] = False
print(data)
