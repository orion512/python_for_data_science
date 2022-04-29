# python_for_data_science

A series of learning examples for python programming.

Each folder contains a different lesson.

## Preparing the Environment

### Virtual Environment
Create a new virtual environemnt
```
python -m venv venv  # The second parameter is a path to the virtual env.
```

Activate the new virtual environment
```
# Windows
.\venv\Scripts\activate

# Unix
source venv/bin/activate
```

Leaving the virtual environment
```
deactivate
```

## 1. Context Managers
Context managers a a python spcific features so we can consider them as idiomatic.

### Agenda
- What are context managers? (example 1)
- How context managers work? (example 2)
- Context manager with a DB connection (example 3)
- Implementation of context managers (example 4)

## 2. List Comprehensions
- Loops vs comprehensions (example 1)
- Simulation of loops and comprehensions (example 2)
    - comprehensions seem to perform ~15% better
- Comprehensions vs vectorised implementation (example 3)
    - vectorised implementation seems to perform ~95% better
- Filter vs comprehensions (example 4)
