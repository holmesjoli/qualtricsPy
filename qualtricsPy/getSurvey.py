from qualtricsPy.utils import params, config, \
    get, surveyEndpoint


class getSurveyParams(params, config):

    def __init__(self):
        """
        """
        params.__init__(self)
        config.__init__(self)
        self.surveyId = self.getSurvey["id"]
        self.endpoint = surveyEndpoint(self.dataCenter, self.surveyId)
        self.headers = self.authHeader


class getSurvey(getSurveyParams):

    def __init__(self):
        """
        """
        getSurveyParams.__init__(self)
        get(self.endpoint, self.headers)
