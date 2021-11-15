db.auth('comp3122', '23456')
db = db.getSiblingDB('delivery_orders')
db.createCollection('deliveries')