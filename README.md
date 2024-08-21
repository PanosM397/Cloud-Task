# Cloud-Task

## Εφαρμογή Web ELK Stack

### Επισκόπηση έργου

Αυτό το έργο περιλαμβάνει την ανάπτυξη και υλοποίηση μιας ασφαλούς διαδικτυακής εφαρμογής για την πραγματοποίηση αναζητήσεων στη μηχανή Elasticsearch και την παρουσίαση των σχετικών αποτελεσμάτων. Η εφαρμογή έχει κατασκευαστεί με χρήση Python (Flask) και είναι ενσωματωμένη με μια στοίβα ELK (Elasticsearch, Logstash, Kibana). Ο πρωταρχικός στόχος είναι να δοθεί η δυνατότητα στους χρήστες να αναζητούν δεδομένα με ασφάλεια στο Elasticsearch και να οπτικοποιούν τα αποτελέσματα μέσω μιας φιλικής προς τον χρήστη διεπαφής.

## Πίνακας περιεχομένων

- [Επισκόπηση έργου](#επισκόπηση-έργου)
- [Χαρακτηριστικά](#χαρακτηριστικά)
- [Τεχνολογίες που χρησιμοποιούνται](#τεχνολογίες-που-χρησιμοποιούνται)
- [Ρύθμιση στοίβας ELK](#ρύθμιση-στοίβας-elk)
  - [Προαπαιτούμενα](#προαπαιτούμενα)
  - [Βήμα 1: Ρύθμιση της εικονικής μηχανής](#βήμα-1-ρύθμιση-της-εικονικής-μηχανής)
  - [Βήμα 2: Εγκατάσταση Docker και Docker Compose](#βήμα-2-εγκατάσταση-docker-και-docker-compose)
  - [Βήμα 3: Διαμόρφωση και ανάπτυξη της Στοίβας ELK](#βήμα-3-διαμόρφωση-και-ανάπτυξη-της-στοίβας-elk)
  - [Βήμα 4: Ρύθμιση TLS για ασφαλή επικοινωνία](#βήμα-4-ρύθμιση-tls-για-ασφαλή-επικοινωνία)
  - [Βήμα 5: Ενσωμάτωση Beats για απορρόφηση δεδομένων](#βήμα-5-ενσωμάτωση-beats-για-απορρόφηση-δεδομένων)
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
- **Docker & Docker Compose**: Για κοντέινερ και ανάπτυξη.
- **TLS/SSL**: Για ασφαλή επικοινωνία.

## Ρύθμιση στοίβας ELK

### Προαπαιτούμενα

Πριν ρυθμίσετε τη στοίβα ELK, βεβαιωθείτε ότι είναι διαθέσιμα τα ακόλουθα:

- Μια εικονική μηχανή που εκτελεί το Ubuntu Server 18.04 LTS.
- Επαρκείς πόροι (CPU, RAM, Δίσκος) για την εκτέλεση των Elasticsearch, Logstash, Kibana και Beats.
- Το Docker και το Docker Compose είναι εγκατεστημένα στο VM.

### Βήμα 1: Ρύθμιση της εικονικής μηχανής

- **Δημιουργία εικονικής μηχανής**: Ρυθμίστε μια εικονική μηχανή χρησιμοποιώντας τον πάροχο cloud που προτιμάτε ή τον local hypervisor (π.χ. AWS, Azure, VirtualBox).
- **Πρόσβαση SSH**: Βεβαιωθείτε ότι το SSH έχει διαμορφωθεί για ασφαλή απομακρυσμένη πρόσβαση.

### Βήμα 2: Εγκατάσταση Docker και Docker Compose

- Ενημερώστε τη λίστα πακέτων:
  ```
  sudo apt-get ενημέρωση
  ```
- Εγκαταστήστε το Docker:
  ```
  sudo apt-get install -y docker.io
  ```
- Εγκαταστήστε το Docker Compose:
  ```
  sudo apt-get install -y docker-compose
  ```
- Επαλήθευση εγκατάστασης:
  ```
  docker --έκδοση
  docker-compose --έκδοση
  ```

### Βήμα 3: Διαμόρφωση και ανάπτυξη της Στοίβας ELK

- **Δημιουργήστε ένα αρχείο σύνθεσης Docker**:
  - Δημιουργήστε ένα αρχείο `docker-compose.yml` για να ορίσετε τις υπηρεσίες για το Elasticsearch, το Logstash και το Kibana.
- **Εκτελέστε τη Στοίβα ELK**:
  ```
  docker-compose up -d
  ```
- **Επαληθεύστε τις Υπηρεσίες**:
  - Ελέγξτε ότι όλες οι υπηρεσίες εκτελούνται σωστά χρησιμοποιώντας:
  ```
  docker-compose ps
  ```

### Βήμα 4: Ρύθμιση TLS για ασφαλή επικοινωνία

- **Δημιουργία πιστοποιητικών**:
  - Χρησιμοποιήστε το εργαλείο Elasticsearch `certutil` για να δημιουργήσετε πιστοποιητικά SSL.
- **Διαμόρφωση TLS**:
  - Τροποποιήστε τα αρχεία `elasticsearch.yml` και `kibana.yml` για να συμπεριλάβετε τις διαδρομές προς τα πιστοποιητικά SSL.
- **Επανεκκινήστε τις Υπηρεσίες**:
  ```
  docker-compose restart
  ```

### Βήμα 5: Ενσωμάτωση Beats για απορρόφηση δεδομένων

- **Εγκατάσταση και διαμόρφωση Beats**:
  - Εγκαταστήστε τα Filebeat και Auditbeat στο VM και διαμορφώστε τα ώστε να στέλνουν δεδομένα στο Logstash ή απευθείας στο Elasticsearch.
- **Έναρξη Beats**:
  ```
  sudo service filebeat start
  sudo service auditbeat start
  ```
- **Επαλήθευση απορρόφησης δεδομένων**:
  - Χρησιμοποιήστε το Kibana για να επαληθεύσετε ότι τα δεδομένα από το Beats απορροφώνται σωστά.

## Ρύθμιση εφαρμογής Ιστού

### Εγκατάσταση

- Κλωνοποιήστε το αποθετήριο:
  ```
  git clone https://github.com/[YourGitHubUsername]/elk-web-app.git
  cd elk-web-app
  ```
- Εγκατάσταση εξαρτήσεων:
  ```
  pip install -r requirements.txt
  ```

### Διαμόρφωση

- **Ρύθμιση κλειδιού API**:
  - Βεβαιωθείτε ότι το κλειδί API του Elasticsearch είναι αποθηκευμένο σε ένα αρχείο `key.json` στον ριζικό κατάλογο.
- **Μεταβλητές Περιβάλλοντος**:
  - Ρυθμίστε τις απαραίτητες μεταβλητές περιβάλλοντος (π.χ. `FLASK_APP`, `FLASK_ENV`).

### Εκτέλεση της Εφαρμογής

- Ξεκινήστε την εφαρμογή Flask:
  ```
  flask run
  ```
- **Πρόσβαση στην Εφαρμογή**:
  - Ανοίξτε το πρόγραμμα περιήγησής σας και μεταβείτε στη διεύθυνση `http://localhost:5000`.

## Αντιμετώπιση προβλημάτων

- **Ζητήματα Docker**: Εάν οι υπηρεσίες Docker αποτύχουν να ξεκινήσουν, ελέγξτε την κατανομή πόρων και τα αρχεία καταγραφής υπηρεσιών χρησιμοποιώντας `docker-compose logs`.
- **Ζητήματα SSL/TLS**: Βεβαιωθείτε ότι όλα τα πιστοποιητικά έχουν ρυθμιστεί σωστά και ότι οι υπηρεσίες τα αναγνωρίζουν.
- **Απορρόφηση δεδομένων Beats**: Βεβαιωθείτε ότι τα αρχεία διαμόρφωσης Beats είναι σωστά και ότι το Elasticsearch ή το Logstash είναι προσβάσιμο.

## Άδεια

Αυτό το έργο αδειοδοτείται βάσει της άδειας MIT - δείτε το αρχείο `LICENSE` για λεπτομέρειες.
