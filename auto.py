import pymongo
import datetime
import json
from flask import Flask, render_template, request, url_for, redirect, abort, jsonify, make_response
from flask_cors import CORS, cross_origin
from bson import json_util
from bson.json_util import dumps,ObjectId
import random
import gridfs

app=Flask(__name__)


@app.route('/autoComplete',methods=['GET','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def autoComplete():
	if request.method == 'GET':
		#post= request.json
		client = pymongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
		db=client.hack_wt
		posts=db.community
		value=request.args.get('value',type=str)
		ab=posts.find({'communityName':{'$regex':value}})
		di=json.loads(json_util.dumps(ab))
		return jsonify({'List':di}),201


if __name__ == '__main__':
	app.run(debug=True)
		