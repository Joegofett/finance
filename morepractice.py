import yfinance as yf

#Below is showing different listing's of the endpoints and what it looks like


Tesla       =  yf.Ticker("TSLA")
Amazon      =  yf.Ticker("AMZN")
RGA         =  yf.Ticker("RGA")

# print(Tesla.info["priceToBook"])
# print(Tesla.info["returnOnEquity"])


# print("Amazon Info -------------------------------------------------------------------")
# print(Amazon.info)

# {'zip': '98109-5210', 
# 'sector': 'Consumer Cyclical', 
# 'fullTimeEmployees': 1622000, 
# 'longBusinessSummary': 'Amazon.com, Inc. engages in the retail sale of consumer products and subscriptions in North America and internationally. The company operates through three segments: North America, International, and Amazon Web Services (AWS). It sells merchandise and content purchased for resale from third-party sellers through physical and online stores. The company also manufactures and sells electronic devices, including Kindle, Fire tablets, Fire TVs, Rings, and Echo and other devices; provides Kindle Direct Publishing, an online service that allows independent authors and publishers to make their books available in the Kindle Store; and develops and produces media content. In addition, it offers programs that enable sellers to sell their products on its websites, as well as its stores; and programs that allow authors, musicians, filmmakers, Twitch streamers, skill and app developers, and others to publish and sell content. Further, the company provides compute, storage, database, analytics, machine learning, and other services, as well as fulfillment, advertising, publishing, and digital content subscriptions. Additionally, it offers Amazon Prime, a membership program, which provides free shipping of various items; access to streaming of movies and series; and other services. The company serves consumers, sellers, developers, enterprises, and content creators. Amazon.com, Inc. was incorporated in 1994 and is headquartered in Seattle, Washington.', 
# 'city': 'Seattle',
# 'phone': '206 266 1000', 
# 'state': 'WA', 
# 'country': 'United States', 
# 'companyOfficers': [], 
# 'website': 'https://www.amazon.com', 
# 'maxAge': 1, 
# 'address1': '410 Terry Avenue North', 
# 'industry': 'Internet Retail', 
# 'ebitdaMargins': 0.11658, 
# 'profitMargins': 0.04482, 
# 'grossMargins': 0.42137, 
# 'operatingCashflow': 39324000256, 
# 'revenueGrowth': 0.073, 
# 'operatingMargins': 0.04172, 
# 'ebitda': 55698001920, 
# 'targetLowPrice': 112.5, 
# 'recommendationKey': 'buy', 
# 'grossProfits': 197478000000, 
# 'freeCashflow': -9018749952, 
# 'targetMedianPrice': 175, 
# 'currentPrice': 123.23, 
# 'earningsGrowth': None, 
# 'currentRatio': 0.96, 
# 'returnOnAssets': 0.03395, 
# 'numberOfAnalystOpinions': 51, 
# 'targetMeanPrice': 178.48, 
# 'debtToEquity': 109.9, 
# 'returnOnEquity': 0.18045999, 
# 'targetHighPrice': 232.75, 
# 'totalCash': 66384998400, 
# 'totalDebt': 147266994176, 
# 'totalRevenue': 477748002816, 
# 'totalCashPerShare': 6.525, 
# 'financialCurrency': 'USD', 
# 'revenuePerShare': 47.092, 
# 'quickRatio': 0.707, 
# 'recommendationMean': 1.7, 
# 'exchange': 'NMS', 
# 'shortName': 'Amazon.com, Inc.', 
# 'longName': 'Amazon.com, Inc.', 
# 'exchangeTimezoneName': 'America/New_York', 
# 'exchangeTimezoneShortName': 'EDT', 
# 'isEsgPopulated': False, 
# 'gmtOffSetMilliseconds': '-14400000', 
# 'quoteType': 'EQUITY', 
# 'symbol': 'AMZN', 
# 'messageBoardId': 'finmb_18749', 
# 'market': 'us_market', 
# 'annualHoldingsTurnover': None,
# 'enterpriseToRevenue': 2.827, 
# 'beta3Year': None, 
# 'enterpriseToEbitda': 24.248, 
# '52WeekChange': -0.23538119, 
# 'morningStarRiskRating': None, 
# 'forwardEps': 2.7, 
# 'revenueQuarterlyGrowth': None, 
# 'sharesOutstanding': 10174400512, 
# 'fundInceptionDate': None, 
# 'annualReportExpenseRatio': None, 
# 'totalAssets': None, 
# 'bookValue': 13.175, 
# 'sharesShort': 94478620, 
# 'sharesPercentSharesOut': 0.0093, 
# 'fundFamily': None, 
# 'lastFiscalYearEnd': 1640908800, 
# 'heldPercentInstitutions': 0.6072, 
# 'netIncomeToCommon': 21412999168, 
# 'trailingEps': 2.085, 
# 'lastDividendValue': None, 
# 'SandP52WeekChange': -0.025035143, 
# 'priceToBook': 9.353321, 
# 'heldPercentInsiders': 0.098579995, 
# 'nextFiscalYearEnd': 1703980800, 
# 'yield': None, 
# 'mostRecentQuarter': 1648684800,
# 'shortRatio': 0.95, 
# 'sharesShortPreviousMonthDate': 1649894400,
# 'floatShares': 9159207028, 
# 'beta': 1.235027, 
# 'enterpriseValue': 1350546620416, 
# 'priceHint': 2, 
# 'threeYearAverageReturn': None,
# 'lastSplitDate': 1654473600, 
# 'lastSplitFactor': '20:1', 
# 'legalType': None, 
# 'lastDividendDate': None, 
# 'morningStarOverallRating': None, 
# 'earningsQuarterlyGrowth': None, 
# 'priceToSalesTrailing12Months': 2.624378, 
# 'dateShortInterest': 1652400000, 
# 'pegRatio': 3.8, 
# 'ytdReturn': None, 
# 'forwardPE': 45.64074, 
# 'lastCapGain': None, 
# 'shortPercentOfFloat': 0.0106, 
# 'sharesShortPriorMonth': 71099020, 
# 'impliedSharesOutstanding': 0,
# 'category': None, 
# 'fiveYearAverageReturn': None, 
# 'previousClose': 124.79, 
# 'regularMarketOpen': 122.005, 
# 'twoHundredDayAverage': 156.72887, 
# 'trailingAnnualDividendYield': 0, 
# 'payoutRatio': 0, 
# 'volume24Hr': None,
# 'regularMarketDayHigh': 124.1, 
# 'navPrice': None, 
# 'averageDailyVolume10Day': 109577750, 
# 'regularMarketPreviousClose': 124.79, 
# 'fiftyDayAverage': 134.29642, 
# 'trailingAnnualDividendRate': 0, 
# 'open': 122.005, 
# 'toCurrency': None, 
# 'averageVolume10days': 109577750, 
# 'expireDate': None,
# 'algorithm': None, 
# 'dividendRate': None, 
# 'exDividendDate': None, 
# 'circulatingSupply': None, 
# 'startDate': None, 
# 'regularMarketDayLow': 120.63, 
# 'currency': 'USD', 
# 'trailingPE': 59.10312, 
# 'regularMarketVolume': 37837308, 
# 'lastMarket': None, 
# 'maxSupply': None, 
# 'openInterest': None, 
# 'marketCap': 1253791367168, 
# 'volumeAllCurrencies': None, 
# 'strikePrice': None, 
# 'averageVolume': 87417865, 
# 'dayLow': 120.63,
#  'ask': 123.74, 
# 'askSize': 900,
#  'volume': 37837308, 
# 'fiftyTwoWeekHigh': 188.654, 
# 'fromCurrency': None, 
# 'fiveYearAvgDividendYield': None, 
# 'fiftyTwoWeekLow': 101.26, 
# 'bid': 123.72, 
# 'tradeable': False,
#  'dividendYield': None,
#  'bidSize': 900, 
# 'dayHigh': 124.1, 
# 'regularMarketPrice': 123.23, 
# 'preMarketPrice': 122.15, 
# 'logo_url': 'https://logo.clearbit.com/amazon.com', 
# 'trailingPegRatio': 2.9974}

