INSERT OR IGNORE INTO Softwares (SoftwareId, Name, DefaultDatabasePath, Link) VALUES
(1, 'BackupManager', '~\Documents\Shard\data', 'https://github.com/DennisTurco/BackupManager'),
(2, 'ReadmeMe', NULL, 'https://github.com/DennisTurco/RemindMe');

INSERT OR IGNORE INTO Operators(OperatorId, Name, Surname, Email, Password, InsertDate) VALUES
('ASDGHJF1234', 'Admin', 'Admin', 'admin@gmail.com', 'asdasd123', date());