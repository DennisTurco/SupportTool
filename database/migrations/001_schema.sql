PRAGMA foreign_keys = off;

CREATE TABLE IF NOT EXISTS Configurations (
  Code TEXT PRIMARY KEY,
  Value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Operators (
  OperatorId TEXT PRIMARY KEY NOT NULL,
  Name TEXT NOT NULL,
  Surname TEXT NOT NULL,
  Email TEXT NOT NULL,
  Password TEXT NOT NULL,
  InsertDate INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Softwares (
  SoftwareId INTEGER PRIMARY KEY,
  Name TEXT UNIQUE NOT NULL,
  DefaultDatabasePath TEXT,
  Link TEXT
);

CREATE TABLE IF NOT EXISTS SupportActions (
  SupportActionId INTEGER PRIMARY KEY AUTOINCREMENT,
  OperatorId TEXT,
  SoftwareId INTEGER,
  ActionType INTEGER NOT NULL, -- [note: "enum del tipo -> EXTEND_SUBSCRIPTION, CREATE_SUBSCRIPTION, FORCE_EXPIRE"]
  StartDate INTEGER NOT NULL,
  EndDate INTEGER NOT NULL,
  InsertDate INTEGER NOT NULL,
  Notes TEXT,
  FOREIGN KEY(OperatorId) REFERENCES Operators(OperatorId),
  FOREIGN KEY(SoftwareId) REFERENCES Softwares(SoftwareId)
);

PRAGMA foreign_keys = on;
