import flask, json, redis
from pymongo import MongoClient

##############################
# Init library / connections
##############################

flask_app = flask.Flask(__name__)
deliveriesdb = MongoClient('mongodb://comp3122:23456@delivery_order_db:27017')

@flask_app.route('/<order_id>', methods=['GET'])
def get_order(order_id):
    orders = deliveriesdb.delivery_orders.deliveries.find_one({'orders.order_id': order_id}, { '_id': 0})
    if not orders:
        return {'error': 'not found'}, 404
    orders = orders['orders']
    for order in orders:
        if order['order_id'] == order_id:
            return order, 200
            
if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=True, port=15000)

