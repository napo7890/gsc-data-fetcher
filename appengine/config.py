from datetime import datetime, timedelta
import pytz

site_list = {'site': 'site_url'}

# Since GCS data is dated, specify the offset from today.
OFFSET_DATE = 4
# Set Timezone ('US/Eastern', 'US/Central', 'US/Pacific', 'Europe/London')
GSC_TIMEZONE = 'US/Pacific'

END_DATE = (datetime.now(pytz.timezone(GSC_TIMEZONE)) - timedelta(days=OFFSET_DATE)).strftime(
   "%Y-%m-%d")  # Returns the GCS format date based on OFFSET_DATE

START_DATE = END_DATE

OAUTH_SCOPE = ('https://www.googleapis.com/auth/webmasters.readonly', 'https://www.googleapis.com/auth/webmasters')

# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

CLIENT_SECRET_JSON = 'YOUR_CLIENT_SECRET.json'

GSC_QUERY_DATE = {
    "startDate": START_DATE,
    "endDate": END_DATE,
    "searchType": "web",
    "dimensions": [
        "date"
    ],
    "rowLimit": 5000
}

GSC_QUERY_PAGE_DATE = {
    "startDate": START_DATE,
    "endDate": END_DATE,
    "searchType": "web",
    "dimensions": [
        "page",
        "date"
    ],
    "rowLimit": 5000
}

GSC_QUERY_QUERY_DATE = {
    "startDate": START_DATE,
    "endDate": END_DATE,
    "searchType": "web",
    "dimensions": [
        "query",
        "date"
    ],
    "rowLimit": 5000
}

GSC_QUERY_DEVICE = {
    "startDate": START_DATE,
    "endDate": END_DATE,
    "searchType": "web",
    "dimensions": [
        "device"
    ],
    "rowLimit": 5000
}

GSC_QUERY_QUERY_DATE_PAGE = {
    "startDate": START_DATE,
    "endDate": END_DATE,
    "searchType": "web",
    "dimensions": [
        "query",
        "date",
        "page"
    ],
    "rowLimit": 5000
}
