# Cloud-Task

## Εφαρμογή Web ELK Stack

### Επισκόπηση έργου

Αυτό το έργο περιλαμβάνει την ανάπτυξη και υλοποίηση μιας ασφαλούς διαδικτυακής εφαρμογής για την πραγματοποίηση αναζητήσεων στη μηχανή Elasticsearch και την παρουσίαση των σχετικών αποτελεσμάτων. Η εφαρμογή έχει κατασκευαστεί με χρήση Python (Flask) και είναι ενσωματωμένη με μια ELK stack (Elasticsearch, Logstash, Kibana). Ο πρωταρχικός στόχος είναι να δοθεί η δυνατότητα στους χρήστες να αναζητούν δεδομένα με ασφάλεια στο Elasticsearch και να οπτικοποιούν τα αποτελέσματα μέσω μιας φιλικής προς τον χρήστη διεπαφής.

## Πίνακας περιεχομένων

- [Επισκόπηση έργου](#επισκόπηση-έργου)
- [Χαρακτηριστικά](#χαρακτηριστικά)
- [Τεχνολογίες που χρησιμοποιούνται](#τεχνολογίες-που-χρησιμοποιούνται)
- [Ρύθμιση ELK Stack](#ρύθμιση-elk-stack)
  - [Προαπαιτούμενα](#προαπαιτούμενα)
  - [Βήμα 1: Ρύθμιση της εικονικής μηχανής](#βήμα-1-ρύθμιση-της-εικονικής-μηχανής)
  - [Βήμα 2: Εγκατάσταση Docker και Docker Compose](#βήμα-2-εγκατάσταση-docker-και-docker-compose)
  - [Βήμα 3: Διαμόρφωση και ανάπτυξη της ELK Stack](#βήμα-3-διαμόρφωση-και-ανάπτυξη-της-elk-stack)
- [Ρύθμιση εφαρμογής Ιστού](#ρύθμιση-εφαρμογής-ιστού)
  - [Εγκατάσταση](#εγκατάσταση)
  - [Διαμόρφωση](#διαμόρφωση)
  - [Εκτέλεση της Εφαρμογής](#εκτέλεση-της-εφαρμογής)
- [Αντιμετώπιση προβλημάτων](#αντιμετώπιση-προβλημάτων)
- [Άδεια](#άδεια)

## Χαρακτηριστικά

- Ασφαλής αναζήτηση του Elasticsearch χρησιμοποιώντας κλειδιά API και TLS.
- Φιλική προς τον χρήστη διεπαφή ιστού για την εκτέλεση αναζητήσεων.
- Οπτικοποίηση δεδομένων τόσο μέσω του Kibana όσο και της προσαρμοσμένης διεπαφής χρήστη.
- Ενσωμάτωση με Beats για απορρόφηση δεδομένων σε πραγματικό χρόνο.

## Τεχνολογίες που χρησιμοποιούνται

- **Elasticsearch**: Για ευρετηρίαση και αναζήτηση δεδομένων.
- **Logstash**: Για επεξεργασία και προώθηση δεδομένων.
- **Kibana**: Για οπτικοποίηση δεδομένων.
- **Beats**: Για αποστολή δεδομένων.
- **Python (Flask)**: Για την εφαρμογή web.
- **Docker & Docker Compose**: Για containerization και development.
- **TLS/SSL**: Για ασφαλή επικοινωνία.

## Ρύθμιση ELK Stack

### Προαπαιτούμενα

Πριν ρυθμίσετε την ELK stack, βεβαιωθείτε ότι είναι διαθέσιμα τα ακόλουθα:

- Μια εικονική μηχανή που εκτελεί το Ubuntu Server 20.04 LTS.
- Επαρκείς πόροι (CPU, RAM, Δίσκος) για την εκτέλεση των Elasticsearch, Logstash, Kibana και Beats.
- Το Docker και το Docker Compose είναι εγκατεστημένα στο VM.

### Βήμα 1: Ρύθμιση της εικονικής μηχανής

- **Δημιουργία εικονικής μηχανής**: Ρυθμίστε μια εικονική μηχανή χρησιμοποιώντας τον πάροχο cloud που προτιμάτε ή κάποιον local hypervisor (π.χ. AWS, Azure, VirtualBox).
- **Πρόσβαση SSH**: Βεβαιωθείτε ότι το SSH έχει διαμορφωθεί για ασφαλή απομακρυσμένη πρόσβαση.

### Βήμα 2: Εγκατάσταση Docker και Docker Compose

- Ενημερώστε τη λίστα πακέτων:
  ```
  sudo apt-get update && sudo apt-get upgrade -y
  ```
- Εγκαταστήστε το Docker:
  ```
  sudo apt-get install docker.io -y
  ```
- Εγκαταστήστε το Docker Compose:
  ```
  sudo apt-get install docker-compose -y
  ```
- Επαλήθευση εγκατάστασης:
  ```
  docker --version
  docker-compose --version
  ```

### Βήμα 3: Διαμόρφωση και ανάπτυξη της Στοίβας ELK

- **Κλωνοποιήστε το αποθετήριο**:
  ```
  sudo git clone https://github.com/swimlane/elk-tls-docker.git /opt/elk-tls-docker
  cd /opt/elk-tls-docker
  ```
- **Δημιουργήστε το αρχείο .env**:
  ```
  sudo mv .env-example .env
  sudo nano .env
  ```
- **Κάντε τις απαραίτητες αλλαγές στο αρχείο .env, προσθέτωντας τον κωδικό σας**:

  ```
    ELK_VERSION=7.16.0
    ELASTIC_USERNAME=elastic
    ELASTIC_PASSWORD=some_password

    # Configuration Variables
    ELASTICSEARCH_HEAP=2g
    LOGSTASH_HEAP=1g
    PACKETBEAT_HEAP=256m
    FILEBEAT_HEAP=256m
    METRICBEAT_HEAP=256m
    XPACK_ENCRYPTION_KEY=somesuperlongstringlikethisoneMQBbtsynu4bV2uxLy

    # Self signed TLS certificates
    CA_PASSWORD=some_password
    CA_DAYS=3650
    ELASTIC_DIR=/usr/share/elasticsearch
    LOGSTASH_DIR=/usr/share/logstash
    KIBANA_DIR=/usr/share/kibana
    PACKETBEAT_DIR=/usr/share/packetbeat
    FILEBEAT_DIR=/usr/share/filebeat
    METRICBEAT_DIR=/usr/share/metricbeat

    # Letsencrypt certificates
    ## Setting STAGING to true means it will generate self-signed certificates
    ## Setting STAGING to false means it will generate letsencrypt certificates
    # STAGING=false
    STAGING=true

    # swag Configuration
    #DOMAIN=mydomain.com
    #SUBDOMAIN=kibana
    #SUBFOLDER=kibana
    #EMAIL=email@email.com
    #TIMEZONE=America/Chicago
  ```

- **Κάντε τις απαραίτητες αλλαγές στο αρχείο docker-compose.yml**:

  ```
    services:
    elasticsearch:
        container_name: elasticsearch
        hostname: elasticsearch
        image: docker.elastic.co/elasticsearch/elasticsearch:7.16.0
    #    build:
    #      context: elasticsearch/
    #      args:
    #        ELK_VERSION: ${ELK_VERSION}
        restart: unless-stopped
        environment:
        CONFIG_DIR: ${ELASTIC_DIR}/config
        ELASTIC_USERNAME: ${ELASTIC_USERNAME}
        ELASTIC_PASSWORD: ${ELASTIC_PASSWORD}
        ES_JAVA_OPTS: -Xmx${ELASTICSEARCH_HEAP} -Xms${ELASTICSEARCH_HEAP}
        bootstrap.memory_lock: "true"
        discovery.type: single-node
        volumes:
        - data:${ELASTIC_DIR}
        - ./elasticsearch/config/elasticsearch.yml:${ELASTIC_DIR}/config/elasticsearch.yml:ro
        secrets:
        - source: elasticsearch.keystore
            target: ${ELASTIC_DIR}/config/elasticsearch.keystore
        - source: ca.crt
            target: ${ELASTIC_DIR}/config/ca.crt
        - source: elasticsearch.cert
            target: ${ELASTIC_DIR}/config/elasticsearch.crt
        - source: elasticsearch.key
            target: ${ELASTIC_DIR}/config/elasticsearch.key
        ports:
        - "9200:9200"
        - "9300:9300"
        healthcheck:
        test: curl -s https://elasticsearch:9200 >/dev/null; if [[ $$? == 52 ]]; then echo 0; else echo 1; fi
        interval: 30s
        timeout: 10s
        retries: 5
        ulimits:
        memlock:
            soft: -1
            hard: -1
        nofile:
            soft: 200000
            hard: 200000
        networks:
        - elk

    kibana:
        container_name: kibana
        hostname: kibana
        image: docker.elastic.co/kibana/kibana:7.16.0
    #    build:
    #      context: kibana/
    #      args:
    #        ELK_VERSION: $ELK_VERSION
        restart: unless-stopped
        volumes:
        - ./kibana/config/kibana.yml:${KIBANA_DIR}/config/kibana.yml:ro
        environment:
        CONFIG_DIR: ${KIBANA_DIR}/config
        ELASTIC_USERNAME: ${ELASTIC_USERNAME}
        ELASTIC_PASSWORD: ${ELASTIC_PASSWORD}
        ENCRYPTION_KEY: ${XPACK_ENCRYPTION_KEY}
        KIBANA_URL: ${KIBANA_URL}
        XPACK.INFRA.ENABLED: "false"
        secrets:
        - source: ca.crt
            target: ${KIBANA_DIR}/config/ca.crt
        - source: kibana.cert
            target: ${KIBANA_DIR}/config/kibana.crt
        - source: kibana.key
            target: ${KIBANA_DIR}/config/kibana.key
        healthcheck:
        test: curl -s https://kibana:5601 >/dev/null; if [[ $$? == 52 ]]; then echo 0; else echo 1; fi
        interval: 30s
        timeout: 10s
        retries: 5
        ports:
        - "5601:5601"
        networks:
        - elk
        depends_on:
        - elasticsearch

    logstash:
        container_name: logstash
        hostname: logstash
        image: docker.elastic.co/logstash/logstash:7.16.0
    #    build:
    #      context: logstash/
    #      args:
    #        ELK_VERSION: $ELK_VERSION
        restart: unless-stopped
        volumes:
        - ./logstash/config/logstash.yml:${LOGSTASH_DIR}/config/logstash.yml
        - ./logstash/pipeline/logstash.conf:${LOGSTASH_DIR}/pipeline/logstash.conf
        - ./logstash/pipeline/metricbeat.conf:${LOGSTASH_DIR}/pipeline/metricbeat.conf
        environment:
        path.settings: null
        CONFIG_DIR: ${LOGSTASH_DIR}/config
        ELASTIC_USERNAME: ${ELASTIC_USERNAME}
        ELASTIC_PASSWORD: ${ELASTIC_PASSWORD}
        LS_JAVA_OPTS: "-Xmx${LOGSTASH_HEAP} -Xms${LOGSTASH_HEAP}"
        secrets:
        - source: ca.crt
            target: ${LOGSTASH_DIR}/config/ca.crt
        - source: logstash.cert
            target: ${LOGSTASH_DIR}/config/logstash.crt
        - source: logstash.pkcs8.key
            target: ${LOGSTASH_DIR}/config/logstash.pkcs8.key
        - source: logstash.key
            target: ${LOGSTASH_DIR}/config/logstash.key
        - source: logstash.p12
            target: ${LOGSTASH_DIR}/config/logstash.p12
        networks:
        - elk
        ports:
        - "12201:12201/udp"
        - "5044:5044"
        - "5045:5045/tcp"
        - "5046:5046"
        - "9600:9600"
        - "5000:5000/tcp"
        - "5000:5000/udp"
        depends_on:
        - elasticsearch
        - kibana

    packetbeat:
        container_name: packetbeat
        hostname: packetbeat
        user: root
        image: docker.elastic.co/beats/packetbeat:7.16.0
    #    build:
    #      context: packetbeat/
    #      args:
    #        ELK_VERSION: $ELK_VERSION
        restart: unless-stopped
        cap_add:
        - NET_ADMIN
        - NET_RAW
        command: packetbeat -e -strict.perms=false
        volumes:
        - ./packetbeat/config/packetbeat.yml:${PACKETBEAT_DIR}/packetbeat.yml:ro
        - /var/run/docker.sock:/var/run/docker.sock
        environment:
        CONFIG_DIR: ${PACKETBEAT_DIR}/config
        ELASTIC_USERNAME: ${ELASTIC_USERNAME}
        ELASTIC_PASSWORD: ${ELASTIC_PASSWORD}
        LS_JAVA_OPTS: "-Xmx${PACKETBEAT_HEAP} -Xms${PACKETBEAT_HEAP}"
        secrets:
        - source: ca.crt
        target: /etc/pki/ca-trust/source/anchors/ca.crt
        - source: packetbeat.cert
        target: ${PACKETBEAT_DIR}/config/packetbeat.crt
        - source: packetbeat.key
        target: ${PACKETBEAT_DIR}/config/packetbeat.key
        networks:
        - elk
        depends_on:
        - logstash

    metricbeat:
        container_name: metricbeat
        hostname: metricbeat
        user: root
        image: docker.elastic.co/beats/metricbeat:7.16.0
    #    build:
    #      context: metricbeat/
    #      args:
    #        ELK_VERSION: $ELK_VERSION
        restart: unless-stopped
        cap_add:
        - NET_ADMIN
        - NET_RAW
        command:
        - /bin/bash
        - -c
        - while true; do metricbeat -e; sleep 1; done
        volumes:
        - ./metricbeat/config/metricbeat.yml:${METRICBEAT_DIR}/metricbeat.yml
        - /var/run/docker.sock:/var/run/docker.sock
        environment:
        CONFIG_DIR: ${METRICBEAT_DIR}/config
        ELASTIC_USERNAME: ${ELASTIC_USERNAME}
        ELASTIC_PASSWORD: ${ELASTIC_PASSWORD}
        LS_JAVA_OPTS: "-Xmx${METRICBEAT_HEAP} -Xms${METRICBEAT_HEAP}"
        secrets:
        - source: elastic-stack-ca.p12
            target: /etc/pki/ca-trust/source/anchors/elastic-stack-ca.p12
        - source: ca.crt
            target: /etc/pki/ca-trust/source/anchors/ca.crt
        - source: metricbeat.cert
            target: ${METRICBEAT_DIR}/config/metricbeat.crt
        - source: metricbeat.key
            target: ${METRICBEAT_DIR}/config/metricbeat.key
        networks:
        - elk
        depends_on:
        - logstash
        - kibana

    filebeat:
        container_name: filebeat
        hostname: filebeat
        image: docker.elastic.co/beats/filebeat:7.16.0
    #    build:
    #      context: filebeat/
    #      args:
    #        ELK_VERSION: $ELK_VERSION
        restart: unless-stopped
        command: >
        sh -c "filebeat -e"
        volumes:
        - ./filebeat/config/filebeat.yml:${FILEBEAT_DIR}/filebeat.yml:ro
        environment:
        CONFIG_DIR: ${FILEBEAT_DIR}/config
        LS_JAVA_OPTS: "-Xmx${FILEBEAT_HEAP} -Xms${FILEBEAT_HEAP}"
        ELASTIC_USERNAME: ${ELASTIC_USERNAME}
        ELASTIC_PASSWORD: ${ELASTIC_PASSWORD}
        secrets:
        - source: ca.crt
            target: ${FILEBEAT_DIR}/config/ca.crt
        - source: filebeat.cert
            target: ${FILEBEAT_DIR}/config/filebeat.crt
        - source: filebeat.key
            target: ${FILEBEAT_DIR}/config/filebeat.key
        ports:
        - "9000:9000"
        networks:
        - elk
        depends_on:
        - logstash

    elastic-agent:
        container_name: elastic-agent
        hostname: elastic-agent
        image: docker.elastic.co/beats/elastic-agent:7.16.0
    #    build:
    #      context: elastic-agent/
    #      args:
    #        ELK_VERSION: $ELK_VERSION
        restart: unless-stopped
        environment:
        FLEET_CA: '/ca.crt'
        ELK_VERSION: ${ELK_VERSION}
        KIBANA_HOST: "https://kibana:5601"
        ELASTICSEARCH_USERNAME: ${ELASTIC_USERNAME}
        ELASTICSEARCH_PASSWORD: ${ELASTIC_PASSWORD}
        ELASTICSEARCH_HOSTS: "https://elasticsearch:9200"
        FLEET_ENROLL_INSECURE: 1
        ENROLL_FORCE: 1
        PREFLIGHT_CHECK: 1
        secrets:
        - source: ca.crt
            target: /ca.crt
        ports:
        - "2222:22"
        networks:
        - elk
        depends_on:
        - logstash

    networks:
    elk:
        driver: bridge
  ```

- **Αλλάξτε το αρχείο setup.sh**:
  ```
  cd setup
  sudo nano setup.sh
  ```
- **Αλλάξτε το αρχείο setup.sh sτην γραμμή 19**:

  https://github.com/swimlane/elk-tls-docker/issues/27

  ```
  apt-get update && apt-get install unzip openssl -y
  ```

- **Δημιουργείστε ένα Keystore για self-signed certificates**:
  ```
  sudo docker-compose -f docker-compose.setup.yml run --rm certs
  ```
- **Εκτελέστε την ELK stack**:
  ```
  sudo docker-compose up -d
  ```
- **Επαληθεύστε τις Υπηρεσίες**:
  Ελέγξτε ότι όλες οι υπηρεσίες εκτελούνται σωστά χρησιμοποιώντας:

  ```
  sudo docker-compose ps
  sudo docker-compose logs kibana
  ```

- **Δημιουργία REST API key**:

  ```
  curl -u elastic:your_password -k -X POST "https://localhost:9200/_security/api_key" -H "Content-Type: application/json" -d' { "name": "the_app_name", "role_descriptors": {"the_app_name_role" { "cluster": ["all"], "index": [{"names": ["*"], "privileges": ["all"] } ] } } }'
  ```

- **Επαλήθευση απορρόφησης δεδομένων**:
  ```
  sudo docker-compose logs kibana
  ```

## Ρύθμιση εφαρμογής Ιστού

### Εγκατάσταση

- Κλωνοποιήστε το αποθετήριο:
  ```
  git clone https://github.com/PanosM397/Cloud-Task.git
  ```
- Εγκατάσταση εξαρτήσεων:
  ```
  pip install elasticsearch
  pip install jsonlib
  pip install requests
  pip install Flask-WTF
  pip install Flask
  ```

### Διαμόρφωση

- **Ρύθμιση κλειδιού API**:
  - Βεβαιωθείτε ότι το κλειδί API του Elasticsearch είναι αποθηκευμένο σε ένα αρχείο `key.json` στον φάκελο της εφαρμογής.
- **Ρύθμιση remote ip**:
  - Εισάγετε την διεύθυνση ip του VM σας.

### Εκτέλεση της Εφαρμογής

- Ξεκινήστε την εφαρμογή Flask:
  ```
  flask run
  ```
- **Πρόσβαση στην Εφαρμογή**:
  - Ανοίξτε το πρόγραμμα περιήγησής σας και μεταβείτε στη διεύθυνση `http://localhost:5000`.

## Αντιμετώπιση προβλημάτων

- **Ζητήματα Docker**: Εάν οι υπηρεσίες Docker αποτύχουν να ξεκινήσουν, ελέγξτε την κατανομή πόρων και τα αρχεία καταγραφής υπηρεσιών χρησιμοποιώντας `sudo docker-compose logs`.
- **Ζητήματα SSL/TLS**: Βεβαιωθείτε ότι όλα τα πιστοποιητικά έχουν ρυθμιστεί σωστά και ότι οι υπηρεσίες τα αναγνωρίζουν.

## Άδεια

Αυτό το έργο αδειοδοτείται βάσει της άδειας GNU - δείτε το αρχείο `LICENSE` για λεπτομέρειες.
