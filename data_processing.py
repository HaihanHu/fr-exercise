#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 20:34:37 2021

@author: shirleyhu
"""

import json
import time

def get_key(d, key, default="null"):
    if len(key) == 1:
        key = key[0]
        if 'id' in key:
            return d[key]['$oid']
        if key in d.keys():
            return d[key]

    if len(key) == 2:
        subkey = key[1]
        key = key[0]
        if key in d.keys():
            if 'id' in subkey:
                return d[key][subkey]['$oid']
            return d[key][subkey]

    return default


def time_format(timestamp):
    if timestamp == 'null':
        return timestamp
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(timestamp/1000.)))


def get_dict_data(d, keys):
    result = []
    for key in keys:
        r = get_key(d, key[1])
        if key[2]:
            r = time_format(r)
        if isinstance(r, str):
            if "," in r:
                r = r.replace(",", "-")
        if isinstance(r, bool):
            r = 1 if r else 0
        if key[1] == 'finalPrice':
            r =  float(r)
        result.append(r)
    return result

def drop_duplicates(data):
    result = []
    for d in data:
        if d not in result:
            result.append(d)
    return result

def process_users_table_data():
    file_name = "/Users/shirleyhu/Downloads/users.json"
    save_file_name = "/Users/shirleyhu/Desktop/users.csv"
    users = []
    keys = [
        ['active', ['active'], False],
        ['role', ['role'], False],
        ['signUpSource', ['signUpSource'], False],
        ['state', ['state'], False],
        ['userId', ['_id'], False],
        ['createdDate', ['createdDate', '$date'], True],
        ['lastLogin', ['lastLogin', '$date'], True],

    ]
    with open(file_name) as f, open(save_file_name, "w") as f1:
        for line in f:
            user = get_dict_data(json.loads( line.strip("\n") ), keys)
            user = ",".join([str(_) for _ in user]) + "\n"
            users.append(user)
        users = list(set(users))
        f1.writelines(users)


def process_brands_table_data():
    file_name = "/Users/shirleyhu/Downloads/brands.json"
    save_file_name = "/Users/shirleyhu/Desktop/brands.csv"
    brands = []
    keys = [
        ['barcode', ['barcode'], False],
        ['category', ['category'], False],
        ['categoryCode', ['categoryCode'], False],
        ['name', ['name'], False],
        ['topBrand', ['topBrand'], False],
        ['brandId', ['_id'], False],
        ['cpgId', ['cpg', '$id'], False],
        ['cpgRef', ['cpg', '$ref'], False],
        ['brandCode', ['brandCode'], False],

    ]
    with open(file_name, encoding="utf-8") as f, open(save_file_name, "w", encoding='utf-8') as f1:
        for line in f:
            brand = get_dict_data(json.loads( line.strip("\n") ), keys)
            brand = ",".join([str(_) for _ in brand]) + "\n"
            brands.append(brand)
        brands = drop_duplicates(brands)
        f1.writelines(brands)

def process_receipts_table_data():
    file_name = "/Users/shirleyhu/Downloads/receipts.json"
    save_file_name = "/Users/shirleyhu/Desktop/receipts.csv"
    receipts = []

    keys = [
        ['bonusPointsEarned', ['bonusPointsEarned'], False],
        ['bonusPointsEarnedReason', ['bonusPointsEarnedReason'], False],
        ['pointsEarned', ['pointsEarned'], False],
        ['purchasedItemCount', ['purchasedItemCount'], False],
        ['rewardsReceiptStatus', ['rewardsReceiptStatus'], False],
        ['totalSpent', ['totalSpent'], False],
        ['userId', ['userId'], False],
        ['receiptId', ['_id'], False],
        ['createDate', ['createDate','$date'], True],
        ['scanDate', ['dateScanned','$date'], True],
        ['finishDate', ['finishedDate','$date'], True],
        ['modifyDate', ['modifyDate','$date'], True],
        ['pointsAwardedDate', ['pointsAwardedDate','$date'], True],
        ['purchaseDate', ['purchaseDate','$date'], True],
    ]
    with open(file_name, encoding="utf-8") as f, open(save_file_name, "w", encoding='utf-8') as f1:
        for line in f:
            receipt = get_dict_data(json.loads(line.strip("\n")), keys)
            receipt = ",".join([str(_) for _ in receipt]) + "\n"
            receipts.append(receipt)
        receipts = drop_duplicates(receipts)
        f1.write(
            ",".join([i[0] for i in keys]) + '\n'
        )
        f1.writelines(receipts)

def process_receiptitemlist_table_data():
    file_name = "/Users/shirleyhu/Downloads/receipts.json"
    save_file_name = "/Users/shirleyhu/Desktop/receiptitemlist.csv"
    receiptitemlist = []
    keys = [
        ['barcode', ['barcode'], False],
        ['description', ['description'], False],
        ['finalPrice', ['finalPrice'], False],
        ['itemPrice', ['itemPrice'], False],
        ['needsFetchReview', ['needsFetchReview'], False],
        ['partnerItemId', ['partnerItemId'], False],
        ['preventTargetGapPoints', ['preventTargetGapPoints'], False],
        ['quantityPurchased', ['quantityPurchased'], False],
        ['userFlaggedBarcode', ['userFlaggedBarcode'], False],
        ['userFlaggedNewItem', ['userFlaggedNewItem'], False],
        ['userFlaggedPrice', ['userFlaggedPrice'], False],
        ['userFlaggedQuantity', ['userFlaggedQuantity'], False],
        ['bonusPointsEarnedReason', ['bonusPointsEarnedReason'], False],
        ['pointsNotAwardedReason', ['pointsNotAwardedReason'], False],
        ['pointsPayerId', ['pointsPayerId'], False],
        ['rewardsGroup', ['rewardsGroup'], False],
        ['rewardsProductPartnerId', ['rewardsProductPartnerId'], False],
        ['userFlaggedDescription', ['userFlaggedDescription'], False],
        ['originalMetaBriteBarcode', ['originalMetaBriteBarcode'], False],
        ['originalMetaBriteDescription', ['originalMetaBriteDescription'], False],
        ['brandCode', ['brandCode'], False],
        ['competitorRewardsGroup', ['competitorRewardsGroup'], False],
        ['discountedItemPrice', ['discountedItemPrice'], False],
        ['originalReceiptItemText', ['originalReceiptItemText'], False],
        ['itemNumber', ['itemNumber'], False],
        ['originalMetaBriteQuantityPurchased', ['originalMetaBriteQuantityPurchased'], False],
        ['pointsEarned', ['pointsEarned'], False],
        ['targetPrice', ['targetPrice'], False],
        ['competitiveProduct', ['competitiveProduct'], False],
        ['originalFinalPrice', ['originalFinalPrice'], False],
        ['originalMetaBriteItemPrice', ['originalMetaBriteItemPrice'], False],
        ['deleted', ['deleted'], False],
        ['priceAfterCoupon', ['priceAfterCoupon'], False],
        ['metabriteCampaignId', ['metabriteCampaignId'], False],
    ]

    with open(file_name, encoding="utf-8") as f, \
            open(save_file_name, "w", encoding='utf-8') as f1:
        id = 0
        for line in f:
            data = json.loads(line.strip("\n"))
            receiptId = data["_id"]['$oid']
            if "rewardsReceiptItemList" in data.keys():
                for d in data['rewardsReceiptItemList']:
                    lst = get_dict_data(d, keys)
                    lst = [id] + lst + [receiptId]
                    lst = ",".join([str(_) for _ in lst]) + "\n"
                    id += 1
                    receiptitemlist.append(lst)
        keys = [["id"]] + keys + [["receiptId"]]

        f1.write(
            ",".join([i[0] for i in keys]) + '\n'
        )
        f1.writelines(receiptitemlist[0:5137])
        f1.writelines(receiptitemlist[5138:])


if __name__ == '__main__':
    process_users_table_data()
    process_brands_table_data()
    
    process_receipts_table_data()

    process_receiptitemlist_table_data()