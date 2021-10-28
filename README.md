# PUB-SUB

kafka kurulumu için yml dosyası => https://github.com/confluentinc/cp-all-in-one/blob/6.2.1-post/cp-all-in-one/docker-compose.yml
dosyayı indirdikten sonra aynı klasörün içinde "docker-compose up -d" komutu çalıştırılmalı.

- pythonda indirilmesi gereken paketler confluent-kafka, pymongo.
- mongoDB database yetkisi verildi maillerinize gelmiş olması lazım.

- localhost:9021 arayüzünden Topics kısmından "vehicle_topic", "detection1_topic", "detection2_topic", "detection3_topic" oluştur.
- docker-hub connector cli'ye 'confluent-hub install mongodb/kafka-connect-mongodb:1.6.1' koduyla mongoDB connector'ı yükle. (ilgili link: https://www.confluent.io/hub/mongodb/kafka-connect-mongodb) yükledikten sonra gözükmesi için container'ın kapatılıp açılması lazım bende öyle oldu.
- connectorları oluştururken database ismi olarak Violation, violation1_topic için collection violation1,  violation2_topic için collection violation2,  violation3_topic için collection violation3 olmalı.
- org.apache.kafka.connect.storage.StringConverter
- https://www.youtube.com/watch?v=_6NuTTQdDn4 videosunda gösterildiği gibi connectorları oluştur.
- daha sonra consumerları çalıştır "python consumerismi.py"
- daha sonra mesaj produce etmek için "python producerismi.py" kodunu çalıştır mesajı consumerlar alıp detection topiclere atacak oradan mongoDB connectorları da DB'ye
yükleyecek.
