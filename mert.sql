DROP DATABASE IF EXISTS muhely;
  CREATE DATABASE muhely;
  USE muhely;
  
  DROP TABLE IF EXISTS szgk;
  
  CREATE TABLE szgk(
      id INT, 
      tipus VARCHAR(20), 
      modell VARCHAR(20), 
      rendszam VARCHAR(15), 
      ajtok_szama INT,
      gyartas_eve DATE,
      PRIMARY KEY (id)
  );
  CREATE TABLE autótulajdonosok (
  	  special_id INT,
      szin VARCHAR(20),
      modositasok VARCHAR(5),
      szerzodes_datum DATE,
      id INT,
      PRIMARY KEY (special_id),
      FOREIGN KEY (id) REFERENCES szgk (id)
  );
  
  INSERT INTO szgk (id, tipus, modell, rendszam, ajtok_szama, gyartas_eve) VALUES(10, 'Opel', 'Corsa C', 'AAA123', 4, '2002-10-03'); 
  INSERT INTO szgk (id, tipus, modell, rendszam, ajtok_szama, gyartas_eve) VALUES(11, 'Ford', 'Rascla 99', 'BBB456', 4, '2012-01-26'); 
  INSERT INTO szgk (id, tipus, modell, rendszam, ajtok_szama, gyartas_eve) VALUES(12, 'Opel', 'Corsa B Alpha', 'CCC789', 2, '2000-05-06'); 
  INSERT INTO szgk (id, tipus, modell, rendszam, ajtok_szama, gyartas_eve) VALUES(13, 'Volga', 'Tennis Ball 46 D', 'DDD124', 4, '2022-09-19'); 
  
  INSERT INTO autótulajdonosok (special_id, szin, modositasok, szerzodes_datum, id) VALUES(1774435, 'Pírós','False','2002-11-11',10);
  INSERT INTO autótulajdonosok (special_id, szin, modositasok, szerzodes_datum, id) VALUES(1777957, 'Szürke','True','2012-06-09',11);
  INSERT INTO autótulajdonosok (special_id, szin, modositasok, szerzodes_datum, id) VALUES(1770149, 'Fehér','False','2000-05-11',12);
  INSERT INTO autótulajdonosok (special_id, szin, modositasok, szerzodes_datum, id) VALUES(1770905, 'Pírós','True','2022-09-24',13);