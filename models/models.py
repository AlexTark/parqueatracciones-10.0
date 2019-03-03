# -*- coding: utf-8 -*-

from odoo import models, fields, api

class parqueatracciones_atracciones(models.Model):
    _name = 'parqueatracciones.atracciones'

    name = fields.Char(string="IDAtraccion", required=True, help="Introduce el ID de la atraccion")
    nombre = fields.Char(strings="Nombre", required=True, help="Introduce el nombre de la atraccion")
    altura = fields.Integer(strings="AlturaMinima")
    zona = fields.Selection([('0','Zona Infantil'),('1','Zona Adulta'),('2','Zona Acuatica')])
    description = fields.Text()
    empleados = fields.Many2many("parqueatracciones.empleados", string="Empleados", ondelete="cascade")


class parqueatracciones_entradas(models.Model):
    _name = 'parqueatracciones.entradas'

    name = fields.Char(string="IDEntrada", required=True, help="Introduce el ID de la entrada")
    tipo = fields.Selection([('0','Infantil'),('1','Adulta'),('2','Premium'),('3','Reducida')], string="Tipo", default="0")
    precio = fields.Float(compute="_value_pc", store=True)
    clientes = fields.One2many("parqueatracciones.clientes","entradas", string="Clientes")

    def tipo_selection(self):
        return [(1,'Infantil'),(2,'Adulta'),(3,'Premium'),(4,'Reducida')]

    @api.depends('tipo')
    def _value_pc(self):
        if self.tipo == '0':
            self.precio = 19.99
        if self.tipo == '1':
            self.precio = 29.99
        if self.tipo == '2':
            self.precio = 39.99
        if self.tipo == '3':
            self.precio = 23.99


class parqueatracciones_empleados(models.Model):
    _name = 'parqueatracciones.empleados'

    name = fields.Char(string="DNI", required=True, help="Introduce el DNI del empleado")
    nombre = fields.Char(strings="Nombre", required=True, help="Introduce el nombre del empleado")
    apellidos = fields.Char(strings="Apellidos", required=True, help="Introduce los apellidos del empleado")
    salario = fields.Float(strings="Salario", required=True, help="Introduce el salario del empleado")
    fecha_alta = fields.Date(strings="Fecha_Alta", required=True, help="Introduce la fecha de alta del empleado")
    atracciones = fields.Many2many("parqueatracciones.atracciones", string="Atracciones", ondelete="cascade")


class parqueatracciones_clientes(models.Model):
    _name = 'parqueatracciones.clientes'

    name = fields.Char(string="DNI", required=True, help="Introduce el DNI del cliente")
    nombre = fields.Char(strings="Nombre", required=True, help="Introduce el nombre del cliente")
    apellidos = fields.Char(strings="Apellidos", required=True, help="Introduce los apellidos del cliente")
    correo = fields.Char(strings="Correo electronico", required=True, help="Introduce el correo del cliente")
    entradas = fields.Many2one("parqueatracciones.entradas", string="Entrada", ondelete="cascade")
    atracciones = fields.Many2many("parqueatracciones.atracciones", string="Atracciones", ondelete="cascade")