CREATE TABLE machinists(
	uniqname VARCHAR(20) NOT NULL,
  password VARCHAR(256) NOT NULL,
	fullname VARCHAR(40) NOT NULL,
	millStatus VARCHAR(40) NOT NULL,
  latheStatus VARCHAR(40) NOT NULL,
  cncMillStatus VARCHAR(40) NOT NULL,
  cncLatheStatus VARCHAR(40) NOT NULL,
  haasStatus VARCHAR(40) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(uniqname)
);

CREATE TABLE queue(
	uniqname VARCHAR(20) NOT NULL,
  password VARCHAR(256) NOT NULL,
	fullname VARCHAR(40) NOT NULL,
	millStatus VARCHAR(40) NOT NULL,
  latheStatus VARCHAR(40) NOT NULL,
  cncMillStatus VARCHAR(40) NOT NULL,
  cncLatheStatus VARCHAR(40) NOT NULL,
  haasStatus VARCHAR(40) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(uniqname),
  FOREIGN KEY(uniqname) REFERENCES machinists(uniqname)
);

CREATE TABLE parts(
	name VARCHAR(20) NOT NULL,
	number VARCHAR(40) NOT NULL,
	leadDesigner VARCHAR(40) NOT NULL,
	leadMachinist VARCHAR(64) NOT NULL,
  designCheck VARCHAR(40) NOT NULL,
  productionCheck VARCHAR(40) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(number)
);

CREATE TABLE ops(
	name VARCHAR(20) NOT NULL,
	number VARCHAR(40) NOT NULL,
	leadDesigner VARCHAR(40) NOT NULL,
	leadMachinist VARCHAR(64) NOT NULL,
  designCheck VARCHAR(40) NOT NULL,
  productionCheck VARCHAR(40) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(number),
  FOREIGN KEY(number) REFERENCES parts(number)
);