|                  Race condition |                                                                                                                                                                                                 Definition |                                                                                                              Solution |
| ------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------------------: |
|                      Dirty read |                                                                                                                                   One client reads another client’s writes before they have been committed |                                                                                           Read committed and stronger |
|                     Dirty write |                                                                                                                         One client overwrites data that another client has written, but not yet committed. |                                                                                       All transaction implementations |
| Read skew (nonrepeatable reads) |                                                                                                                                  A client sees different parts of the database at different points in time |                                                                                          snapshot isolation with MVCC |
|                     lost update |                                                            Two clients concurrently perform a read-modify-write cycle. One overwrites the other’s write without incorporating its changes, so data is lost | snapshot isolation or manual lock (Atomic write operations, Explicit locking, Automatically detecting lost updates, ) |
|                      Write skew | A transaction reads something, makes a decision based on the value it saw, and writes the decision to the database. However, by the time the write is made, the premise of the decision is no longer true. |                                                                                                serializable isolation |
|                   Phantom reads |                                                                        A transaction reads objects that match some search condition. Another client makes a write that affects the results of that search. |                                                                                                    snapshot isolation |

Read committed:

1. only see data that has been committed (no dirty reads).
2. only overwrite data that has been committed (no dirty writes).

Default setting in Oracle 11g, PostgreSQL, SQL Server 2012, MemSQL, and many other databases [8]

Snapshot isolation:

- The idea is that each transaction reads from a consistent snapshot of the database.
- supported by PostgreSQL, MySQL with the InnoDB storage engine, Oracle, SQL Server, and others [23, 31, 32].
