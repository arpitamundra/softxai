import requests
from flask import Flask,request,jsonify

app = Flask()

db = ""


class Employee(db.model):
    id = db.Column(db.Integer,primary_key= True)
    emp_name = db.Column(db.String(100))
    salary = db.Column(db.Float)
    dept_id = db.Column(db.String(100))


def create_emp():
    data = request.json
    emp =Employee(emp_name= data["emp_name"],dept_id = data["dept_id"],salary = data["salary"])
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message":"emp created"})

def get_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error":"emp not found"},404)
    return jsonify({"id":emp.id,"emp_name":emp.emp_name,"salary":emp.salary,"dept_id":emp.dept_id})


def get_emp_list():
    dept = request.args.get("department")
    if dept:
        emps = Employee.query.filter_by(dept=dept.dept_id).all()
    else:
        emps = Employee.query.all()

    return jsonify([{"id":emp.id,"emp_name":emp.emp_name,"salary":emp.salary,"dept_id":emp.dept_id} for emp in emps ])


def update_emp(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error":"emp not found"})
    else:
        data = request.json
        emp.emp_name = data.get("emp_name",emp.emp_name)
        emp.salary = data.get("salary",emp.salary)
        emp.dept_id = data.get("dept_id",emp.dept_id)
        db.session.commit()
        return jsonify({"message":"emp details updated"})