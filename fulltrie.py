import os
from flask import Flask, jsonify
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


app = Flask(__name__)


rpc_user = os.environ['LBRYCRD_RPC_USER']
rpc_password = os.environ['LBRYCRD_RPC_PASSWORD']
rpc_port = os.environ['LBRYCRD_RPC_PORT']
rpc_url = os.environ['LBRYCRD_RPC_URL']
rpc_conn_string = "http://%s:%s@%s:%s" % (rpc_user, rpc_password, rpc_url, str(rpc_port))


@app.route('/')
def getfulltrie():
    conn = AuthServiceProxy(rpc_conn_string)
    r = conn.getclaimsintrie()
    result = {'result': r}
    return jsonify(**result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
