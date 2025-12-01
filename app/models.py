from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Node(db.Model):
    __tablename__ = 'node'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    devices = db.relationship('Device', backref='node', lazy=True)

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(15), nullable=False)
    management_vlan = db.Column(db.Integer)
    node_id = db.Column(db.Integer, db.ForeignKey('node.id'))
    template_id = db.Column(db.Integer, db.ForeignKey('template.id'))
    snmp_version = db.Column(db.Enum('1', '2c', '3'), default='2c')
    snmp_community = db.Column(db.String(50), default='public')
    snmp_port = db.Column(db.Integer, default=161)

class Template(db.Model):
    __tablename__ = 'template'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    vendor = db.Column(db.String(50))
    model = db.Column(db.String(50))
    description = db.Column(db.Text)
    actions = db.relationship('TemplateAction', backref='template', lazy=True)

class TemplateAction(db.Model):
    __tablename__ = 'template_action'
    id = db.Column(db.Integer, primary_key=True)
    template_id = db.Column(db.Integer, db.ForeignKey('template.id'))
    name = db.Column(db.String(100), nullable=False)
    oid = db.Column(db.String(255))
    timeout = db.Column(db.Integer, default=30)
    is_active = db.Column(db.Boolean, default=True)