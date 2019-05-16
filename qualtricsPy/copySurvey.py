import requests
from qualtricsPy.utils import params, config


class copySurveyParams(config):

    def __init__(self):
        """
        Initializes the copy survey parameters
        """
        params.__init__(self)
        config.__init__(self)
        self.surveyId = self.copySurvey["id"]
        self.surveyName = self.copySurvey["name"]
        self.endpoint = "https://{0}.qualtrics.com/API/v3/surveys/"
        self.endpoint = self.endpoint.format(self.dataCenter)
        self.data = {"projectName": self.surveyName}
        self.headers = {"content-type": "application/json",
                        "x-copy-source": self.surveyId,
                        "x-copy-destination": self.userId,
                        "X-copy-destination-owner": self.userId}
        self.headers.update(self.authHeader)


class copySurvey(params, copySurveyParams):

    def __init__(self):
        """
        Copys the survey and renames it
        """
        copySurveyParams.__init__(self)

        self.response = requests.post(url=self.endpoint,
                                      json=self.data,
                                      headers=self.headers)

        if self.response.status_code == requests.codes.ok:
            pass
        else:
            self.response.raise_for_status()