# print("Amazon Financials")
# print(Amazon.financials)

# Amazon Financials
#                                             2021-12-31      2020-12-31      2019-12-31      2018-12-31
# Research Development                     56052000000.0   42740000000.0   35931000000.0   28837000000.0
# Effect Of Accounting Charges                      None            None            None            None
# Income Before Tax                        38155000000.0   24194000000.0   13962000000.0   11270000000.0
# Minority Interest                                 None            None            None            None
# Net Income                               33364000000.0   21331000000.0   11588000000.0   10073000000.0
# Selling General Administrative          116485000000.0   87193000000.0   64313000000.0   52177000000.0
# Gross Profit                            197478000000.0  152757000000.0  114986000000.0   93731000000.0
# Ebit                                     24879000000.0   22899000000.0   14541000000.0   12421000000.0
# Operating Income                         24879000000.0   22899000000.0   14541000000.0   12421000000.0
# Other Operating Expenses                    62000000.0     -75000000.0     201000000.0     296000000.0
# Interest Expense                         -1809000000.0   -1647000000.0   -1600000000.0   -1417000000.0
# Extraordinary Items                               None            None            None            None
# Non Recurring                                     None            None            None            None
# Other Items                                       None            None            None            None
# Income Tax Expense                        4791000000.0    2863000000.0    2374000000.0    1197000000.0
# Total Revenue                           469822000000.0  386064000000.0  280522000000.0  232887000000.0
# Total Operating Expenses                444943000000.0  363165000000.0  265981000000.0  220466000000.0
# Cost Of Revenue                         272344000000.0  233307000000.0  165536000000.0  139156000000.0
# Total Other Income Expense Net           13276000000.0    1295000000.0    -579000000.0   -1151000000.0
# Discontinued Operations                           None            None            None            None
# Net Income From Continuing Ops           33364000000.0   21331000000.0   11588000000.0   10073000000.0
# Net Income Applicable To Common Shares   33364000000.0   21331000000.0   11588000000.0   10073000000.0

