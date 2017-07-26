frappe.provide("erpnext.item");

frappe.ui.form.on("Item", {
  list_price: function(frm) {
    frm.set_value("list_price_with_tax", frm.doc.list_price);
		if (frm.doc.list_price){
      if (frm.doc.taxes){
        $.each(frm.doc.taxes, function(index, data){
          var rate = flt(data.tax_rate / 100);
          var price = flt(frm.doc.list_price * (1+rate));
          frm.set_value("list_price_with_tax", price);
    		})

      }
		}
		frm.refresh_fields();
	},

  cost_price: function(frm) {
    frm.set_value("cost_price_with_tax", frm.doc.cost_price);

		if (frm.doc.cost_price){
      if (frm.doc.taxes){
        $.each(frm.doc.taxes, function(index, data){
          var rate = flt(data.tax_rate / 100);
          var price = flt(frm.doc.cost_price * (1+rate));
          frm.set_value("cost_price_with_tax", price);
    		})

      }
		}
		frm.refresh_fields();
	},

  item_group: function(frm){
    var group = frm.doc.item_group;
    frappe.db.get_value("Item Group", {item_group_name: frm.doc.item_group}, "tax", function(r) {
      var row = frm.add_child("taxes");
      row.tax_type = r.tax;
      row.tax_rate = 14;
      refresh_field(['taxes']);
    })
    frm.refresh_fields();
  }
});


frappe.ui.form.on('Item Tax', {

  tax_rate: function(frm, cdt, cdn) {
		var tax = frappe.get_doc(cdt, cdn);
		if(tax.tax_rate) {
			return calculate_prices(frm)
		}
	}
})

var calculate_prices = function(frm) {
	var doc = frm.doc;
	doc.list_price_with_tax = 0;
	doc.cost_price_with_tax = 0;

	if(doc.taxes) {
		$.each(doc.taxes, function(index, data){
      var rate = flt(data.tax_rate / 100);
      var list_price = flt(doc.list_price * (1+rate));
      var cost_price = flt(doc.cost_price * (1+rate));
      doc.list_price_with_tax = list_price;
      doc.cost_price_with_tax = cost_price;
		})
	}
	refresh_field('list_price_with_tax')
	refresh_field('cost_price_with_tax')
}
