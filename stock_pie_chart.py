from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt

stocks=[]
prices=[]

#used for the while loop to end
flag=True

while flag:
    print('These are the stock(s) currently in the chart:\n')
    print(stocks)
    add_another=input('\nDo you want to add another stock? y/n\n')
    add_another.lower()
    if add_another=='y':
        ticker=input('\nEnter the stock you want to add\n')
        stocks.append(ticker)
        stock_price=si.get_live_price(ticker)
        shares=int(input('How many shares of {} do you have?\n'.format(ticker)))
        equity=stock_price*shares
        prices.append(equity)
    else:
        print('ok, moving on')
        flag=False
        
cash=input("How much money do you have in your stock account that isnt invested in stocks (cash)\n") 
stocks.append('cash')
prices.append(cash)
colors=['#3498DB']

plt.pie(prices, labels=stocks, autopct='%1.2f%%', wedgeprops={'edgecolor':'0', 'linewidth':1, 'linestyle': '-', 'antialiased': True}, colors=colors)
plt.axis=('equal')       
    