# print("Amazon Balance Sheet")
# print(Amazon.balance_sheet)

# Amazon Balance Sheet
#                              2021-12-31    2020-12-31    2019-12-31    2018-12-31
# Intangible Assets          5.107000e+09  4.981000e+09  4.049000e+09  4.110000e+09
# Capital Surplus            5.553800e+10  4.286500e+10  3.365800e+10  2.679100e+10
# Total Liab                 2.823040e+11  2.277910e+11  1.631880e+11  1.190990e+11
# Total Stockholder Equity   1.382450e+11  9.340400e+10  6.206000e+10  4.354900e+10
# Other Current Liab         1.802700e+10  1.526700e+10  1.220200e+10  9.959000e+09
# Total Assets               4.205490e+11  3.211950e+11  2.252480e+11  1.626480e+11
# Common Stock               5.000000e+06  5.000000e+06  5.000000e+06  5.000000e+06
# Other Current Assets       2.420000e+08  2.330000e+08  2.760000e+08  4.180000e+08
# Retained Earnings          8.591500e+10  5.255100e+10  3.122000e+10  1.962500e+10
# Other Liab                 1.744300e+10  1.361700e+10  1.217100e+10  1.756300e+10
# Good Will                  1.537100e+10  1.501700e+10  1.475400e+10  1.454800e+10
# Treasury Stock            -3.213000e+09 -2.017000e+09 -2.823000e+09 -2.872000e+09
# Other Assets               1.812500e+10  1.209700e+10  1.009600e+10  6.370000e+09
# Cash                       3.622000e+10  4.212200e+10  3.609200e+10  3.175000e+10
# Total Current Liabilities  1.422660e+11  1.263850e+11  8.781200e+10  6.839100e+10
# Short Long Term Debt       1.687000e+09  1.266000e+09  1.305000e+09  1.371000e+09
# Other Stockholder Equity  -1.376000e+09 -1.800000e+08 -9.860000e+08 -1.035000e+09
# Property Plant Equipment   2.163630e+11  1.506670e+11  9.784600e+10  6.179700e+10
# Total Current Assets       1.615800e+11  1.327330e+11  9.633400e+10  7.510100e+10
# Long Term Investments      4.003000e+09  5.700000e+09  2.169000e+09  7.220000e+08
# Net Tangible Assets        1.177670e+11  7.340600e+10  4.325700e+10  2.489100e+10
# Short Term Investments     5.982900e+10  4.227400e+10  1.892900e+10  9.500000e+09
# Net Receivables            3.264900e+10  2.430900e+10  2.054000e+10  1.625900e+10
# Long Term Debt             5.494400e+10  3.521600e+10  2.341400e+10  2.349500e+10
# Inventory                  3.264000e+10  2.379500e+10  2.049700e+10  1.717400e+10
# Accounts Payable           7.866400e+10  7.253900e+10  4.718300e+10  3.819200e+10





