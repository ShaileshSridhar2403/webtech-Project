import pymongo
import datetime
import json
from flask import Flask, render_template, request, url_for, redirect, abort, jsonify, make_response
from flask_cors import CORS, cross_origin
from bson import json_util
from bson.json_util import dumps
import random
import gridfs

app=Flask(__name__)


@app.route('/addCommunity',methods=['POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def addCommunity():
	if request.method == 'POST':
		post= request.json
		client = pymongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
		db=client.hack_wt
		posts=db.community
		post_id=posts.insert_one(post)
		client.close()
		return "added"


if __name__ == '__main__':
	app.run(debug=True)
