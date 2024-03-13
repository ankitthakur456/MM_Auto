from pyModbusTCP.client import ModbusClient
from logger import log

IP_ADDRESS = '192.168.000.003'
PORT = 502


def conn():
    try:
        client = ModbusClient(host=IP_ADDRESS, port=PORT, unit_id=1, auto_open=True, auto_close=True, timeout=2)
        log.info(f"")
        log.info(f"connected with plc")
        return client
    except Exception as e:
        log.error(f"Error: {e}")
        return None


def read_plc():
    mb_client = conn()
    if mb_client:
        try:
            count_data = mb_client.read_holding_registers(2, 1)
            if count_data:
                return count_data
            else:
                return [None]
        except Exception as msg:
            log.error(f"Error: {msg}")
            return [None]
    return None

data = read_plc()
print(data)
