def get_transactions(st):
    global transactions
    if st == 'print_it':
        for transaction in transactions:
            print(transaction[0], transaction[1], transaction[2])
    else:
        phone, action = st.split('-')
        action_type, amount = action.split(':')
        amount = int(amount)

        for transaction in transactions:
            if transaction[1] == action_type:
                transaction[0] += 1
                transaction[2] += amount
                break
        else:
                transactions.append([1, action_type, amount])


transactions = []
get_transactions('880005553535-перевод:100')
get_transactions('111111111-перевод:1000')
get_transactions('880005553535-оплата_жкх:10000')
get_transactions('89065664312-перевод:50000000')
get_transactions('print_it')