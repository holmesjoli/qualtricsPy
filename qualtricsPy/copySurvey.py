from qualtricsPy.utils import params, endpoint
from qualtricsPy.apiVerbs import post


class copySurveyParams(params):

    def __init__(self, config):
        """
        Initializes the copy survey parameters class.
        :param config: the configuration file
        :type config: dct
        """
        params.__init__(self)

        self.surveyId = config["id"]
        self.surveyName = config["name"]
        self.endpoint = endpoint(self.dataCenter)
        self.data = {"projectName": self.surveyName}
        self.headers = {"content-type": "application/json",
                        "x-copy-source": self.surveyId,
                        "x-copy-destination": self.ownerId,
                        "X-copy-destination-owner": self.ownerId}
        self.headers.update(self.authHeader)


class copySurvey(copySurveyParams):

    def __init__(self, config):
        """
        Copys the survey and renames it
        :param config: the configuration file
        :type config: dct
        """
        copySurveyParams.__init__(self, config)
        post(self.endpoint, self.data, self.headers)
