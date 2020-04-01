CREATE TABLE binaries (
    id INTEGER,
    sha256 TEXT,
    PRIMARY KEY (id)
);

CREATE UNIQUE INDEX ndx__binary__sha256 ON binaries (
    sha256
);