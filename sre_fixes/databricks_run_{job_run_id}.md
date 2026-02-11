## Databricks Job Failure Report

### Run Information

* **Job ID:** 899259752937932
* **Job Run ID:** 55170935381912
* **Task Run ID:** 681232651011705

### Error Details

```
ZeroDivisionError: division by zero
```

### Error Traceback

```
--------------------------------------------------------------------------
ZeroDivisionError                           Traceback (most recent call last)
File <command-7649400096761122>, line 41
    main()

File <command-7649400096761122>, line 35, in main()
    output = process_data(data)

File <command-7649400096761122>, line 27, in process_data(data)
    result.append(x / 0)   # ❌ Bug

ZeroDivisionError: division by zero
```
