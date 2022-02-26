/* 新增 index */
CREATE INDEX idx ON member (username, password);

/* 刪除 index */
ALTER TABLE member DROP INDEX idx;