  DROP DATABASE IF EXISTS kutyamenhely;
  CREATE DATABASE kutyamenhely;
  USE kutyamenhely;
  
   DROP TABLE IF EXISTS szgkla;
   DROP TABLE IF EXISTS kutya_gazdájának;
  
  CREATE TABLE szgkla(
      id INT(11) PRIMARY KEY AUTO_INCREMENT, 
      nev VARCHAR(20) NOT NULL,
      kor INT(11) CHECK (kor < 30),
      nem VARCHAR(15) DEFAULT "kan",
      megjegyzes VARCHAR(500)
  );
  CREATE TABLE kutya_gazdájának (
  	  special_id INT,
      nev VARCHAR(20),
      kor INT(11),
      id INT(11) PRIMARY KEY AUTO_INCREMENT,
      FOREIGN KEY (id) REFERENCES szgkla (id)
  );
  
  INSERT INTO szgkla (id, nev, kor, nem, megjegyzes) VALUES(1, 'Opal', 1, 'nöstény', 'KUTYA'); 
  INSERT INTO szgkla (id, nev, kor, nem, megjegyzes) VALUES(2, 'gyere ide takarogy', 6, 'kan', 'Megjegyzés mert'); 
  INSERT INTO szgkla (id, nev, kor, nem, megjegyzes) VALUES(3, 'Csóva', 9, 'kan', 'dogo dogo dogo dogo'); 
  INSERT INTO szgkla (id, nev, kor, nem, megjegyzes) VALUES(4, 'Csirke', 29, 'nöszény', 'egy jó kutya'); 
  
  INSERT INTO kutya_gazdájának (special_id, nev, kor, id) VALUES(1774435, 'Tiszta Gábor', 22,1);
  INSERT INTO kutya_gazdájának (special_id, nev, kor, id) VALUES(1777957, 'Margit Shubejtun',10 ,2);
  INSERT INTO kutya_gazdájának (special_id, nev, kor, id) VALUES(1770149, 'Kovács Pityu',45 ,3);
  INSERT INTO kutya_gazdájának (special_id, nev, kor, id) VALUES(1770905, 'Elegáns Margarit',26 ,4);