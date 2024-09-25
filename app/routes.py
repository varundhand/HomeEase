from flask import request, jsonify
from app import app, db
from app.models import Admin, Service, ServiceProfessional, Customer, ServiceRequest

@app.route('/admin/create_service', methods=['POST'])
def create_service():
    data = request.get_json()
    new_service = Service(
        name=data['name'],
        description=data['description'],
        base_price=data['price']
    )
    db.session.add(new_service)
    db.session.commit()
    return jsonify({'message': 'Service created successfully'}), 201

@app.route('/admin/approve_professional/<int:id>', methods=['PUT'])
def approve_professional(id):
    professional = ServiceProfessional.query.get_or_404(id)
    # Logic to verify and approve
    return jsonify({'message': 'Professional approved'}), 200

@app.route('/admin/block_user/<int:id>', methods=['PUT'])
def block_user(id):
    # Block logic for customer or professional
    return jsonify({'message': 'User blocked'}), 200