# print("RGA Financials --------------------------------------------------------------------------------------")
# print(RGA.financials)
# print("RGA Balance Sheet------------------------------------------------------------------------------------")
# print(RGA.balance_sheet)
# print("RGA Earnings------------------------------------------------------------------------------------------")
# print(RGA.earnings)

# print("Amazon Cash flow")
# print(Amazon.cashflow)


# Amazon Cash flow
#                                              2021-12-31    2020-12-31    2019-12-31    2018-12-31
# Investments                               -7.730000e+08 -2.224200e+10 -9.131000e+09  1.140000e+09
# Change To Liabilities                      5.916000e+09  1.874500e+10  9.904000e+09  4.414000e+09
# Total Cashflows From Investing Activities -5.815400e+10 -5.961100e+10 -2.428100e+10 -1.236900e+10
# Net Borrowings                             6.291000e+09 -1.104000e+09 -1.006600e+10 -7.686000e+09
# Total Cash From Financing Activities       6.291000e+09 -1.104000e+09 -1.006600e+10 -7.686000e+09
# Change To Operating Activities             2.123000e+09  5.754000e+09 -1.383000e+09  4.720000e+08
# Net Income                                 3.336400e+10  2.133100e+10  1.158800e+10  1.007300e+10
# Change In Cash                            -5.900000e+09  5.967000e+09  4.237000e+09  1.031700e+10
# Effect Of Exchange Rate                   -3.640000e+08  6.180000e+08  7.000000e+07 -3.510000e+08
# Total Cash From Operating Activities       4.632700e+10  6.606400e+10  3.851400e+10  3.072300e+10
# Depreciation                               3.429600e+10  2.525100e+10  2.178900e+10  1.534100e+10
# Change To Inventory                       -9.487000e+09 -2.849000e+09 -3.278000e+09 -1.314000e+09
# Change To Account Receivables             -1.816300e+10 -8.169000e+09 -7.681000e+09 -4.615000e+09
# Change To Netincome                       -1.722000e+09  6.001000e+09  7.575000e+09  6.352000e+09
# Capital Expenditures                      -6.105300e+10 -4.014000e+10 -1.686100e+10 -1.342700e+10
# Other Cashflows From Investing Activities           NaN           NaN           NaN  2.104000e+09


# print("Amazon Earnings")
# print(Amazon.earnings)
# Amazon Earnings
#            Revenue     Earnings
# Year
# 2018  232887000000  10073000000
# 2019  280522000000  11588000000
# 2020  386064000000  21331000000
# 2021  469822000000  33364000000

# print("Amazon News")
# print(Amazon.news)


