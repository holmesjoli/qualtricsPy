from qualtricsPy.utils import params, surveyEndpoint
from qualtricsPy.apiVerbs import get


class getSurveyParams(params):

    def __init__(self, config):
        """
        Initializes the get survey parameters class.
        :param config: the configuration file
        :type config: dct
        """
        params.__init__(self)

        self.surveyId = config["id"]
        self.endpoint = surveyEndpoint(self.dataCenter, self.surveyId)
        self.headers = self.authHeader


class getSurvey(getSurveyParams):

    def __init__(self, config):
        """
        Returns attributes about the specified survey.
        :param config: the configuration file
        :type config: dct
        """
        getSurveyParams.__init__(self, config)
        get(self.endpoint, self.headers)
