from datetime import datetime
import pytz


def convertToParisTZ(date: datetime) -> datetime:
    # Import Paris Timezone
    paris_tz = pytz.timezone('Europe/Paris')
    # Convert date/time and return in Paris time
    return date.astimezone(paris_tz)