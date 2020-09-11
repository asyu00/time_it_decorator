# time_it_decorator


- Usage
  ```
  from .decorator import time_it
  
  
  @time_it
  def my_func_with_return():
    # some intensive stuff
    do_my_stuff = 'hi'
    return do_my_stuff
  
  print(my_func_with_return())
  > Start to time my_func_with_return: 2020-09-11 04:57:07.469117'
  > my_func_with_return executed: 2020-09-11 04:57:07.469155'
  > Elapsed Time for my_func_with_return: 0:00:00.000038
  > hi
  
  
  def my_func_no_return():
    # some intensive stuff
    do_my_stuff = 'hi'
    
  my_func_no_return()
  > Start to time my_func_no_return: 2020-09-11 04:57:07.469117'
  > my_func_no_return executed: 2020-09-11 04:57:07.469155'
  > Elapsed Time for my_func_no_return: 0:00:00.000038
  ```
  
