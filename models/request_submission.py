from odoo import models,fields,api
import logging

# declare new model
class Request(models.Model):
    _name='vendor.adjustment.request'

    order_id=fields.Many2one('sale.order',string='Order Id',required=True)
    adjustment_detail=fields.Text(string="Adjustment Detail",required=True)
    comment=fields.Text(string="Comment",required=True)
    email=fields.Char(string="Email",required=True)
    

# declare Odoo decorator 'api.model' for automatic email notification
# new record is created
    @api.model
    def create(self, values):
        record = super(Request, self).create(values)
        # Trigger the automated Email action on record creation
        template = self.env.ref('Vendor_Self_Service_Portal.id_order_adjustment_request_submission')
        template.send_mail(record.id, force_send=True)
        return record
        