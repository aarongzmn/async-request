This is a demo that shows how asynchronous requests can be done in python. This significantly speeds up API request because the program does not have to wait for each response before moving onto the next step.

I tested synchronous vs asynchronous API request.
My test involved doing 25 API calls with each method.

sync.py took 15.84 seconds to complete.

async.py took 1.04 seconds to complete.