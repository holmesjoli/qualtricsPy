import requests
from qualtricsPy.utils import params


class copySurvey(params):

    def __init__(self):
        """
        Copys the survey and renames it
        """
        params.__init__(self)
        self.data = {"projectName": self.surveyName}
        self.headers = {"content-type": "application/json",
                        "x-copy-source": self.surveyId,
                        "x-copy-destination": self.userId,
                        "X-copy-destination-owner": self.userId}

        self.headers.update(self.authHeader)

        self.endpoint = "https://{0}.qualtrics.com/API/v3/surveys/"
        self.endpoint = self.endpoint.format(self.dataCenter)
        self.response = requests.post(url=self.endpoint,
                                      json=self.data,
                                      headers=self.headers)

        if self.response.status_code == requests.codes.ok:
            pass
        else:
            self.response.raise_for_status()
