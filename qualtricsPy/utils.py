import requests

from utilsPy.config import read_yaml


class config(object):

    def __init__(self):
        """
        Initiates the configuration class
        """
        self.config = read_yaml("config.yaml")
        self.copySurvey = self.config["copySurvey"]
        self.addQuestion = self.config["addQuestion"]


class credentials(object):

    def __init__(self):
        """
        Initiates the credential configuration class.
        """
        cred = read_yaml("qualtricsCredentials.yaml")
        self.userId = cred["userId"]
        self.dataCenter = cred["dataCenter"]
        self.clientId = cred["client"]["id"]
        self.clientSecret = cred["client"]["secret"]
        self.token = cred["token"]


class tokenAuth(credentials):

    def __init__(self):
        """
        Initiats the token authentication header class
        """
        credentials.__init__(self)

        self.authHeader = {"x-api-token": self.token}


class twoFactorOauth(credentials):

    def __init__(self):
        """
        Returns the token for two-factor authentication from qualtrics.
        """
        credentials.__init__(self)

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

        self.authHeader = {"authorization":
                           "bearer {}".format(self.accessToken)}


class params(credentials):

    def __init__(self):

        credentials.__init__(self)
        self.authHeader = twoFactorOauth().authHeader
