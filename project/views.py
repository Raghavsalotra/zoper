from project import app
from flask import jsonify,request,abort
from project.data import data
from project.helper.datahelper import Datahelper


@app.route("/api/getall", methods=["GET"])
def get_all():
    try:
        return jsonify({"data": data.record})
    except Exception, e:
        print e.message


@app.route('/api/get/<int:data_id>', methods=["GET"])
def get_data_id(data_id):
    try:
        return Datahelper.get_data(data_id)
    except Exception, e:
        print e.message
    return "No Data Found"



@app.route("/api/update/<int:data_id>", methods=["PUT"])
def update_data(data_id):
    print data_id
    if not request.json:
        print request.json
        abort(400)
    res = Datahelper.update_data(data_id, request.json)
    if res == 0:
        return jsonify({"Update":False})
    else:
        return jsonify({"Update":True})


@app.route("/api/delete/<int:data_id>", methods=["DELETE"])
def delete_data(data_id):
    res = Datahelper.delete_data(data_id)
    if res == 1:
        return jsonify({"delete": True})
    else:
        return jsonify({"delete": False})


