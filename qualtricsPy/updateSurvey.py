import requests
from qualtricsPy.utils import params, config, post


class updateSurveyParams(params, config):

    def __init__(self):
        """
        Initializes the copy survey parameters
        """
        params.__init__(self)
        config.__init__(self)
        self.surveyId = self.updateSurvey["id"]
        self.surveyName = self.surveyName["name"]
        self.endpoint = "https://{0}.qualtrics.com/API/v3/surveys/{1}"
        self.endpoint = self.endpoint.format(self.dataCenter, self.surveyId)
        self.data = {"projectName": self.surveyName}
        self.headers = {"content-type": "application/json"}
        self.headers.update(self.authHeader)


class updateSurvey(updateSurveyParams):

    def __init__(self):
        """
        Updates an existing survey's metadata
        """
        updateSurveyParams.__init__(self)
        post(self.endpoint, self.data, self.headers)
