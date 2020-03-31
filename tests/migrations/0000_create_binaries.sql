CREATE TABLE binary (
    id INTEGER PRIMARY KEY ASC,
    sha256 TEXT
);

CREATE UNIQUE INDEX ndx__binary__sha256 ON binary(
    sha256
);