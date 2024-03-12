from strategy import generate_report_short, generate_report_long, generate_report_very_short, generate_report_short_long

capital = 1000

short_portfolio = generate_report_short(capital)
long_portfolio = generate_report_long(capital)
very_short_portfolio = generate_report_very_short(capital)
short_long_portfolio = generate_report_short_long(capital)


print(short_long_portfolio)
