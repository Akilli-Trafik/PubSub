# PUB-SUB

kafka kurulumu için yml dosyası => https://github.com/confluentinc/cp-all-in-one/blob/6.2.1-post/cp-all-in-one/docker-compose.yml
dosyayı indirdikten sonra aynı klasörün içinde "docker-compose up -d" komutu çalıştırılmalı.

- mongoDB database yetkisi verildi maillerinize gelmiş olması lazım.

- localhost:9092 arayüzünden Topics kısmından "vehicle_topic", "detection1_topic", "detection2_topic", "detection3_topic" oluştur.
- docker-hub connector cli'ye 'confluent-hub install mongodb/kafka-connect-mongodb:1.6.1' koduyla mongoDB connector'ı yükle. (ilgili link: https://www.confluent.io/hub/mongodb/kafka-connect-mongodb)
- https://www.youtube.com/watch?v=_6NuTTQdDn4 videosunda gösterildiği gibi connectorları oluştur.
- daha sonra consumerları çalıştır "python consumerismi.py"
- daha sonra mesaj produce etmek için "python producerismi.py" kodunu çalıştır mesajı consumerlar alıp detection topiclere atacak oradan mongoDB connectorları da DB'ye
yükleyecek.
