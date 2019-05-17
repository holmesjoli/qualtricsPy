from qualtricsPy.utils import params
from qualtricsPy.apiVerbs import post
from qualtricsPy.endpoints import surveyDefinitionEndpoint


class createQuestionParams(params):

    def __init__(self, config):
        """
        Initializes the create question parameters.
        :param config: the configuration file
        :type config: dct
        """
        params.__init__(self)

        self.surveyId = config["id"]
        self.data = config["question"]
        self.endpoint = surveyDefinitionEndpoint(self.dataCenter,
                                                 self.surveyId)
        self.headers = {"accept": "application/json",
                        "content-type": "application/json"}
        self.headers.update(self.authHeader)


class createQuestion(createQuestionParams):

    def __init__(self, config):
        """
        Creates a new question in the specified survey
        :param config: the configuration file
        :type config: dct
        """
        createQuestionParams.__init__(self, config)
        post(self.endpoint, self.data, self.headers)
