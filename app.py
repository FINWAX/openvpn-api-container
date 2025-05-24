from flask import Flask, jsonify, request

from vpn_service.config import API_PORT
from vpn_service.service.logs import logger
from vpn_service.usage.cases import provide_startapp_connection_to_openvpn, disconnect_from_openvpn, connection_info, \
    connect_to_openvpn

app = Flask(__name__)

@app.route('/api/info', methods=['GET'])
def info():
    con_inf, error = connection_info()

    if error:
        return jsonify({
            'error': error
        })

    return jsonify(con_inf)


@app.route('/api/connect', methods=['GET'])
def connect_openvpn():
    config_name = request.args.get('configName')
    if not config_name:
        return jsonify({'ok': False, 'error': 'configName is required'})

    connected, error = connect_to_openvpn(config_name)
    if error:
        return jsonify({
            'error': error
        })

    return jsonify({'ok': connected})


@app.route('/api/disconnect', methods=['GET'])
def disconnect_openvpn():
    disconnected, error = disconnect_from_openvpn()
    if error:
        return jsonify({
            'error': error
        })

    return jsonify({'ok': disconnected})

if __name__ == '__main__':
    startup_connected, startup_error = provide_startapp_connection_to_openvpn()
    logger.info(f'Startup connection: {startup_connected} ({startup_error}).')

    app.run(host='0.0.0.0', port=API_PORT)
