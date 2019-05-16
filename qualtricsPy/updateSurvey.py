from qualtricsPy.utils import params, surveyEndpoint
from qualtricsPy.apiVerbs import put


class updateSurveyParams(params):

    def __init__(self, config):
        """
        Initializes the copy survey parameters
        :param config: the configuration file
        :type config: dct
        """
        params.__init__(self)
        self.surveyId = config["id"]
        self.surveyName = config["name"]
        self.active = config["active"]
        self.endpoint = surveyEndpoint(self.dataCenter, self.surveyId)
        self.data = {"name": self.surveyName,
                     "isActive": self.active}
        self.headers = {"content-type": "application/json"}
        self.headers.update(self.authHeader)


class updateSurvey(updateSurveyParams):

    def __init__(self, config):
        """
        Updates an existing survey's metadata
        :param config: the configuration file
        :type config: dct
        """
        updateSurveyParams.__init__(self, config)
        put(self.endpoint, self.data, self.headers)
