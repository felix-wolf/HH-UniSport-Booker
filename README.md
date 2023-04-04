# HH-UniSport-Booker

A python script to automatically sign up for specified courses at Hochschulsport Hambug.

The script mimics a browser by using selenium.

In order to register for a new course, configure a json file named `bookings.json` as shown in the template.

The json needs the password of the user but is NOT tracked by git.

### Json Format:

```json
[
	{
		"user": {
			"email": "<email>",
			"password": "<password>"
		},
		"course": {
			"name": "<nameOfCourse>",
			"level": "<nameOfLevel>"
		},
		"timeToBook": {
			"day": "1/2/3/4/5/6/7",
			"time": "hh:mm"
		}
	}
]
```

### Execution

Ideally, the script is executed every 30 minutes as a cronjob.

Call: ```python3 main.py```

Furthermore, if you use an virtual environment for the dependencies, this is needed cronjob:

```
*/30 * * * * <pathToFolder>/volleyballScript/venv/bin/python <pathToFolder>/volleyballScript/src/main.py >> /tmp/log.txt

```

## Setup

The script needs the chromedriver file for the specific OS in the same directory level.