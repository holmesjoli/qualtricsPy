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


def blockDefinitionEndpoint(dataCenter, surveyId, blockId):
    """
    Create the endpoint for the survey-definition api
    :param dataCenter: the qualtrics data center, e.g. co1, ca1
    :type dataCenter: str
    :param surveyId: the id of the survey that will be updated
    :type surveyId: str
    :param blockId: the id of the blockt hat will be update
    :type blockId: str
    """
    e = "https://{}.qualtrics.com/API/v3/survey-definitions/{}/blocks/{}"
    return e.format(dataCenter, surveyId, blockId)
