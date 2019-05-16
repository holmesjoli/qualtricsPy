import requests

from utilsPy.config import read_yaml


class credentials(object):

    def __init__(self):
        """
        Initiates the credential configuration class.
        """
        cred = read_yaml("qualtricsCredentials.yaml")
        self.ownerId = cred["ownerId"]
        self.organizationId = cred["organizationId"]
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


def endpoint(dataCenter):
    """
    Create the endpoint for the survey api
    :param dataCenter: the qualtrics data center, e.g. co1, ca1
    :type dataCenter: str
    """
    e = "https://{}.qualtrics.com/API/v3/surveys/"
    return e.format(dataCenter)


def surveyEndpoint(dataCenter, surveyId):
    """
    Create the endpoint for the survey api for a specific survey
    :param dataCenter: the qualtrics data center, e.g. co1, ca1
    :type dataCenter: str
    :param surveyId: the id of the survey that will be updated
    :type surveyId: str
    """
    e = "https://{}.qualtrics.com/API/v3/surveys/{}"
    return e.format(dataCenter, surveyId)


def surveyDefinitionEndpoint(dataCenter, surveyId):
    """
    Create the endpoint for the survey-definition api
    :param dataCenter: the qualtrics data center, e.g. co1, ca1
    :type dataCenter: str
    :param surveyId: the id of the survey that will be updated
    :type surveyId: str
    """
    e = "https://{}.qualtrics.com/API/v3/survey-definitions/{}/questions"
    return e.format(dataCenter, surveyId)
