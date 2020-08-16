Source code from MIT 6.824 Distributed system

# Goroutines, closures
- goroutines are lightweight threads, run concurrently with each other
    - program terminates when main goroutine exits
- closures: identifier capture, binding gotchas
    - closure.go: go has first-class functions, combine nicely with goroutines.
      has access to variables in the enclosing scope.
    - loop.go: pattern to spawn goroutines in a loop
    - bad.go: illustrates a common bug: i references outer i, which has been
      mutated (run multiple times, see different results)

# Concurrency primitives
* Time
    - sleep.go: time.Now, time.Sleep
    - sleep-cancel.go: don't write infinite loops; in labs, rf.killed()

* Mutexes
    - bad.go
    - basic.go: basic usage
        - defer, semantics
    - per-field.go: locks protect invariants, not "locks protect access to shared data"
        - critical section: temporarily break invariants, restore them before
      unlock, so nobody observes in-progress updates
        - lock: ensure atomicity of block of code
        - racing audits and transfers
    - bank.go

* Condition variables
    - use case; wait, signal, broadcast
    - vote-count-1.go ... vote-count-4.go
    - cond.txt, how to avoid bugs
        - lock around use
        - check condition in loop

* Channels
    - queue-like synchronization primitive
    - producer-consumer.go
    - wait for N things
    - not good for
        - kicking another goroutine, that may or may not be waiting
    - unbuffered.go: default, synchronous!
    - deadlock.go
    - I personally avoid channels for the most part and program with shared memory (mutexes and condvars) instead
