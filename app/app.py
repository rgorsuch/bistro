
from flask import Flask,request
from flask import jsonify
import redis
import logging

app = Flask(__name__)
log = logging.getLogger(__name__)


@app.route("/", methods=['GET'])
def get_bistro():
    return jsonify({'project':'bistro', 'version':'1.0.0'})

#connecting to the database
def connect_to_redis():
	redis_url = 'redis://redis-11874.c15.us-east-1-2.ec2.cloud.redislabs.com:11874'
	log.info("Connection to redis with url: "+redis_url)

	r = redis.from_url(redis_url)

	log.info("Redis Connected")
	return r

#adding a key-value pair to the database, to add foo:bar, send in /redis/foo/bar
@app.route("/redis/<string:key>/<string:value>")
def set_redis(key, value):
	r = connect_to_redis()
	if r.set(key,value):
		log.info("Added a key-value to the redis Database, namely: "+key+":"+value)
		return 'Successfully added key/value '+key+':'+value+' to the Redis Database '
	else:
		return 'Nothing added to Redis'

#obtaining the key-value pair from the database,to get the value associated with key foo, send in /redis/foo
@app.route("/redis/<string:key>")
def get_redis(key):
	r = connect_to_redis()
	ans = str(r.get(key), 'utf-8')
	log.info("Obtained the value of the key "+key+" from the database, namely: "+ans)
	return "The value of key "+key+" is "+ans



@app.route("/", methods=['POST'])
def post_bistro():
    return jsonify({'method': 'POST'})


@app.route("/", methods=['PUT'])
def put_bistro():
    return jsonify({'method': 'PUT'})


@app.route("/", methods=['DELETE'])
def delete_bistro():
    return jsonify({'method': 'PUT'})


if __name__=="__main__":
    app.run()




