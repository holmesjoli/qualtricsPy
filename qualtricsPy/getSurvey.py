from qualtricsPy.utils import params, config, \
     surveyEndpoint
from qualtricsPy.apiVerbs import get


class getSurveyParams(params, config):

    def __init__(self):
        """
        Initializes the get survey parameters class.
        """
        params.__init__(self)
        config.__init__(self)
        self.surveyId = self.getSurvey["id"]
        self.endpoint = surveyEndpoint(self.dataCenter, self.surveyId)
        self.headers = self.authHeader


class getSurvey(getSurveyParams):

    def __init__(self):
        """
        Returns attributes about the specified survey.
        """
        getSurveyParams.__init__(self)
        get(self.endpoint, self.headers)
