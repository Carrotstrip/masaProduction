CREATE TABLE machinists(
	uniqname VARCHAR(8) NOT NULL,
  password VARCHAR(256) NOT NULL,
	fullname VARCHAR(40) NOT NULL,
	profilePic VARCHAR(256),
	millStatus VARCHAR(40),
  latheStatus VARCHAR(40),
  cncMillStatus VARCHAR(40),
  cncLatheStatus VARCHAR(40),
  haasStatus VARCHAR(40),
	available VARCHAR(40),
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(uniqname)
);

CREATE TABLE parts(
	name VARCHAR(20) NOT NULL,
	number VARCHAR(40) NOT NULL,
	designer VARCHAR(40) NOT NULL,
  machinist VARCHAR(64),
  designCheck VARCHAR(40),
  productionCheck VARCHAR(40),
	status VARCHAR(40),
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(number)
);

CREATE TABLE ops(
	name VARCHAR(128) NOT NULL,
	number VARCHAR(20) NOT NULL,
	designer VARCHAR(40) NOT NULL,
	machinist VARCHAR(64),
	status VARCHAR(40),
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(number),
  FOREIGN KEY(number) REFERENCES parts(number)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

CREATE TABLE inventory(
	id VARCHAR(40) NOT NULL,
	type VARCHAR(40) NOT NULL,
  length VARCHAR(64),
	diameter VARCHAR(64),
	area VARCHAR(64),
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(number)
);