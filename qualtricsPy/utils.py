import requests

from utilsPy.config import read_yaml


class config(object):

    def __init__(self):
        """
        Initiates the configuration class
        """
        config = read_yaml("config.yaml")
        self.userId = config["qualtrics"]["userId"]
        self.dataCenter = config["qualtrics"]["dataCenter"]
        self.clientId = config["qualtrics"]["client"]["id"]
        self.clientSecret = config["qualtrics"]["client"]["secret"]
        self.surveyId = config["qualtrics"]["copySurvey"]["id"]
        self.surveyName = config["qualtrics"]["copySurvey"]["name"]
        self.token = config["qualtrics"]["token"]


class tokenAuth(config):

    def __init__(self):
        """
        Initiats the token authentication header class
        """
        config.__init__(self)

        self.authHeader = {"x-api-token": self.token}


class twoFactorOauth(config):

    def __init__(self):
        """
        Returns the token for two-factor authentication from qualtrics.
        """
        config.__init__(self)

        self.endpoint = "https://{0}.qualtrics.com/oauth2/token"
        self.endpoint = self.endpoint.format(self.dataCenter)
        self.data = {"grant_type": "client_credentials"}

        self.response = requests.post(self.endpoint,
                                      auth=(self.clientId,
                                            self.clientSecret),
                                      data=self.data)

        if self.response.status_code == requests.codes.ok:
            self.accessToken = self.response.json()["access_token"]
        else:
            self.response.raise_for_status()

        self.authHeader = {"authorization": "bearer {}".format(self.accessToken)}


class params(config):

    def __init__(self):

        config.__init__(self)
        self.authHeader = twoFactorOauth().authHeader
