from odoo import _, api, fields, models

class Airparcel(models.Model):
    _name = 'airparcel.shipping'
    _description = 'Airparcel Shipping Management'


    name = fields.Char('Producto')
    product_id_number = fields.Char('Id del Producto', default=lambda self:_('New'))
    product_weight = fields.Float('Peso total')
    product_price = fields.Float('Precio del Producto')
    product_type = fields.Char('Categoria de Producto')
    product_package = fields.Selection(selection=[('box','Caja'), ('envelope','Sobre')], string='Tipo de paquete')
    provider_id = fields.Many2one('res.partner', string='Proveedor')
    provider_cuit = fields.Char( string='Cuit del proveedor', related='provider_id.vat')
    importer_id = fields.Many2one('res.partner', string='Importador')
    importer_cuit = fields.Char('Cuit del importador', related='importer_id.vat')
    owner = fields.Char(string='Nombre y Apellido')
    owner_phone = fields.Char(string='Telefono')
    owner_email = fields.Char('Email')
    owner_address = fields.Char('Direccion Particular')
    owner_city = fields.Char('Ciudad')
    owner_state = fields.Char('Provincia')
    owner_cp = fields.Integer('CP')
    owner_type = fields.Selection(selection=[('compañia','Compañia'),('particular','Particular')])
    location_bar=fields.Selection(selection=[
        ('wc','World Class Almacen'),
        ('aduana', 'Aduana'),
        ('ap', 'Airparcel Almacen')], default='wc', string='Ubicacion', required=True)
    status_bar = fields.Selection(selection=[
        ('travel', 'En viaje'),
        ('arrived','Arribado'),
        ('dispatched','Despachado')], default='travel', string='Estado', required=True)
    barcode = fields.Char('Codigo de Barras')
    presupuesto = fields.Float("presupuesto en dolares")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['product_id_number'] = self.env['ir.sequence'].next_by_code('airparcel.shipping')
        return super(Airparcel, self).create(vals_list)
    

    def _conect_to_Fedex(self):
        # conectar con la api de aduana
        # respuesta True o False
        pass

    def action_to_wc(self):
        for rec in self:
            rec.location_bar = 'wc'
            rec.status_bar = 'travel'

    def action_to_aduana(self):
        for rec in self:
            rec.location_bar = 'aduana'
            rec.status_bar = 'travel'

    def action_to_ap(self):
        for rec in self:
            rec.location_bar = 'ap'
            rec.status_bar = 'travel'