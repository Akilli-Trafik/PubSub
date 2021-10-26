import socket
import json
from confluent_kafka import Producer

conf = {
    'bootstrap.servers': "localhost:9092,localhost:9092",
    'client.id': socket.gethostname()
}

producer = Producer(conf)


def cbfunction(err, msg):
    if err is not None:
        print("Mesaj oluşturulurken bir hata oluştu: %s: %s" %
              (str(msg), str(err)))
    else:
        print("Mesaj oluşturuldu")


# json objesi olarak mesajı oluşturuyoruz
jsonObj = {
    "message": "Sonunda mesajı database'e yollayabiliyoz."
}
# json objesini json string'e çeviriyoruz.
jsonStr = json.dumps(jsonObj)

# vehicle_topic'e mesajı yolluyoruz.
producer.produce(topic="vehicle_topic",
                 value=jsonStr,
                 callback=cbfunction)
producer.poll(1)
