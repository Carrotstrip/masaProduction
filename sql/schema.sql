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
	queuePosition VARCHAR(40),
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(uniqname)
);

CREATE TABLE parts(
	id integer NOT NULL,
	name VARCHAR(40) NOT NULL,
	number VARCHAR(20) NOT NULL,
	deadline DATE,
	designer VARCHAR(40) NOT NULL,
  machinist VARCHAR(64),
	cadModel VARCHAR(64),
	drawing VARCHAR(64),
  designCheck VARCHAR(40),
  productionCheck VARCHAR(40),
	status VARCHAR(40),
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(id)
);

CREATE TABLE revs(
	partId integer NOT NULL,
	id VARCHAR(20) NOT NULL,
	name VARCHAR(40) NOT NULL,
	number VARCHAR(20) NOT NULL,
	designer VARCHAR(40) NOT NULL,
	machinist VARCHAR(64),
	status VARCHAR(40),
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(id),
  FOREIGN KEY(partId) REFERENCES parts(id)
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
	PRIMARY KEY(id)
);