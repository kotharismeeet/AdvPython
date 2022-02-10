# AdvPython

## [Itertools](https://www.youtube.com/watch?v=Qu3dThVy6KQ)
1. count ``` itertools.count(start arg, step arg)```
2. cycle ``` itertools.cycle()```
3. repeat ```itertools.repeat()```
4. starmap ```itertools.starmap(func for eg. pow, [(0,2),(1,1),(2,2)]```
5. combinations ```itertools.combination(list, k)```
6. combinations_with_repeat (permutations) ```itertools.combination_with_replacement(list,k)```
7. chain
8. isslice ```itertools.isslice(range(10),start,end)```
9. selectors ```itertools.selectors(list,boolean_list)```

## Clean Code using [virtualenv](https://drive.google.com/file/d/1mDxSIwOwrXuMxydZ_huK8jiJJl4eQixG/view?usp=sharing) in python

1. How to install pip
```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```
```python3 get-pip.py```
2. Install virtualEnv
```pip install virtualenv```
3. Create VirtualEnv
```virtualenv env```
4. Activate VirtualEnv
```. env\bin\activate```

## [Event Loops](https://www.youtube.com/watch?v=8zKuNo4ay8E) in [python](https://www.youtube.com/watch?v=t5Bo1Je9EmE&t=873s)

Why do we need Callback Queue?
```
print('Starts')

def fun():
  sleep(5)
  print('Timeout')
 
print('End')
```

```
import asyncio

async def main():
  print('Searce')
  task= asyncio.create_task((foo('text'))
  awit asyncio.sleep(.5)
  print('finished')
  
 async def foo(text):
  print(text)
  await asyncio.sleep(10)
  
 asyncio.run(main())

```

## Setting up ![](DockerFile) config for django projects
