from flask import jsonify
from sqlalchemy import text

from app import app, db


@app.route('/utils/noname', methods=['GET'])
def insert_values_lessor_noname():
    res = db.session.execute(text("CALL insert_values_lessor_noname"))
    res_list = [str(row) for row in res]
    return jsonify({'lessor': res_list})


@app.route('/utils/insert', methods=['GET'])
def insert_values_lessor():
    conn = db.engine.raw_connection()
    results = conn.cursor().callproc('insert_into_lessor', [{'email_': 'dadadadadada'}, {'phone_': 'dadadadad'},
                                                            {'first_name_': 'dadadadadadad'},
                                                            {'last_name_': 'dadadadadada'}])
    conn.close()
    print(results)
    res_list = [str(row) for row in results]
    return jsonify({'lessor': res_list})


@app.route('/utils/many', methods=['GET'])
def insert_m_to_m():
    conn = db.engine.raw_connection()
    results = conn.cursor().callproc('add_apartment_amenity', [{'apartment_id_': 1}, {'amenity_id_': 1}])
    conn.close()
    print(results)
    res_list = [str(row) for row in results]
    return jsonify({'lessor': res_list})

@app.route('/utils/aggregate', methods=['GET'])
def insert_aggregate():
    conn = db.engine.raw_connection()
    results = conn.cursor().callproc('select_aggregate_from_rating', [{'type_of_search': 'AVG'}])
    conn.close()
    print(results)
    res_list = [str(row) for row in results]
    return jsonify({'lessor': res_list})
