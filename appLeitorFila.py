import time
import json
import stomp
import appFilaConf as fila
import persistencia


class Leitor(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_error(self, frame):
        print('Erro ao ler fila: "%s"' % frame.body)

    def on_message(self, frame):

        tarefa = json.loads(frame.body)
        persistencia.salvar(tarefa)

        print('Msg "%s"' % frame.body)
   
conn = fila.obterConexao()

conn.set_listener('', Leitor(conn))

conn.subscribe(destination=fila.confFila, id=1, ack='auto')

while True:
    print('Lendo fila...')
    time.sleep(5)


conn.disconnect()