from flask import Flask
from flask import  request, jsonify
from flask_pymongo import  PyMongo
import recommenderSystem2 as rs
import json
import wt_api as dbapi

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)

def getCommunity():
        client = PyMongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
        db=client.hack_wt
        posts=db.community
        li=[]
        x=posts.find({})
        for i in x:
            li.append(i['communityID'])
        return jsonify({'data':li})

@app.route("/user_actions", methods=['POST'])
def user_actions():
    user_actions = mongo.db.user_actions
    user = request.json['UserID']
    property_id = request.json['communityID']
    action = request.json['action']
    user_actions_id = user_actions.insert({'UserID': user, 'propertyId': property_id, 'rating': action})
    new_user_action = user_actions.find_one({'_id': user_actions_id })
    return "Whatever"

@app.route("/user_recommendations/<user>", methods=['GET'])
def user_recommendations(user):
    client = PyMongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
    db = client.hack_wt
    user_actions = db.ratings
    communityIDs = getCommunity()
    output = []
    for s in user_actions.find():
        output.append({'UserID' : s['UserID'], 'communityID' : s['communityID'], 'rating': s['rating']})
    df = rs.makeDfFromData(output)
    model = rs.trainModel(df)
    output = rs.outputTopK(model,user,communityIDs,3)
    return jsonify({'result' : output})

#@app.route("/user_recommendations/propList/<users>", methods=['POST'])
#def preference_sort(user):
#    propList = request.json['properties']
#    u

if __name__ == '__main__':
    app.run()