# Amazon News
# [{'uuid': 'cb31d4b9-cf4b-3585-b17d-fe1f80604881', 'title': 'Fintech Stocks To Buy And Watch Or Sell As Competition Intensifies', 'publisher': "Investor's Business Daily", 'link': 'https://finance.yahoo.com/m/cb31d4b9-cf4b-3585-b17d-fe1f80604881/fintech-stocks-to-buy-and.html', 'providerPublishTime': 1654602903, 'type': 'STORY'}, 
# {'uuid': 'd0d8ab6d-54bd-3e7e-880a-f67c51c695ff', 'title': '4 Growth Stocks to Buy and Hold Forever', 'publisher': 'Motley Fool', 'link': 'https://finance.yahoo.com/m/d0d8ab6d-54bd-3e7e-880a-f67c51c695ff/4-growth-stocks-to-buy-and.html', 'providerPublishTime': 1654600500, 'type': 'STORY'}, 
# {'uuid': 'b6ad9afc-e821-31f9-89bc-5d2dd1cef736', 'title': '2 Warren Buffett Stocks to Buy and Hold for Decades', 'publisher': 'Motley Fool', 'link': 'https://finance.yahoo.com/m/b6ad9afc-e821-31f9-89bc-5d2dd1cef736/2-warren-buffett-stocks-to.html', 'providerPublishTime': 1654599900, 'type': 'STORY'},
# {'uuid': '580b060c-937e-44a6-a8cb-df31efc510e1', 'title': 'Target ratchets up discounts and cuts guidance in response to more cautious shoppers', 'publisher': 'Yahoo Finance', 'link': 'https://finance.yahoo.com/news/target-more-cautious-shopper-discounts-guidance-100033736-110004100.html', 'providerPublishTime': 1654599604, 'type': 'STORY'}, 
# {'uuid': '94e3ed75-a808-47f4-b431-502390ac3bfa', 'title': "Google and Amazon urge Biden administration to alter 'aging out' immigration policies", 'publisher': 'Yahoo Finance', 'link': 'https://finance.yahoo.com/news/amazon-google-us-chamber-of-commerceh-1-b-visas-letter-100727687.html', 'providerPublishTime': 1654596447, 'type': 'STORY'},
# {'uuid': 'eb9459aa-31fd-3fd5-811d-47a8b3342a1b', 'title': 'Should You Sell Amazon After Its Stock Split?', 'publisher': 'Motley Fool', 'link': 'https://finance.yahoo.com/m/eb9459aa-31fd-3fd5-811d-47a8b3342a1b/should-you-sell-amazon-after.html', 'providerPublishTime': 1654596000, 'type': 'STORY'}, 
# {'uuid': 'e88ec62c-61d7-38d4-8812-ba651148fe8b', 'title': '7 Surefire Stocks I Plan to Hold for at Least 20 Years', 'publisher': 'Motley Fool', 'link': 'https://finance.yahoo.com/m/e88ec62c-61d7-38d4-8812-ba651148fe8b/7-surefire-stocks-i-plan-to.html', 'providerPublishTime': 1654593660, 'type': 'STORY'}, 
# {'uuid': '835ba58e-6051-3146-9843-0eb7a422dc76', 'title': 'RPT-GRAPHIC-Amazon stock split may draw retail traders in tough market', 'publisher': 'Reuters', 'link': 'https://finance.yahoo.com/news/rpt-graphic-amazon-stock-split-050000792.html', 'providerPublishTime': 1654578000, 'type': 'STORY'}]





# print("Amazon Calendar")
# print(Amazon.calendar)


# Amazon Calendar
#                                     0                    1
# Earnings Date     2022-07-27 10:59:00  2022-08-01 12:00:00
# Earnings Average                 0.16                 0.16
# Earnings Low                    -0.03                -0.03
# Earnings High                    0.47                 0.47
# Revenue Average          119640000000         119640000000
# Revenue Low              116000000000         116000000000
# Revenue High             121513000000         121513000000


# print(Amazon.info["priceToBook"])
# print(Amazon.info["returnOnEquity"])