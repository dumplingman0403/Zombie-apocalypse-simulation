# Zombie apocalypse simulation via Moore neighborhood

## Introduction
### Infections rules
- 1. Infected people will turns into zombies with different levels Lv1, Lv2, Lv3. The higher level is, the lower probability will be of being able to cure them. The highest level, level 3, are considered incurable.
- 2. Antidote can only be developed after a period of time (threshold).
- 3. The person who has been injected the antidote will not be infected again (Immunity).
- 4. The antidote will be dropped to survivors at a random area by U.S Air Force.


### Scienarios 
- 1. The antidote will continue to drop to survivors randomly over the total uninfected area by the U.S Air Force.
- 2. The antidote will be dropped to survivors one time in a specific area by the U.S. Air Force. From there the antidote will spread among the other survivors, preventing them from becoming zombies, as well as potentially curing the level one and two zombies. Previously mentioned, level 3 zombies can not be cured. 

## Demo

### Senario 1
<img src='Image/senario_1.gif' alt = 'senario1_demo'>

### Senario 2
<img src='Image/senario_2.gif' alt = 'senario2_demo'>

## How to run 

Run Scenario 1

```bash
python3 Scenario 1.py
```
Run Scenario 2

```bash
python3 Scenario 2.py
```

