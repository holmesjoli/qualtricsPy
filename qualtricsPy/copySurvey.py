from qualtricsPy.utils import params, config, post, endpoint


class copySurveyParams(params, config):

    def __init__(self):
        """
        Initializes the copy survey parameters
        """
        params.__init__(self)
        config.__init__(self)
        self.surveyId = self.copySurvey["id"]
        self.surveyName = self.copySurvey["name"]
        self.endpoint = endpoint(self.dataCenter)
        self.data = {"projectName": self.surveyName}
        self.headers = {"content-type": "application/json",
                        "x-copy-source": self.surveyId,
                        "x-copy-destination": self.ownerId,
                        "X-copy-destination-owner": self.ownerId}
        self.headers.update(self.authHeader)


class copySurvey(copySurveyParams):

    def __init__(self):
        """
        Copys the survey and renames it
        """
        copySurveyParams.__init__(self)
        post(self.endpoint, self.data, self.headers)
