# Write your code here:

# Don't touch anthing below this line 🙅🏻‍♂️🙅🏻‍♀️

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01


def get_yearly_revenue(m_revenue):
    """
    Takes monthly_revenue and returns revenue for a year.
    monthly_revenue (월간 매출)를 인수로 받고, revenue for a year (연간 매출)를 리턴.
    """
    return m_revenue * 12


def get_yearly_expenses(m_expenses):
    """
    Takes monthly_expenses returns expenses for a year.
    monthly_expenses (월간 비용)를 인수로 받고, expenses for a year (연간 비용)를 리턴.
    """

    return m_expenses * 12


def get_tax_amount(profit):
    """
    Takes profit returns tax_amount.
    profit (이익) 를 인수로 받고, tax_amount (세금 금액) 를 리턴.
    """

    if (profit > 100000):
        return profit * 0.25
    else:
        return profit * 0.15


def apply_tax_credits(tax_amount, tax_credits=0):
    """
    Takes tax_amount and tax_credits returns amount to discount.
    tax_amount (세금 금액), tax_credits (세액 공제율)를 인수로 받고, amount to discount (할인할 금액)를 리턴.
    """
    discount_tax_amount = tax_amount * (tax_credits / 100)
    return discount_tax_amount


profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(
    monthly_expenses)

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")
