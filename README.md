# VolleyballScript
A python script to automatically sign up for volleyball courses at Hochschulsport Hambug.

The script mimics a browser by using selenium.

Needed login details are to be stored in a json file at root level, which is not tracked in git.

### Json Format:

```json
{
	"users": [
		{
			"email": "<value>",
			"pwd": "<value>"
		}
	]
}
```

### Execution

Call the script with the appropiate command line arguments to automatically enrole in a course.

Example: ```python volleyballScript.py 3``` where 3 is the Stufe you want to go to.

Stufe options are: 1, 2a, 2b, 23, 3, Spielkurs.

## Setup

The script needs the chromedriver file for the specific OS in the same directory level.