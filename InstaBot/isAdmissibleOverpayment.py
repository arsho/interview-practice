def isAdmissibleOverpayment(prices, notes, x):
    total_insta_price = sum(prices)
    store_price = []
    for i in range(len(prices)):
        current_insta_price = prices[i]
        current_store_price = current_insta_price
        current_note = notes[i]
        if "higher" in current_note:
            val = float(current_note.split("%")[0])
            current_store_price = current_insta_price/(1+(val/100.0))
        elif "lower" in current_note:
            val = float(current_note.split("%")[0])
            current_store_price = current_insta_price/(1-(val/100.0))
        store_price.append(current_store_price)
    total_store_price = sum(store_price)
    return total_insta_price<=total_store_price+x