def calculate_cost_with_tax(doc, method):
    from frappe.utils import flt
    cost_price = doc.cost_price
    list_price = doc.list_price
    cost_price_with_tax = 0
    list_price_with_tax = 0
    for tax in doc.taxes:
        rate = flt(tax.tax_rate)/flt(100)
        cost_price_with_tax = flt(cost_price) * flt(1+rate)
        list_price_with_tax = flt(list_price) * flt(1+rate)
    doc.cost_price_with_tax = cost_price_with_tax
    doc.list_price_with_tax = list_price_with_tax
