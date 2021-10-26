import socket
from confluent_kafka import Consumer, Producer, KafkaError
consumerconf = {
    'bootstrap.servers': "localhost:9092,localhost:9092",
    'group.id': 'group-2',
    'auto.offset.reset': 'smallest'
}
producerconf = {
    'bootstrap.servers': "localhost:9092,localhost:9092",
    'client.id': socket.gethostname()
}

consumer = Consumer(consumerconf)
producer = Producer(producerconf)


def cbfunction(err, msg):
    if err is not None:
        print("Mesaj oluşturulurken bir hata oluştu: %s: %s" %
              (str(msg), str(err)))
    else:
        print("Mesaj oluşturuldu")


def msg_process(msg):
    print(msg.value())
    producer.produce(topic='detection3_topic',
                     value=msg.value(),
                     callback=cbfunction)
    producer.poll(1)


running = True


def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                msg_process(msg)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


def shutdown():
    running = False


# vehicle_topic is topic name
basic_consume_loop(consumer, ['vehicle_topic'])
