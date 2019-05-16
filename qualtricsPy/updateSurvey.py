import requests
from qualtricsPy.utils import params, config, post, surveyEndpoint


class updateSurveyParams(params, config):

    def __init__(self):
        """
        Initializes the copy survey parameters
        """
        params.__init__(self)
        config.__init__(self)
        self.surveyId = self.updateSurvey["id"]
        self.surveyName = self.updateSurvey["name"]
        self.active = self.updateSurvey["active"]
        self.endpoint = surveyEndpoint(self.dataCenter, self.surveyId)
        self.data = {"name": self.surveyName,
                     "isActive": self.active}
        self.headers = {"content-type": "application/json"}
        self.headers.update(self.authHeader)


class updateSurvey(updateSurveyParams):

    def __init__(self):
        """
        Updates an existing survey's metadata
        """
        updateSurveyParams.__init__(self)
        post(self.endpoint, self.data, self.headers)
