from qualtricsPy.utils import params
from qualtricsPy.apiVerbs import post
from qualtricsPy.endpoints import surveyDefinitionEndpoint


class createBlockParams(params):

    def __init__(self, config):
        """
        Initializes the create block parameters class.
        :param config: the configuration file
        :type config: dct
        """
        params.__init__(self)

        self.surveyId = config["id"]
        self.data = config["block"]
        self.endpoint = "{}{}".format(surveyDefinitionEndpoint(self.dataCenter,
                                                               self.surveyId),
                                      "/blocks")
        self.headers = {"content-type": "application/json"}
        self.headers.update(self.authHeader)


class createBlock(createBlockParams):

    def __init__(self, config):
        """
        Creates a new block in the specified survey
        :param config: the configuration file
        :type config: dct
        """
        createBlockParams.__init__(self, config)
        post(self.endpoint, self.data, self.headers)
